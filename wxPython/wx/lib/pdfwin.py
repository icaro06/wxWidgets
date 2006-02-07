#----------------------------------------------------------------------
# Name:        wx.lib.pdfwin
# Purpose:     A class that allows the use of the Acrobat PSF reader
#              ActiveX control
#
# Author:      Robin Dunn
#
# Created:     22-March-2004
# RCS-ID:      $Id$
# Copyright:   (c) 2004 by Total Control Software
# Licence:     wxWindows license
#----------------------------------------------------------------------
# This module was generated by the wx.activex.GernerateAXModule class
# (See also the genaxmodule script.)

import wx
import wx.activex

clsID = '{CA8A9780-280D-11CF-A24D-444553540000}'
progID = 'AcroPDF.PDF.1'



# Create eventTypes and event binders
wxEVT_Error = wx.activex.RegisterActiveXEvent('OnError')
wxEVT_Message = wx.activex.RegisterActiveXEvent('OnMessage')

EVT_Error = wx.PyEventBinder(wxEVT_Error, 1)
EVT_Message = wx.PyEventBinder(wxEVT_Message, 1)


# Derive a new class from ActiveXWindow
class PDFWindow(wx.activex.ActiveXWindow):
    def __init__(self, parent, ID=-1, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, name='PDFWindow'):
        wx.activex.ActiveXWindow.__init__(self, parent,
            wx.activex.CLSID('{CA8A9780-280D-11CF-A24D-444553540000}'),
            ID, pos, size, style, name)
        
    # Methods exported by the ActiveX object
    def QueryInterface(self, riid):
        return self.CallAXMethod('QueryInterface', riid)

    def AddRef(self):
        return self.CallAXMethod('AddRef')

    def Release(self):
        return self.CallAXMethod('Release')

    def GetTypeInfoCount(self):
        return self.CallAXMethod('GetTypeInfoCount')

    def GetTypeInfo(self, itinfo, lcid):
        return self.CallAXMethod('GetTypeInfo', itinfo, lcid)

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid):
        return self.CallAXMethod('GetIDsOfNames', riid, rgszNames, cNames, lcid)

    def Invoke(self, dispidMember, riid, lcid, wFlags, pdispparams):
        return self.CallAXMethod('Invoke', dispidMember, riid, lcid, wFlags, pdispparams)

    def LoadFile(self, fileName):
        return self.CallAXMethod('LoadFile', fileName)

    def setShowToolbar(self, On):
        return self.CallAXMethod('setShowToolbar', On)

    def gotoFirstPage(self):
        return self.CallAXMethod('gotoFirstPage')

    def gotoLastPage(self):
        return self.CallAXMethod('gotoLastPage')

    def gotoNextPage(self):
        return self.CallAXMethod('gotoNextPage')

    def gotoPreviousPage(self):
        return self.CallAXMethod('gotoPreviousPage')

    def setCurrentPage(self, n):
        return self.CallAXMethod('setCurrentPage', n)

    def goForwardStack(self):
        return self.CallAXMethod('goForwardStack')

    def goBackwardStack(self):
        return self.CallAXMethod('goBackwardStack')

    def setPageMode(self, pageMode):
        return self.CallAXMethod('setPageMode', pageMode)

    def setLayoutMode(self, layoutMode):
        return self.CallAXMethod('setLayoutMode', layoutMode)

    def setNamedDest(self, namedDest):
        return self.CallAXMethod('setNamedDest', namedDest)

    def Print(self):
        return self.CallAXMethod('Print')

    def printWithDialog(self):
        return self.CallAXMethod('printWithDialog')

    def setZoom(self, percent):
        return self.CallAXMethod('setZoom', percent)

    def setZoomScroll(self, percent, left, top):
        return self.CallAXMethod('setZoomScroll', percent, left, top)

    def setView(self, viewMode):
        return self.CallAXMethod('setView', viewMode)

    def setViewScroll(self, viewMode, offset):
        return self.CallAXMethod('setViewScroll', viewMode, offset)

    def setViewRect(self, left, top, width, height):
        return self.CallAXMethod('setViewRect', left, top, width, height)

    def printPages(self, from_, to):
        return self.CallAXMethod('printPages', from_, to)

    def printPagesFit(self, from_, to, shrinkToFit):
        return self.CallAXMethod('printPagesFit', from_, to, shrinkToFit)

    def printAll(self):
        return self.CallAXMethod('printAll')

    def printAllFit(self, shrinkToFit):
        return self.CallAXMethod('printAllFit', shrinkToFit)

    def setShowScrollbars(self, On):
        return self.CallAXMethod('setShowScrollbars', On)

    def GetVersions(self):
        return self.CallAXMethod('GetVersions')

    def setCurrentHightlight(self, a, b, c, d):
        return self.CallAXMethod('setCurrentHightlight', a, b, c, d)

    def setCurrentHighlight(self, a, b, c, d):
        return self.CallAXMethod('setCurrentHighlight', a, b, c, d)

    def postMessage(self, strArray):
        return self.CallAXMethod('postMessage', strArray)

    # Getters, Setters and properties
    def _get_src(self):
        return self.GetAXProp('src')
    def _set_src(self, src):
        self.SetAXProp('src', src)
    src = property(_get_src, _set_src)

    def _get_messageHandler(self):
        return self.GetAXProp('messageHandler')
    def _set_messageHandler(self, messageHandler):
        self.SetAXProp('messageHandler', messageHandler)
    messagehandler = property(_get_messageHandler, _set_messageHandler)


