/////////////////////////////////////////////////////////////////////////////
// Name:        src/osx/textctrl_osx.cpp
// Purpose:     wxTextCtrl
// Author:      Stefan Csomor
// Modified by: Ryan Norton (MLTE GetLineLength and GetLineText)
// Created:     1998-01-01
// RCS-ID:      $Id: textctrl.cpp 54820 2008-07-29 20:04:11Z SC $
// Copyright:   (c) Stefan Csomor
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

#include "wx/wxprec.h"

#if wxUSE_TEXTCTRL

#include "wx/textctrl.h"

#ifndef WX_PRECOMP
    #include "wx/intl.h"
    #include "wx/app.h"
    #include "wx/utils.h"
    #include "wx/dc.h"
    #include "wx/button.h"
    #include "wx/menu.h"
    #include "wx/settings.h"
    #include "wx/msgdlg.h"
    #include "wx/toplevel.h"
#endif

#ifdef __DARWIN__
    #include <sys/types.h>
    #include <sys/stat.h>
#else
    #include <stat.h>
#endif

#if wxUSE_STD_IOSTREAM
    #if wxUSE_IOSTREAMH
        #include <fstream.h>
    #else
        #include <fstream>
    #endif
#endif

#include "wx/filefn.h"
#include "wx/sysopt.h"
#include "wx/thread.h"

#include "wx/osx/private.h"

IMPLEMENT_DYNAMIC_CLASS(wxTextCtrl, wxTextCtrlBase)

BEGIN_EVENT_TABLE(wxTextCtrl, wxTextCtrlBase)
    EVT_DROP_FILES(wxTextCtrl::OnDropFiles)
    EVT_CHAR(wxTextCtrl::OnChar)
    EVT_MENU(wxID_CUT, wxTextCtrl::OnCut)
    EVT_MENU(wxID_COPY, wxTextCtrl::OnCopy)
    EVT_MENU(wxID_PASTE, wxTextCtrl::OnPaste)
    EVT_MENU(wxID_UNDO, wxTextCtrl::OnUndo)
    EVT_MENU(wxID_REDO, wxTextCtrl::OnRedo)
    EVT_MENU(wxID_CLEAR, wxTextCtrl::OnDelete)
    EVT_MENU(wxID_SELECTALL, wxTextCtrl::OnSelectAll)

    EVT_CONTEXT_MENU(wxTextCtrl::OnContextMenu)

    EVT_UPDATE_UI(wxID_CUT, wxTextCtrl::OnUpdateCut)
    EVT_UPDATE_UI(wxID_COPY, wxTextCtrl::OnUpdateCopy)
    EVT_UPDATE_UI(wxID_PASTE, wxTextCtrl::OnUpdatePaste)
    EVT_UPDATE_UI(wxID_UNDO, wxTextCtrl::OnUpdateUndo)
    EVT_UPDATE_UI(wxID_REDO, wxTextCtrl::OnUpdateRedo)
    EVT_UPDATE_UI(wxID_CLEAR, wxTextCtrl::OnUpdateDelete)
    EVT_UPDATE_UI(wxID_SELECTALL, wxTextCtrl::OnUpdateSelectAll)
END_EVENT_TABLE()


void wxTextCtrl::Init()
{
    m_editable = true ;
    m_dirty = false;

    m_maxLength = 0;
    m_privateContextMenu = NULL;
    m_triggerOnSetValue = true ;
}

wxTextCtrl::~wxTextCtrl()
{
#if wxUSE_MENUS
    delete m_privateContextMenu;
#endif
}

