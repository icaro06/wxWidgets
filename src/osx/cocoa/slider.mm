/////////////////////////////////////////////////////////////////////////////
// Name:        src/osx/cocoa/slider.mm
// Purpose:     wxSlider
// Author:      Stefan Csomor
// Modified by:
// Created:     1998-01-01
// RCS-ID:      $Id: slider.cpp 54129 2008-06-11 19:30:52Z SC $
// Copyright:   (c) Stefan Csomor
// Licence:       wxWindows licence
/////////////////////////////////////////////////////////////////////////////

#include "wx/wxprec.h"

#if wxUSE_SLIDER

#include "wx/slider.h"
#include "wx/osx/private.h"

@interface wxNSSlider : NSSlider
{
}
@end

@implementation wxNSSlider

+ (void)initialize
{
    static BOOL initialized = NO;
    if (!initialized) 
    {
        initialized = YES;
        wxOSXCocoaClassAddWXMethods(self);
    }
}

@end

class wxSliderCocoaImpl : public wxWidgetCocoaImpl
{
public :
    wxSliderCocoaImpl(wxWindowMac* peer , WXWidget w) :
        wxWidgetCocoaImpl(peer, w)
    {
    }
    
    ~wxSliderCocoaImpl()
    {
    }

    virtual void clickedAction(WXWidget slf, void* _cmd, void *sender);
    virtual void mouseEvent(WX_NSEvent event, WXWidget slf, void* _cmd);
};

// we will have a mouseDown, then in the native 
// implementation of mouseDown the tracking code
// is calling clickedAction, therefore we wire this
// to thumbtrack and only after super mouseDown 
// returns we will call the thumbrelease

void wxSliderCocoaImpl::clickedAction( WXWidget slf, void *_cmd, void *sender)
{
    wxWindow* wxpeer = (wxWindow*) GetWXPeer();
    if ( wxpeer )
        wxpeer->TriggerScrollEvent(wxEVT_SCROLL_THUMBTRACK);
}

void wxSliderCocoaImpl::mouseEvent(WX_NSEvent event, WXWidget slf, void *_cmd)
{
    wxWidgetCocoaImpl::mouseEvent(event, slf, _cmd);
    
    if ( strcmp( sel_getName((SEL) _cmd) , "mouseDown:") == 0 )
    {
        wxWindow* wxpeer = (wxWindow*) GetWXPeer();
        if ( wxpeer )
            wxpeer->OSXHandleClicked(0);
    }
}



wxWidgetImplType* wxWidgetImpl::CreateSlider( wxWindowMac* wxpeer, 
                                    wxWindowMac* parent, 
                                    wxWindowID id, 
                                    wxInt32 value,
                                    wxInt32 minimum,
                                    wxInt32 maximum,
                                    const wxPoint& pos, 
                                    const wxSize& size,
                                    long style, 
                                    long extraStyle)
{
    NSRect r = wxOSXGetFrameForControl( wxpeer, pos , size ) ;
    wxNSSlider* v = [[wxNSSlider alloc] initWithFrame:r];

    int tickMarks = 0;
    if ( style & wxSL_AUTOTICKS )
    {
        tickMarks = (maximum - minimum) + 1; // +1 for the 0 value

        // keep the number of tickmarks from becoming unwieldly, therefore below it is ok to cast
        // it to a UInt16
        while (tickMarks > 20)
            tickMarks /= 5;
            
        [v setNumberOfTickMarks:tickMarks];
        [v setTickMarkPosition:NSTickMarkBelow];
    }

    [v setMinValue: minimum];
    [v setMaxValue: maximum];
    [v setFloatValue: (double) value];
    wxWidgetCocoaImpl* c = new wxSliderCocoaImpl( wxpeer, v );
    return c;
}

#endif // wxUSE_SLIDER