#  PROPERTIES
#  --------------------
#  src
#      type:string  arg:string  canGet:True  canSet:True
#  
#  messagehandler
#      type:VT_VARIANT  arg:VT_VARIANT  canGet:True  canSet:True
#  
#  
#  
#  
#  METHODS
#  --------------------
#  QueryInterface
#      retType:  VT_VOID
#      params:
#          riid
#              in:True  out:False  optional:False  type:unsupported type 29
#          ppvObj
#              in:False  out:True  optional:False  type:unsupported type 26
#  
#  AddRef
#      retType:  int
#  
#  Release
#      retType:  int
#  
#  GetTypeInfoCount
#      retType:  VT_VOID
#      params:
#          pctinfo
#              in:False  out:True  optional:False  type:int
#  
#  GetTypeInfo
#      retType:  VT_VOID
#      params:
#          itinfo
#              in:True  out:False  optional:False  type:int
#          lcid
#              in:True  out:False  optional:False  type:int
#          pptinfo
#              in:False  out:True  optional:False  type:unsupported type 26
#  
#  GetIDsOfNames
#      retType:  VT_VOID
#      params:
#          riid
#              in:True  out:False  optional:False  type:unsupported type 29
#          rgszNames
#              in:True  out:False  optional:False  type:unsupported type 26
#          cNames
#              in:True  out:False  optional:False  type:int
#          lcid
#              in:True  out:False  optional:False  type:int
#          rgdispid
#              in:False  out:True  optional:False  type:int
#  
#  Invoke
#      retType:  VT_VOID
#      params:
#          dispidMember
#              in:True  out:False  optional:False  type:int
#          riid
#              in:True  out:False  optional:False  type:unsupported type 29
#          lcid
#              in:True  out:False  optional:False  type:int
#          wFlags
#              in:True  out:False  optional:False  type:int
#          pdispparams
#              in:True  out:False  optional:False  type:unsupported type 29
#          pvarResult
#              in:False  out:True  optional:False  type:VT_VARIANT
#          pexcepinfo
#              in:False  out:True  optional:False  type:unsupported type 29
#          puArgErr
#              in:False  out:True  optional:False  type:int
#  
#  LoadFile
#      retType:  bool
#      params:
#          fileName
#              in:True  out:False  optional:False  type:string
#  
#  setShowToolbar
#      retType:  VT_VOID
#      params:
#          On
#              in:True  out:False  optional:False  type:bool
#  
#  gotoFirstPage
#      retType:  VT_VOID
#  
#  gotoLastPage
#      retType:  VT_VOID
#  
#  gotoNextPage
#      retType:  VT_VOID
#  
#  gotoPreviousPage
#      retType:  VT_VOID
#  
#  setCurrentPage
#      retType:  VT_VOID
#      params:
#          n
#              in:True  out:False  optional:False  type:int
#  
#  goForwardStack
#      retType:  VT_VOID
#  
#  goBackwardStack
#      retType:  VT_VOID
#  
#  setPageMode
#      retType:  VT_VOID
#      params:
#          pageMode
#              in:True  out:False  optional:False  type:string
#  
#  setLayoutMode
#      retType:  VT_VOID
#      params:
#          layoutMode
#              in:True  out:False  optional:False  type:string
#  
#  setNamedDest
#      retType:  VT_VOID
#      params:
#          namedDest
#              in:True  out:False  optional:False  type:string
#  
#  Print
#      retType:  VT_VOID
#  
#  printWithDialog
#      retType:  VT_VOID
#  
#  setZoom
#      retType:  VT_VOID
#      params:
#          percent
#              in:True  out:False  optional:False  type:double
#  
#  setZoomScroll
#      retType:  VT_VOID
#      params:
#          percent
#              in:True  out:False  optional:False  type:double
#          left
#              in:True  out:False  optional:False  type:double
#          top
#              in:True  out:False  optional:False  type:double
#  
#  setView
#      retType:  VT_VOID
#      params:
#          viewMode
#              in:True  out:False  optional:False  type:string
#  
#  setViewScroll
#      retType:  VT_VOID
#      params:
#          viewMode
#              in:True  out:False  optional:False  type:string
#          offset
#              in:True  out:False  optional:False  type:double
#  
#  setViewRect
#      retType:  VT_VOID
#      params:
#          left
#              in:True  out:False  optional:False  type:double
#          top
#              in:True  out:False  optional:False  type:double
#          width
#              in:True  out:False  optional:False  type:double
#          height
#              in:True  out:False  optional:False  type:double
#  
#  printPages
#      retType:  VT_VOID
#      params:
#          from
#              in:True  out:False  optional:False  type:int
#          to
#              in:True  out:False  optional:False  type:int
#  
#  printPagesFit
#      retType:  VT_VOID
#      params:
#          from
#              in:True  out:False  optional:False  type:int
#          to
#              in:True  out:False  optional:False  type:int
#          shrinkToFit
#              in:True  out:False  optional:False  type:bool
#  
#  printAll
#      retType:  VT_VOID
#  
#  printAllFit
#      retType:  VT_VOID
#      params:
#          shrinkToFit
#              in:True  out:False  optional:False  type:bool
#  
#  setShowScrollbars
#      retType:  VT_VOID
#      params:
#          On
#              in:True  out:False  optional:False  type:bool
#  
#  GetVersions
#      retType:  VT_VARIANT
#  
#  setCurrentHightlight
#      retType:  VT_VOID
#      params:
#          a
#              in:True  out:False  optional:False  type:int
#          b
#              in:True  out:False  optional:False  type:int
#          c
#              in:True  out:False  optional:False  type:int
#          d
#              in:True  out:False  optional:False  type:int
#  
#  setCurrentHighlight
#      retType:  VT_VOID
#      params:
#          a
#              in:True  out:False  optional:False  type:int
#          b
#              in:True  out:False  optional:False  type:int
#          c
#              in:True  out:False  optional:False  type:int
#          d
#              in:True  out:False  optional:False  type:int
#  
#  postMessage
#      retType:  VT_VOID
#      params:
#          strArray
#              in:True  out:False  optional:False  type:VT_VARIANT
#  
#  
#  
#  
#  EVENTS
#  --------------------
#  Error
#      retType:  VT_VOID
#  
#  Message
#      retType:  VT_VOID
#  
#  
#  
#  
