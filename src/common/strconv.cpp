/////////////////////////////////////////////////////////////////////////////
// Name:        strconv.cpp
// Purpose:     Unicode conversion classes
// Author:      Ove Kaaven, Robert Roebling, Vadim Zeitlin, Vaclav Slavik
// Modified by:
// Created:     29/01/98
// RCS-ID:      $Id$
// Copyright:   (c) 1999 Ove Kaaven, Robert Roebling, Vadim Zeitlin, Vaclav Slavik
// Licence:     wxWindows license
/////////////////////////////////////////////////////////////////////////////

// ============================================================================
// declarations
// ============================================================================

// ----------------------------------------------------------------------------
// headers
// ----------------------------------------------------------------------------

#ifdef __GNUG__
  #pragma implementation "strconv.h"
#endif

// For compilers that support precompilation, includes "wx.h".
#include "wx/wxprec.h"

#ifdef __BORLANDC__
  #pragma hdrstop
#endif

#ifdef __WXMSW__
  #include "wx/msw/private.h"
#endif

#include <errno.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>


#include "wx/debug.h"
#include "wx/strconv.h"
#include "wx/intl.h"
#include "wx/log.h"

// ----------------------------------------------------------------------------
// globals
// ----------------------------------------------------------------------------

WXDLLEXPORT_DATA(wxMBConv *) wxConvCurrent = &wxConvLibc;


// ============================================================================
// implementation
// ============================================================================

#if wxUSE_WCHAR_T

#ifdef __SALFORDC__
  #include <clib.h>
#endif

#ifdef HAVE_ICONV
  #include <iconv.h>
#endif

#ifdef __WXMSW__
  #include <windows.h>
#endif

#define BSWAP_UCS4(str, len) { unsigned _c; for (_c=0; _c<len; _c++) str[_c]=wxUINT32_SWAP_ALWAYS(str[_c]); }
#define BSWAP_UTF16(str, len) { unsigned _c; for (_c=0; _c<len; _c++) str[_c]=wxUINT16_SWAP_ALWAYS(str[_c]); }

// under Unix SIZEOF_WCHAR_T is defined by configure, but under other platforms
// it might be not defined - assume the most common value
#ifndef SIZEOF_WCHAR_T
    #define SIZEOF_WCHAR_T 2
#endif // !defined(SIZEOF_WCHAR_T)

#if SIZEOF_WCHAR_T == 4
    #define WC_NAME         "UCS4"
    #define WC_BSWAP         BSWAP_UCS4
    #ifdef WORDS_BIGENDIAN
      #define WC_NAME_BEST  "UCS-4BE"
    #else
      #define WC_NAME_BEST  "UCS-4LE"
    #endif
#elif SIZEOF_WCHAR_T == 2
    #define WC_NAME         "UTF16"
    #define WC_BSWAP         BSWAP_UTF16
    #define WC_UTF16
    #ifdef WORDS_BIGENDIAN
      #define WC_NAME_BEST  "UTF-16BE"
    #else
      #define WC_NAME_BEST  "UTF-16LE"
    #endif
#else // sizeof(wchar_t) != 2 nor 4
    // I don't know what to do about this
    #error "Weird sizeof(wchar_t): please report your platform details to wx-users mailing list"
#endif


#ifdef WC_UTF16

static size_t encode_utf16(wxUint32 input, wchar_t *output)
{
    if (input<=0xffff)
    {
        if (output) *output++ = input;
        return 1;
    }
    else if (input>=0x110000)
    {
        return (size_t)-1;
    }
    else
    {
        if (output)
        {
            *output++ = (input >> 10)+0xd7c0;
            *output++ = (input&0x3ff)+0xdc00;
        }
        return 2;
    }
}

static size_t decode_utf16(const wchar_t* input, wxUint32& output)
{
    if ((*input<0xd800) || (*input>0xdfff))
    {
        output = *input;
        return 1;
    }
    else if ((input[1]<0xdc00) || (input[1]>=0xdfff))
    {
        output = *input;
        return (size_t)-1;
    }
    else
    {
        output = ((input[0] - 0xd7c0) << 10) + (input[1] - 0xdc00);
        return 2;
    }
}