bool wxTextCtrl::Create( wxWindow *parent,
    wxWindowID id,
    const wxString& str,
    const wxPoint& pos,
    const wxSize& size,
    long style,
    const wxValidator& validator,
    const wxString& name )
{
    m_macIsUserPane = false ;
    m_editable = true ;

    if ( ! (style & wxNO_BORDER) )
        style = (style & ~wxBORDER_MASK) | wxSUNKEN_BORDER ;

    if ( !wxTextCtrlBase::Create( parent, id, pos, size, style & ~(wxHSCROLL | wxVSCROLL), validator, name ) )
        return false;

    if ( m_windowStyle & wxTE_MULTILINE )
    {
        // always turn on this style for multi-line controls
        m_windowStyle |= wxTE_PROCESS_ENTER;
        style |= wxTE_PROCESS_ENTER ;
    }


    m_peer = wxWidgetImpl::CreateTextControl( this, GetParent(), GetId(), str, pos, size, style, GetExtraStyle() );

    MacPostControlCreate(pos, size) ;

    // only now the embedding is correct and we can do a positioning update

    MacSuperChangedPosition() ;

    if ( m_windowStyle & wxTE_READONLY)
        SetEditable( false ) ;

    SetCursor( wxCursor( wxCURSOR_IBEAM ) ) ;

    return true;
}

wxTextWidgetImpl* wxTextCtrl::GetTextPeer() const
{
    return dynamic_cast<wxTextWidgetImpl*> (m_peer); 
}

void wxTextCtrl::MacSuperChangedPosition()
{
    wxWindow::MacSuperChangedPosition() ;
#if wxOSX_USE_CARBON
    GetPeer()->SuperChangedPosition() ;
#endif
}

void wxTextCtrl::MacVisibilityChanged()
{
#if wxOSX_USE_CARBON
    GetPeer()->VisibilityChanged( GetPeer()->IsVisible() );
#endif
}

void wxTextCtrl::MacCheckSpelling(bool check)
{
    GetTextPeer()->CheckSpelling(check);
}

wxString wxTextCtrl::DoGetValue() const
{
    return GetTextPeer()->GetStringValue() ;
}

void wxTextCtrl::GetSelection(long* from, long* to) const
{
    GetTextPeer()->GetSelection( from , to ) ;
}

void wxTextCtrl::DoSetValue(const wxString& str, int flags)
{
    // optimize redraws
    if ( GetValue() == str )
        return;

    GetTextPeer()->SetStringValue( str ) ;

    if ( (flags & SetValue_SendEvent) && m_triggerOnSetValue )
    {
        SendTextUpdatedEvent();
    }
}

void wxTextCtrl::SetMaxLength(unsigned long len)
{
    m_maxLength = len ;
}

bool wxTextCtrl::SetFont( const wxFont& font )
{
    if ( !wxTextCtrlBase::SetFont( font ) )
        return false ;

    GetPeer()->SetFont( font , GetForegroundColour() , GetWindowStyle(), false /* dont ignore black */ ) ;

    return true ;
}

bool wxTextCtrl::SetStyle(long start, long end, const wxTextAttr& style)
{
    GetTextPeer()->SetStyle( start , end , style ) ;

    return true ;
}

bool wxTextCtrl::SetDefaultStyle(const wxTextAttr& style)
{
    wxTextCtrlBase::SetDefaultStyle( style ) ;
    SetStyle( -1  /*current selection*/  , -1 /*current selection*/ , GetDefaultStyle() ) ;

    return true ;
}

// Clipboard operations

void wxTextCtrl::Copy()
{
    if (CanCopy())
        GetTextPeer()->Copy() ;
}

void wxTextCtrl::Cut()
{
    if (CanCut())
    {
        GetTextPeer()->Cut() ;

        wxCommandEvent event( wxEVT_COMMAND_TEXT_UPDATED, m_windowId );
        event.SetEventObject( this );
        HandleWindowEvent( event );
      }
}

void wxTextCtrl::Paste()
{
    if (CanPaste())
    {
        GetTextPeer()->Paste() ;

        // TODO: eventually we should add setting the default style again

        wxCommandEvent event( wxEVT_COMMAND_TEXT_UPDATED, m_windowId );
        event.SetEventObject( this );
        HandleWindowEvent( event );
    }
}

bool wxTextCtrl::CanCopy() const
{
    // Can copy if there's a selection
    long from, to;
    GetSelection( &from, &to );

    return (from != to);
}

