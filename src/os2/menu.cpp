/////////////////////////////////////////////////////////////////////////////
// Name:        menu.cpp
// Purpose:     wxMenu, wxMenuBar, wxMenuItem
// Author:      David Webster
// Modified by:
// Created:     10/10/99
// RCS-ID:      $Id$
// Copyright:   (c) David Webster
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
    #pragma implementation "menu.h"
#endif

// For compilers that support precompilation, includes "wx.h".
#include "wx/wxprec.h"

#ifndef WX_PRECOMP
    #include "wx/frame.h"
    #include "wx/menu.h"
    #include "wx/utils.h"
    #include "wx/intl.h"
    #include "wx/log.h"
#endif

#if wxUSE_OWNER_DRAWN
    #include "wx/ownerdrw.h"
#endif

#include "wx/os2/private.h"

// other standard headers
#include <string.h>

// ----------------------------------------------------------------------------
// global variables
// ----------------------------------------------------------------------------

extern wxMenu*                      wxCurrentPopupMenu;

// ----------------------------------------------------------------------------
// constants
// ----------------------------------------------------------------------------

//
// The (popup) menu title has this special id
//
static const int                    idMenuTitle = -2;

// ----------------------------------------------------------------------------
// macros
// ----------------------------------------------------------------------------

    IMPLEMENT_DYNAMIC_CLASS(wxMenu, wxEvtHandler)
    IMPLEMENT_DYNAMIC_CLASS(wxMenuBar, wxEvtHandler)

// ============================================================================
// implementation
// ============================================================================

// ---------------------------------------------------------------------------
// wxMenu construction, adding and removing menu items
// ---------------------------------------------------------------------------

//
// Construct a menu with optional title (then use append)
//
void wxMenu::Init()
{
    m_bDoBreak = FALSE;

    //
    // Create the menu
    //
    m_hMenu = ::WinCreateWindow( HWND_DESKTOP // parent
                                ,WC_MENU      // type
                                ,"Menu"       // a generic name
                                ,0L           // no style flag
                                ,0L,0L,0L,0L  // no position
                                ,NULLHANDLE   // no owner
                                ,NULLHANDLE   // no insertion position
                                ,0L           // no ID needed for dynamic creation
                                ,NULL         // no control data
                                ,NULL         // no presentation params
                               );
    if (!m_hMenu)
    {
        wxLogLastError("WinLoadMenu");
    }

    //
    // If we have a title, insert it in the beginning of the menu
    //
    if (!!m_title)
    {
        Append( idMenuTitle
               ,m_title
              );
        AppendSeparator();
    }
} // end of wxMenu::Init

//
// The wxWindow destructor will take care of deleting the submenus.
//
wxMenu::~wxMenu()
{
    //
    // We should free PM resources only if PM doesn't do it for us
    // which happens if we're attached to a menubar or a submenu of another
    // menu
    if (!IsAttached() && !GetParent())
    {
        if (!::WinDestroyWindow((HWND)GetHmenu()) )
        {
            wxLogLastError("WinDestroyWindow");
        }
    }

#if wxUSE_ACCEL
    //
    // Delete accels
    //
    WX_CLEAR_ARRAY(m_vAccels);
#endif // wxUSE_ACCEL
} // end of wxMenu::~wxMenu

void wxMenu::Break()
{
    // this will take effect during the next call to Append()
    m_bDoBreak = TRUE;
} // end of wxMenu::Break

#if wxUSE_ACCEL

int wxMenu::FindAccel(
  int                               nId
) const
{
    size_t                          n;
    size_t                          nCount = m_vAccels.GetCount();

    for (n = 0; n < nCount; n++)
    {
        if (m_vAccels[n]->m_command == nId)
            return n;
    }
    return wxNOT_FOUND;
} // end of wxMenu::FindAccel