#endif // WC_UTF16

// ----------------------------------------------------------------------------
// wxMBConv
// ----------------------------------------------------------------------------

WXDLLEXPORT_DATA(wxMBConv) wxConvLibc;

size_t wxMBConv::MB2WC(wchar_t *buf, const char *psz, size_t n) const
{
    return wxMB2WC(buf, psz, n);
}

size_t wxMBConv::WC2MB(char *buf, const wchar_t *psz, size_t n) const
{
    return wxWC2MB(buf, psz, n);
}

const wxWCharBuffer wxMBConv::cMB2WC(const char *psz) const
{
    if (psz)
    {
        size_t nLen = MB2WC((wchar_t *) NULL, psz, 0);
        if (nLen == (size_t)-1)
            return wxWCharBuffer((wchar_t *) NULL);
        wxWCharBuffer buf(nLen);
        MB2WC((wchar_t *)(const wchar_t *) buf, psz, nLen);
        return buf;
    }
    else
        return wxWCharBuffer((wchar_t *) NULL);
}

const wxCharBuffer wxMBConv::cWC2MB(const wchar_t *psz) const
{
    if (psz)
    {
        size_t nLen = WC2MB((char *) NULL, psz, 0);
        if (nLen == (size_t)-1)
            return wxCharBuffer((char *) NULL);
        wxCharBuffer buf(nLen);
        WC2MB((char *)(const char *) buf, psz, nLen);
        return buf;
    }
    else
        return wxCharBuffer((char *) NULL);
}

// ----------------------------------------------------------------------------
// standard file conversion
// ----------------------------------------------------------------------------

WXDLLEXPORT_DATA(wxMBConvFile) wxConvFile;

// just use the libc conversion for now
size_t wxMBConvFile::MB2WC(wchar_t *buf, const char *psz, size_t n) const
{
    return wxMB2WC(buf, psz, n);
}

size_t wxMBConvFile::WC2MB(char *buf, const wchar_t *psz, size_t n) const
{
    return wxWC2MB(buf, psz, n);
}

// ----------------------------------------------------------------------------
// standard gdk conversion
// ----------------------------------------------------------------------------

#ifdef __WXGTK12__

WXDLLEXPORT_DATA(wxMBConvGdk) wxConvGdk;

#include <gdk/gdk.h>

size_t wxMBConvGdk::MB2WC(wchar_t *buf, const char *psz, size_t n) const
{
    if (buf)
    {
        return gdk_mbstowcs((GdkWChar *)buf, psz, n);
    }
    else
    {
        GdkWChar *nbuf = new GdkWChar[n=strlen(psz)];
        size_t len = gdk_mbstowcs(nbuf, psz, n);
        delete[] nbuf;
        return len;
    }
}

size_t wxMBConvGdk::WC2MB(char *buf, const wchar_t *psz, size_t n) const
{
    char *mbstr = gdk_wcstombs((GdkWChar *)psz);
    size_t len = mbstr ? strlen(mbstr) : 0;
    if (buf)
    {
        if (len > n)
            len = n;
        memcpy(buf, psz, len);
        if (len < n)
            buf[len] = 0;
    }
    return len;
}

#endif // GTK > 1.0

// ----------------------------------------------------------------------------
// UTF-7
// ----------------------------------------------------------------------------

WXDLLEXPORT_DATA(wxMBConvUTF7) wxConvUTF7;

#if 0
static char utf7_setD[]="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        "abcdefghijklmnopqrstuvwxyz"
                        "0123456789'(),-./:?";
static char utf7_setO[]="!\"#$%&*;<=>@[]^_`{|}";
static char utf7_setB[]="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        "abcdefghijklmnopqrstuvwxyz"
                        "0123456789+/";
#endif

