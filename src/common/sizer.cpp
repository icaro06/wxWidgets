/////////////////////////////////////////////////////////////////////////////
// Name:        sizer.cpp
// Purpose:     provide new wxSizer class for layounting
// Author:      Robert Roebling and Robin Dunn
// Modified by:
// Created:     
// RCS-ID:      $Id$
// Copyright:   (c) Robin Dunn, Dirk Holtwick and Robert Roebling
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
#pragma implementation "sizer.h"
#endif

// For compilers that support precompilation, includes "wx.h".
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

#include "wx/sizer.h"
#include "wx/utils.h"

//---------------------------------------------------------------------------
// wxSizerItem
//---------------------------------------------------------------------------

wxSizerItem::wxSizerItem( int width, int height, int option, int flag, int border )
{
    m_window = (wxWindow *) NULL;
    m_sizer = (wxSizer *) NULL;
    m_option = option;
    m_border = border;
    m_flag = flag;
    
    // minimal size is the initial size
    m_minSize.x = width;
    m_minSize.y = height;
    
    // size is set directly
    m_size = m_minSize;
}

wxSizerItem::wxSizerItem( wxWindow *window, int option, int flag, int border )
{
    m_window = window;
    m_sizer = (wxSizer *) NULL;
    m_option = option;
    m_border = border;
    m_flag = flag;
    
    // minimal size is the initial size
    m_minSize = window->GetSize();
    
    // size is calculated later
    // m_size = ...
}

wxSizerItem::wxSizerItem( wxSizer *sizer, int option, int flag, int border )
{
    m_window = (wxWindow *) NULL;
    m_sizer = sizer;
    m_option = option;
    m_border = border;
    m_flag = flag;
    
    // minimal size is calculated later
    // m_minSize = ...
   
    // size is calculated later
    // m_size = ...
}

wxSize wxSizerItem::GetSize()
{
    wxSize ret;
    if (IsSizer())
        ret = m_sizer->GetSize();
    else
    if (IsWindow())
        ret = m_window->GetSize();
    else ret = m_size;
    
    if (m_flag & wxWEST)
        ret.x += m_border;
    if (m_flag & wxEAST)
        ret.x += m_border;
    if (m_flag & wxNORTH)
        ret.y += m_border;
    if (m_flag & wxSOUTH)
        ret.y += m_border;
    
    return ret;
}

wxSize wxSizerItem::CalcMin()
{
    wxSize ret;
    if (IsSizer())
        ret = m_sizer->CalcMin();
/*  
    The minimum size of a window should be the
    initial size, as saved in m_minSize, not the
    current size.
    
    else
    if (IsWindow())
        ret = m_window->GetSize();
*/
    else ret = m_minSize;
    
    if (m_flag & wxWEST)
        ret.x += m_border;
    if (m_flag & wxEAST)
        ret.x += m_border;
    if (m_flag & wxNORTH)
        ret.y += m_border;
    if (m_flag & wxSOUTH)
        ret.y += m_border;
    
    return ret;
}

void wxSizerItem::SetDimension( wxPoint pos, wxSize size )
{
    if (m_flag & wxWEST)
    {
        pos.x += m_border;
        size.x -= m_border;
    }
    if (m_flag & wxEAST)
    {
        size.x -= m_border;
    }
    if (m_flag & wxNORTH)
    {
        pos.y += m_border;
        size.y -= m_border;
    }
    if (m_flag & wxSOUTH)
    {
        size.y -= m_border;
    }
	
    if (IsSizer())
        m_sizer->SetDimension( pos.x, pos.y, size.x, size.y );
	
    if (IsWindow())
        m_window->SetSize( pos.x, pos.y, size.x, size.y );

    m_size = size;
}

bool wxSizerItem::IsWindow()
{
    return (m_window != NULL);
}

bool wxSizerItem::IsSizer()
{
    return (m_sizer != NULL);
}

bool wxSizerItem::IsSpacer()
{
    return (m_window == NULL) && (m_sizer == NULL);
}

//---------------------------------------------------------------------------
// wxSizer
//---------------------------------------------------------------------------

wxSizer::wxSizer()
{
    m_children.DeleteContents( TRUE );
}

wxSizer::~wxSizer()
{
}
   
void wxSizer::Add( wxWindow *window, int option, int flag, int border )
{
    m_children.Append( new wxSizerItem( window, option, flag, border ) );
}

void wxSizer::Add( wxSizer *sizer, int option, int flag, int border )
{
    m_children.Append( new wxSizerItem( sizer, option, flag, border ) );
}

void wxSizer::Add( int width, int height, int option, int flag, int border )
{
    m_children.Append( new wxSizerItem( width, height, option, flag, border ) );
}

void wxSizer::Fit( wxWindow *window )
{
    window->SetSize( GetMinWindowSize( window ) );
}

void wxSizer::Layout()
{
    m_size = CalcMin();
    RecalcSizes();
}