void wxMenu::UpdateAccel(
  wxMenuItem*                       pItem
)
{
    //
    // Find the (new) accel for this item
    //
    wxAcceleratorEntry*             pAccel = wxGetAccelFromString(pItem->GetText());

    if (pAccel)
        pAccel->m_command = pItem->GetId();

    //
    // Find the old one
    //
    int                             n = FindAccel(pItem->GetId());

    if (n == wxNOT_FOUND)
    {
        //
        // No old, add new if any
        //
        if (pAccel)
            m_vAccels.Add(pAccel);
        else
            return;     // skipping RebuildAccelTable() below
    }
    else
    {
        //
        // Replace old with new or just remove the old one if no new
        //
        delete                      m_vAccels[n];

        if (pAccel)
            m_vAccels[n] = pAccel;
        else
            m_vAccels.Remove(n);
    }

    if (IsAttached())
    {
        m_menuBar->RebuildAccelTable();
    }
} // wxMenu::UpdateAccel

#endif // wxUSE_ACCEL

//
// Append a new item or submenu to the menu
//
bool wxMenu::DoInsertOrAppend(
  wxMenuItem*                       pItem
, size_t                            nPos
)
{
#if wxUSE_ACCEL
    UpdateAccel(pItem);
#endif // wxUSE_ACCEL

    //
    // If "Break" has just been called, insert a menu break before this item
    // (and don't forget to reset the flag)
    //
    if (m_bDoBreak)
    {
        m_vMenuData.afStyle |= MIS_BREAK;
        m_bDoBreak = FALSE;
    }

    if (pItem->IsSeparator())
    {
        m_vMenuData.afStyle |= MIS_SEPARATOR;
    }

    //
    // Id is the numeric id for normal menu items and HMENU for submenus as
    // required by ::WinInsertMenu() API
    //

    wxMenu*                         pSubmenu = pItem->GetSubMenu();
    MENUITEM                        vItem;

    if (pSubmenu != NULL )
    {
        wxASSERT_MSG(pSubmenu->GetHMenu(), wxT("invalid submenu"));
        pSubmenu->SetParent(this);

        m_vMenuData.id = (USHORT)pSubmenu->GetHMenu();
        m_vMenuData.afStyle |= MIS_SUBMENU;
    }
    else
    {
        m_vMenuData.id = pItem->GetId();
    }

    BYTE*                           pData;

#if wxUSE_OWNER_DRAWN
    if (pItem->IsOwnerDrawn())
    {
        //
        // Want to get {Measure|Draw}Item messages?
        // item draws itself, pass pointer to it in data parameter
        //
        m_vMenuData.afStyle |= MIS_OWNERDRAW;
        pData = (BYTE*)pItem;
    }
    else
#endif
    {
        //
        // Menu is just a normal string (passed in data parameter)
        //
        m_vMenuData.afStyle |= MIS_TEXT;
        pData = (char*)pItem->GetText().c_str();
    }

    BOOL                            bOk;

    //
    // -1 means this is a sub menu not a menuitem
    //
    if (nPos == (size_t)-1)
    {
        HWND                        hSubMenu = ::WinCreateWindow( HWND_DESKTOP // parent
                                                                 ,WC_MENU      // type
                                                                 ,"Menu"       // a generic name
                                                                 ,0L           // no style flag
                                                                 ,0L,0L,0L,0L  // no position
                                                                 ,NULLHANDLE   // no owner
                                                                 ,NULLHANDLE   // no insertion position
                                                                 ,0L           // no ID needed for dynamic creation
                                                                 ,NULL         // no control data
                                                                 ,NULL         // no presentation params
                                                                );

        m_vMenuData.iPosition   = 0;
        m_vMenuData.hwndSubMenu = hSubMenu;
        m_vMenuData.hItem       = NULLHANDLE;

        bOk = (bool)::WinSendMsg(GetHmenu(), MM_INSERTITEM, (MPARAM)&vItem, (MPARAM)NULL);
    }
    else
    {
        m_vMenuData.iPosition   = nPos;
        m_vMenuData.hwndSubMenu = NULLHANDLE;
        m_vMenuData.hItem       = NULLHANDLE;
        bOk = (bool)::WinSendMsg(GetHmenu(), MM_INSERTITEM, (MPARAM)&vItem, (MPARAM)pData);
    }

    if (!bOk)
    {
        wxLogLastError("Insert or AppendMenu");
        return FALSE;
    }
    else
    {
        //
        // If we're already attached to the menubar, we must update it
        //
        if (IsAttached())
        {
            m_menuBar->Refresh();
        }
        return TRUE;
    }
    return FALSE;
} // end of wxMenu::DoInsertOrAppend