// TODO: write actual implementations of UTF-7 here
size_t wxMBConvUTF7::MB2WC(wchar_t * WXUNUSED(buf),
                           const char * WXUNUSED(psz),
                           size_t WXUNUSED(n)) const
{
  return 0;
}

size_t wxMBConvUTF7::WC2MB(char * WXUNUSED(buf),
                           const wchar_t * WXUNUSED(psz),
                           size_t WXUNUSED(n)) const
{
  return 0;
}

// ----------------------------------------------------------------------------
// UTF-8
// ----------------------------------------------------------------------------

WXDLLEXPORT_DATA(wxMBConvUTF8) wxConvUTF8;

static wxUint32 utf8_max[]=
    { 0x7f, 0x7ff, 0xffff, 0x1fffff, 0x3ffffff, 0x7fffffff, 0xffffffff };

size_t wxMBConvUTF8::MB2WC(wchar_t *buf, const char *psz, size_t n) const
{
    size_t len = 0;

    while (*psz && ((!buf) || (len < n)))
    {
        unsigned char cc = *psz++, fc = cc;
        unsigned cnt;
        for (cnt = 0; fc & 0x80; cnt++)
            fc <<= 1;
        if (!cnt)
        {
            // plain ASCII char
            if (buf)
                *buf++ = cc;
            len++;
        }
        else
        {
            cnt--;
            if (!cnt)
            {
                // invalid UTF-8 sequence
                return (size_t)-1;
            }
            else
            {
                unsigned ocnt = cnt - 1;
                wxUint32 res = cc & (0x3f >> cnt);
                while (cnt--)
                {
                    cc = *psz++;
                    if ((cc & 0xC0) != 0x80)
                    {
                        // invalid UTF-8 sequence
                        return (size_t)-1;
                    }
                    res = (res << 6) | (cc & 0x3f);
                }
                if (res <= utf8_max[ocnt])
                {
                    // illegal UTF-8 encoding
                    return (size_t)-1;
                }
#ifdef WC_UTF16
                size_t pa = encode_utf16(res, buf);
                if (pa == (size_t)-1)
                  return (size_t)-1;
                if (buf)
                    buf += pa;
                len += pa;
#else
                if (buf)
                    *buf++ = res;
                len++;
#endif
            }
        }
    }
    if (buf && (len < n))
        *buf = 0;
    return len;
}

size_t wxMBConvUTF8::WC2MB(char *buf, const wchar_t *psz, size_t n) const
{
    size_t len = 0;

    while (*psz && ((!buf) || (len < n)))
    {
        wxUint32 cc;
#ifdef WC_UTF16
        size_t pa = decode_utf16(psz, cc);
        psz += (pa == (size_t)-1) ? 1 : pa;
#else
        cc=(*psz++) & 0x7fffffff;
#endif
        unsigned cnt;
        for (cnt = 0; cc > utf8_max[cnt]; cnt++) {}
        if (!cnt)
        {
            // plain ASCII char
            if (buf)
                *buf++ = cc;
            len++;
        }

        else
        {
            len += cnt + 1;
            if (buf)
            {
                *buf++ = (-128 >> cnt) | ((cc >> (cnt * 6)) & (0x3f >> cnt));
                while (cnt--)
                    *buf++ = 0x80 | ((cc >> (cnt * 6)) & 0x3f);
            }
        }
    }

    if (buf && (len<n)) *buf = 0;
    return len;
}

// ----------------------------------------------------------------------------
// specified character set
// ----------------------------------------------------------------------------

WXDLLEXPORT_DATA(wxCSConv) wxConvLocal((const wxChar *)NULL);

#include "wx/encconv.h"
#include "wx/fontmap.h"

// TODO: add some tables here
// - perhaps common encodings to common codepages (for Win32)
// - perhaps common encodings to objects ("UTF8" -> wxConvUTF8)
// - move wxEncodingConverter meat in here

#if defined(__WIN32__) && !defined(__WXMICROWIN__)

#if wxUSE_GUI

