/////////////////////////////////////////////////////////////////////////////
// Name:        dirdlg.cpp
// Purpose:     wxDirDialog
// Author:      Julian Smart
// Modified by:
// Created:     01/02/97
// RCS-ID:      $Id$
// Copyright:   (c) Julian Smart and Markus Holzem
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

// ============================================================================
// declarations
// ============================================================================

// ----------------------------------------------------------------------------
// headers
// ----------------------------------------------------------------------------

#ifdef __GNUG__
    #pragma implementation "dirdlg.h"
#endif

// For compilers that support precompilation, includes "wx.h".
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

#if wxUSE_DIRDLG

#if defined(__WIN95__) && !defined(__GNUWIN32_OLD__) && wxUSE_OLE

#ifndef WX_PRECOMP
    #include "wx/utils.h"
    #include "wx/dialog.h"
    #include "wx/dirdlg.h"
    #include "wx/log.h"
    #include "wx/app.h"     // for GetComCtl32Version()
#endif

#include "wx/msw/private.h"

#include <shlobj.h> // Win95 shell

// ----------------------------------------------------------------------------
// constants
// ----------------------------------------------------------------------------

#ifndef MAX_PATH
    #define MAX_PATH 4096      // be generous
#endif

#ifndef BIF_NEWDIALOGSTYLE
    #define BIF_NEWDIALOGSTYLE 0x0040
#endif

#ifndef BIF_NONEWFOLDERBUTTON
    #define BIF_NONEWFOLDERBUTTON  0x0200
#endif

// ----------------------------------------------------------------------------
// wxWindows macros
// ----------------------------------------------------------------------------

IMPLEMENT_CLASS(wxDirDialog, wxDialog)

// ----------------------------------------------------------------------------
// private functions prototypes
// ----------------------------------------------------------------------------

// free the parameter
static void ItemListFree(LPITEMIDLIST pidl);

// the callback proc for the dir dlg
static int CALLBACK BrowseCallbackProc(HWND hwnd, UINT uMsg, LPARAM lp,
                                       LPARAM pData);


// ============================================================================
// implementation
// ============================================================================

// ----------------------------------------------------------------------------
// wxDirDialog
// ----------------------------------------------------------------------------

wxDirDialog::wxDirDialog(wxWindow *parent,
                         const wxString& message,
                         const wxString& defaultPath,
                         long style,
                         const wxPoint& WXUNUSED(pos),
                         const wxSize& WXUNUSED(size),
                         const wxString& WXUNUSED(name))
{
    m_message = message;
    m_parent = parent;

    SetStyle(style);
    SetPath(defaultPath);
}

void wxDirDialog::SetPath(const wxString& path)
{
    m_path = path;

    // SHBrowseForFolder doesn't like '/'s nor the trailing backslashes
    m_path.Replace(_T("/"), _T("\\"));
    if ( !m_path.empty() )
    {
        while ( *(m_path.end() - 1) == _T('\\') )
        {
            m_path.erase(m_path.length() - 1);
        }

        // but the root drive should have a trailing slash (again, this is just
        // the way the native dialog works)
        if ( *(m_path.end() - 1) == _T(':') )
        {
            m_path += _T('\\');
        }
    }
}