bool wxMenu::DoAppend(
  wxMenuItem*                       pItem
)
{
    return wxMenuBase::DoAppend(pItem) && DoInsertOrAppend(pItem);
}

bool wxMenu::DoInsert(
  size_t                            nPos
, wxMenuItem*                       pItem
)
{
    return ( wxMenuBase::DoInsert( nPos
                                  ,pItem) &&
             DoInsertOrAppend( pItem
                              ,nPos
                             ));
} // end of wxMenu::DoInsert

wxMenuItem* wxMenu::DoRemove(
  wxMenuItem*                       pItem
)
{
    //
    // We need to find the items position in the child list
    //
    size_t                          nPos;
    wxMenuItemList::Node*           pNode = GetMenuItems().GetFirst();

    for (nPos = 0; pNode; nPos++)
    {
        if (pNode->GetData() == pItem)
            break;
        pNode = pNode->GetNext();
    }

    //
    // DoRemove() (unlike Remove) can only be called for existing item!
    //
    wxCHECK_MSG(pNode, NULL, wxT("bug in wxMenu::Remove logic"));

#if wxUSE_ACCEL
    //
    // Remove the corresponding accel from the accel table
    //
    int                             n = FindAccel(pItem->GetId());

    if (n != wxNOT_FOUND)
    {
        delete m_vAccels[n];
        m_vAccels.Remove(n);
    }

#endif // wxUSE_ACCEL
    //
    // Remove the item from the menu
    //
    ::WinSendMsg( GetHmenu()
                 ,MM_REMOVEITEM
                 ,MPFROM2SHORT(pItem->GetId(), TRUE)
                 ,(MPARAM)0
                );
    if (IsAttached())
    {
        //
        // Otherwise, the chane won't be visible
        //
        m_menuBar->Refresh();
    }

    //
    // And from internal data structures
    //
    return wxMenuBase::DoRemove(pItem);
} // end of wxMenu::DoRemove

// ---------------------------------------------------------------------------
// accelerator helpers
// ---------------------------------------------------------------------------

#if wxUSE_ACCEL

//
// Create the wxAcceleratorEntries for our accels and put them into provided
// array - return the number of accels we have
//
size_t wxMenu::CopyAccels(
  wxAcceleratorEntry*               pAccels
) const
{
    size_t                          nCount = GetAccelCount();

    for (size_t n = 0; n < nCount; n++)
    {
        *pAccels++ = *m_vAccels[n];
    }
    return nCount;
} // end of wxMenu::CopyAccels

#endif // wxUSE_ACCEL

// ---------------------------------------------------------------------------
// set wxMenu title
// ---------------------------------------------------------------------------

void wxMenu::SetTitle(
  const wxString&                   rLabel
)
{
    bool                            bHasNoTitle = m_title.IsEmpty();
    HWND                            hMenu = GetHmenu();

    m_title = rLabel;
    if (bHasNoTitle)
    {
        if (!rLabel.IsEmpty())
        {
            if (!::WinSetWindowText(hMenu, rLabel.c_str()))
            {
                wxLogLastError("SetMenuTitle");
            }
        }
    }
    else
    {
        if (rLabel.IsEmpty() )
        {
            ::WinSendMsg( GetHmenu()
                         ,MM_REMOVEITEM
                         ,MPFROM2SHORT(hMenu, TRUE)
                         ,(MPARAM)0
                        );
        }
        else
        {
            //
            // Modify the title
            //
            if (!::WinSetWindowText(hMenu, rLabel.c_str()))
            {
                wxLogLastError("SetMenuTitle");
            }
        }
    }
} // end of wxMenu::SetTitle