// VZ: the new version of wxCharsetToCodepage() is more politically correct
//     and should work on other Windows versions as well but the old version is
//     still needed for !wxUSE_FONTMAP || !wxUSE_GUI case

extern long wxEncodingToCodepage(wxFontEncoding encoding)
{
    // translate encoding into the Windows CHARSET
    wxNativeEncodingInfo natveEncInfo;
    if ( !wxGetNativeFontEncoding(encoding, &natveEncInfo) )
        return -1;

    // translate CHARSET to code page
    CHARSETINFO csetInfo;
    if ( !::TranslateCharsetInfo((DWORD *)(DWORD)natveEncInfo.charset,
                                 &csetInfo,
                                 TCI_SRCCHARSET) )
    {
        wxLogLastError(_T("TranslateCharsetInfo(TCI_SRCCHARSET)"));

        return -1;
    }

    return csetInfo.ciACP;
}

#if wxUSE_FONTMAP

extern long wxCharsetToCodepage(const wxChar *name)
{
    // first get the font encoding for this charset
    if ( !name )
        return -1;

    wxFontEncoding enc = wxTheFontMapper->CharsetToEncoding(name, FALSE);
    if ( enc == wxFONTENCODING_SYSTEM )
        return -1;

    // the use the helper function
    return wxEncodingToCodepage(enc);
}

#endif // wxUSE_FONTMAP

#endif // wxUSE_GUI

// include old wxCharsetToCodepage() by OK if needed
#if !wxUSE_GUI || !wxUSE_FONTMAP

#include "wx/msw/registry.h"

// this should work if Internet Exploiter is installed
extern long wxCharsetToCodepage(const wxChar *name)
{
    if (!name)
        return GetACP();

    long CP=-1;

    wxString cn(name);
    do {
        wxString path(wxT("MIME\\Database\\Charset\\"));
        path += cn;
        wxRegKey key(wxRegKey::HKCR, path);

        if (!key.Exists()) break;

        // two cases: either there's an AliasForCharset string,
        // or there are Codepage and InternetEncoding dwords.
        // The InternetEncoding gives us the actual encoding,
        // the Codepage just says which Windows character set to
        // use when displaying the data.
        if (key.HasValue(wxT("InternetEncoding")) &&
            key.QueryValue(wxT("InternetEncoding"), &CP)) break;

        // no encoding, see if it's an alias
        if (!key.HasValue(wxT("AliasForCharset")) ||
            !key.QueryValue(wxT("AliasForCharset"), cn)) break;
    } while (1);

    return CP;
}

#endif // !wxUSE_GUI || !wxUSE_FONTMAP

#endif // Win32

// ============================================================================
// wxCharacterSet and derived classes
// ============================================================================

// ----------------------------------------------------------------------------
// wxCharacterSet is the ABC for the classes below
// ----------------------------------------------------------------------------

class wxCharacterSet
{
public:
    wxCharacterSet(const wxChar*name)
        : cname(name) {}
    virtual ~wxCharacterSet()
        {}
    virtual size_t MB2WC(wchar_t *buf, const char *psz, size_t n)
        { return (size_t)-1; }
    virtual size_t WC2MB(char *buf, const wchar_t *psz, size_t n)
        { return (size_t)-1; }
    virtual bool usable()
        { return FALSE; }
public:
    const wxChar*cname;
};

// ----------------------------------------------------------------------------
// ID_CharSet: implementation of wxCharacterSet using an existing wxMBConv
// ----------------------------------------------------------------------------

class ID_CharSet : public wxCharacterSet
{
public:
    ID_CharSet(const wxChar *name, wxMBConv *cnv)
        : wxCharacterSet(name), work(cnv) {}

    size_t MB2WC(wchar_t *buf, const char *psz, size_t n)
        { return work ? work->MB2WC(buf,psz,n) : (size_t)-1; }

    size_t WC2MB(char *buf, const wchar_t *psz, size_t n)
        { return work ? work->WC2MB(buf,psz,n) : (size_t)-1; }

    bool usable()
        { return work!=NULL; }
public:
    wxMBConv*work;
};


