/////////////////////////////////////////////////////////////////////////////
// Name:        stream.h
// Purpose:     "wxWindows stream" base classes
// Author:      Guilhem Lavaux
// Modified by:
// Created:     11/07/98
// RCS-ID:      $Id$
// Copyright:   (c) Guilhem Lavaux
// Licence:     wxWindows license
/////////////////////////////////////////////////////////////////////////////

#ifndef _WX_WXSTREAM_H__
#define _WX_WXSTREAM_H__

#ifdef __GNUG__
#pragma interface
#endif

#include "wx/defs.h"

#if wxUSE_STREAMS

#include <stdio.h>
#include "wx/object.h"
#include "wx/string.h"
#include "wx/filefn.h"  // for off_t, wxInvalidOffset and wxSeekMode

class WXDLLEXPORT wxStreamBase;
class WXDLLEXPORT wxInputStream;
class WXDLLEXPORT wxOutputStream;

typedef wxInputStream& (*__wxInputManip)(wxInputStream&);
typedef wxOutputStream& (*__wxOutputManip)(wxOutputStream&);

WXDLLEXPORT wxOutputStream& wxEndL(wxOutputStream& o_stream);

// ---------------------------------------------------------------------------
// wxStream: base classes
// ---------------------------------------------------------------------------

#define wxStream_NOERROR    wxSTREAM_NOERROR
#define wxStream_EOF        wxSTREAM_EOF
#define wxStream_WRITE_ERR  wxSTREAM_WRITE_ERROR
#define wxStream_READ_ERR   wxSTREAM_READ_ERROR
  
typedef enum {
  wxSTREAM_NO_ERROR = 0,
  wxSTREAM_NO_ERR = wxSTREAM_NO_ERROR,
  wxSTREAM_NOERROR = wxSTREAM_NO_ERROR,
  
  wxSTREAM_EOF,
  
  wxSTREAM_WRITE_ERROR,
  wxSTREAM_WRITE_ERR = wxSTREAM_WRITE_ERROR,
  
  wxSTREAM_READ_ERROR,
  wxSTREAM_READ_ERR = wxSTREAM_READ_ERROR,
  
} wxStreamError;

class WXDLLEXPORT wxStreamBase 
{
public:
    wxStreamBase();
    virtual ~wxStreamBase();

    bool operator!() const { return (LastError() != wxSTREAM_NOERROR); }
    wxStreamError LastError() const { return m_lasterror; }
    virtual size_t GetSize() const { return ~((size_t)0); }
    size_t StreamSize() const { return GetSize(); }

protected:
    virtual size_t OnSysRead(void *buffer, size_t bufsize);
    virtual size_t OnSysWrite(const void *buffer, size_t bufsize);
    virtual off_t OnSysSeek(off_t seek, wxSeekMode mode);
    virtual off_t OnSysTell() const;

    friend class wxStreamBuffer;

    size_t m_lastcount;
    wxStreamError m_lasterror;
};

class WXDLLEXPORT wxInputStream: public wxStreamBase 
{
public:
    wxInputStream();
    virtual ~wxInputStream();

    // IO functions
    virtual char Peek();
    char GetC();
    virtual wxInputStream& Read(void *buffer, size_t size);
    wxInputStream& Read(wxOutputStream& stream_out);

    // Position functions
    virtual off_t SeekI(off_t pos, wxSeekMode mode = wxFromStart);
    virtual off_t TellI() const;

    // State functions
    virtual size_t LastRead() { return wxStreamBase::m_lastcount; }

    // Ungetch
    size_t Ungetch(const void *buffer, size_t size);
    bool Ungetch(char c);

    // Operators
    wxInputStream& operator>>(wxOutputStream& out) { return Read(out); }
#if wxUSE_SERIAL
    wxInputStream& operator>>(wxObject *& obj);
#endif
    wxInputStream& operator>>( __wxInputManip func) { return func(*this); }

protected:
    // Ungetch managers
    char *m_wback;
    size_t m_wbacksize;
    size_t m_wbackcur;

    char *AllocSpaceWBack(size_t needed_size);
    size_t GetWBack(char *buf, size_t bsize);
};

class WXDLLEXPORT wxOutputStream: public wxStreamBase 
{
public:
    wxOutputStream();
    virtual ~wxOutputStream();

    void PutC(char c);
    virtual wxOutputStream& Write(const void *buffer, size_t size);
    wxOutputStream& Write(wxInputStream& stream_in);

    virtual off_t SeekO(off_t pos, wxSeekMode mode = wxFromStart);
    virtual off_t TellO() const;

    virtual size_t LastWrite() const { return wxStreamBase::m_lastcount; }

    virtual void Sync();

    wxOutputStream& operator<<(wxInputStream& out) { return Write(out); }
#if wxUSE_SERIAL
    wxOutputStream& operator<<(wxObject& obj);
#endif
    wxOutputStream& operator<<( __wxOutputManip func) { return func(*this); }
};

// ---------------------------------------------------------------------------
// A stream for measuring streamed output
// ---------------------------------------------------------------------------