bool wxTextCtrl::CanCut() const
{
    if ( !IsEditable() )
        return false;

    // Can cut if there's a selection
    long from, to;
    GetSelection( &from, &to );

    return (from != to);
}

bool wxTextCtrl::CanPaste() const
{
    if (!IsEditable())
        return false;

    return GetTextPeer()->CanPaste() ;
}

void wxTextCtrl::SetEditable(bool editable)
{
    if ( editable != m_editable )
    {
        m_editable = editable ;
        GetTextPeer()->SetEditable( editable ) ;
    }
}

void wxTextCtrl::SetInsertionPoint(long pos)
{
    SetSelection( pos , pos ) ;
}

void wxTextCtrl::SetInsertionPointEnd()
{
    long pos = GetLastPosition();
    SetInsertionPoint( pos );
}

long wxTextCtrl::GetInsertionPoint() const
{
    long begin, end ;
    GetSelection( &begin , &end ) ;

    return begin ;
}

wxTextPos wxTextCtrl::GetLastPosition() const
{
    return GetTextPeer()->GetLastPosition() ;
}

void wxTextCtrl::Replace(long from, long to, const wxString& str)
{
    GetTextPeer()->Replace( from , to , str ) ;
}

void wxTextCtrl::Remove(long from, long to)
{
    GetTextPeer()->Remove( from , to ) ;
}

void wxTextCtrl::SetSelection(long from, long to)
{
    GetTextPeer()->SetSelection( from , to ) ;
}

void wxTextCtrl::WriteText(const wxString& str)
{
    GetTextPeer()->WriteText( str ) ;
}

void wxTextCtrl::AppendText(const wxString& text)
{
    SetInsertionPointEnd();
    WriteText( text );
}

void wxTextCtrl::Clear()
{
    GetTextPeer()->Clear() ;
}

bool wxTextCtrl::IsModified() const
{
    return m_dirty;
}

bool wxTextCtrl::IsEditable() const
{
    return IsEnabled() && m_editable ;
}

bool wxTextCtrl::AcceptsFocus() const
{
    // we don't want focus if we can't be edited
    return /*IsEditable() && */ wxControl::AcceptsFocus();
}

wxSize wxTextCtrl::DoGetBestSize() const
{
    int wText, hText;

    // these are the numbers from the HIG:
    // we reduce them by the borders first
    wText = 100 ;

    switch ( m_windowVariant )
    {
        case wxWINDOW_VARIANT_NORMAL :
            hText = 22 - 6 ;
            break ;

        case wxWINDOW_VARIANT_SMALL :
            hText = 19 - 6 ;
            break ;

        case wxWINDOW_VARIANT_MINI :
            hText = 15 - 6 ;
            break ;

        default :
            hText = 22 - 6;
            break ;
    }

    // as the above numbers have some free space around the text
    // we get 5 lines like this anyway
    if ( m_windowStyle & wxTE_MULTILINE )
         hText *= 5 ;

    if ( !HasFlag(wxNO_BORDER) )
        hText += 6 ;

    return wxSize(wText, hText);
}

// ----------------------------------------------------------------------------
// Undo/redo
// ----------------------------------------------------------------------------

void wxTextCtrl::Undo()
{
    if (CanUndo())
        GetTextPeer()->Undo() ;
}

void wxTextCtrl::Redo()
{
    if (CanRedo())
        GetTextPeer()->Redo() ;
}

bool wxTextCtrl::CanUndo() const
{
    if ( !IsEditable() )
        return false ;

    return GetTextPeer()->CanUndo() ;
}

bool wxTextCtrl::CanRedo() const
{
    if ( !IsEditable() )
        return false ;

    return GetTextPeer()->CanRedo() ;
}

void wxTextCtrl::MarkDirty()
{
    m_dirty = true;
}

void wxTextCtrl::DiscardEdits()
{
    m_dirty = false;
}

int wxTextCtrl::GetNumberOfLines() const
{
    return GetTextPeer()->GetNumberOfLines() ;
}

long wxTextCtrl::XYToPosition(long x, long y) const
{
    return GetTextPeer()->XYToPosition( x , y ) ;
}

