/////////////////////////////////////////////////////////////////////////////
// Name:        src/common/utilscmn.cpp
// Purpose:     Miscellaneous utility functions and classes
// Author:      Julian Smart
// Modified by:
// Created:     29/01/98
// RCS-ID:      $Id$
// Copyright:   (c) 1998 Julian Smart
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

// ============================================================================
// declarations
// ============================================================================

// ----------------------------------------------------------------------------
// headers
// ----------------------------------------------------------------------------

// For compilers that support precompilation, includes "wx.h".
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

#ifndef WX_PRECOMP
    #include "wx/app.h"
    #include "wx/string.h"
    #include "wx/utils.h"
    #include "wx/intl.h"
    #include "wx/log.h"

    #if wxUSE_GUI
        #include "wx/window.h"
        #include "wx/frame.h"
        #include "wx/menu.h"
        #include "wx/msgdlg.h"
        #include "wx/textdlg.h"
        #include "wx/textctrl.h"    // for wxTE_PASSWORD
        #if wxUSE_ACCEL
            #include "wx/menuitem.h"
            #include "wx/accel.h"
        #endif // wxUSE_ACCEL
    #endif // wxUSE_GUI
#endif // WX_PRECOMP

#include "wx/apptrait.h"

#include "wx/process.h"
#include "wx/txtstrm.h"
#include "wx/uri.h"
#include "wx/mimetype.h"
#include "wx/config.h"

#if defined(__WXWINCE__) && wxUSE_DATETIME
#include "wx/datetime.h"
#endif

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#if !wxONLY_WATCOM_EARLIER_THAN(1,4)
    #if !(defined(_MSC_VER) && (_MSC_VER > 800))
        #include <errno.h>
    #endif
#endif

#if wxUSE_GUI
    #include "wx/colordlg.h"
    #include "wx/fontdlg.h"
    #include "wx/notebook.h"
    #include "wx/statusbr.h"
#endif // wxUSE_GUI

#ifndef __WXPALMOS5__
#ifndef __WXWINCE__
#include <time.h>
#else
#include "wx/msw/wince/time.h"
#endif
#endif // ! __WXPALMOS5__

#ifdef __WXMAC__
#include "wx/osx/private.h"
#endif

#ifndef __WXPALMOS5__
#if !defined(__MWERKS__) && !defined(__WXWINCE__)
    #include <sys/types.h>
    #include <sys/stat.h>
#endif
#endif // ! __WXPALMOS5__

#if defined(__WXMSW__)
    #include "wx/msw/private.h"
    #include "wx/msw/registry.h"
    #include <shellapi.h> // needed for SHELLEXECUTEINFO
#endif

#if wxUSE_GUI && defined(__WXGTK__)
    #include <gtk/gtk.h>    // for GTK_XXX_VERSION constants
#endif

#if wxUSE_BASE

// ----------------------------------------------------------------------------
// common data
// ----------------------------------------------------------------------------

// ============================================================================
// implementation
// ============================================================================

// Array used in DecToHex conversion routine.
static wxChar hexArray[] = wxT("0123456789ABCDEF");

// Convert 2-digit hex number to decimal
int wxHexToDec(const wxString& buf)
{
    int firstDigit, secondDigit;

    if (buf.GetChar(0) >= wxT('A'))
        firstDigit = buf.GetChar(0) - wxT('A') + 10;
    else
       firstDigit = buf.GetChar(0) - wxT('0');

    if (buf.GetChar(1) >= wxT('A'))
        secondDigit = buf.GetChar(1) - wxT('A') + 10;
    else
        secondDigit = buf.GetChar(1) - wxT('0');

    return (firstDigit & 0xF) * 16 + (secondDigit & 0xF );
}

// Convert decimal integer to 2-character hex string
void wxDecToHex(int dec, wxChar *buf)
{
    int firstDigit = (int)(dec/16.0);
    int secondDigit = (int)(dec - (firstDigit*16.0));
    buf[0] = hexArray[firstDigit];
    buf[1] = hexArray[secondDigit];
    buf[2] = 0;
}

// Convert decimal integer to 2 characters
void wxDecToHex(int dec, char* ch1, char* ch2)
{
    int firstDigit = (int)(dec/16.0);
    int secondDigit = (int)(dec - (firstDigit*16.0));
    (*ch1) = (char) hexArray[firstDigit];
    (*ch2) = (char) hexArray[secondDigit];
}

// Convert decimal integer to 2-character hex string
wxString wxDecToHex(int dec)
{
    wxChar buf[3];
    wxDecToHex(dec, buf);
    return wxString(buf);
}

// ----------------------------------------------------------------------------
// misc functions
// ----------------------------------------------------------------------------

// Return the current date/time
wxString wxNow()
{
#ifdef __WXWINCE__
#if wxUSE_DATETIME
    wxDateTime now = wxDateTime::Now();
    return now.Format();
#else
    return wxEmptyString;
#endif
#else
    time_t now = time((time_t *) NULL);
    char *date = ctime(&now);
    date[24] = '\0';
    return wxString::FromAscii(date);
#endif
}

void wxUsleep(unsigned long milliseconds)
{
    wxMilliSleep(milliseconds);
}

const wxChar *wxGetInstallPrefix()
{
    wxString prefix;

    if ( wxGetEnv(wxT("WXPREFIX"), &prefix) )
        return prefix.c_str();

#ifdef wxINSTALL_PREFIX
    return wxT(wxINSTALL_PREFIX);
#else
    return wxEmptyString;
#endif
}

wxString wxGetDataDir()
{
    wxString dir = wxGetInstallPrefix();
    dir <<  wxFILE_SEP_PATH << wxT("share") << wxFILE_SEP_PATH << wxT("wx");
    return dir;
}

bool wxIsPlatformLittleEndian()
{
    // Are we little or big endian? This method is from Harbison & Steele.
    union
    {
        long l;
        char c[sizeof(long)];
    } u;
    u.l = 1;

    return u.c[0] == 1;
}