int wxDirDialog::ShowModal()
{
    wxWindow *parent = GetParent();

    BROWSEINFO bi;
    bi.hwndOwner      = parent ? GetHwndOf(parent) : NULL;
    bi.pidlRoot       = NULL;
    bi.pszDisplayName = NULL;
    bi.lpszTitle      = m_message.c_str();
    bi.ulFlags        = BIF_RETURNONLYFSDIRS | BIF_STATUSTEXT;
    bi.lpfn           = BrowseCallbackProc;
    bi.lParam         = (LPARAM)m_path.c_str();    // param for the callback

    static const int verComCtl32 = wxApp::GetComCtl32Version();

    // we always add the edit box (it doesn't hurt anybody, does it?) if it is
    // supported by the system
    if ( verComCtl32 >= 471 )
    {
        bi.ulFlags |= BIF_EDITBOX;
    }

    // normally the commented out part should work -- but in practice
    // BIF_NONEWFOLDERBUTTON doesn't have any effect (Win2k, comctl 5.81) so I
    // have to disable it [for now]
#if 0
    // to have the "New Folder" button we must use the "new" dialog style which
    // is also the only way to have a resizable dialog
    //
    // "new" style is only available in the version 5.0+ of comctl32.dll
    const bool needNewDir = HasFlag(wxDD_NEW_DIR_BUTTON);
    if ( (needNewDir || HasFlag(wxRESIZE_BORDER)) && (verComCtl32 >= 500) )
    {
        bi.ulFlags |= BIF_NEWDIALOGSTYLE;

        // we'll get the "New Folder" button by default now, don't show it if
        // not needed
        if ( !needNewDir )
            bi.ulFlags |= BIF_NONEWFOLDERBUTTON;
    }
#else
    if ( HasFlag(wxDD_NEW_DIR_BUTTON) && verComCtl32 >= 500 )
    {
        // use the new style to make the "New Folder" button appear
        bi.ulFlags |= BIF_NEWDIALOGSTYLE;
    }
#endif

    // do show the dialog
    LPITEMIDLIST pidl = SHBrowseForFolder(&bi);

    if ( bi.pidlRoot )
    {
        ItemListFree((LPITEMIDLIST)bi.pidlRoot);
    }

    if ( !pidl )
    {
        // Cancel button pressed
        return wxID_CANCEL;
    }

    BOOL ok = SHGetPathFromIDList(pidl, wxStringBuffer(m_path, MAX_PATH));

    ItemListFree(pidl);

    if ( !ok )
    {
        wxLogLastError(wxT("SHGetPathFromIDList"));

        return wxID_CANCEL;
    }

    return wxID_OK;
}

// ----------------------------------------------------------------------------
// private functions
// ----------------------------------------------------------------------------

static int CALLBACK
BrowseCallbackProc(HWND hwnd, UINT uMsg, LPARAM lp, LPARAM pData)
{
    switch(uMsg)
    {
        case BFFM_INITIALIZED:
            // sent immediately after initialisation and so we may set the
            // initial selection here
            //
            // wParam = TRUE => lParam is a string and not a PIDL
            SendMessage(hwnd, BFFM_SETSELECTION, TRUE, pData);
            break;

        case BFFM_SELCHANGED:
            // note that this doesn't work with the new style UI (MSDN doesn't
            // say anything about it, but the comments in shlobj.h do!) but we
            // still execute this code in case it starts working again with the
            // "new new UI" (or would it be "NewUIEx" according to tradition?)
            {
                // Set the status window to the currently selected path.
                wxString strDir;
                if ( SHGetPathFromIDList((LPITEMIDLIST)lp,
                                         wxStringBuffer(strDir, MAX_PATH)) )
                {
                    // NB: this shouldn't be necessary with the new style box
                    //     (which is resizable), but as for now it doesn't work
                    //     anyhow (see the comment above) no harm in doing it

                    // need to truncate or it displays incorrectly
                    static const size_t maxChars = 37;
                    if ( strDir.length() > maxChars )
                    {
                        strDir = strDir.Right(maxChars);
                        strDir = wxString(wxT("...")) + strDir;
                    }

                    SendMessage(hwnd, BFFM_SETSTATUSTEXT,
                                0, (LPARAM)strDir.c_str());
                }
            }
            break;

        //case BFFM_VALIDATEFAILED: -- might be used to provide custom message
        //                             if the user types in invalid dir name
    }

    return 0;
}


static void ItemListFree(LPITEMIDLIST pidl)
{
    if ( pidl )
    {
        LPMALLOC pMalloc;
        SHGetMalloc(&pMalloc);
        if ( pMalloc )
        {
            pMalloc->Free(pidl);
            pMalloc->Release();
        }
        else
        {
            wxLogLastError(wxT("SHGetMalloc"));
        }
    }
}

#else
    #include "../generic/dirdlgg.cpp"
#endif // compiler/platform on which the code here compiles

#endif // wxUSE_DIRDLG
