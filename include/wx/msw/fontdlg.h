/////////////////////////////////////////////////////////////////////////////
// Name:        fontdlg.h
// Purpose:     wxFontDialog class
// Author:      Julian Smart
// Modified by:
// Created:     01/02/97
// RCS-ID:      $Id$
// Copyright:   (c) Julian Smart
// Licence:     wxWidgets licence
/////////////////////////////////////////////////////////////////////////////

#ifndef _WX_MSW_FONTDLG_H_
#define _WX_MSW_FONTDLG_H_

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
    #pragma interface "fontdlg.h"
#endif

// ----------------------------------------------------------------------------
// wxFontDialog
// ----------------------------------------------------------------------------

class WXDLLEXPORT wxFontDialog : public wxFontDialogBase
{
public:
    wxFontDialog() : wxFontDialogBase() { /* must be Create()d later */ }
    wxFontDialog(wxWindow *parent)
        : wxFontDialogBase(parent) { Create(parent); }
    wxFontDialog(wxWindow *parent, const wxFontData& data)
        : wxFontDialogBase(parent, data) { Create(parent, data); }

    virtual int ShowModal();

    // deprecated interface, don't use
    wxFontDialog(wxWindow *parent, const wxFontData *data)
        : wxFontDialogBase(parent, data) { Create(parent, data); }

protected:
    DECLARE_DYNAMIC_CLASS_NO_COPY(wxFontDialog)
};

#endif
    // _WX_MSW_FONTDLG_H_