/*
 * Class to make it easier to specify platform-dependent values
 */

wxArrayInt*  wxPlatform::sm_customPlatforms = NULL;

void wxPlatform::Copy(const wxPlatform& platform)
{
    m_longValue = platform.m_longValue;
    m_doubleValue = platform.m_doubleValue;
    m_stringValue = platform.m_stringValue;
}

wxPlatform wxPlatform::If(int platform, long value)
{
    if (Is(platform))
        return wxPlatform(value);
    else
        return wxPlatform();
}

wxPlatform wxPlatform::IfNot(int platform, long value)
{
    if (!Is(platform))
        return wxPlatform(value);
    else
        return wxPlatform();
}

wxPlatform& wxPlatform::ElseIf(int platform, long value)
{
    if (Is(platform))
        m_longValue = value;
    return *this;
}

wxPlatform& wxPlatform::ElseIfNot(int platform, long value)
{
    if (!Is(platform))
        m_longValue = value;
    return *this;
}

wxPlatform wxPlatform::If(int platform, double value)
{
    if (Is(platform))
        return wxPlatform(value);
    else
        return wxPlatform();
}

wxPlatform wxPlatform::IfNot(int platform, double value)
{
    if (!Is(platform))
        return wxPlatform(value);
    else
        return wxPlatform();
}

wxPlatform& wxPlatform::ElseIf(int platform, double value)
{
    if (Is(platform))
        m_doubleValue = value;
    return *this;
}

wxPlatform& wxPlatform::ElseIfNot(int platform, double value)
{
    if (!Is(platform))
        m_doubleValue = value;
    return *this;
}

wxPlatform wxPlatform::If(int platform, const wxString& value)
{
    if (Is(platform))
        return wxPlatform(value);
    else
        return wxPlatform();
}

wxPlatform wxPlatform::IfNot(int platform, const wxString& value)
{
    if (!Is(platform))
        return wxPlatform(value);
    else
        return wxPlatform();
}

wxPlatform& wxPlatform::ElseIf(int platform, const wxString& value)
{
    if (Is(platform))
        m_stringValue = value;
    return *this;
}

wxPlatform& wxPlatform::ElseIfNot(int platform, const wxString& value)
{
    if (!Is(platform))
        m_stringValue = value;
    return *this;
}

wxPlatform& wxPlatform::Else(long value)
{
    m_longValue = value;
    return *this;
}

wxPlatform& wxPlatform::Else(double value)
{
    m_doubleValue = value;
    return *this;
}

wxPlatform& wxPlatform::Else(const wxString& value)
{
    m_stringValue = value;
    return *this;
}

void wxPlatform::AddPlatform(int platform)
{
    if (!sm_customPlatforms)
        sm_customPlatforms = new wxArrayInt;
    sm_customPlatforms->Add(platform);
}

void wxPlatform::ClearPlatforms()
{
    delete sm_customPlatforms;
    sm_customPlatforms = NULL;
}

/// Function for testing current platform

bool wxPlatform::Is(int platform)
{
#ifdef __WXMSW__
    if (platform == wxOS_WINDOWS)
        return true;
#endif
#ifdef __WXWINCE__
    if (platform == wxOS_WINDOWS_CE)
        return true;
#endif

#if 0

// FIXME: wxWinPocketPC and wxWinSmartPhone are unknown symbols

#if defined(__WXWINCE__) && defined(__POCKETPC__)
    if (platform == wxWinPocketPC)
        return true;
#endif
#if defined(__WXWINCE__) && defined(__SMARTPHONE__)
    if (platform == wxWinSmartPhone)
        return true;
#endif

#endif

#ifdef __WXGTK__
    if (platform == wxPORT_GTK)
        return true;
#endif
#ifdef __WXMAC__
    if (platform == wxPORT_MAC)
        return true;
#endif
#ifdef __WXX11__
    if (platform == wxPORT_X11)
        return true;
#endif
#ifdef __UNIX__
    if (platform == wxOS_UNIX)
        return true;
#endif
#ifdef __WXMGL__
    if (platform == wxPORT_MGL)
        return true;
#endif
#ifdef __OS2__
    if (platform == wxOS_OS2)
        return true;
#endif
#ifdef __WXPM__
    if (platform == wxPORT_PM)
        return true;
#endif
#ifdef __WXCOCOA__
    if (platform == wxPORT_MAC)
        return true;
#endif

    if (sm_customPlatforms && sm_customPlatforms->Index(platform) != wxNOT_FOUND)
        return true;

    return false;
}

// ----------------------------------------------------------------------------
// network and user id functions
// ----------------------------------------------------------------------------

// Get Full RFC822 style email address
bool wxGetEmailAddress(wxChar *address, int maxSize)
{
    wxString email = wxGetEmailAddress();
    if ( !email )
        return false;

    wxStrncpy(address, email, maxSize - 1);
    address[maxSize - 1] = wxT('\0');

    return true;
}

wxString wxGetEmailAddress()
{
    wxString email;

    wxString host = wxGetFullHostName();
    if ( !host.empty() )
    {
        wxString user = wxGetUserId();
        if ( !user.empty() )
        {
            email << user << wxT('@') << host;
        }
    }

    return email;
}

wxString wxGetUserId()
{
    static const int maxLoginLen = 256; // FIXME arbitrary number

    wxString buf;
    bool ok = wxGetUserId(wxStringBuffer(buf, maxLoginLen), maxLoginLen);

    if ( !ok )
        buf.Empty();

    return buf;
}

wxString wxGetUserName()
{
    static const int maxUserNameLen = 1024; // FIXME arbitrary number

    wxString buf;
    bool ok = wxGetUserName(wxStringBuffer(buf, maxUserNameLen), maxUserNameLen);

    if ( !ok )
        buf.Empty();

    return buf;
}

