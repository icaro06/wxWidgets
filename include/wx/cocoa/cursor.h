/////////////////////////////////////////////////////////////////////////////
// Name:        wx/cocoa/cursor.h
// Purpose:     wxCursor class
// Author:      David Elliott <dfe@cox.net>
// Modified by:
// Created:     2002/11/27
// RCS-ID:      $Id$
// Copyright:   (c) David Elliott
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

#ifndef _WX_COCOA_CURSOR_H_
#define _WX_COCOA_CURSOR_H_

#include "wx/bitmap.h"

class WXDLLEXPORT wxCursorRefData : public wxGDIRefData
{
public:
    wxCursorRefData();
    virtual ~wxCursorRefData();

protected:
    int m_width, m_height;
    WX_NSCursor m_hCursor;

    friend class WXDLLIMPEXP_FWD_CORE wxBitmap;
    friend class WXDLLIMPEXP_FWD_CORE wxCursor;

    DECLARE_NO_COPY_CLASS(wxCursorRefData)
};

#define M_CURSORDATA ((wxCursorRefData *)m_refData)
#define M_CURSORHANDLERDATA ((wxCursorRefData *)bitmap->m_refData)

// Cursor
class WXDLLEXPORT wxCursor: public wxBitmap
{
public:
    wxCursor();

    wxCursor(const char bits[], int width, int height,
             int hotSpotX = -1, int hotSpotY = -1,
             const char maskBits[] = NULL);

    wxCursor(const wxString& name, long flags = 0,
             int hotSpotX = 0, int hotSpotY = 0);

    wxCursor(int cursor_type);
    virtual ~wxCursor();

    // FIXME: operator==() is wrong!
    bool operator==(const wxCursor& cursor) const { return m_refData == cursor.m_refData; }
    bool operator!=(const wxCursor& cursor) const { return !(*this == cursor); }

    WX_NSCursor GetNSCursor() const { return M_CURSORDATA ? M_CURSORDATA->m_hCursor : 0; }

    DECLARE_DYNAMIC_CLASS(wxCursor)
};

extern WXDLLEXPORT void wxSetCursor(const wxCursor& cursor);

#endif
    // _WX_COCOA_CURSOR_H_