// ============================================================================
// The classes doing conversion using the iconv_xxx() functions
// ============================================================================

#ifdef HAVE_ICONV

// VS: glibc 2.1.3 is broken in that iconv() conversion to/from UCS4 fails with E2BIG
//     if output buffer is _exactly_ as big as needed. Such case is (unless there's
//     yet another bug in glibc) the only case when iconv() returns with (size_t)-1
//     (which means error) and says there are 0 bytes left in the input buffer --
//     when _real_ error occurs, bytes-left-in-input buffer is non-zero. Hence,
//     this alternative test for iconv() failure.
//     [This bug does not appear in glibc 2.2.]
#if defined(__GLIBC__) && __GLIBC__ == 2 && __GLIBC_MINOR__ <= 1
#define ICONV_FAILED(cres, bufLeft) ((cres == (size_t)-1) && \
                                     (errno != E2BIG || bufLeft != 0))
#else
#define ICONV_FAILED(cres, bufLeft)  (cres == (size_t)-1)
#endif

#define ICONV_CHAR_CAST(x)  ((ICONV_CONST char **)(x))

// ----------------------------------------------------------------------------
// IC_CharSet: encapsulates an iconv character set
// ----------------------------------------------------------------------------

class IC_CharSet : public wxCharacterSet
{
public:
    IC_CharSet(const wxChar *name);
    virtual ~IC_CharSet();

    virtual size_t MB2WC(wchar_t *buf, const char *psz, size_t n);
    virtual size_t WC2MB(char *buf, const wchar_t *psz, size_t n);

    bool usable() const
        { return (m2w != (iconv_t)-1) && (w2m != (iconv_t)-1); }

protected:
    // the iconv handlers used to translate from multibyte to wide char and in
    // the other direction
    iconv_t m2w,
            w2m;

private:
    // the name (for iconv_open()) of a wide char charset - if none is
    // available on this machine, it will remain NULL
    static const char *ms_wcCharsetName;

    // true if the wide char encoding we use (i.e. ms_wcCharsetName) has
    // different endian-ness than the native one
    static bool ms_wcNeedsSwap;
};

const char *IC_CharSet::ms_wcCharsetName = NULL;
bool IC_CharSet::ms_wcNeedsSwap = FALSE;

IC_CharSet::IC_CharSet(const wxChar *name)
          : wxCharacterSet(name)
{
    // check for charset that represents wchar_t:
    if (ms_wcCharsetName == NULL)
    {
        ms_wcNeedsSwap = FALSE;

        // try charset with explicit bytesex info (e.g. "UCS-4LE"):
        ms_wcCharsetName = WC_NAME_BEST;
        m2w = iconv_open(ms_wcCharsetName, wxConvLibc.cWX2MB(name));

        if (m2w == (iconv_t)-1)
        {
            // try charset w/o bytesex info (e.g. "UCS4")
            // and check for bytesex ourselves:
            ms_wcCharsetName = WC_NAME;
            m2w = iconv_open(ms_wcCharsetName, wxConvLibc.cWX2MB(name));

            // last bet, try if it knows WCHAR_T pseudo-charset
            if (m2w == (iconv_t)-1)
            {
                ms_wcCharsetName = "WCHAR_T";
                m2w = iconv_open(ms_wcCharsetName, wxConvLibc.cWX2MB(name));
            }

            if (m2w != (iconv_t)-1)
            {
                char    buf[2], *bufPtr;
                wchar_t wbuf[2], *wbufPtr;
                size_t  insz, outsz;
                size_t  res;

                buf[0] = 'A';
                buf[1] = 0;
                wbuf[0] = 0;
                insz = 2;
                outsz = SIZEOF_WCHAR_T * 2;
                wbufPtr = wbuf;
                bufPtr = buf;

                res = iconv(m2w, ICONV_CHAR_CAST(&bufPtr), &insz,
                            (char**)&wbufPtr, &outsz);

                if (ICONV_FAILED(res, insz))
                {
                    ms_wcCharsetName = NULL;
                    wxLogLastError(wxT("iconv"));
                    wxLogError(_("Convertion to charset '%s' doesn't work."), name);
                }
                else
                {
                    ms_wcNeedsSwap = wbuf[0] != (wchar_t)buf[0];
                }
            }
            else
            {
                ms_wcCharsetName = NULL;
                
                // VS: we must not output an error here, since wxWindows will safely
                //     fall back to using wxEncodingConverter.
                wxLogTrace(wxT("strconv"), wxT("Impossible to convert to/from charset '%s' with iconv, falling back to wxEncodingConverter."), name);
                //wxLogError(
            }
        }
        wxLogTrace(wxT("strconv"), wxT("wchar_t charset is '%s', needs swap: %i"), ms_wcCharsetName, ms_wcNeedsSwap);
    }
    else // we already have ms_wcCharsetName
    {
        m2w = iconv_open(ms_wcCharsetName, wxConvLibc.cWX2MB(name));
    }

    // NB: don't ever pass NULL to iconv_open(), it may crash!
    if ( ms_wcCharsetName )
    {
        w2m = iconv_open(wxConvLibc.cWX2MB(name), ms_wcCharsetName);
    }
    else
    {
        w2m = (iconv_t)-1;
    }
}