void wxSizer::SetSizeHints( wxWindow *window )
{
    wxSize size( GetMinWindowSize( window ) );
    window->SetSizeHints( size.x, size.y );
}

wxSize wxSizer::GetMinWindowSize( wxWindow *window )
{
    wxSize minSize( GetMinSize() );
    wxSize size( window->GetSize() );
    wxSize client_size( window->GetClientSize() );
    return wxSize( minSize.x+size.x-client_size.x,
                   minSize.y+size.y-client_size.y ); 
}

void wxSizer::SetDimension( int x, int y, int width, int height )
{
    m_position.x = x;
    m_position.y = y;
    m_size.x = width;
    m_size.y = height;
    RecalcSizes();
}

//---------------------------------------------------------------------------
// wxBoxSizer
//---------------------------------------------------------------------------

wxBoxSizer::wxBoxSizer( int orient )
{
    m_orient = orient;
}

void wxBoxSizer::RecalcSizes()
{
    if (m_children.GetCount() == 0)
    {
        SetDimension( m_position.x, m_position.y, 2, 2 );
        return;
    }
    
    int delta = 0;
    int extra = 0;
    if (m_stretchable)
    {
        if (m_orient == wxHORIZONTAL)
        {
            delta = (m_size.x - m_fixedWidth) / m_stretchable;
            extra = (m_size.x - m_fixedWidth) % m_stretchable;
	}
	else
	{
            delta = (m_size.y - m_fixedHeight) / m_stretchable;
            extra = (m_size.y - m_fixedHeight) % m_stretchable;
	}
    }
    
    wxPoint pt( m_position );
    
    wxNode *node = m_children.GetFirst();
    while (node)
    {
        wxSizerItem *item = (wxSizerItem*) node->Data();

	int weight = 1;
	if (item->GetOption())
	    weight = item->GetOption();
	
	wxSize size( item->CalcMin() );
	
	if (m_orient == wxVERTICAL)
	{
	    long height = size.y;
	    if (item->GetOption())
	    {
	        height = (delta * weight) + extra;
		extra = 0; // only the first item will get the remainder as extra size
	    }
	    
	    wxPoint child_pos( pt );
	    wxSize  child_size( wxSize( size.x, height) );
	    
	    if (item->GetFlag() & wxALIGN_RIGHT)
	      child_pos.x += m_size.x - size.x;
	    else if (item->GetFlag() & wxCENTER)
	      child_pos.x += (m_size.x - size.x) / 2;
	    else if (item->GetFlag() & wxEXPAND)
	      child_size.x = m_size.x;
	      
	    item->SetDimension( child_pos, child_size );
	    
	    pt.y += height;
	}
	else
	{
	    long width = size.x;
	    if (item->GetOption())
	    {
	        width = (delta * weight) + extra;
		extra = 0; // only the first item will get the remainder as extra size
	    }
	    
	    wxPoint child_pos( pt );
	    wxSize  child_size( wxSize(width, size.y) );
	    
	    if (item->GetFlag() & wxALIGN_BOTTOM)
	      child_pos.y += m_size.y - size.y;
	    else if (item->GetFlag() & wxCENTER)
	      child_pos.y += (m_size.y - size.y) / 2;
	    else if (item->GetFlag() & wxEXPAND)
	      child_size.y = m_size.y;
	      
	    item->SetDimension( child_pos, child_size );
	    
	    pt.x += width;
	}

	node = node->Next();
    }
}

wxSize wxBoxSizer::CalcMin()
{
    if (m_children.GetCount() == 0)
        return wxSize(2,2);
    
    m_stretchable = 0;
    m_minWidth = 0;
    m_minHeight = 0;
    m_fixedWidth = 0;
    m_fixedHeight = 0;
    
    wxNode *node = m_children.GetFirst();
    while (node)
    {
        wxSizerItem *item = (wxSizerItem*) node->Data();
	
	int weight = 1;
	if (item->GetOption())
	    weight = item->GetOption();
	
	wxSize size( item->CalcMin() );
	
	if (m_orient == wxHORIZONTAL)
	{
	    m_minWidth += (size.x * weight);
	    m_minHeight = wxMax( m_minHeight, size.y );
	}
	else
	{
	    m_minHeight += (size.y * weight);
	    m_minWidth = wxMax( m_minWidth, size.x );
	}
	
	if (item->GetOption())
	{
	    m_stretchable += weight;
	}
	else
	{
	    if (m_orient == wxVERTICAL)
	    {
		m_fixedHeight += size.y;
		m_fixedWidth = wxMax( m_fixedWidth, size.x );
	    }
	    else
	    {
		m_fixedWidth += size.x;
		m_fixedHeight = wxMax( m_fixedHeight, size.y );
	    }
	}
	
	node = node->Next();
    }
	
    return wxSize( m_minWidth, m_minHeight );
}
