/////////////////////////////////////////////////////////////////////////////
// Name:        bmpbuttn.cpp
// Purpose:
// Author:      Robert Roebling
// Id:          $Id$
// Copyright:   (c) 1998 Robert Roebling
// Licence:   	wxWindows licence
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
#pragma implementation "bmpbuttn.h"
#endif

#include "wx/bmpbuttn.h"

//-----------------------------------------------------------------------------
// classes
//-----------------------------------------------------------------------------

class wxBitmapButton;

//-----------------------------------------------------------------------------
// data
//-----------------------------------------------------------------------------

extern bool   g_blockEventsOnDrag;

//-----------------------------------------------------------------------------
// "clicked"
//-----------------------------------------------------------------------------

static void gtk_bmpbutton_clicked_callback( GtkWidget *WXUNUSED(widget), wxBitmapButton *button )
{
  if (!button->HasVMT()) return;
  if (g_blockEventsOnDrag) return;
  
  wxCommandEvent event(wxEVT_COMMAND_BUTTON_CLICKED, button->GetId());
  event.SetEventObject(button);
  button->GetEventHandler()->ProcessEvent(event);
}

//-----------------------------------------------------------------------------
// wxBitmapButton
//-----------------------------------------------------------------------------

IMPLEMENT_DYNAMIC_CLASS(wxBitmapButton,wxControl)

wxBitmapButton::wxBitmapButton(void)
{
}

bool wxBitmapButton::Create(  wxWindow *parent, wxWindowID id, const wxBitmap &bitmap,
      const wxPoint &pos, const wxSize &size, 
      long style, const wxValidator& validator, const wxString &name )
{
  m_needParent = TRUE;
  
  wxSize newSize = size;

  PreCreation( parent, id, pos, newSize, style, name );
  
  SetValidator( validator );

  m_bitmap = bitmap;
  m_label = "";
  
  m_widget = gtk_button_new();
  
  if (m_bitmap.Ok())
  {
    GdkBitmap *mask = (GdkBitmap *) NULL;
    if (m_bitmap.GetMask()) mask = m_bitmap.GetMask()->GetBitmap();
    GtkWidget *pixmap = gtk_pixmap_new( m_bitmap.GetPixmap(), mask );
    
    gtk_widget_show( pixmap );
    gtk_container_add( GTK_CONTAINER(m_widget), pixmap );
  }
  
  if (newSize.x == -1) newSize.x = m_bitmap.GetHeight()+10;
  if (newSize.y == -1) newSize.y = m_bitmap.GetWidth()+10;
  SetSize( newSize.x, newSize.y );
  
  gtk_signal_connect( GTK_OBJECT(m_widget), "clicked", 
    GTK_SIGNAL_FUNC(gtk_bmpbutton_clicked_callback), (gpointer*)this );

  m_parent->AddChild( this );

  (m_parent->m_insertCallback)( m_parent, this );
  
  PostCreation();
  
  SetBackgroundColour( parent->GetBackgroundColour() );

  Show( TRUE );
    
  return TRUE;
}
      
void wxBitmapButton::SetDefault(void)
{
/*
  GTK_WIDGET_SET_FLAGS( m_widget, GTK_CAN_DEFAULT );
  gtk_widget_grab_default( m_widget );
*/
}

void wxBitmapButton::SetLabel( const wxString &label )
{
  wxCHECK_RET( m_widget != NULL, "invalid button" );

  wxControl::SetLabel( label );
}

wxString wxBitmapButton::GetLabel(void) const
{
  wxCHECK_MSG( m_widget != NULL, "", "invalid button" );

  return wxControl::GetLabel();
}

void wxBitmapButton::SetBitmapLabel( const wxBitmap& bitmap )
{
  wxCHECK_RET( m_widget != NULL, "invalid button" );

  m_bitmap = bitmap;
  if (!m_bitmap.Ok()) return;
  
  GtkButton *bin = GTK_BUTTON( m_widget );
  GtkPixmap *g_pixmap = GTK_PIXMAP( bin->child );
  
  GdkBitmap *mask = (GdkBitmap *) NULL;
  if (m_bitmap.GetMask()) mask = m_bitmap.GetMask()->GetBitmap();
  
  gtk_pixmap_set( g_pixmap, m_bitmap.GetPixmap(), mask );
}

void wxBitmapButton::ApplyWidgetStyle()
{
}

