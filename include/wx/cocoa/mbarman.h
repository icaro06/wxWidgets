///////////////////////////////////////////////////////////////////////////////
// Name:        wx/cocoa/mbarman.h
// Purpose:     wxMenuBarManager class
// Author:      David Elliott
// Modified by:
// Created:     2003/09/04
// RCS-ID:      $Id$
// Copyright:   (c) 2003 David Elliott
// Licence:     wxWindows licence
///////////////////////////////////////////////////////////////////////////////

#ifndef __WX_COCOA_MBARMAN_H__
#define __WX_COCOA_MBARMAN_H__

#if wxUSE_MENUS

#include "wx/toplevel.h"

// ========================================================================
// wxMenuBarManager
// ========================================================================
class WXDLLEXPORT wxMenuBarManager : public wxObject
{
// ------------------------------------------------------------------------
// initialization/destruction
// ------------------------------------------------------------------------
public:
    wxMenuBarManager();
    virtual ~wxMenuBarManager();
// ------------------------------------------------------------------------
// Single instance
// ------------------------------------------------------------------------
public:
    static wxMenuBarManager *GetInstance() { return sm_mbarmanInstance; }
    static void CreateInstance();
    static void DestroyInstance();
protected:
    static wxMenuBarManager *sm_mbarmanInstance;
// ------------------------------------------------------------------------
// Implementation
// ------------------------------------------------------------------------
public:
    void SetMainMenuBar(wxMenuBar* menubar);
    void CocoaInternalIdle();
    void WindowDidBecomeKey(wxTopLevelWindowNative *win);
    void WindowDidResignKey(wxTopLevelWindowNative *win, bool uninstallMenuBar = true);
    void WindowDidBecomeMain(wxTopLevelWindowNative *win);
    void WindowDidResignMain(wxTopLevelWindowNative *win);
    void UpdateWindowMenuBar(wxTopLevelWindowNative *win);
protected:
    void SetMenuBar(wxMenuBar* menubar);
    void InstallMenuBarForWindow(wxTopLevelWindowNative *win);
    void InstallMainMenu();
    WX_NSMenu m_menuApp;
    WX_NSMenu m_menuServices;
    WX_NSMenu m_menuWindows;
    WX_NSMenu m_menuMain;
    // Some menu bar needs to be installed
    bool m_needMenuBar;
    // Is main menu bar the current one
    bool m_mainMenuBarInstalled;
    // Main menu (if app provides one)
    wxMenuBar *m_mainMenuBar;
    wxTopLevelWindowNative *m_windowKey;
    wxTopLevelWindowNative *m_windowMain;
};

#endif // wxUSE_MENUS
#endif // _WX_COCOA_MBARMAN_H_