IC_CharSet::~IC_CharSet()
{
    if ( m2w != (iconv_t)-1 )
        iconv_close(m2w);
    if ( w2m != (iconv_t)-1 )
        iconv_close(w2m);
}

size_t IC_CharSet::MB2WC(wchar_t *buf, const char *psz, size_t n)
{
    size_t inbuf = strlen(psz);
    size_t outbuf = n * SIZEOF_WCHAR_T;
    size_t res, cres;
    // VS: Use these instead of psz, buf because iconv() modifies its arguments:
    wchar_t *bufPtr = buf;
    const char *pszPtr = psz;

    if (buf)
    {
        // have destination buffer, convert there
        cres = iconv(m2w,
                     ICONV_CHAR_CAST(&pszPtr), &inbuf,
                     (char**)&bufPtr, &outbuf);
        res = n - (outbuf / SIZEOF_WCHAR_T);

        if (ms_wcNeedsSwap)
        {
            // convert to native endianness
            WC_BSWAP(buf /* _not_ bufPtr */, res)
        }
    }
    else
    {
        // no destination buffer... convert using temp buffer
        // to calculate destination buffer requirement
        wchar_t tbuf[8];
        res = 0;
        do {
            bufPtr = tbuf;
            outbuf = 8*SIZEOF_WCHAR_T;

            cres = iconv(m2w,
                         ICONV_CHAR_CAST(&pszPtr), &inbuf,
                         (char**)&bufPtr, &outbuf );

            res += 8-(outbuf/SIZEOF_WCHAR_T);
        } while ((cres==(size_t)-1) && (errno==E2BIG));
    }

    if (ICONV_FAILED(cres, inbuf))
    {
        //VS: it is ok if iconv fails, hence trace only
        wxLogTrace(wxT("strconv"), wxT("iconv failed: %s"), wxSysErrorMsg(wxSysErrorCode()));
        return (size_t)-1;
    }

    return res;
}