bool wxTextCtrl::PositionToXY(long pos, long *x, long *y) const
{
    return GetTextPeer()->PositionToXY( pos , x , y ) ;
}

void wxTextCtrl::ShowPosition(long pos)
{
    return GetTextPeer()->ShowPosition(pos) ;
}

int wxTextCtrl::GetLineLength(long lineNo) const
{
    return GetTextPeer()->GetLineLength(lineNo) ;
}

wxString wxTextCtrl::GetLineText(long lineNo) const
{
    return GetTextPeer()->GetLineText(lineNo) ;
}

void wxTextCtrl::Command(wxCommandEvent & event)
{
    SetValue(event.GetString());
    ProcessCommand(event);
}

void wxTextCtrl::OnDropFiles(wxDropFilesEvent& event)
{
    // By default, load the first file into the text window.
    if (event.GetNumberOfFiles() > 0)
        LoadFile( event.GetFiles()[0] );
}

void wxTextCtrl::OnChar(wxKeyEvent& event)
{
    int key = event.GetKeyCode() ;
    bool eat_key = false ;
    long from, to;

    if ( key == 'a' && event.MetaDown() )
    {
        SelectAll() ;

        return ;
    }

    if ( key == 'c' && event.MetaDown() )
    {
        if ( CanCopy() )
            Copy() ;

        return ;
    }

    if ( !IsEditable() && key != WXK_LEFT && key != WXK_RIGHT && key != WXK_DOWN && key != WXK_UP && key != WXK_TAB &&
        !( key == WXK_RETURN && ( (m_windowStyle & wxTE_PROCESS_ENTER) || (m_windowStyle & wxTE_MULTILINE) ) )
//        && key != WXK_PAGEUP && key != WXK_PAGEDOWN && key != WXK_HOME && key != WXK_END
        )
    {
        // eat it
        return ;
    }

    // Check if we have reached the max # of chars (if it is set), but still
    // allow navigation and deletion
    GetSelection( &from, &to );
    if ( !IsMultiLine() && m_maxLength && GetValue().length() >= m_maxLength &&
        key != WXK_LEFT && key != WXK_RIGHT && key != WXK_TAB && key != WXK_UP && key != WXK_DOWN && 
        key != WXK_BACK && key != WXK_DELETE && !( key == WXK_RETURN && (m_windowStyle & wxTE_PROCESS_ENTER) ) &&
        from == to )
    {
        // eat it, we don't want to add more than allowed # of characters

        // TODO: generate EVT_TEXT_MAXLEN()
        return;
    }

    // assume that any key not processed yet is going to modify the control
    m_dirty = true;

    if ( key == 'v' && event.MetaDown() )
    {
        if ( CanPaste() )
            Paste() ;

        return ;
    }

    if ( key == 'x' && event.MetaDown() )
    {
        if ( CanCut() )
            Cut() ;

        return ;
    }

    switch ( key )
    {
        case WXK_RETURN:
            if (m_windowStyle & wxTE_PROCESS_ENTER)
            {
                wxCommandEvent event(wxEVT_COMMAND_TEXT_ENTER, m_windowId);
                event.SetEventObject( this );
                event.SetString( GetValue() );
                if ( HandleWindowEvent(event) )
                    return;
            }

            if ( !(m_windowStyle & wxTE_MULTILINE) )
            {
                wxTopLevelWindow *tlw = wxDynamicCast(wxGetTopLevelParent(this), wxTopLevelWindow);
                if ( tlw && tlw->GetDefaultItem() )
                {
                    wxButton *def = wxDynamicCast(tlw->GetDefaultItem(), wxButton);
                    if ( def && def->IsEnabled() )
                    {
                        wxCommandEvent event(wxEVT_COMMAND_BUTTON_CLICKED, def->GetId() );
                        event.SetEventObject(def);
                        def->Command(event);

                        return ;
                    }
                }

                // this will make wxWidgets eat the ENTER key so that
                // we actually prevent line wrapping in a single line text control
                eat_key = true;
            }
            break;

        case WXK_TAB:
            if ( !(m_windowStyle & wxTE_PROCESS_TAB))
            {
                int flags = 0;
                if (!event.ShiftDown())
                    flags |= wxNavigationKeyEvent::IsForward ;
                if (event.ControlDown())
                    flags |= wxNavigationKeyEvent::WinChange ;
                Navigate(flags);

                return;
            }
            else
            {
                // This is necessary (don't know why);
                // otherwise the tab will not be inserted.
                WriteText(wxT("\t"));
                eat_key = true;
            }
            break;

        default:
            break;
    }

    if (!eat_key)
    {
        // perform keystroke handling
        event.Skip(true) ;
    }

    if ( ( key >= 0x20 && key < WXK_START ) ||
         ( key >= WXK_NUMPAD0 && key <= WXK_DIVIDE ) ||
         key == WXK_RETURN ||
         key == WXK_DELETE ||
         key == WXK_BACK)
    {
        wxCommandEvent event1(wxEVT_COMMAND_TEXT_UPDATED, m_windowId);
        event1.SetEventObject( this );
        wxPostEvent( GetEventHandler(), event1 );
    }
}

