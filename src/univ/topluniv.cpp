/////////////////////////////////////////////////////////////////////////////
// Name:        topluniv.cpp
// Author:      Vaclav Slavik
// Id:          $Id$
// Copyright:   (c) 2001 SciTech Software, Inc. (www.scitechsoft.com)
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

// ============================================================================
// declarations
// ============================================================================

// ----------------------------------------------------------------------------
// headers
// ----------------------------------------------------------------------------

#ifdef __GNUG__
    #pragma implementation "univtoplevel.h"
#endif

// For compilers that support precompilation, includes "wx.h".
#include "wx/wxprec.h"

#ifdef __BORLANDC__
#pragma hdrstop
#endif

#include "wx/defs.h"
#include "wx/toplevel.h"
#include "wx/univ/renderer.h"
#include "wx/dcclient.h"
#include "wx/bitmap.h"
#include "wx/image.h"
#include "wx/cshelp.h"


// ----------------------------------------------------------------------------
// event tables
// ----------------------------------------------------------------------------

BEGIN_EVENT_TABLE(wxTopLevelWindow, wxTopLevelWindowNative)
    WX_EVENT_TABLE_INPUT_CONSUMER(wxTopLevelWindow)
    EVT_NC_PAINT(wxTopLevelWindow::OnNcPaint)
END_EVENT_TABLE()

WX_FORWARD_TO_INPUT_CONSUMER(wxTopLevelWindow)


// ============================================================================
// implementation
// ============================================================================

int wxTopLevelWindow::ms_drawDecorations = -1;

void wxTopLevelWindow::Init()
{
    m_isActive = FALSE;
    m_windowStyle = 0;
    m_pressedButton = 0;
}

bool wxTopLevelWindow::Create(wxWindow *parent,
                              wxWindowID id,
                              const wxString& title,
                              const wxPoint& pos,
                              const wxSize& sizeOrig,
                              long style,
                              const wxString &name)
{
    // init them to avoid compiler warnings
    long styleOrig = 0,
         exstyleOrig = 0;

    if ( ms_drawDecorations == -1 )
        ms_drawDecorations = TRUE;
        // FIXME_MGL -- this is temporary; we assume for now that native TLW
        //              can't do decorations, which is not true

    if ( ms_drawDecorations )
    {
        CreateInputHandler(wxINP_HANDLER_TOPLEVEL);

        styleOrig = style;
        exstyleOrig = GetExtraStyle();
        style &= ~(wxCAPTION | wxMINIMIZE_BOX | wxMAXIMIZE_BOX | 
                   wxSYSTEM_MENU | wxRESIZE_BORDER | wxFRAME_TOOL_WINDOW | 
                   wxTHICK_FRAME);
        style = wxSIMPLE_BORDER;
        SetExtraStyle(exstyleOrig & 
                      ~(wxFRAME_EX_CONTEXTHELP | wxDIALOG_EX_CONTEXTHELP));
    }

    if ( !wxTopLevelWindowNative::Create(parent, id, title, pos, 
                                         sizeOrig, style, name) )
        return FALSE;

    if ( ms_drawDecorations )
    {
        m_windowStyle = styleOrig;
        m_exStyle = exstyleOrig;
    }
        
    return TRUE;
}

bool wxTopLevelWindow::ShowFullScreen(bool show, long style)
{
    if ( show == IsFullScreen() ) return FALSE;
    
    if ( ms_drawDecorations )
    {
        if ( show )
        {
            m_fsSavedStyle = m_windowStyle;
            if ( style & wxFULLSCREEN_NOBORDER )
                m_windowStyle |= wxSIMPLE_BORDER;
            if ( style & wxFULLSCREEN_NOCAPTION )
                m_windowStyle &= ~wxCAPTION;
        }
        else
        {
            m_windowStyle = m_fsSavedStyle;
        }
    }

    return wxTopLevelWindowNative::ShowFullScreen(show, style);
}

long wxTopLevelWindow::GetDecorationsStyle() const
{
    long style = 0;

    if ( m_windowStyle & wxCAPTION )
    {
        style |= wxTOPLEVEL_TITLEBAR | wxTOPLEVEL_BUTTON_CLOSE;
        if ( m_windowStyle & wxMINIMIZE_BOX )
            style |= wxTOPLEVEL_BUTTON_ICONIZE;
        if ( m_windowStyle & wxMAXIMIZE_BOX )
            style |= wxTOPLEVEL_BUTTON_MAXIMIZE;
#if wxUSE_HELP
        if ( m_exStyle & (wxFRAME_EX_CONTEXTHELP | wxDIALOG_EX_CONTEXTHELP))
            style |= wxTOPLEVEL_BUTTON_HELP;
#endif
    }
    if ( (m_windowStyle & (wxSIMPLE_BORDER | wxNO_BORDER)) == 0 )
        style |= wxTOPLEVEL_BORDER;
    if ( m_windowStyle & (wxRESIZE_BORDER | wxTHICK_FRAME) )
        style |= wxTOPLEVEL_RESIZEABLE;
        
    if ( IsMaximized() )
        style |= wxTOPLEVEL_MAXIMIZED;
    if ( GetIcon().Ok() )
        style |= wxTOPLEVEL_ICON;
    if ( m_isActive )
        style |= wxTOPLEVEL_ACTIVE;

    return style;
}