// ---------------------------------------------------------------------------
// event processing
// ---------------------------------------------------------------------------

bool wxMenu::OS2Command(
  WXUINT                            WXUNUSED(uParam)
, WXWORD                            vId
)
{
    //
    // Ignore commands from the menu title
    //

    if (vId != (WXWORD)idMenuTitle)
    {
        wxCommandEvent              vEvent(wxEVT_COMMAND_MENU_SELECTED);

        vEvent.SetEventObject(this);
        vEvent.SetId(vId);
        vEvent.SetInt(vId);
        ProcessCommand(vEvent);
    }
    return TRUE;
} // end of wxMenu::OS2Command

bool wxMenu::ProcessCommand(
  wxCommandEvent&                   rEvent
)
{
    bool                            bProcessed = FALSE;

#if wxUSE_MENU_CALLBACK
    //
    // Try a callback
    //
    if (m_callback)
    {
        (void)(*(m_callback))(*this, rEvent);
        bProcessed = TRUE;
    }
#endif // wxUSE_MENU_CALLBACK

    //
    // Try the menu's event handler
    //
    if (!bProcessed && GetEventHandler())
    {
        bProcessed = GetEventHandler()->ProcessEvent(rEvent);
    }

    //
    // Try the window the menu was popped up from (and up through the
    // hierarchy)
    wxWindow*                       pWin = GetInvokingWindow();

    if (!bProcessed && pWin)
        bProcessed = pWin->GetEventHandler()->ProcessEvent(rEvent);
    return bProcessed;
} // end of wxMenu::ProcessCommand

// ---------------------------------------------------------------------------
// other
// ---------------------------------------------------------------------------

void wxMenu::Attach(
  wxMenuBar*                        pMenubar
)
{
    //
    // Menu can be in at most one menubar because otherwise they would both
    // delete the menu pointer
    //
    wxASSERT_MSG(!m_menuBar, wxT("menu belongs to 2 menubars, expect a crash"));
    m_menuBar = pMenubar;
} // end of

void wxMenu::Detach()
{
    wxASSERT_MSG( m_menuBar, wxT("can't detach menu if it's not attached") );
    m_menuBar = NULL;
} // end of wxMenu::Detach

wxWindow* wxMenu::GetWindow() const
{
    if (m_invokingWindow != NULL)
        return m_invokingWindow;
    else if ( m_menuBar != NULL)
        return m_menuBar->GetFrame();

    return NULL;
} // end of wxMenu::GetWindow

// ---------------------------------------------------------------------------
// Menu Bar
// ---------------------------------------------------------------------------

void wxMenuBar::Init()
{
    m_eventHandler = this;
    m_pMenuBarFrame = NULL;
    m_hMenu = 0;
} // end of wxMenuBar::Init

wxMenuBar::wxMenuBar()
{
    Init();
} // end of wxMenuBar::wxMenuBar

wxMenuBar::wxMenuBar(
 long                               WXUNUSED(lStyle)
)
{
    Init();
} // end of wxMenuBar::wxMenuBar

wxMenuBar::wxMenuBar(
  int                               nCount
, wxMenu*                           vMenus[]
, const wxString                    sTitles[]
)
{
    Init();

    m_titles.Alloc(nCount);
    for ( int i = 0; i < nCount; i++ )
    {
        m_menus.Append(vMenus[i]);
        m_titles.Add(sTitles[i]);
        vMenus[i]->Attach(this);
    }
} // end of wxMenuBar::wxMenuBar

wxMenuBar::~wxMenuBar()
{
} // end of wxMenuBar::~wxMenuBar

// ---------------------------------------------------------------------------
// wxMenuBar helpers
// ---------------------------------------------------------------------------