size_t IC_CharSet::WC2MB(char *buf, const wchar_t *psz, size_t n)
{
#if defined(__BORLANDC__) && (__BORLANDC__ > 0x530)
    size_t inbuf = std::wcslen(psz) * SIZEOF_WCHAR_T;
#else
    size_t inbuf = ::wcslen(psz) * SIZEOF_WCHAR_T;
#endif
    size_t outbuf = n;
    size_t res, cres;

    wchar_t *tmpbuf = 0;

    if (ms_wcNeedsSwap)
    {
        // need to copy to temp buffer to switch endianness
        // this absolutely doesn't rock!
        // (no, doing WC_BSWAP twice on the original buffer won't help, as it
        //  could be in read-only memory, or be accessed in some other thread)
        tmpbuf=(wchar_t*)malloc((inbuf+1)*SIZEOF_WCHAR_T);
        memcpy(tmpbuf,psz,(inbuf+1)*SIZEOF_WCHAR_T);
        WC_BSWAP(tmpbuf, inbuf)
        psz=tmpbuf;
    }

    if (buf)
    {
        // have destination buffer, convert there
        cres = iconv( w2m, ICONV_CHAR_CAST(&psz), &inbuf, &buf, &outbuf );

        res = n-outbuf;
    }
    else
    {
        // no destination buffer... convert using temp buffer
        // to calculate destination buffer requirement
        char tbuf[16];
        res = 0;
        do {
            buf = tbuf; outbuf = 16;

            cres = iconv( w2m, ICONV_CHAR_CAST(&psz), &inbuf, &buf, &outbuf );

            res += 16 - outbuf;
        } while ((cres==(size_t)-1) && (errno==E2BIG));
    }

    if (ms_wcNeedsSwap)
    {
        free(tmpbuf);
    }

    if (ICONV_FAILED(cres, inbuf))
    {
        //VS: it is ok if iconv fails, hence trace only
        wxLogTrace(wxT("strconv"), wxT("iconv failed: %s"), wxSysErrorMsg(wxSysErrorCode()));
        return (size_t)-1;
    }

    return res;
}

#endif // HAVE_ICONV

// ============================================================================
// Win32 conversion classes
// ============================================================================

#if defined(__WIN32__) && !defined(__WXMICROWIN__)
class CP_CharSet : public wxCharacterSet
{
public:
    CP_CharSet(const wxChar* name)
        : wxCharacterSet(name)
        {
            m_CodePage = wxCharsetToCodepage(name);
        }

    size_t MB2WC(wchar_t *buf, const char *psz, size_t n)
    {
        size_t len =
            MultiByteToWideChar(m_CodePage, 0, psz, -1, buf, buf ? n : 0);
        //VS: returns # of written chars for buf!=NULL and *size*
        //    needed buffer for buf==NULL
        return len ? (buf ? len : len-1) : (size_t)-1;
    }

    size_t WC2MB(char *buf, const wchar_t *psz, size_t n)
    {
        size_t len = WideCharToMultiByte(m_CodePage, 0, psz, -1, buf,
                                         buf ? n : 0, NULL, NULL);
        //VS: returns # of written chars for buf!=NULL and *size*
        //    needed buffer for buf==NULL
        return len ? (buf ? len : len-1) : (size_t)-1;
    }

    bool usable()
        { return m_CodePage != -1; }

public:
    long m_CodePage;
};
#endif // __WIN32__

// ============================================================================
// wxEncodingConverter based conversion classes
// ============================================================================

#if wxUSE_FONTMAP

class EC_CharSet : public wxCharacterSet
{
public:
    // temporarily just use wxEncodingConverter stuff,
    // so that it works while a better implementation is built
    EC_CharSet(const wxChar* name) : wxCharacterSet(name),
                                     enc(wxFONTENCODING_SYSTEM)
    {
        if (name)
            enc = wxTheFontMapper->CharsetToEncoding(name, FALSE);
        m2w.Init(enc, wxFONTENCODING_UNICODE);
        w2m.Init(wxFONTENCODING_UNICODE, enc);
    }

    size_t MB2WC(wchar_t *buf, const char *psz, size_t n)
    {
        size_t inbuf = strlen(psz);
        if (buf)
            m2w.Convert(psz,buf);
        return inbuf;
    }

    size_t WC2MB(char *buf, const wchar_t *psz, size_t n)
    {
#if ( defined(__BORLANDC__) && (__BORLANDC__ > 0x530) ) \
    || ( defined(__MWERKS__) && defined(__WXMSW__) )
        size_t inbuf = std::wcslen(psz);
#else
        size_t inbuf = ::wcslen(psz);
#endif
        if (buf)
            w2m.Convert(psz,buf);

        return inbuf;
    }