wxString wxGetHostName()
{
    static const size_t hostnameSize = 257;

    wxString buf;
    bool ok = wxGetHostName(wxStringBuffer(buf, hostnameSize), hostnameSize);

    if ( !ok )
        buf.Empty();

    return buf;
}

wxString wxGetFullHostName()
{
    static const size_t hostnameSize = 257;

    wxString buf;
    bool ok = wxGetFullHostName(wxStringBuffer(buf, hostnameSize), hostnameSize);

    if ( !ok )
        buf.Empty();

    return buf;
}

wxString wxGetHomeDir()
{
    wxString home;
    wxGetHomeDir(&home);

    return home;
}

#if 0

wxString wxGetCurrentDir()
{
    wxString dir;
    size_t len = 1024;
    bool ok;
    do
    {
        ok = getcwd(dir.GetWriteBuf(len + 1), len) != NULL;
        dir.UngetWriteBuf();

        if ( !ok )
        {
            if ( errno != ERANGE )
            {
                wxLogSysError(_T("Failed to get current directory"));

                return wxEmptyString;
            }
            else
            {
                // buffer was too small, retry with a larger one
                len *= 2;
            }
        }
        //else: ok
    } while ( !ok );

    return dir;
}

#endif // 0

// ----------------------------------------------------------------------------
// wxExecute
// ----------------------------------------------------------------------------

// wxDoExecuteWithCapture() helper: reads an entire stream into one array
//
// returns true if ok, false if error
#if wxUSE_STREAMS
static bool ReadAll(wxInputStream *is, wxArrayString& output)
{
    wxCHECK_MSG( is, false, _T("NULL stream in wxExecute()?") );

    // the stream could be already at EOF or in wxSTREAM_BROKEN_PIPE state
    is->Reset();

    wxTextInputStream tis(*is);

    for ( ;; )
    {
        wxString line = tis.ReadLine();

        // check for EOF before other errors as it's not really an error
        if ( is->Eof() )
        {
            // add the last, possibly incomplete, line
            if ( !line.empty() )
                output.Add(line);
            break;
        }

        // any other error is fatal
        if ( !*is )
            return false;

        output.Add(line);
    }

    return true;
}
#endif // wxUSE_STREAMS

// this is a private function because it hasn't a clean interface: the first
// array is passed by reference, the second by pointer - instead we have 2
// public versions of wxExecute() below
static long wxDoExecuteWithCapture(const wxString& command,
                                   wxArrayString& output,
                                   wxArrayString* error,
                                   int flags)
{
    // create a wxProcess which will capture the output
    wxProcess *process = new wxProcess;
    process->Redirect();

    long rc = wxExecute(command, wxEXEC_SYNC | flags, process);

#if wxUSE_STREAMS
    if ( rc != -1 )
    {
        if ( !ReadAll(process->GetInputStream(), output) )
            rc = -1;

        if ( error )
        {
            if ( !ReadAll(process->GetErrorStream(), *error) )
                rc = -1;
        }

    }
#else
    wxUnusedVar(output);
    wxUnusedVar(error);
#endif // wxUSE_STREAMS/!wxUSE_STREAMS

    delete process;

    return rc;
}

long wxExecute(const wxString& command, wxArrayString& output, int flags)
{
    return wxDoExecuteWithCapture(command, output, NULL, flags);
}

long wxExecute(const wxString& command,
               wxArrayString& output,
               wxArrayString& error,
               int flags)
{
    return wxDoExecuteWithCapture(command, output, &error, flags);
}

// ----------------------------------------------------------------------------
// wxApp::Yield() wrappers for backwards compatibility
// ----------------------------------------------------------------------------

bool wxYield()
{
    return wxTheApp && wxTheApp->Yield();
}

bool wxYieldIfNeeded()
{
    return wxTheApp && wxTheApp->Yield(true);
}

// Id generation
static long wxCurrentId = 100;

long wxNewId()
{
    // skip the part of IDs space that contains hard-coded values:
    if (wxCurrentId == wxID_LOWEST)
        wxCurrentId = wxID_HIGHEST + 1;

    return wxCurrentId++;
}

long
wxGetCurrentId(void) { return wxCurrentId; }

void
wxRegisterId (long id)
{
  if (id >= wxCurrentId)
    wxCurrentId = id + 1;
}

// ----------------------------------------------------------------------------
// wxQsort, adapted by RR to allow user_data
// ----------------------------------------------------------------------------

/* This file is part of the GNU C Library.
   Written by Douglas C. Schmidt (schmidt@ics.uci.edu).

   Douglas Schmidt kindly gave permission to relicence the
   code under the wxWindows licence:

From: "Douglas C. Schmidt" <schmidt@dre.vanderbilt.edu>
To: Robert Roebling <robert.roebling@uni-ulm.de>
Subject: Re: qsort licence
Date: Mon, 23 Jul 2007 03:44:25 -0500
Sender: schmidt@dre.vanderbilt.edu
Message-Id: <20070723084426.64F511000A8@tango.dre.vanderbilt.edu>

Hi Robert,

> [...] I'm asking if you'd be willing to relicence your code
> under the wxWindows licence. [...]

That's fine with me [...]

Thanks,

     Doug */


/* Byte-wise swap two items of size SIZE. */
#define SWAP(a, b, size)                                                      \
  do                                                                              \
    {                                                                              \
      register size_t __size = (size);                                              \
      register char *__a = (a), *__b = (b);                                      \
      do                                                                      \
        {                                                                      \
          char __tmp = *__a;                                                      \
          *__a++ = *__b;                                                      \
          *__b++ = __tmp;                                                      \
        } while (--__size > 0);                                                      \
    } while (0)

/* Discontinue quicksort algorithm when partition gets below this size.
   This particular magic number was chosen to work best on a Sun 4/260. */
#define MAX_THRESH 4

/* Stack node declarations used to store unfulfilled partition obligations. */
typedef struct
  {
    char *lo;
    char *hi;
  } stack_node;