// ----------------------------------------------------------------------------
// standard handlers for standard edit menu events
// ----------------------------------------------------------------------------

void wxTextCtrl::OnCut(wxCommandEvent& WXUNUSED(event))
{
    Cut();
}

void wxTextCtrl::OnCopy(wxCommandEvent& WXUNUSED(event))
{
    Copy();
}

void wxTextCtrl::OnPaste(wxCommandEvent& WXUNUSED(event))
{
    Paste();
}

void wxTextCtrl::OnUndo(wxCommandEvent& WXUNUSED(event))
{
    Undo();
}

void wxTextCtrl::OnRedo(wxCommandEvent& WXUNUSED(event))
{
    Redo();
}

void wxTextCtrl::OnDelete(wxCommandEvent& WXUNUSED(event))
{
    long from, to;

    GetSelection( &from, &to );
    if (from != -1 && to != -1)
        Remove( from, to );
}

void wxTextCtrl::OnSelectAll(wxCommandEvent& WXUNUSED(event))
{
    SetSelection(-1, -1);
}

void wxTextCtrl::OnUpdateCut(wxUpdateUIEvent& event)
{
    event.Enable( CanCut() );
}

void wxTextCtrl::OnUpdateCopy(wxUpdateUIEvent& event)
{
    event.Enable( CanCopy() );
}

void wxTextCtrl::OnUpdatePaste(wxUpdateUIEvent& event)
{
    event.Enable( CanPaste() );
}

void wxTextCtrl::OnUpdateUndo(wxUpdateUIEvent& event)
{
    event.Enable( CanUndo() );
}

void wxTextCtrl::OnUpdateRedo(wxUpdateUIEvent& event)
{
    event.Enable( CanRedo() );
}

void wxTextCtrl::OnUpdateDelete(wxUpdateUIEvent& event)
{
    long from, to;

    GetSelection( &from, &to );
    event.Enable( from != -1 && to != -1 && from != to && IsEditable() ) ;
}

void wxTextCtrl::OnUpdateSelectAll(wxUpdateUIEvent& event)
{
    event.Enable(GetLastPosition() > 0);
}

// CS: Context Menus only work with MLTE implementations or non-multiline HIViews at the moment

void wxTextCtrl::OnContextMenu(wxContextMenuEvent& event)
{
    if ( GetTextPeer()->HasOwnContextMenu() )
    {
        event.Skip() ;
        return ;
    }

#if wxUSE_MENUS
    if (m_privateContextMenu == NULL)
    {
        m_privateContextMenu = new wxMenu;
        m_privateContextMenu->Append(wxID_UNDO, _("&Undo"));
        m_privateContextMenu->Append(wxID_REDO, _("&Redo"));
        m_privateContextMenu->AppendSeparator();
        m_privateContextMenu->Append(wxID_CUT, _("Cu&t"));
        m_privateContextMenu->Append(wxID_COPY, _("&Copy"));
        m_privateContextMenu->Append(wxID_PASTE, _("&Paste"));
        m_privateContextMenu->Append(wxID_CLEAR, _("&Delete"));
        m_privateContextMenu->AppendSeparator();
        m_privateContextMenu->Append(wxID_SELECTALL, _("Select &All"));
    }

    if (m_privateContextMenu != NULL)
        PopupMenu(m_privateContextMenu);
#endif
}