void wxMenuBar::Refresh()
{
    wxCHECK_RET( IsAttached(), wxT("can't refresh unatteched menubar") );

//    DrawMenuBar(GetHwndOf(m_menuBarFrame));
}

WXHMENU wxMenuBar::Create()
{
    MENUITEM                        vItem;

    if (m_hMenu != 0 )
        return m_hMenu;

    wxCHECK_MSG(!m_hMenu, TRUE, wxT("menubar already created"));

    //
    // Create an empty menu and then fill it with insertions
    //
    m_hMenu = ::WinCreateWindow( HWND_DESKTOP // parent
                                ,WC_MENU      // type
                                ,"Menu"       // a generic name
                                ,0L           // no style flag
                                ,0L,0L,0L,0L  // no position
                                ,NULLHANDLE   // no owner
                                ,NULLHANDLE   // no insertion position
                                ,0L           // no ID needed for dynamic creation
                                ,NULL         // no control data
                                ,NULL         // no presentation params
                               );
    if (!m_hMenu)
    {
        wxLogLastError("CreateMenu");
    }
    else
    {
        size_t                      nCount = GetMenuCount();

        for (size_t i = 0; i < nCount; i++)
        {
            vItem.iPosition   = 0;
            vItem.afStyle     = MIS_SUBMENU | MIS_TEXT;
            vItem.afAttribute = (USHORT)0;
            vItem.id          = (USHORT)0;
            vItem.hwndSubMenu = m_menus[i]->GetHMenu();
            vItem.hItem       = NULLHANDLE;

            ::WinSendMsg(GetHmenu(), MM_INSERTITEM, (MPARAM)&vItem, (MPARAM)m_titles[i].c_str());
        }
    }
    return m_hMenu;
} // end of wxMenuBar::Create

// ---------------------------------------------------------------------------
// wxMenuBar functions to work with the top level submenus
// ---------------------------------------------------------------------------

//
// NB: we don't support owner drawn top level items for now, if we do these
//     functions would have to be changed to use wxMenuItem as well
//
void wxMenuBar::EnableTop(
  size_t                            nPos
, bool                              bEnable
)
{
    wxCHECK_RET(IsAttached(), wxT("doesn't work with unattached menubars"));
    USHORT                          uFlag = 0;
    SHORT                           nId;

    if(!bEnable)
       uFlag = MIA_DISABLED;

    nId = SHORT1FROMMR(::WinSendMsg((HWND)m_hMenu, MM_ITEMIDFROMPOSITION, MPFROMSHORT(nPos), (MPARAM)0));
    if (nId == MIT_ERROR)
    {
        wxLogLastError("LogLastError");
        return;
    }
    ::WinSendMsg((HWND)m_hMenu, MM_SETITEMATTR, MPFROM2SHORT(nId, TRUE), MPFROM2SHORT(uFlag, uFlag));
    Refresh();
} // end of wxMenuBar::EnableTop

void wxMenuBar::SetLabelTop(
  size_t                            nPos
, const wxString&                   rLabel
)
{
    SHORT                           nId;
    MENUITEM                        vItem;

    wxCHECK_RET(nPos < GetMenuCount(), wxT("invalid menu index"));
    m_titles[nPos] = rLabel;

    if (!IsAttached())
    {
        return;
    }

    nId = SHORT1FROMMR(::WinSendMsg((HWND)m_hMenu, MM_ITEMIDFROMPOSITION, MPFROMSHORT(nPos), (MPARAM)0));
    if (nId == MIT_ERROR)
    {
        wxLogLastError("LogLastError");
        return;
    }
    if(!::WinSendMsg( (HWND)m_hMenu
                     ,MM_QUERYITEM
                     ,MPFROM2SHORT(nId, TRUE)
                     ,MPARAM(&vItem)
                    ))
    {
        wxLogLastError("QueryItem");
    }
    nId = vItem.id;

    if (::WinSendMsg(GetHmenu(), MM_SETITEMTEXT, MPFROMSHORT(nId), (MPARAM)rLabel.c_str()));
    {
        wxLogLastError("ModifyMenu");
    }
    Refresh();
} // end of wxMenuBar::SetLabelTop