/* The next 4 #defines implement a very fast in-line stack abstraction. */
#define STACK_SIZE        (8 * sizeof(unsigned long int))
#define PUSH(low, high)   ((void) ((top->lo = (low)), (top->hi = (high)), ++top))
#define POP(low, high)    ((void) (--top, (low = top->lo), (high = top->hi)))
#define STACK_NOT_EMPTY   (stack < top)


/* Order size using quicksort.  This implementation incorporates
   four optimizations discussed in Sedgewick:

   1. Non-recursive, using an explicit stack of pointer that store the
      next array partition to sort.  To save time, this maximum amount
      of space required to store an array of MAX_INT is allocated on the
      stack.  Assuming a 32-bit integer, this needs only 32 *
      sizeof(stack_node) == 136 bits.  Pretty cheap, actually.

   2. Chose the pivot element using a median-of-three decision tree.
      This reduces the probability of selecting a bad pivot value and
      eliminates certain extraneous comparisons.

   3. Only quicksorts TOTAL_ELEMS / MAX_THRESH partitions, leaving
      insertion sort to order the MAX_THRESH items within each partition.
      This is a big win, since insertion sort is faster for small, mostly
      sorted array segments.

   4. The larger of the two sub-partitions is always pushed onto the
      stack first, with the algorithm then concentrating on the
      smaller partition.  This *guarantees* no more than log (n)
      stack size is needed (actually O(1) in this case)!  */

void wxQsort(void *const pbase, size_t total_elems,
                             size_t size, CMPFUNCDATA cmp, const void* user_data)
{
  register char *base_ptr = (char *) pbase;
  const size_t max_thresh = MAX_THRESH * size;

  if (total_elems == 0)
    /* Avoid lossage with unsigned arithmetic below.  */
    return;

  if (total_elems > MAX_THRESH)
    {
      char *lo = base_ptr;
      char *hi = &lo[size * (total_elems - 1)];
      stack_node stack[STACK_SIZE];
      stack_node *top = stack;

      PUSH (NULL, NULL);

      while (STACK_NOT_EMPTY)
        {
          char *left_ptr;
          char *right_ptr;

          /* Select median value from among LO, MID, and HI. Rearrange
             LO and HI so the three values are sorted. This lowers the
             probability of picking a pathological pivot value and
             skips a comparison for both the LEFT_PTR and RIGHT_PTR. */

          char *mid = lo + size * ((hi - lo) / size >> 1);

          if ((*cmp) ((void *) mid, (void *) lo, user_data) < 0)
            SWAP (mid, lo, size);
          if ((*cmp) ((void *) hi, (void *) mid, user_data) < 0)
            SWAP (mid, hi, size);
          else
            goto jump_over;
          if ((*cmp) ((void *) mid, (void *) lo, user_data) < 0)
            SWAP (mid, lo, size);
        jump_over:;
          left_ptr  = lo + size;
          right_ptr = hi - size;

          /* Here's the famous ``collapse the walls'' section of quicksort.
             Gotta like those tight inner loops!  They are the main reason
             that this algorithm runs much faster than others. */
          do
            {
              while ((*cmp) ((void *) left_ptr, (void *) mid, user_data) < 0)
                left_ptr += size;

              while ((*cmp) ((void *) mid, (void *) right_ptr, user_data) < 0)
                right_ptr -= size;

              if (left_ptr < right_ptr)
                {
                  SWAP (left_ptr, right_ptr, size);
                  if (mid == left_ptr)
                    mid = right_ptr;
                  else if (mid == right_ptr)
                    mid = left_ptr;
                  left_ptr += size;
                  right_ptr -= size;
                }
              else if (left_ptr == right_ptr)
                {
                  left_ptr += size;
                  right_ptr -= size;
                  break;
                }
            }
          while (left_ptr <= right_ptr);

          /* Set up pointers for next iteration.  First determine whether
             left and right partitions are below the threshold size.  If so,
             ignore one or both.  Otherwise, push the larger partition's
             bounds on the stack and continue sorting the smaller one. */

          if ((size_t) (right_ptr - lo) <= max_thresh)
            {
              if ((size_t) (hi - left_ptr) <= max_thresh)
                /* Ignore both small partitions. */
                POP (lo, hi);
              else
                /* Ignore small left partition. */
                lo = left_ptr;
            }
          else if ((size_t) (hi - left_ptr) <= max_thresh)
            /* Ignore small right partition. */
            hi = right_ptr;
          else if ((right_ptr - lo) > (hi - left_ptr))
            {
              /* Push larger left partition indices. */
              PUSH (lo, right_ptr);
              lo = left_ptr;
            }
          else
            {
              /* Push larger right partition indices. */
              PUSH (left_ptr, hi);
              hi = right_ptr;
            }
        }
    }

  /* Once the BASE_PTR array is partially sorted by quicksort the rest
     is completely sorted using insertion sort, since this is efficient
     for partitions below MAX_THRESH size. BASE_PTR points to the beginning
     of the array to sort, and END_PTR points at the very last element in
     the array (*not* one beyond it!). */

  {
    char *const end_ptr = &base_ptr[size * (total_elems - 1)];
    char *tmp_ptr = base_ptr;
    char *thresh = base_ptr + max_thresh;
    if ( thresh > end_ptr )
        thresh = end_ptr;
    register char *run_ptr;

    /* Find smallest element in first threshold and place it at the
       array's beginning.  This is the smallest array element,
       and the operation speeds up insertion sort's inner loop. */

    for (run_ptr = tmp_ptr + size; run_ptr <= thresh; run_ptr += size)
      if ((*cmp) ((void *) run_ptr, (void *) tmp_ptr, user_data) < 0)
        tmp_ptr = run_ptr;

    if (tmp_ptr != base_ptr)
      SWAP (tmp_ptr, base_ptr, size);

    /* Insertion sort, running from left-hand-side up to right-hand-side.  */

    run_ptr = base_ptr + size;
    while ((run_ptr += size) <= end_ptr)
      {
        tmp_ptr = run_ptr - size;
        while ((*cmp) ((void *) run_ptr, (void *) tmp_ptr, user_data) < 0)
          tmp_ptr -= size;

        tmp_ptr += size;
        if (tmp_ptr != run_ptr)
          {
            char *trav;

            trav = run_ptr + size;
            while (--trav >= run_ptr)
              {
                char c = *trav;
                char *hi, *lo;

                for (hi = lo = trav; (lo -= size) >= tmp_ptr; hi = lo)
                  *hi = *lo;
                *hi = c;
              }
          }
      }
  }
}