void wxTopLevelWindow::RefreshTitleBar()
{
    wxNcPaintEvent event(GetId());
    event.SetEventObject(this);
    GetEventHandler()->ProcessEvent(event);
}

// ----------------------------------------------------------------------------
// client area handling
// ----------------------------------------------------------------------------

wxPoint wxTopLevelWindow::GetClientAreaOrigin() const
{
    if ( ms_drawDecorations )
    {
        int w, h;
        wxTopLevelWindowNative::DoGetClientSize(&w, &h);
        wxRect rect = wxRect(wxTopLevelWindowNative::GetClientAreaOrigin(),
                             wxSize(w, h));
        rect = m_renderer->GetFrameClientArea(rect, 
                                              GetDecorationsStyle());
        return rect.GetPosition();
    }
    else
    {
        return wxTopLevelWindowNative::GetClientAreaOrigin();
    }
}

void wxTopLevelWindow::DoGetClientSize(int *width, int *height) const
{
    if ( ms_drawDecorations )
    {
        int w, h;
        wxTopLevelWindowNative::DoGetClientSize(&w, &h);
        wxRect rect = wxRect(wxTopLevelWindowNative::GetClientAreaOrigin(),
                             wxSize(w, h));
        rect = m_renderer->GetFrameClientArea(rect, 
                                              GetDecorationsStyle());
        if ( width )
            *width = rect.width;
        if ( height )
            *height = rect.height;
    }
    else
        wxTopLevelWindowNative::DoGetClientSize(width, height);
}

void wxTopLevelWindow::DoSetClientSize(int width, int height)
{
    if ( ms_drawDecorations )
    {
        wxSize size = m_renderer->GetFrameTotalSize(wxSize(width, height), 
                                               GetDecorationsStyle());
        wxTopLevelWindowNative::DoSetClientSize(size.x, size.y);
    }
    else
        wxTopLevelWindowNative::DoSetClientSize(width, height);
}

void wxTopLevelWindow::OnNcPaint(wxPaintEvent& event)
{
    if ( !ms_drawDecorations || !m_renderer )
        event.Skip();
    else
    {
        // get the window rect
        wxRect rect;
        wxSize size = GetSize();
        rect.x =
        rect.y = 0;
        rect.width = size.x;
        rect.height = size.y;

        wxWindowDC dc(this);
        m_renderer->DrawFrameTitleBar(dc, rect, 
                                      GetTitle(), m_titlebarIcon,
                                      GetDecorationsStyle(),
                                      m_pressedButton,
                                      wxCONTROL_PRESSED);
    }
}

long wxTopLevelWindow::HitTest(const wxPoint& pt) const
{
    int w, h;
    wxTopLevelWindowNative::DoGetClientSize(&w, &h);
    wxRect rect(wxTopLevelWindowNative::GetClientAreaOrigin(), wxSize(w, h));
    
    return m_renderer->HitTestFrame(rect, pt, GetDecorationsStyle());
}

// ----------------------------------------------------------------------------
// icons
// ----------------------------------------------------------------------------

void wxTopLevelWindow::SetIcon(const wxIcon& icon)
{
    wxTopLevelWindowNative::SetIcon(icon);
    if ( !m_renderer ) return;

    wxSize size = m_renderer->GetFrameIconSize();
    
    if ( !icon.Ok() || size.x == -1  )
        m_titlebarIcon = icon;
    else
    {
        wxBitmap bmp1;
        bmp1.CopyFromIcon(icon);
        if ( !bmp1.Ok() )
            m_titlebarIcon = wxNullIcon;
        else if ( bmp1.GetWidth() == size.x && bmp1.GetHeight() == size.y )
            m_titlebarIcon = icon;
        else
        {
            wxImage img = bmp1.ConvertToImage();
            img.Rescale(size.x, size.y);
            m_titlebarIcon.CopyFromBitmap(wxBitmap(img));
        }
    }
}

// ----------------------------------------------------------------------------
// actions
// ----------------------------------------------------------------------------