class wxCountingOutputStream: public wxOutputStream 
{
public:
    wxCountingOutputStream();

    size_t GetSize() const;
    bool Ok() const { return TRUE; }

protected:
    size_t OnSysWrite(const void *buffer, size_t size);
    off_t OnSysSeek(off_t pos, wxSeekMode mode);
    off_t OnSysTell() const;

    size_t m_currentPos;
};


// ---------------------------------------------------------------------------
// "Filter" streams
// ---------------------------------------------------------------------------

class WXDLLEXPORT wxFilterInputStream: public wxInputStream 
{
public:
    wxFilterInputStream();
    wxFilterInputStream(wxInputStream& stream);
    ~wxFilterInputStream();

    char Peek() { return m_parent_i_stream->Peek(); }

    size_t GetSize() const { return m_parent_i_stream->GetSize(); }

protected:
    wxInputStream *m_parent_i_stream;
};

class WXDLLEXPORT wxFilterOutputStream: public wxOutputStream 
{
public:
    wxFilterOutputStream();
    wxFilterOutputStream(wxOutputStream& stream);
    ~wxFilterOutputStream();

    size_t GetSize() const { return m_parent_o_stream->GetSize(); }

protected:
    wxOutputStream *m_parent_o_stream;
};

// ---------------------------------------------------------------------------
// Stream buffer
// ---------------------------------------------------------------------------

class WXDLLEXPORT wxStreamBuffer 
{
public:
    typedef enum {
        read = 0, write, read_write
    } BufMode;

    wxStreamBuffer(wxStreamBase& stream, BufMode mode);
    wxStreamBuffer(BufMode mode);
    wxStreamBuffer(const wxStreamBuffer& buf);
    ~wxStreamBuffer();

    // Filtered IO
    size_t Read(void *buffer, size_t size);
    size_t Read(wxStreamBuffer *buf);
    size_t Write(const void *buffer, size_t size);
    size_t Write(wxStreamBuffer *buf);

    char Peek();
    char GetChar();
    void PutChar(char c);
    off_t Tell() const;
    off_t Seek(off_t pos, wxSeekMode mode);

    // Buffer control
    void ResetBuffer();
    void SetBufferIO(char *buffer_start, char *buffer_end);
    void SetBufferIO(size_t bufsize);
    char *GetBufferStart() const { return m_buffer_start; }
    char *GetBufferEnd() const { return m_buffer_end; }
    char *GetBufferPos() const { return m_buffer_pos; }
    off_t GetIntPosition() const { return m_buffer_pos-m_buffer_start; }
    void SetIntPosition(off_t pos) { m_buffer_pos = m_buffer_start+pos; }
    size_t GetLastAccess() const { return m_buffer_end-m_buffer_start; }

    void Fixed(bool fixed) { m_fixed = fixed; }
    void Flushable(bool f) { m_flushable = f; }

    bool FlushBuffer();
    bool FillBuffer();
    size_t GetDataLeft();

    // Misc.
    wxStreamBase *Stream() { return m_stream; }

protected:
    void GetFromBuffer(void *buffer, size_t size);
    void PutToBuffer(const void *buffer, size_t size);

    char *m_buffer_start, *m_buffer_end, *m_buffer_pos;
    size_t m_buffer_size;

    bool m_fixed, m_flushable;

    wxStreamBase *m_stream;
    BufMode m_mode;
    bool m_destroybuf, m_destroystream;
};

// ---------------------------------------------------------------------------
// wxBufferedStreams
// ---------------------------------------------------------------------------

class wxBufferedInputStream: public wxFilterInputStream 
{
public:
    wxBufferedInputStream(wxInputStream& stream);
    ~wxBufferedInputStream();

    char Peek();
    wxInputStream& Read(void *buffer, size_t size);
  
    // Position functions
    off_t SeekI(off_t pos, wxSeekMode mode = wxFromStart);
    off_t TellI() const;

    wxStreamBuffer *InputStreamBuffer() const { return m_i_streambuf; }

protected:
    size_t OnSysRead(void *buffer, size_t bufsize);
    off_t OnSysSeek(off_t seek, wxSeekMode mode);
    off_t OnSysTell() const;  

    wxStreamBuffer *m_i_streambuf;
};

class wxBufferedOutputStream: public wxFilterOutputStream 
{
public:
    wxBufferedOutputStream(wxOutputStream& stream);
    ~wxBufferedOutputStream();

    wxOutputStream& Write(const void *buffer, size_t size);
  
    // Position functions
    off_t SeekO(off_t pos, wxSeekMode mode = wxFromStart);
    off_t TellO() const;

    void Sync();

    size_t GetSize() const;
  
    wxStreamBuffer *OutputStreamBuffer() const { return m_o_streambuf; }

protected:
    size_t OnSysWrite(const void *buffer, size_t bufsize);
    off_t OnSysSeek(off_t seek, wxSeekMode mode);
    off_t OnSysTell() const;  

    wxStreamBuffer *m_o_streambuf;
};

#endif
  // wxUSE_STREAMS

#endif
  // _WX_WXSTREAM_H__
