///////////////////////////////////////////////////////////////////////////////
// Name:        wx/evtloop.h
// Purpose:     declares wxEventLoop class
// Author:      Vadim Zeitlin
// Modified by:
// Created:     01.06.01
// RCS-ID:      $Id$
// Copyright:   (c) 2001 Vadim Zeitlin <zeitlin@dptmaths.ens-cachan.fr>
// Licence:     wxWindows licence
///////////////////////////////////////////////////////////////////////////////

#ifndef _WX_EVTLOOP_H_
#define _WX_EVTLOOP_H_

#ifdef __GNUG__
    #pragma interface "evtloop.h"
#endif

// ----------------------------------------------------------------------------
// wxEventLoop: a GUI event loop
// ----------------------------------------------------------------------------

class WXDLLEXPORT wxEventLoop
{
public:
    // ctor
    wxEventLoop() { m_impl = NULL; }

    // dtor
    virtual ~wxEventLoop();

    // start the event loop, return the exit code when it is finished
    virtual int Run();

    // exit from the loop with the given exit code
    virtual void Exit(int rc = 0);

    // return TRUE if any events are available
    virtual bool Pending() const;

    // dispatch a single event, return FALSE if we should exit from the loop
    virtual bool Dispatch();

    // is the event loop running now?
    virtual bool IsRunning() const;

protected:
    // the pointer to the port specific implementation class
    class WXDLLEXPORT wxEventLoopImpl *m_impl;
};

#endif // _WX_EVTLOOP_H_