wxString wxMenuBar::GetLabelTop(
  size_t                            nPos
) const
{
    wxCHECK_MSG( nPos < GetMenuCount(), wxEmptyString,
                 wxT("invalid menu index in wxMenuBar::GetLabelTop") );
    return m_titles[nPos];
} // end of wxMenuBar::GetLabelTop

// ---------------------------------------------------------------------------
// wxMenuBar construction
// ---------------------------------------------------------------------------

wxMenu* wxMenuBar::Replace(
  size_t                             nPos
, wxMenu*                            pMenu
, const wxString&                    rTitle
)
{
    SHORT                            nId;
    wxMenu*                          pMenuOld = wxMenuBarBase::Replace( nPos
                                                                       ,pMenu
                                                                       ,rTitle
                                                                      );


    nId = SHORT1FROMMR(::WinSendMsg((HWND)m_hMenu, MM_ITEMIDFROMPOSITION, MPFROMSHORT(nPos), (MPARAM)0));
    if (nId == MIT_ERROR)
    {
        wxLogLastError("LogLastError");
        return NULL;
    }
    if (!pMenuOld)
        return FALSE;
    m_titles[nPos] = rTitle;
    if (IsAttached())
    {
        ::WinSendMsg((HWND)m_hMenu, MM_DELETEITEM, MPFROM2SHORT(nId, TRUE), (MPARAM)0);
        ::WinSendMsg((HWND)m_hMenu, MM_INSERTITEM, (MPARAM)&pMenu->m_vMenuData, (MPARAM)rTitle.c_str());

#if wxUSE_ACCEL
        if (pMenuOld->HasAccels() || pMenu->HasAccels())
        {
            //
            // Need to rebuild accell table
            //
            RebuildAccelTable();
        }
#endif // wxUSE_ACCEL
        Refresh();
    }
    return pMenuOld;
} // end of wxMenuBar::Replace

bool wxMenuBar::Insert(
  size_t                            nPos
, wxMenu*                           pMenu
, const wxString&                   rTitle
)
{
    if (!wxMenuBarBase::Insert( nPos
                               ,pMenu
                               ,rTitle
                              ))
        return FALSE;

    m_titles.Insert( rTitle
                    ,nPos
                   );

    pMenu->Attach(this);

    if (IsAttached())
    {
        ::WinSendMsg((HWND)m_hMenu, MM_INSERTITEM, (MPARAM)&pMenu->m_vMenuData, (MPARAM)rTitle.c_str());
#if wxUSE_ACCEL
        if (pMenu->HasAccels())
        {
            // need to rebuild accell table
            RebuildAccelTable();
        }
#endif // wxUSE_ACCEL
        Refresh();
    }
    return TRUE;
} // end of wxMenuBar::Insert

bool wxMenuBar::Append(
  wxMenu*                           pMenu
, const wxString&                   rTitle
)
{
    WXHMENU                         hSubmenu = pMenu ? pMenu->GetHMenu() : 0;

    wxCHECK_MSG(hSubmenu, FALSE, wxT("can't append invalid menu to menubar"));

    if (!wxMenuBarBase::Append(pMenu, rTitle))
        return FALSE;

    pMenu->Attach(this);
    m_titles.Add(rTitle);

    if ( IsAttached() )
    {
        pMenu->m_vMenuData.iPosition = MIT_END;
        ::WinSendMsg((HWND)m_hMenu, MM_INSERTITEM, (MPARAM)&pMenu->m_vMenuData, (MPARAM)rTitle.c_str());
#if wxUSE_ACCEL
        if (pMenu->HasAccels())
        {
            //
            // Need to rebuild accell table
            //
            RebuildAccelTable();
        }
#endif // wxUSE_ACCEL
        Refresh();
    }
    return TRUE;
} // end of wxMenuBar::Append