void wxTopLevelWindow::ClickTitleBarButton(long button)
{
    switch ( button )
    {
        case wxTOPLEVEL_BUTTON_CLOSE:
            Close();
            break;

        case wxTOPLEVEL_BUTTON_ICONIZE:
            Iconize();
            break;

        case wxTOPLEVEL_BUTTON_MAXIMIZE:
            Maximize();
            break;

        case wxTOPLEVEL_BUTTON_RESTORE:
            Restore();
            break;

        case wxTOPLEVEL_BUTTON_HELP:
#if wxUSE_HELP
            {
            wxContextHelp contextHelp(this);
            }
#endif
            break;
            
        default:
            wxFAIL_MSG(wxT("incorrect button specification"));
    }
}

bool wxTopLevelWindow::PerformAction(const wxControlAction& action,
                                     long numArg,
                                     const wxString& strArg)
{
    if ( action == wxACTION_TOPLEVEL_ACTIVATE )
    {
        if ( m_isActive != (bool)numArg )
        {
            Refresh();
            m_isActive = (bool)numArg;
            wxNcPaintEvent event(GetId());
            event.SetEventObject(this);
            GetEventHandler()->ProcessEvent(event);
        }
        return TRUE;
    }
    
    else if ( action == wxACTION_TOPLEVEL_BUTTON_PRESS )
    {
        m_pressedButton = numArg;
        RefreshTitleBar();
        return TRUE;
    }
    
    else if ( action == wxACTION_TOPLEVEL_BUTTON_RELEASE )
    {
        m_pressedButton = 0;
        RefreshTitleBar();
        return TRUE;
    }
    
    else if ( action == wxACTION_TOPLEVEL_BUTTON_CLICK )
    {
        m_pressedButton = 0;
        RefreshTitleBar();
        ClickTitleBarButton(numArg);
        return TRUE;
    }
    
    else
        return FALSE;
}


// ============================================================================
// wxStdFrameInputHandler: handles focus, resizing and titlebar buttons clicks
// ============================================================================

wxStdFrameInputHandler::wxStdFrameInputHandler(wxInputHandler *inphand)
            : wxStdInputHandler(inphand)
{
    m_winCapture = NULL;
    m_winHitTest = 0;
    m_winPressed = 0;
}

bool wxStdFrameInputHandler::HandleMouse(wxInputConsumer *consumer,
                                         const wxMouseEvent& event)
{
    // the button has 2 states: pressed and normal with the following
    // transitions between them:
    //
    //      normal -> left down -> capture mouse and go to pressed state
    //      pressed -> left up inside -> generate click -> go to normal
    //                         outside ------------------>
    //
    // the other mouse buttons are ignored
    if ( event.Button(1) )
    {
        if ( event.ButtonDown(1) )
        {
            wxTopLevelWindow *w = wxStaticCast(consumer->GetInputWindow(), wxTopLevelWindow);
            long hit = w->HitTest(event.GetPosition());
            
            if ( hit & wxHT_TOPLEVEL_ANY_BUTTON )
            {
                m_winCapture = w;
                m_winCapture->CaptureMouse();
                m_winHitTest = hit;
                m_winPressed = hit;
                consumer->PerformAction(wxACTION_TOPLEVEL_BUTTON_PRESS, m_winPressed);
                return TRUE;
            }
        }

        else // up
        {
            if ( m_winCapture )
            {
                m_winCapture->ReleaseMouse();
                m_winCapture = NULL;

                if ( m_winHitTest == m_winPressed )
                {
                    consumer->PerformAction(wxACTION_TOPLEVEL_BUTTON_CLICK, m_winPressed);
                    return TRUE;
                }
            }
            //else: the mouse was released outside the window, this doesn't
            //      count as a click
        }
    }

    return wxStdInputHandler::HandleMouse(consumer, event);
}

bool wxStdFrameInputHandler::HandleMouseMove(wxInputConsumer *consumer, 
                                             const wxMouseEvent& event)
{
    // we only have to do something when the mouse leaves/enters the pressed
    // button and don't care about the other ones
    if ( event.GetEventObject() == m_winCapture )
    {
        long hit = m_winCapture->HitTest(event.GetPosition());

        if ( hit != m_winHitTest )
        {
            if ( hit != m_winPressed )
                consumer->PerformAction(wxACTION_TOPLEVEL_BUTTON_RELEASE, m_winPressed);
            else
                consumer->PerformAction(wxACTION_TOPLEVEL_BUTTON_PRESS, m_winPressed);
            
            m_winHitTest = hit;
            return TRUE;
        }
    }

    return wxStdInputHandler::HandleMouseMove(consumer, event);
}

bool wxStdFrameInputHandler::HandleActivation(wxInputConsumer *consumer, 
                                              bool activated)
{
    consumer->PerformAction(wxACTION_TOPLEVEL_ACTIVATE, activated);
    return FALSE;
}