#endif // wxUSE_BASE

// ============================================================================
// GUI-only functions from now on
// ============================================================================

#if wxUSE_GUI

// ----------------------------------------------------------------------------
// Launch document with default app
// ----------------------------------------------------------------------------

bool wxLaunchDefaultApplication(const wxString& document, int flags)
{
    wxUnusedVar(flags);

#ifdef __WXMAC__
    static const char * const OPEN_CMD = "/usr/bin/open";
    if ( wxFileExists(OPEN_CMD) &&
            wxExecute(wxString(OPEN_CMD) + " " + document) )
        return true;
#elif defined(__UNIX__)
    // Our best best is to use xdg-open from freedesktop.org cross-desktop
    // compatibility suite xdg-utils
    // (see http://portland.freedesktop.org/wiki/) -- this is installed on
    // most modern distributions and may be tweaked by them to handle
    // distribution specifics.
    wxString path, xdg_open;
    if ( wxGetEnv("PATH", &path) &&
         wxFindFileInPath(&xdg_open, path, "xdg-open") )
    {
        if ( wxExecute(xdg_open + " " + document) )
            return true;
    }
#elif defined(__WXMSW__)
    const INT_PTR result = (INT_PTR)::ShellExecute
                                      (
                                        NULL,           // parent window
                                        _T("open"),
                                        document.wx_str(),
                                        NULL,           // parameters
                                        NULL,           // working directory
                                        SW_SHOWDEFAULT
                                      );
    if ( result > 32 )
        return true;
#endif

    return false;
}

// ----------------------------------------------------------------------------
// Launch default browser
// ----------------------------------------------------------------------------

#ifdef __WXCOCOA__
// Private method in Objective-C++ source file.
bool wxCocoaLaunchDefaultBrowser(const wxString& url, int flags);
#endif

static bool DoLaunchDefaultBrowser(const wxString& urlOrig, int flags)
{
    wxUnusedVar(flags);

    // set the scheme of url to http if it does not have one
    // RR: This doesn't work if the url is just a local path
    wxString url(urlOrig);
    wxURI uri(url);
    if ( !uri.HasScheme() )
    {
        if (wxFileExists(urlOrig))
            url.Prepend( wxT("file://") );
        else
            url.Prepend(wxT("http://"));
    }


#if defined(__WXMSW__)

#if wxUSE_IPC
    if ( flags & wxBROWSER_NEW_WINDOW )
    {
        // ShellExecuteEx() opens the URL in an existing window by default so
        // we can't use it if we need a new window
        wxRegKey key(wxRegKey::HKCR, uri.GetScheme() + _T("\\shell\\open"));
        if ( !key.Exists() )
        {
            // try default browser, it must be registered at least for http URLs
            key.SetName(wxRegKey::HKCR, _T("http\\shell\\open"));
        }

        if ( key.Exists() )
        {
            wxRegKey keyDDE(key, wxT("DDEExec"));
            if ( keyDDE.Exists() )
            {
                // we only know the syntax of WWW_OpenURL DDE request for IE,
                // optimistically assume that all other browsers are compatible
                // with it
                static const wxChar *TOPIC_OPEN_URL = wxT("WWW_OpenURL");
                wxString ddeCmd;
                wxRegKey keyTopic(keyDDE, wxT("topic"));
                bool ok = keyTopic.Exists() &&
                            keyTopic.QueryDefaultValue() == TOPIC_OPEN_URL;
                if ( ok )
                {
                    ddeCmd = keyDDE.QueryDefaultValue();
                    ok = !ddeCmd.empty();
                }

                if ( ok )
                {
                    // for WWW_OpenURL, the index of the window to open the URL
                    // in is -1 (meaning "current") by default, replace it with
                    // 0 which means "new" (see KB article 160957)
                    ok = ddeCmd.Replace(wxT("-1"), wxT("0"),
                                        false /* only first occurrence */) == 1;
                }

                if ( ok )
                {
                    // and also replace the parameters: the topic should
                    // contain a placeholder for the URL
                    ok = ddeCmd.Replace(wxT("%1"), url, false) == 1;
                }

                if ( ok )
                {
                    // try to send it the DDE request now but ignore the errors
                    wxLogNull noLog;

                    const wxString ddeServer = wxRegKey(keyDDE, wxT("application"));
                    if ( wxExecuteDDE(ddeServer, TOPIC_OPEN_URL, ddeCmd) )
                        return true;

                    // this is not necessarily an error: maybe browser is
                    // simply not running, but no matter, in any case we're
                    // going to launch it using ShellExecuteEx() below now and
                    // we shouldn't try to open a new window if we open a new
                    // browser anyhow
                }
            }
        }
    }
#endif // wxUSE_IPC

    WinStruct<SHELLEXECUTEINFO> sei;
    sei.lpFile = url.c_str();
    sei.lpVerb = _T("open");
    sei.nShow = SW_SHOWNORMAL;
    sei.fMask = SEE_MASK_FLAG_NO_UI; // we give error message ourselves

    ::ShellExecuteEx(&sei);

    const INT_PTR nResult = (INT_PTR)sei.hInstApp;

    // Firefox returns file not found for some reason, so make an exception
    // for it
    if ( nResult > 32 || nResult == SE_ERR_FNF )
    {
#ifdef __WXDEBUG__
        // Log something if SE_ERR_FNF happens
        if ( nResult == SE_ERR_FNF )
            wxLogDebug(wxT("SE_ERR_FNF from ShellExecute -- maybe FireFox?"));
#endif // __WXDEBUG__
        return true;
    }
#elif defined(__WXCOCOA__)
    // NOTE: We need to call the real implementation from src/cocoa/utils.mm
    // because the code must use Objective-C features.
    return wxCocoaLaunchDefaultBrowser(url, flags);
#elif defined(__WXMAC__) && !defined(__WXOSX_IPHONE__)
    wxCFRef< CFURLRef > curl( CFURLCreateWithString( kCFAllocatorDefault,
            wxCFStringRef( url ), NULL ) );
    OSStatus err = LSOpenCFURLRef( curl , NULL );

    if (err == noErr)
    {
        return true;
    }
    else
    {
        wxLogDebug(wxT("Browser Launch error %d"), (int) err);
        return false;
    }
#else
    // (non-Mac, non-MSW)

#ifdef __UNIX__

    // Our best best is to use xdg-open from freedesktop.org cross-desktop
    // compatibility suite xdg-utils
    // (see http://portland.freedesktop.org/wiki/) -- this is installed on
    // most modern distributions and may be tweaked by them to handle
    // distribution specifics. Only if that fails, try to find the right
    // browser ourselves.
    wxString path, xdg_open;
    if ( wxGetEnv("PATH", &path) &&
         wxFindFileInPath(&xdg_open, path, "xdg-open") )
    {
        if ( wxExecute(xdg_open + " " + url) )
            return true;
    }

    wxString desktop = wxTheApp->GetTraits()->GetDesktopEnvironment();

    // GNOME and KDE desktops have some applications which should be always installed
    // together with their main parts, which give us the
    if (desktop == wxT("GNOME"))
    {
        wxArrayString errors;
        wxArrayString output;

        // gconf will tell us the path of the application to use as browser
        long res = wxExecute( wxT("gconftool-2 --get /desktop/gnome/applications/browser/exec"),
                              output, errors, wxEXEC_NODISABLE );
        if (res >= 0 && errors.GetCount() == 0)
        {
            wxString cmd = output[0];
            cmd << _T(' ') << url;
            if (wxExecute(cmd))
                return true;
        }
    }
    else if (desktop == wxT("KDE"))
    {
        // kfmclient directly opens the given URL
        if (wxExecute(wxT("kfmclient openURL ") + url))
            return true;
    }
#endif

    bool ok = false;
    wxString cmd;

#if wxUSE_MIMETYPE
    wxFileType *ft = wxTheMimeTypesManager->GetFileTypeFromExtension(_T("html"));
    if ( ft )
    {
        wxString mt;
        ft->GetMimeType(&mt);

        ok = ft->GetOpenCommand(&cmd, wxFileType::MessageParameters(url));
        delete ft;
    }
#endif // wxUSE_MIMETYPE

    if ( !ok || cmd.empty() )
    {
        // fallback to checking for the BROWSER environment variable
        cmd = wxGetenv(wxT("BROWSER"));
        if ( !cmd.empty() )
            cmd << _T(' ') << url;
    }

    ok = ( !cmd.empty() && wxExecute(cmd) );
    if (ok)
        return ok;

    // no file type for HTML extension
    wxLogError(_("No default application configured for HTML files."));

#endif // !wxUSE_MIMETYPE && !__WXMSW__

    wxLogSysError(_("Failed to open URL \"%s\" in default browser."),
                  url.c_str());

    return false;
}

