/////////////////////////////////////////////////////////////////////////////
// Name:        control.h
// Purpose:     wxControl class
// Author:      AUTHOR
// Modified by:
// Created:     ??/??/98
// RCS-ID:      $Id$
// Copyright:   (c) AUTHOR
// Licence:   	wxWindows licence
/////////////////////////////////////////////////////////////////////////////

#ifndef _WX_CONTROL_H_
#define _WX_CONTROL_H_

#ifdef __GNUG__
#pragma interface "control.h"
#endif

// General item class
class WXDLLEXPORT wxControl : public wxControlBase
{
    DECLARE_ABSTRACT_CLASS(wxControl)

public:
   wxControl();
   virtual ~wxControl();

   // Simulates an event
   virtual void Command(wxCommandEvent& event) { ProcessCommand(event); }

   // implementation from now on
   // --------------------------

   // Calls the callback and appropriate event handlers
   bool ProcessCommand(wxCommandEvent& event);


   wxList& GetSubcontrols() { return m_subControls; }

   void OnEraseBackground(wxEraseEvent& event);

#if WXWIN_COMPATIBILITY
   virtual void SetButtonColour(const wxColour& WXUNUSED(col)) { }
   wxColour* GetButtonColour() const { return NULL; }

   inline virtual void SetLabelFont(const wxFont& font);
   inline virtual void SetButtonFont(const wxFont& font);
   inline wxFont& GetLabelFont() const;
   inline wxFont& GetButtonFont() const;

   // Adds callback
   inline void Callback(const wxFunction function);

   wxFunction GetCallback() { return m_callback; }

protected:
   wxFunction       m_callback;     // Callback associated with the window
#endif // WXWIN_COMPATIBILITY

protected:
   // For controls like radiobuttons which are really composite
   wxList m_subControls;

   virtual wxSize DoGetBestSize();

   // create the control of the given class with the given style, returns FALSE
   // if creation failed
   bool MSWCreateControl(const wxChar *classname, WXDWORD style);

   // determine the extended styles combination for this window (may slightly
   // modify styl parameter)
   WXDWORD GetExStyle(WXDWORD& style) const;

private:
   DECLARE_EVENT_TABLE()
};


#if WXWIN_COMPATIBILITY
    inline void wxControl::Callback(const wxFunction f) { m_callback = f; };
    inline wxFont& wxControl::GetLabelFont() const { return GetFont(); }
    inline wxFont& wxControl::GetButtonFont() const { return GetFont(); }
    inline void wxControl::SetLabelFont(const wxFont& font) { SetFont(font); }
    inline void wxControl::SetButtonFont(const wxFont& font) { SetFont(font); }
#endif // WXWIN_COMPATIBILITY

wxControl *wxFindControlFromMacControl(ControlHandle inControl ) ;
void wxAssociateControlWithMacControl(ControlHandle inControl, wxControl *control) ;
void wxRemoveMacControlAssociation(wxControl *control) ;

#endif
    // _WX_CONTROL_H_