bool wxTextCtrl::MacSetupCursor( const wxPoint& pt )
{
    if ( !GetTextPeer()->SetupCursor( pt ) )
        return wxWindow::MacSetupCursor( pt ) ;
    else
        return true ;
}

// ----------------------------------------------------------------------------
// implementation base class
// ----------------------------------------------------------------------------

void wxTextWidgetImpl::SetStyle(long WXUNUSED(start),
                                long WXUNUSED(end),
                                const wxTextAttr& WXUNUSED(style))
{
}

void wxTextWidgetImpl::Copy()
{
}

void wxTextWidgetImpl::Cut()
{
}

void wxTextWidgetImpl::Paste()
{
}

bool wxTextWidgetImpl::CanPaste() const
{
    return false ;
}

void wxTextWidgetImpl::SetEditable(bool WXUNUSED(editable))
{
}

long wxTextWidgetImpl::GetLastPosition() const
{
    return GetStringValue().length() ;
}

void wxTextWidgetImpl::Replace( long from , long to , const wxString &val )
{
    SetSelection( from , to ) ;
    WriteText( val ) ;
}

void wxTextWidgetImpl::Remove( long from , long to )
{
    SetSelection( from , to ) ;
    WriteText( wxEmptyString) ;
}

void wxTextWidgetImpl::Clear()
{
    SetStringValue( wxEmptyString ) ;
}

bool wxTextWidgetImpl::CanUndo() const
{
    return false ;
}

void wxTextWidgetImpl::Undo()
{
}

bool wxTextWidgetImpl::CanRedo()  const
{
    return false ;
}

void wxTextWidgetImpl::Redo()
{
}

long wxTextWidgetImpl::XYToPosition(long WXUNUSED(x), long WXUNUSED(y)) const
{
    return 0 ;
}

bool wxTextWidgetImpl::PositionToXY(long WXUNUSED(pos),
                                    long *WXUNUSED(x),
                                    long *WXUNUSED(y)) const
{
    return false ;
}

void wxTextWidgetImpl::ShowPosition( long WXUNUSED(pos) )
{
}

int wxTextWidgetImpl::GetNumberOfLines() const
{
    ItemCount lines = 0 ;
    wxString content = GetStringValue() ;
    lines = 1;

    for (size_t i = 0; i < content.length() ; i++)
    {
        if (content[i] == '\r')
            lines++;
    }

    return lines ;
}

wxString wxTextWidgetImpl::GetLineText(long lineNo) const
{
    // TODO: change this if possible to reflect real lines
    wxString content = GetStringValue() ;

    // Find line first
    int count = 0;
    for (size_t i = 0; i < content.length() ; i++)
    {
        if (count == lineNo)
        {
            // Add chars in line then
            wxString tmp;

            for (size_t j = i; j < content.length(); j++)
            {
                if (content[j] == '\n')
                    return tmp;

                tmp += content[j];
            }

            return tmp;
        }

        if (content[i] == '\n')
            count++;
    }

    return wxEmptyString ;
}

int wxTextWidgetImpl::GetLineLength(long lineNo) const
{
    // TODO: change this if possible to reflect real lines
    wxString content = GetStringValue() ;

    // Find line first
    int count = 0;
    for (size_t i = 0; i < content.length() ; i++)
    {
        if (count == lineNo)
        {
            // Count chars in line then
            count = 0;
            for (size_t j = i; j < content.length(); j++)
            {
                count++;
                if (content[j] == '\n')
                    return count;
            }

            return count;
        }

        if (content[i] == '\n')
            count++;
    }

    return 0 ;
}

#endif // wxUSE_TEXTCTRL