bool wxLaunchDefaultBrowser(const wxString& url, int flags)
{
    if ( flags & wxBROWSER_NOBUSYCURSOR )
        return DoLaunchDefaultBrowser(url, flags);

    wxBusyCursor bc;
    return DoLaunchDefaultBrowser(url, flags);
}

// ----------------------------------------------------------------------------
// Menu accelerators related functions
// ----------------------------------------------------------------------------

wxChar *wxStripMenuCodes(const wxChar *in, wxChar *out)
{
#if wxUSE_MENUS
    wxString s = wxMenuItem::GetLabelText(in);
#else
    wxString str(in);
    wxString s = wxStripMenuCodes(str);
#endif // wxUSE_MENUS
    if ( out )
    {
        // go smash their buffer if it's not big enough - I love char * params
        memcpy(out, s.c_str(), s.length() * sizeof(wxChar));
    }
    else
    {
        out = new wxChar[s.length() + 1];
        wxStrcpy(out, s.c_str());
    }

    return out;
}

wxString wxStripMenuCodes(const wxString& in, int flags)
{
    wxASSERT_MSG( flags, _T("this is useless to call without any flags") );

    wxString out;

    size_t len = in.length();
    out.reserve(len);

    for ( size_t n = 0; n < len; n++ )
    {
        wxChar ch = in[n];
        if ( (flags & wxStrip_Mnemonics) && ch == _T('&') )
        {
            // skip it, it is used to introduce the accel char (or to quote
            // itself in which case it should still be skipped): note that it
            // can't be the last character of the string
            if ( ++n == len )
            {
                wxLogDebug(_T("Invalid menu string '%s'"), in.c_str());
            }
            else
            {
                // use the next char instead
                ch = in[n];
            }
        }
        else if ( (flags & wxStrip_Accel) && ch == _T('\t') )
        {
            // everything after TAB is accel string, exit the loop
            break;
        }

        out += ch;
    }

    return out;
}

// ----------------------------------------------------------------------------
// Window search functions
// ----------------------------------------------------------------------------

/*
 * If parent is non-NULL, look through children for a label or title
 * matching the specified string. If NULL, look through all top-level windows.
 *
 */

wxWindow *
wxFindWindowByLabel (const wxString& title, wxWindow * parent)
{
    return wxWindow::FindWindowByLabel( title, parent );
}


/*
 * If parent is non-NULL, look through children for a name
 * matching the specified string. If NULL, look through all top-level windows.
 *
 */