wxMenu* wxMenuBar::Remove(
  size_t                            nPos
)
{
    wxMenu*                         pMenu = wxMenuBarBase::Remove(nPos);
    SHORT                           nId;

    if (!pMenu)
        return NULL;

    nId = SHORT1FROMMR(::WinSendMsg((HWND)GetHmenu(), MM_ITEMIDFROMPOSITION, MPFROMSHORT(nPos), (MPARAM)0));
    if (nId == MIT_ERROR)
    {
        wxLogLastError("LogLastError");
        return NULL;
    }
    if (IsAttached())
    {
        ::WinSendMsg((HWND)GetHmenu(), MM_DELETEITEM, MPFROM2SHORT(nId, TRUE), (MPARAM)0);
        pMenu->Detach();

#if wxUSE_ACCEL
        if (pMenu->HasAccels())
        {
            //
            // Need to rebuild accell table
            //
            RebuildAccelTable();
        }
#endif // wxUSE_ACCEL
        Refresh();
    }
    m_titles.Remove(nPos);
    return pMenu;
} // end of wxMenuBar::Remove

#if wxUSE_ACCEL

void wxMenuBar::RebuildAccelTable()
{
    //
    // Merge the accelerators of all menus into one accel table
    //
    size_t                          nAccelCount = 0;
    size_t                          i;
    size_t                          nCount = GetMenuCount();

    for (i = 0; i < nCount; i++)
    {
        nAccelCount += m_menus[i]->GetAccelCount();
    }

    if (nAccelCount)
    {
        wxAcceleratorEntry*         pAccelEntries = new wxAcceleratorEntry[nAccelCount];

        nAccelCount = 0;
        for (i = 0; i < nCount; i++)
        {
            nAccelCount += m_menus[i]->CopyAccels(&pAccelEntries[nAccelCount]);
        }
        m_vAccelTable = wxAcceleratorTable( nAccelCount
                                           ,pAccelEntries
                                          );
        delete [] pAccelEntries;
    }
} // end of wxMenuBar::RebuildAccelTable

#endif // wxUSE_ACCEL

void wxMenuBar::Attach(
  wxFrame*                          pFrame
)
{
    wxASSERT_MSG( !IsAttached(), wxT("menubar already attached!") );
    m_pMenuBarFrame = pFrame;

#if wxUSE_ACCEL
    RebuildAccelTable();
#endif // wxUSE_ACCEL
} // end of wxMenuBar::Attach

void wxMenuBar::Detach()
{
    ::WinDestroyWindow((HWND)m_hMenu);
    m_hMenu = (WXHMENU)NULL;
    m_pMenuBarFrame = NULL;
} // end of wxMenuBar::Detach

// ---------------------------------------------------------------------------
// wxMenuBar searching for menu items
// ---------------------------------------------------------------------------

//
// Find the itemString in menuString, and return the item id or wxNOT_FOUND
//
int wxMenuBar::FindMenuItem(
  const wxString&                   rMenuString
, const wxString&                   rItemString
) const
{
    wxString                        sMenuLabel = wxStripMenuCodes(rMenuString);
    size_t                          nCount = GetMenuCount();

    for (size_t i = 0; i < nCount; i++)
    {
        wxString                    sTitle = wxStripMenuCodes(m_titles[i]);

        if (rMenuString == sTitle)
            return m_menus[i]->FindItem(rItemString);
    }
    return wxNOT_FOUND;
} // end of wxMenuBar::FindMenuItem

wxMenuItem* wxMenuBar::FindItem(
  int                               nId
, wxMenu**                          ppItemMenu
) const
{
    if (ppItemMenu)
        *ppItemMenu = NULL;

    wxMenuItem*                     pItem = NULL;
    size_t                          nCount = GetMenuCount();

    for (size_t i = 0; !pItem && (i < nCount); i++)
    {
        pItem = m_menus[i]->FindItem( nId
                                     ,ppItemMenu
                                    );
    }
    return pItem;
} // end of wxMenuBar::FindItem