    bool usable()
        { return (enc!=wxFONTENCODING_SYSTEM) && (enc!=wxFONTENCODING_DEFAULT); }

public:
    wxFontEncoding enc;
    wxEncodingConverter m2w, w2m;
};

#endif // wxUSE_FONTMAP

// ----------------------------------------------------------------------------
// the function creating the wxCharacterSet for the specified charset on the
// current system, trying all possibilities
// ----------------------------------------------------------------------------

static wxCharacterSet *wxGetCharacterSet(const wxChar *name)
{
    wxCharacterSet *cset = NULL;
    if (name)
    {
        if (wxStricmp(name, wxT("UTF8")) == 0 || wxStricmp(name, wxT("UTF-8")) == 0)
        {
            cset = new ID_CharSet(name, &wxConvUTF8);
        }
        else
        {
#ifdef HAVE_ICONV
            cset = new IC_CharSet(name); // may not take NULL
#endif
        }
    }

    if (cset && cset->usable())
        return cset;

    if (cset)
    {
        delete cset;
        cset = NULL;
    }

#if defined(__WIN32__) && !defined(__WXMICROWIN__)
    cset = new CP_CharSet(name); // may take NULL
    if (cset->usable())
        return cset;

    delete cset;
#endif // __WIN32__

#if wxUSE_FONTMAP
    cset = new EC_CharSet(name);
    if (cset->usable())
        return cset;
#endif // wxUSE_FONTMAP

    delete cset;
    wxLogError(_("Unknown encoding '%s'!"), name);
    return NULL;
}

// ============================================================================
// wxCSConv implementation
// ============================================================================

wxCSConv::wxCSConv(const wxChar *charset)
{
    m_name = (wxChar *)NULL;
    m_cset = (wxCharacterSet *) NULL;
    m_deferred = TRUE;

    SetName(charset);
}

wxCSConv::~wxCSConv()
{
    free(m_name);
    delete m_cset;
}

void wxCSConv::SetName(const wxChar *charset)
{
    if (charset)
    {
        m_name = wxStrdup(charset);
        m_deferred = TRUE;
    }
}

void wxCSConv::LoadNow()
{
    if (m_deferred)
    {
        if ( !m_name )
        {
            wxString name = wxLocale::GetSystemEncodingName();
            if ( !name.empty() )
                SetName(name);
        }

        // wxGetCharacterSet() complains about NULL name
        m_cset = m_name ? wxGetCharacterSet(m_name) : NULL;
        m_deferred = FALSE;
    }
}

size_t wxCSConv::MB2WC(wchar_t *buf, const char *psz, size_t n) const
{
    ((wxCSConv *)this)->LoadNow(); // discard constness

    if (m_cset)
        return m_cset->MB2WC(buf, psz, n);

    // latin-1 (direct)
    size_t len = strlen(psz);

    if (buf)
    {
        for (size_t c = 0; c <= len; c++)
            buf[c] = (unsigned char)(psz[c]);
    }

    return len;
}

size_t wxCSConv::WC2MB(char *buf, const wchar_t *psz, size_t n) const
{
    ((wxCSConv *)this)->LoadNow(); // discard constness

    if (m_cset)
        return m_cset->WC2MB(buf, psz, n);

    // latin-1 (direct)
#if ( defined(__BORLANDC__) && (__BORLANDC__ > 0x530) ) \
    || ( defined(__MWERKS__) && defined(__WXMSW__) )
    size_t len=std::wcslen(psz);
#else
    size_t len=::wcslen(psz);
#endif
    if (buf)
    {
        for (size_t c = 0; c <= len; c++)
            buf[c] = (psz[c] > 0xff) ? '?' : psz[c];
    }

    return len;
}

#else // !wxUSE_WCHAR_T

// ----------------------------------------------------------------------------
// stand-ins in absence of wchar_t
// ----------------------------------------------------------------------------

WXDLLEXPORT_DATA(wxMBConv) wxConvLibc, wxConvFile;

#endif // wxUSE_WCHAR_T