wxWindow *
wxFindWindowByName (const wxString& name, wxWindow * parent)
{
    return wxWindow::FindWindowByName( name, parent );
}

// Returns menu item id or wxNOT_FOUND if none.
int
wxFindMenuItemId(wxFrame *frame,
                 const wxString& menuString,
                 const wxString& itemString)
{
#if wxUSE_MENUS
    wxMenuBar *menuBar = frame->GetMenuBar ();
    if ( menuBar )
        return menuBar->FindMenuItem (menuString, itemString);
#else // !wxUSE_MENUS
    wxUnusedVar(frame);
    wxUnusedVar(menuString);
    wxUnusedVar(itemString);
#endif // wxUSE_MENUS/!wxUSE_MENUS

    return wxNOT_FOUND;
}

// Try to find the deepest child that contains 'pt'.
// We go backwards, to try to allow for controls that are spacially
// within other controls, but are still siblings (e.g. buttons within
// static boxes). Static boxes are likely to be created _before_ controls
// that sit inside them.
wxWindow* wxFindWindowAtPoint(wxWindow* win, const wxPoint& pt)
{
    if (!win->IsShown())
        return NULL;

    // Hack for wxNotebook case: at least in wxGTK, all pages
    // claim to be shown, so we must only deal with the selected one.
#if wxUSE_NOTEBOOK
    if (win->IsKindOf(CLASSINFO(wxNotebook)))
    {
      wxNotebook* nb = (wxNotebook*) win;
      int sel = nb->GetSelection();
      if (sel >= 0)
      {
        wxWindow* child = nb->GetPage(sel);
        wxWindow* foundWin = wxFindWindowAtPoint(child, pt);
        if (foundWin)
           return foundWin;
      }
    }
#endif

    wxWindowList::compatibility_iterator node = win->GetChildren().GetLast();
    while (node)
    {
        wxWindow* child = node->GetData();
        wxWindow* foundWin = wxFindWindowAtPoint(child, pt);
        if (foundWin)
          return foundWin;
        node = node->GetPrevious();
    }

    wxPoint pos = win->GetPosition();
    wxSize sz = win->GetSize();
    if ( !win->IsTopLevel() && win->GetParent() )
    {
        pos = win->GetParent()->ClientToScreen(pos);
    }

    wxRect rect(pos, sz);
    if (rect.Contains(pt))
        return win;

    return NULL;
}

wxWindow* wxGenericFindWindowAtPoint(const wxPoint& pt)
{
    // Go backwards through the list since windows
    // on top are likely to have been appended most
    // recently.
    wxWindowList::compatibility_iterator node = wxTopLevelWindows.GetLast();
    while (node)
    {
        wxWindow* win = node->GetData();
        wxWindow* found = wxFindWindowAtPoint(win, pt);
        if (found)
            return found;
        node = node->GetPrevious();
    }
    return NULL;
}

// ----------------------------------------------------------------------------
// GUI helpers
// ----------------------------------------------------------------------------

/*
 * N.B. these convenience functions must be separate from msgdlgg.cpp, textdlgg.cpp
 * since otherwise the generic code may be pulled in unnecessarily.
 */

#if wxUSE_MSGDLG

int wxMessageBox(const wxString& message, const wxString& caption, long style,
                 wxWindow *parent, int WXUNUSED(x), int WXUNUSED(y) )
{
    long decorated_style = style;

    if ( ( style & ( wxICON_EXCLAMATION | wxICON_HAND | wxICON_INFORMATION | wxICON_QUESTION ) ) == 0 )
    {
        decorated_style |= ( style & wxYES ) ? wxICON_QUESTION : wxICON_INFORMATION ;
    }

    wxMessageDialog dialog(parent, message, caption, decorated_style);

    int ans = dialog.ShowModal();
    switch ( ans )
    {
        case wxID_OK:
            return wxOK;
        case wxID_YES:
            return wxYES;
        case wxID_NO:
            return wxNO;
        case wxID_CANCEL:
            return wxCANCEL;
    }

    wxFAIL_MSG( _T("unexpected return code from wxMessageDialog") );

    return wxCANCEL;
}

void wxInfoMessageBox(wxWindow* parent)
{
    // don't translate these strings, they're for diagnostics purposes only
    wxString msg;
    msg.Printf(_T("wxWidgets Library (%s port)\n")
               _T("Version %d.%d.%d%s%s, compiled at %s %s\n")
               _T("Runtime version of toolkit used is %d.%d.%s\n")
               _T("Copyright (c) 1995-2008 wxWidgets team"),
               wxPlatformInfo::Get().GetPortIdName().c_str(),
               wxMAJOR_VERSION,
               wxMINOR_VERSION,
               wxRELEASE_NUMBER,
#if wxUSE_UNICODE
               L" (Unicode)",
#else
               wxEmptyString,
#endif
#ifdef __WXDEBUG__
               _T(" Debug build"),
#else
               wxEmptyString,
#endif
               __TDATE__,
               __TTIME__,
               wxPlatformInfo::Get().GetToolkitMajorVersion(),
               wxPlatformInfo::Get().GetToolkitMinorVersion(),
#ifdef __WXGTK__
               wxString::Format("\nThe compile-time GTK+ version is %d.%d.%d.",
                                GTK_MAJOR_VERSION,
                                GTK_MINOR_VERSION,
                                GTK_MICRO_VERSION).c_str()
#else
               wxEmptyString
#endif
               );
    wxMessageBox(msg, _T("wxWidgets information"),
                 wxICON_INFORMATION | wxOK,
                 parent);
}

#endif // wxUSE_MSGDLG

#if wxUSE_TEXTDLG

wxString wxGetTextFromUser(const wxString& message, const wxString& caption,
                        const wxString& defaultValue, wxWindow *parent,
                        wxCoord x, wxCoord y, bool centre )
{
    wxString str;
    long style = wxTextEntryDialogStyle;

    if (centre)
        style |= wxCENTRE;
    else
        style &= ~wxCENTRE;

    wxTextEntryDialog dialog(parent, message, caption, defaultValue, style, wxPoint(x, y));

    if (dialog.ShowModal() == wxID_OK)
    {
        str = dialog.GetValue();
    }

    return str;
}

wxString wxGetPasswordFromUser(const wxString& message,
                               const wxString& caption,
                               const wxString& defaultValue,
                               wxWindow *parent,
                               wxCoord x, wxCoord y, bool centre )
{
    wxString str;
    long style = wxTextEntryDialogStyle;

    if (centre)
        style |= wxCENTRE;
    else
        style &= ~wxCENTRE;

    wxPasswordEntryDialog dialog(parent, message, caption, defaultValue,
                             style, wxPoint(x, y));
    if ( dialog.ShowModal() == wxID_OK )
    {
        str = dialog.GetValue();
    }

    return str;
}

#endif // wxUSE_TEXTDLG

#if wxUSE_COLOURDLG

wxColour wxGetColourFromUser(wxWindow *parent,
                             const wxColour& colInit,
                             const wxString& caption,
                             wxColourData *ptrData)
{
    // contains serialized representation of wxColourData used the last time
    // the dialog was shown: we want to reuse it the next time in order to show
    // the same custom colours to the user (and we can't just have static
    // wxColourData itself because it's a GUI object and so should be destroyed
    // before GUI shutdown and doing it during static cleanup is too late)
    static wxString s_strColourData;

    wxColourData data;
    if ( !ptrData )
    {
        ptrData = &data;
        if ( !s_strColourData.empty() )
        {
            if ( !data.FromString(s_strColourData) )
            {
                wxFAIL_MSG( "bug in wxColourData::FromString()?" );
            }

#ifdef __WXMSW__
            // we don't get back the "choose full" flag value from the native
            // dialog and so we can't preserve it between runs, so we decide to
            // always use it as it seems better than not using it (user can
            // just ignore the extra controls in the dialog but having to click
            // a button each time to show them would be very annoying
            data.SetChooseFull(true);
#endif // __WXMSW__
        }
    }

    if ( colInit.IsOk() )
    {
        ptrData->SetColour(colInit);
    }

    wxColour colRet;
    wxColourDialog dialog(parent, ptrData);
    if (!caption.empty())
        dialog.SetTitle(caption);
    if ( dialog.ShowModal() == wxID_OK )
    {
        *ptrData = dialog.GetColourData();
        colRet = ptrData->GetColour();
        s_strColourData = ptrData->ToString();
    }
    //else: leave colRet invalid

    return colRet;
}

#endif // wxUSE_COLOURDLG

#if wxUSE_FONTDLG

wxFont wxGetFontFromUser(wxWindow *parent, const wxFont& fontInit, const wxString& caption)
{
    wxFontData data;
    if ( fontInit.Ok() )
    {
        data.SetInitialFont(fontInit);
    }

    wxFont fontRet;
    wxFontDialog dialog(parent, data);
    if (!caption.empty())
        dialog.SetTitle(caption);
    if ( dialog.ShowModal() == wxID_OK )
    {
        fontRet = dialog.GetFontData().GetChosenFont();
    }
    //else: leave it invalid

    return fontRet;
}

#endif // wxUSE_FONTDLG

// ----------------------------------------------------------------------------
// wxSafeYield and supporting functions
// ----------------------------------------------------------------------------

void wxEnableTopLevelWindows(bool enable)
{
    wxWindowList::compatibility_iterator node;
    for ( node = wxTopLevelWindows.GetFirst(); node; node = node->GetNext() )
        node->GetData()->Enable(enable);
}

wxWindowDisabler::wxWindowDisabler(bool disable)
{
    m_disabled = disable;
    if ( disable )
        DoDisable();
}

wxWindowDisabler::wxWindowDisabler(wxWindow *winToSkip)
{
    m_disabled = true;
    DoDisable(winToSkip);
}

void wxWindowDisabler::DoDisable(wxWindow *winToSkip)
{
    // remember the top level windows which were already disabled, so that we
    // don't reenable them later
    m_winDisabled = NULL;

    wxWindowList::compatibility_iterator node;
    for ( node = wxTopLevelWindows.GetFirst(); node; node = node->GetNext() )
    {
        wxWindow *winTop = node->GetData();
        if ( winTop == winToSkip )
            continue;

        // we don't need to disable the hidden or already disabled windows
        if ( winTop->IsEnabled() && winTop->IsShown() )
        {
            winTop->Disable();
        }
        else
        {
            if ( !m_winDisabled )
            {
                m_winDisabled = new wxWindowList;
            }

            m_winDisabled->Append(winTop);
        }
    }
}

wxWindowDisabler::~wxWindowDisabler()
{
    if ( !m_disabled )
        return;

    wxWindowList::compatibility_iterator node;
    for ( node = wxTopLevelWindows.GetFirst(); node; node = node->GetNext() )
    {
        wxWindow *winTop = node->GetData();
        if ( !m_winDisabled || !m_winDisabled->Find(winTop) )
        {
            winTop->Enable();
        }
        //else: had been already disabled, don't reenable
    }

    delete m_winDisabled;
}

// Yield to other apps/messages and disable user input to all windows except
// the given one
bool wxSafeYield(wxWindow *win, bool onlyIfNeeded)
{
    wxWindowDisabler wd(win);

    bool rc;
    if (onlyIfNeeded)
        rc = wxYieldIfNeeded();
    else
        rc = wxYield();

    return rc;
}

// Don't synthesize KeyUp events holding down a key and producing KeyDown
// events with autorepeat. On by default and always on in wxMSW. wxGTK version
// in utilsgtk.cpp.
#ifndef __WXGTK__
bool wxSetDetectableAutoRepeat( bool WXUNUSED(flag) )
{
    return true;    // detectable auto-repeat is the only mode MSW supports
}
#endif // !wxGTK

#endif // wxUSE_GUI
