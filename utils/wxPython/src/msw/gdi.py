# This file was created automatically by SWIG.
import gdic

from misc import *
class wxBitmapPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self, gdic=gdic):
        if self.thisown == 1 :
            gdic.delete_wxBitmap(self.this)
    def Create(self,arg0,arg1,*args):
        val = apply(gdic.wxBitmap_Create,(self.this,arg0,arg1,)+args)
        return val
    def GetDepth(self):
        val = gdic.wxBitmap_GetDepth(self.this)
        return val
    def GetHeight(self):
        val = gdic.wxBitmap_GetHeight(self.this)
        return val
    def GetPalette(self):
        val = gdic.wxBitmap_GetPalette(self.this)
        val = wxPalettePtr(val)
        return val
    def GetMask(self):
        val = gdic.wxBitmap_GetMask(self.this)
        val = wxMaskPtr(val)
        return val
    def GetWidth(self):
        val = gdic.wxBitmap_GetWidth(self.this)
        return val
    def LoadFile(self,arg0,arg1):
        val = gdic.wxBitmap_LoadFile(self.this,arg0,arg1)
        return val
    def Ok(self):
        val = gdic.wxBitmap_Ok(self.this)
        return val
    def SaveFile(self,arg0,arg1,*args):
        argl = map(None,args)
        try: argl[0] = argl[0].this
        except: pass
        args = tuple(argl)
        val = apply(gdic.wxBitmap_SaveFile,(self.this,arg0,arg1,)+args)
        return val
    def SetDepth(self,arg0):
        val = gdic.wxBitmap_SetDepth(self.this,arg0)
        return val
    def SetHeight(self,arg0):
        val = gdic.wxBitmap_SetHeight(self.this,arg0)
        return val
    def SetMask(self,arg0):
        val = gdic.wxBitmap_SetMask(self.this,arg0.this)
        return val
    def SetPalette(self,arg0):
        val = gdic.wxBitmap_SetPalette(self.this,arg0.this)
        return val
    def SetWidth(self,arg0):
        val = gdic.wxBitmap_SetWidth(self.this,arg0)
        return val
    def __repr__(self):
        return "<C wxBitmap instance>"
class wxBitmap(wxBitmapPtr):
    def __init__(self,arg0,arg1) :
        self.this = gdic.new_wxBitmap(arg0,arg1)
        self.thisown = 1




class wxMaskPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self, gdic=gdic):
        if self.thisown == 1 :
            gdic.delete_wxMask(self.this)
    def __repr__(self):
        return "<C wxMask instance>"
class wxMask(wxMaskPtr):
    def __init__(self,arg0) :
        self.this = gdic.new_wxMask(arg0.this)
        self.thisown = 1




class wxIconPtr(wxBitmapPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self, gdic=gdic):
        if self.thisown == 1 :
            gdic.delete_wxIcon(self.this)
    def GetDepth(self):
        val = gdic.wxIcon_GetDepth(self.this)
        return val
    def GetHeight(self):
        val = gdic.wxIcon_GetHeight(self.this)
        return val
    def GetWidth(self):
        val = gdic.wxIcon_GetWidth(self.this)
        return val
    def LoadFile(self,arg0,arg1):
        val = gdic.wxIcon_LoadFile(self.this,arg0,arg1)
        return val
    def Ok(self):
        val = gdic.wxIcon_Ok(self.this)
        return val
    def SetDepth(self,arg0):
        val = gdic.wxIcon_SetDepth(self.this,arg0)
        return val
    def SetHeight(self,arg0):
        val = gdic.wxIcon_SetHeight(self.this,arg0)
        return val
    def SetWidth(self,arg0):
        val = gdic.wxIcon_SetWidth(self.this,arg0)
        return val
    def __repr__(self):
        return "<C wxIcon instance>"
class wxIcon(wxIconPtr):
    def __init__(self,arg0,arg1,*args) :
        self.this = apply(gdic.new_wxIcon,(arg0,arg1,)+args)
        self.thisown = 1




class wxCursorPtr(wxBitmapPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self, gdic=gdic):
        if self.thisown == 1 :
            gdic.delete_wxCursor(self.this)
    def Ok(self):
        val = gdic.wxCursor_Ok(self.this)
        return val
    def __repr__(self):
        return "<C wxCursor instance>"
class wxCursor(wxCursorPtr):
    def __init__(self,arg0,arg1,*arg                      // Alternate 'constructor'
    wxColour* wxNamedColour(const wxString& colorName) {
        return new wxColour(colorName);
    }
                                      // Alternate 'constructor'
    wxMemoryDC* wxMemoryDCFromDC(wxDC* oldDC) {
        return new wxMemoryDC(oldDC);
    }

#if 0
extern wxFont * wxNORMAL_FONT; 
extern wxFont * wxSMALL_FONT; 
extern wxFont * wxITALIC_FONT; 
extern wxFont * wxSWISS_FONT; 
extern wxPen * wxRED_PEN; 
extern wxPen * wxCYAN_PEN; 
extern wxPen * wxGREEN_PEN; 
extern wxPen * wxBLACK_PEN; 
extern wxPen * wxWHITE_PEN; 
extern wxPen * wxTRANSPARENT_PEN; 
extern wxPen * wxBLACK_DASHED_PEN; 
extern wxPen * wxGREY_PEN; 
extern wxPen * wxMEDIUM_GREY_PEN; 
extern wxPen * wxLIGHT_GREY_PEN; 
extern wxBrush * wxBLUE_BRUSH; 
extern wxBrush * wxGREEN_BRUSH; 
extern wxBrush * wxWHITE_BRUSH; 
extern wxBrush * wxBLACK_BRUSH; 
extern wxBrush * wxTRANSPARENT_BRUSH; 
extern wxBrush * wxCYAN_BRUSH; 
extern wxBrush * wxRED_BRUSH; 
extern wxBrush * wxGREY_BRUSH; 
extern wxBrush * wxMEDIUM_GREY_BRUSH; 
extern wxBrush * wxLIGHT_GREY_BRUSH; 
extern wxColour * wxBLACK; 
extern wxColour * wxWHITE; 
extern wxColour * wxRED; 
extern wxColour * wxBLUE; 
extern wxColour * wxGREEN; 
extern wxColour * wxCYAN; 
extern wxColour * wxLIGHT_GREY; 
extern wxCursor * wxSTANDARD_CURSOR; 
extern wxCursor * wxHOURGLASS_CURSOR; 
extern wxCursor * wxCROSS_CURSOR; 
extern wxBitmap  wxNullBitmap; 
extern wxIcon  wxNullIcon; 
extern wxCursor  wxNullCursor; 
extern wxPen  wxNullPen; 
extern wxBrush  wxNullBrush; 
extern wxPalette  wxNullPalette; 
extern wxFont  wxNullFont; 
extern wxColour  wxNullColour; 

#endif
static PyObject *_wrap_wxEmptyBitmap(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _result;
    int  _arg0;
    int  _arg1;
    int  _arg2 = -1;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"ii|i:wxEmptyBitmap",&_arg0,&_arg1,&_arg2)) 
        return NULL;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxBitmap *)wxEmptyBitmap(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxBitmap_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static PyObject *_wrap_wxNoRefBitmap(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _result;
    char * _arg0;
    long  _arg1;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"sl:wxNoRefBitmap",&_arg0,&_arg1)) 
        return NULL;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxBitmap *)wxNoRefBitmap(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxBitmap_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static PyObject *_wrap_wxBitmapFromData(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _result;
    char * _arg0;
    long  _arg1;
    int  _arg2;
    int  _arg3;
    int  _arg4 = 1;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"slii|i:wxBitmapFromData",&_arg0,&_arg1,&_arg2,&_arg3,&_arg4)) 
        return NULL;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxBitmap *)wxBitmapFromData(_arg0,_arg1,_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxBitmap_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static PyObject *_wrap_wxMaskColour(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxMask * _result;
    wxBitmap * _arg0;
    wxColour * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxMaskColour",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxMaskColour. Expected _wxBitmap_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxMaskColour. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxMask *)wxMaskColour(*_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxMask_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static PyObject *_wrap_wxStockCursor(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxCursor * _result;
    int  _arg0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"i:wxStockCursor",&_arg0)) 
        return NULL;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxCursor *)wxPyStockCursor(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxCursor_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static PyObject *_wrap_wxNamedColour(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxColour * _result;
    wxString * _arg0;
    PyObject * _obj0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"O:wxNamedColour",&_obj0)) 
        return NULL;
{
    if (!PyString_Check(_obj0)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg0 = new wxString(PyString_AsString(_obj0), PyString_Size(_obj0));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxColour *)wxNamedColour(*_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxColour_p");
    _resultobj = Py_BuildValue("s",_ptemp);
{
    if (_obj0)
        delete _arg0;
}
    return _resultobj;
}

static PyObject *_wrap_wxMemoryDCFromDC(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxMemoryDC * _result;
    wxDC * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxMemoryDCFromDC",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxMemoryDCFromDC. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxMemoryDC *)wxMemoryDCFromDC(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxMemoryDC_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static int _wrap_wxNORMAL_FONT_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxNORMAL_FONT is read-only.");
    return 1;
}

static PyObject *_wrap_wxNORMAL_FONT_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxNORMAL_FONT,"_wxFont_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxSMALL_FONT_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxSMALL_FONT is read-only.");
    return 1;
}

static PyObject *_wrap_wxSMALL_FONT_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxSMALL_FONT,"_wxFont_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxITALIC_FONT_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxITALIC_FONT is read-only.");
    return 1;
}

static PyObject *_wrap_wxITALIC_FONT_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxITALIC_FONT,"_wxFont_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxSWISS_FONT_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxSWISS_FONT is read-only.");
    return 1;
}

static PyObject *_wrap_wxSWISS_FONT_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxSWISS_FONT,"_wxFont_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxRED_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxRED_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxRED_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxRED_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxCYAN_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxCYAN_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxCYAN_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxCYAN_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxGREEN_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxGREEN_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxGREEN_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxGREEN_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxBLACK_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxBLACK_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxBLACK_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxBLACK_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxWHITE_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxWHITE_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxWHITE_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxWHITE_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxTRANSPARENT_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxTRANSPARENT_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxTRANSPARENT_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxTRANSPARENT_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxBLACK_DASHED_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxBLACK_DASHED_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxBLACK_DASHED_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxBLACK_DASHED_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxGREY_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxGREY_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxGREY_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxGREY_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxMEDIUM_GREY_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxMEDIUM_GREY_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxMEDIUM_GREY_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxMEDIUM_GREY_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxLIGHT_GREY_PEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxLIGHT_GREY_PEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxLIGHT_GREY_PEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxLIGHT_GREY_PEN,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxBLUE_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxBLUE_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxBLUE_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxBLUE_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxGREEN_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxGREEN_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxGREEN_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxGREEN_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxWHITE_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxWHITE_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxWHITE_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxWHITE_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxBLACK_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxBLACK_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxBLACK_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxBLACK_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxTRANSPARENT_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxTRANSPARENT_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxTRANSPARENT_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxTRANSPARENT_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxCYAN_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxCYAN_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxCYAN_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxCYAN_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxRED_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxRED_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxRED_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxRED_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxGREY_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxGREY_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxGREY_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxGREY_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxMEDIUM_GREY_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxMEDIUM_GREY_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxMEDIUM_GREY_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxMEDIUM_GREY_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxLIGHT_GREY_BRUSH_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxLIGHT_GREY_BRUSH is read-only.");
    return 1;
}

static PyObject *_wrap_wxLIGHT_GREY_BRUSH_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxLIGHT_GREY_BRUSH,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxBLACK_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxBLACK is read-only.");
    return 1;
}

static PyObject *_wrap_wxBLACK_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxBLACK,"_wxColour_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxWHITE_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxWHITE is read-only.");
    return 1;
}

static PyObject *_wrap_wxWHITE_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxWHITE,"_wxColour_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxRED_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxRED is read-only.");
    return 1;
}

static PyObject *_wrap_wxRED_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxRED,"_wxColour_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxBLUE_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxBLUE is read-only.");
    return 1;
}

static PyObject *_wrap_wxBLUE_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxBLUE,"_wxColour_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxGREEN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxGREEN is read-only.");
    return 1;
}

static PyObject *_wrap_wxGREEN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxGREEN,"_wxColour_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxCYAN_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxCYAN is read-only.");
    return 1;
}

static PyObject *_wrap_wxCYAN_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxCYAN,"_wxColour_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxLIGHT_GREY_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxLIGHT_GREY is read-only.");
    return 1;
}

static PyObject *_wrap_wxLIGHT_GREY_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxLIGHT_GREY,"_wxColour_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxSTANDARD_CURSOR_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxSTANDARD_CURSOR is read-only.");
    return 1;
}

static PyObject *_wrap_wxSTANDARD_CURSOR_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxSTANDARD_CURSOR,"_wxCursor_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxHOURGLASS_CURSOR_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxHOURGLASS_CURSOR is read-only.");
    return 1;
}

static PyObject *_wrap_wxHOURGLASS_CURSOR_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxHOURGLASS_CURSOR,"_wxCursor_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxCROSS_CURSOR_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxCROSS_CURSOR is read-only.");
    return 1;
}

static PyObject *_wrap_wxCROSS_CURSOR_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp, (char *) wxCROSS_CURSOR,"_wxCursor_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxNullBitmap_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxNullBitmap is read-only.");
    return 1;
}

static PyObject *_wrap_wxNullBitmap_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp,(char *) &wxNullBitmap,"_wxBitmap_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxNullIcon_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxNullIcon is read-only.");
    return 1;
}

static PyObject *_wrap_wxNullIcon_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp,(char *) &wxNullIcon,"_wxIcon_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxNullCursor_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxNullCursor is read-only.");
    return 1;
}

static PyObject *_wrap_wxNullCursor_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp,(char *) &wxNullCursor,"_wxCursor_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxNullPen_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxNullPen is read-only.");
    return 1;
}

static PyObject *_wrap_wxNullPen_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp,(char *) &wxNullPen,"_wxPen_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxNullBrush_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxNullBrush is read-only.");
    return 1;
}

static PyObject *_wrap_wxNullBrush_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp,(char *) &wxNullBrush,"_wxBrush_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxNullPalette_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxNullPalette is read-only.");
    return 1;
}

static PyObject *_wrap_wxNullPalette_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp,(char *) &wxNullPalette,"_wxPalette_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxNullFont_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxNullFont is read-only.");
    return 1;
}

static PyObject *_wrap_wxNullFont_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp,(char *) &wxNullFont,"_wxFont_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

static int _wrap_wxNullColour_set(PyObject *val) {

    PyErr_SetString(PyExc_TypeError,"Variable wxNullColour is read-only.");
    return 1;
}

static PyObject *_wrap_wxNullColour_get() {
    PyObject * pyobj;
    char ptemp[128];

    SWIG_MakePtr(ptemp,(char *) &wxNullColour,"_wxColour_p");
    pyobj = PyString_FromString(ptemp);
    return pyobj;
}

#define new_wxBitmap(_swigarg0,_swigarg1) (new wxBitmap(_swigarg0,_swigarg1))
static PyObject *_wrap_new_wxBitmap(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _result;
    wxString * _arg0;
    long  _arg1;
    PyObject * _obj0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"Ol:new_wxBitmap",&_obj0,&_arg1)) 
        return NULL;
{
    if (!PyString_Check(_obj0)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg0 = new wxString(PyString_AsString(_obj0), PyString_Size(_obj0));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxBitmap *)new_wxBitmap(*_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxBitmap_p");
    _resultobj = Py_BuildValue("s",_ptemp);
{
    if (_obj0)
        delete _arg0;
}
    return _resultobj;
}

#define delete_wxBitmap(_swigobj) (delete _swigobj)
static PyObject *_wrap_delete_wxBitmap(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:delete_wxBitmap",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of delete_wxBitmap. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        delete_wxBitmap(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxBitmap_Create(_swigobj,_swigarg0,_swigarg1,_swigarg2)  (_swigobj->Create(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_wxBitmap_Create(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _arg0;
    int  _arg1;
    int  _arg2;
    int  _arg3 = -1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sii|i:wxBitmap_Create",&_argc0,&_arg1,&_arg2,&_arg3)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_Create. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBitmap_Create(_arg0,_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxBitmap_GetDepth(_swigobj)  (_swigobj->GetDepth())
static PyObject *_wrap_wxBitmap_GetDepth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxBitmap * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBitmap_GetDepth",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_GetDepth. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxBitmap_GetDepth(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxBitmap_GetHeight(_swigobj)  (_swigobj->GetHeight())
static PyObject *_wrap_wxBitmap_GetHeight(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxBitmap * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBitmap_GetHeight",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_GetHeight. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxBitmap_GetHeight(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxBitmap_GetPalette(_swigobj)  (_swigobj->GetPalette())
static PyObject *_wrap_wxBitmap_GetPalette(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPalette * _result;
    wxBitmap * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBitmap_GetPalette",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_GetPalette. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxPalette *)wxBitmap_GetPalette(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxPalette_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxBitmap_GetMask(_swigobj)  (_swigobj->GetMask())
static PyObject *_wrap_wxBitmap_GetMask(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxMask * _result;
    wxBitmap * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBitmap_GetMask",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_GetMask. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxMask *)wxBitmap_GetMask(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxMask_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxBitmap_GetWidth(_swigobj)  (_swigobj->GetWidth())
static PyObject *_wrap_wxBitmap_GetWidth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxBitmap * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBitmap_GetWidth",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_GetWidth. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxBitmap_GetWidth(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxBitmap_LoadFile(_swigobj,_swigarg0,_swigarg1)  (_swigobj->LoadFile(_swigarg0,_swigarg1))
static PyObject *_wrap_wxBitmap_LoadFile(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxBitmap * _arg0;
    wxString * _arg1;
    long  _arg2;
    char * _argc0 = 0;
    PyObject * _obj1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sOl:wxBitmap_LoadFile",&_argc0,&_obj1,&_arg2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_LoadFile. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    if (!PyString_Check(_obj1)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg1 = new wxString(PyString_AsString(_obj1), PyString_Size(_obj1));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxBitmap_LoadFile(_arg0,*_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
{
    if (_obj1)
        delete _arg1;
}
    return _resultobj;
}

#define wxBitmap_Ok(_swigobj)  (_swigobj->Ok())
static PyObject *_wrap_wxBitmap_Ok(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxBitmap * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBitmap_Ok",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_Ok. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxBitmap_Ok(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxBitmap_SaveFile(_swigobj,_swigarg0,_swigarg1,_swigarg2)  (_swigobj->SaveFile(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_wxBitmap_SaveFile(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxBitmap * _arg0;
    wxString * _arg1;
    int  _arg2;
    wxPalette * _arg3 = NULL;
    char * _argc0 = 0;
    PyObject * _obj1 = 0;
    char * _argc3 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sOi|s:wxBitmap_SaveFile",&_argc0,&_obj1,&_arg2,&_argc3)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_SaveFile. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    if (!PyString_Check(_obj1)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg1 = new wxString(PyString_AsString(_obj1), PyString_Size(_obj1));
}
    if (_argc3) {
        if (SWIG_GetPtr(_argc3,(void **) &_arg3,"_wxPalette_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 4 of wxBitmap_SaveFile. Expected _wxPalette_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxBitmap_SaveFile(_arg0,*_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
{
    if (_obj1)
        delete _arg1;
}
    return _resultobj;
}

#define wxBitmap_SetDepth(_swigobj,_swigarg0)  (_swigobj->SetDepth(_swigarg0))
static PyObject *_wrap_wxBitmap_SetDepth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxBitmap_SetDepth",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_SetDepth. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBitmap_SetDepth(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxBitmap_SetHeight(_swigobj,_swigarg0)  (_swigobj->SetHeight(_swigarg0))
static PyObject *_wrap_wxBitmap_SetHeight(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxBitmap_SetHeight",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_SetHeight. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBitmap_SetHeight(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxBitmap_SetMask(_swigobj,_swigarg0)  (_swigobj->SetMask(_swigarg0))
static PyObject *_wrap_wxBitmap_SetMask(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _arg0;
    wxMask * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxBitmap_SetMask",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_SetMask. Expected _wxBitmap_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxMask_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxBitmap_SetMask. Expected _wxMask_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBitmap_SetMask(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxBitmap_SetPalette(_swigobj,_swigarg0)  (_swigobj->SetPalette(_swigarg0))
static PyObject *_wrap_wxBitmap_SetPalette(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _arg0;
    wxPalette * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxBitmap_SetPalette",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_SetPalette. Expected _wxBitmap_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxPalette_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxBitmap_SetPalette. Expected _wxPalette_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBitmap_SetPalette(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxBitmap_SetWidth(_swigobj,_swigarg0)  (_swigobj->SetWidth(_swigarg0))
static PyObject *_wrap_wxBitmap_SetWidth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxBitmap_SetWidth",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBitmap_SetWidth. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBitmap_SetWidth(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define new_wxMask(_swigarg0) (new wxMask(_swigarg0))
static PyObject *_wrap_new_wxMask(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxMask * _result;
    wxBitmap * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:new_wxMask",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of new_wxMask. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxMask *)new_wxMask(*_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxMask_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define delete_wxMask(_swigobj) (delete _swigobj)
static PyObject *_wrap_delete_wxMask(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxMask * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:delete_wxMask",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxMask_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of delete_wxMask. Expected _wxMask_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        delete_wxMask(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

static void *SwigwxIconTowxBitmap(void *ptr) {
    wxIcon *src;
    wxBitmap *dest;
    src = (wxIcon *) ptr;
    dest = (wxBitmap *) src;
    return (void *) dest;
}

#define new_wxIcon(_swigarg0,_swigarg1,_swigarg2,_swigarg3) (new wxIcon(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_new_wxIcon(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxIcon * _result;
    wxString * _arg0;
    long  _arg1;
    int  _arg2 = -1;
    int  _arg3 = -1;
    PyObject * _obj0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"Ol|ii:new_wxIcon",&_obj0,&_arg1,&_arg2,&_arg3)) 
        return NULL;
{
    if (!PyString_Check(_obj0)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg0 = new wxString(PyString_AsString(_obj0), PyString_Size(_obj0));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxIcon *)new_wxIcon(*_arg0,_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxIcon_p");
    _resultobj = Py_BuildValue("s",_ptemp);
{
    if (_obj0)
        delete _arg0;
}
    return _resultobj;
}

#define delete_wxIcon(_swigobj) (delete _swigobj)
static PyObject *_wrap_delete_wxIcon(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxIcon * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:delete_wxIcon",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of delete_wxIcon. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        delete_wxIcon(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxIcon_GetDepth(_swigobj)  (_swigobj->GetDepth())
static PyObject *_wrap_wxIcon_GetDepth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxIcon * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxIcon_GetDepth",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxIcon_GetDepth. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxIcon_GetDepth(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxIcon_GetHeight(_swigobj)  (_swigobj->GetHeight())
static PyObject *_wrap_wxIcon_GetHeight(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxIcon * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxIcon_GetHeight",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxIcon_GetHeight. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxIcon_GetHeight(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxIcon_GetWidth(_swigobj)  (_swigobj->GetWidth())
static PyObject *_wrap_wxIcon_GetWidth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxIcon * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxIcon_GetWidth",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxIcon_GetWidth. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxIcon_GetWidth(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxIcon_LoadFile(_swigobj,_swigarg0,_swigarg1)  (_swigobj->LoadFile(_swigarg0,_swigarg1))
static PyObject *_wrap_wxIcon_LoadFile(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxIcon * _arg0;
    wxString * _arg1;
    long  _arg2;
    char * _argc0 = 0;
    PyObject * _obj1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sOl:wxIcon_LoadFile",&_argc0,&_obj1,&_arg2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxIcon_LoadFile. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    if (!PyString_Check(_obj1)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg1 = new wxString(PyString_AsString(_obj1), PyString_Size(_obj1));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxIcon_LoadFile(_arg0,*_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
{
    if (_obj1)
        delete _arg1;
}
    return _resultobj;
}

#define wxIcon_Ok(_swigobj)  (_swigobj->Ok())
static PyObject *_wrap_wxIcon_Ok(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxIcon * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxIcon_Ok",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxIcon_Ok. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxIcon_Ok(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxIcon_SetDepth(_swigobj,_swigarg0)  (_swigobj->SetDepth(_swigarg0))
static PyObject *_wrap_wxIcon_SetDepth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxIcon * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxIcon_SetDepth",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxIcon_SetDepth. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxIcon_SetDepth(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxIcon_SetHeight(_swigobj,_swigarg0)  (_swigobj->SetHeight(_swigarg0))
static PyObject *_wrap_wxIcon_SetHeight(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxIcon * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxIcon_SetHeight",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxIcon_SetHeight. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxIcon_SetHeight(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxIcon_SetWidth(_swigobj,_swigarg0)  (_swigobj->SetWidth(_swigarg0))
static PyObject *_wrap_wxIcon_SetWidth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxIcon * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxIcon_SetWidth",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxIcon_SetWidth. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxIcon_SetWidth(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

static void *SwigwxCursorTowxBitmap(void *ptr) {
    wxCursor *src;
    wxBitmap *dest;
    src = (wxCursor *) ptr;
    dest = (wxBitmap *) src;
    return (void *) dest;
}

#define new_wxCursor(_swigarg0,_swigarg1,_swigarg2,_swigarg3) (new wxCursor(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_new_wxCursor(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxCursor * _result;
    wxString * _arg0;
    long  _arg1;
    int  _arg2 = 0;
    int  _arg3 = 0;
    PyObject * _obj0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"Ol|ii:new_wxCursor",&_obj0,&_arg1,&_arg2,&_arg3)) 
        return NULL;
{
    if (!PyString_Check(_obj0)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg0 = new wxString(PyString_AsString(_obj0), PyString_Size(_obj0));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxCursor *)new_wxCursor(*_arg0,_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxCursor_p");
    _resultobj = Py_BuildValue("s",_ptemp);
{
    if (_obj0)
        delete _arg0;
}
    return _resultobj;
}

#define delete_wxCursor(_swigobj) (delete _swigobj)
static PyObject *_wrap_delete_wxCursor(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxCursor * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:delete_wxCursor",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxCursor_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of delete_wxCursor. Expected _wxCursor_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        delete_wxCursor(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxCursor_Ok(_swigobj)  (_swigobj->Ok())
static PyObject *_wrap_wxCursor_Ok(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxCursor * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxCursor_Ok",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxCursor_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxCursor_Ok. Expected _wxCursor_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxCursor_Ok(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

static wxFont *new_wxFont(int pointSize,int family,int style,int weight,int underline,char *faceName) {

            return wxTheFontList->FindOrCreateFont(pointSize, family, style, weight,
                                                   underline, faceName);
        }

static PyObject *_wrap_new_wxFont(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxFont * _result;
    int  _arg0;
    int  _arg1;
    int  _arg2;
    int  _arg3;
    int  _arg4 = (0);
    char * _arg5 = "";
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"iiii|is:new_wxFont",&_arg0,&_arg1,&_arg2,&_arg3,&_arg4,&_arg5)) 
        return NULL;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxFont *)new_wxFont(_arg0,_arg1,_arg2,_arg3,_arg4,_arg5);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxFont_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxFont_GetFaceName(_swigobj)  (_swigobj->GetFaceName())
static PyObject *_wrap_wxFont_GetFaceName(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxString * _result;
    wxFont * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxFont_GetFaceName",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_GetFaceName. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = new wxString (wxFont_GetFaceName(_arg0));

    wxPy_END_ALLOW_THREADS;
}{
    _resultobj = PyString_FromString(WXSTRINGCAST *(_result));
}
{
    delete _result;
}
    return _resultobj;
}

#define wxFont_GetFamily(_swigobj)  (_swigobj->GetFamily())
static PyObject *_wrap_wxFont_GetFamily(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxFont * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxFont_GetFamily",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_GetFamily. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxFont_GetFamily(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxFont_GetFontId(_swigobj)  (_swigobj->GetFontId())
static PyObject *_wrap_wxFont_GetFontId(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxFont * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxFont_GetFontId",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_GetFontId. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxFont_GetFontId(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxFont_GetPointSize(_swigobj)  (_swigobj->GetPointSize())
static PyObject *_wrap_wxFont_GetPointSize(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxFont * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxFont_GetPointSize",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_GetPointSize. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxFont_GetPointSize(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxFont_GetStyle(_swigobj)  (_swigobj->GetStyle())
static PyObject *_wrap_wxFont_GetStyle(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxFont * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxFont_GetStyle",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_GetStyle. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxFont_GetStyle(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxFont_GetUnderlined(_swigobj)  (_swigobj->GetUnderlined())
static PyObject *_wrap_wxFont_GetUnderlined(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxFont * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxFont_GetUnderlined",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_GetUnderlined. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxFont_GetUnderlined(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxFont_GetWeight(_swigobj)  (_swigobj->GetWeight())
static PyObject *_wrap_wxFont_GetWeight(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxFont * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxFont_GetWeight",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_GetWeight. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxFont_GetWeight(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxFont_SetFaceName(_swigobj,_swigarg0)  (_swigobj->SetFaceName(_swigarg0))
static PyObject *_wrap_wxFont_SetFaceName(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxFont * _arg0;
    wxString * _arg1;
    char * _argc0 = 0;
    PyObject * _obj1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sO:wxFont_SetFaceName",&_argc0,&_obj1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_SetFaceName. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    if (!PyString_Check(_obj1)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg1 = new wxString(PyString_AsString(_obj1), PyString_Size(_obj1));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxFont_SetFaceName(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    if (_obj1)
        delete _arg1;
}
    return _resultobj;
}

#define wxFont_SetFamily(_swigobj,_swigarg0)  (_swigobj->SetFamily(_swigarg0))
static PyObject *_wrap_wxFont_SetFamily(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxFont * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxFont_SetFamily",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_SetFamily. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxFont_SetFamily(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxFont_SetPointSize(_swigobj,_swigarg0)  (_swigobj->SetPointSize(_swigarg0))
static PyObject *_wrap_wxFont_SetPointSize(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxFont * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxFont_SetPointSize",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_SetPointSize. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxFont_SetPointSize(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxFont_SetStyle(_swigobj,_swigarg0)  (_swigobj->SetStyle(_swigarg0))
static PyObject *_wrap_wxFont_SetStyle(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxFont * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxFont_SetStyle",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_SetStyle. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxFont_SetStyle(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxFont_SetUnderlined(_swigobj,_swigarg0)  (_swigobj->SetUnderlined(_swigarg0))
static PyObject *_wrap_wxFont_SetUnderlined(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxFont * _arg0;
    bool  _arg1;
    char * _argc0 = 0;
    int tempbool1;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxFont_SetUnderlined",&_argc0,&tempbool1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_SetUnderlined. Expected _wxFont_p.");
        return NULL;
        }
    }
    _arg1 = (bool ) tempbool1;
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxFont_SetUnderlined(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxFont_SetWeight(_swigobj,_swigarg0)  (_swigobj->SetWeight(_swigarg0))
static PyObject *_wrap_wxFont_SetWeight(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxFont * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxFont_SetWeight",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxFont_SetWeight. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxFont_SetWeight(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define new_wxColour(_swigarg0,_swigarg1,_swigarg2) (new wxColour(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_new_wxColour(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxColour * _result;
    unsigned char  _arg0 = 0;
    unsigned char  _arg1 = 0;
    unsigned char  _arg2 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"|bbb:new_wxColour",&_arg0,&_arg1,&_arg2)) 
        return NULL;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxColour *)new_wxColour(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxColour_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define delete_wxColour(_swigobj) (delete _swigobj)
static PyObject *_wrap_delete_wxColour(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxColour * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:delete_wxColour",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of delete_wxColour. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        delete_wxColour(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxColour_Red(_swigobj)  (_swigobj->Red())
static PyObject *_wrap_wxColour_Red(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    unsigned char  _result;
    wxColour * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxColour_Red",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxColour_Red. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (unsigned char )wxColour_Red(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("b",_result);
    return _resultobj;
}

#define wxColour_Green(_swigobj)  (_swigobj->Green())
static PyObject *_wrap_wxColour_Green(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    unsigned char  _result;
    wxColour * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxColour_Green",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxColour_Green. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (unsigned char )wxColour_Green(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("b",_result);
    return _resultobj;
}

#define wxColour_Blue(_swigobj)  (_swigobj->Blue())
static PyObject *_wrap_wxColour_Blue(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    unsigned char  _result;
    wxColour * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxColour_Blue",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxColour_Blue. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (unsigned char )wxColour_Blue(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("b",_result);
    return _resultobj;
}

#define wxColour_Ok(_swigobj)  (_swigobj->Ok())
static PyObject *_wrap_wxColour_Ok(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxColour * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxColour_Ok",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxColour_Ok. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxColour_Ok(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxColour_Set(_swigobj,_swigarg0,_swigarg1,_swigarg2)  (_swigobj->Set(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_wxColour_Set(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxColour * _arg0;
    unsigned char  _arg1;
    unsigned char  _arg2;
    unsigned char  _arg3;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sbbb:wxColour_Set",&_argc0,&_arg1,&_arg2,&_arg3)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxColour_Set. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxColour_Set(_arg0,_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

static PyObject * wxColour_Get(wxColour *self) {
            PyObject* rv = PyTuple_New(3);
            PyTuple_SetItem(rv, 0, PyInt_FromLong(self->Red()));
            PyTuple_SetItem(rv, 1, PyInt_FromLong(self->Green()));
            PyTuple_SetItem(rv, 2, PyInt_FromLong(self->Blue()));
            return rv;
        }
static PyObject *_wrap_wxColour_Get(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    PyObject * _result;
    wxColour * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxColour_Get",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxColour_Get. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (PyObject *)wxColour_Get(_arg0);

    wxPy_END_ALLOW_THREADS;
}{
  _resultobj = _result;
}
    return _resultobj;
}

static wxPen *new_wxPen(wxColour *colour,int width,int style) {
            return wxThePenList->FindOrCreatePen(*colour, width, style);
        }

static PyObject *_wrap_new_wxPen(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPen * _result;
    wxColour * _arg0;
    int  _arg1 = 1;
    int  _arg2 = (wxSOLID);
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s|ii:new_wxPen",&_argc0,&_arg1,&_arg2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of new_wxPen. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxPen *)new_wxPen(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxPen_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxPen_GetCap(_swigobj)  (_swigobj->GetCap())
static PyObject *_wrap_wxPen_GetCap(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxPen * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxPen_GetCap",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_GetCap. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxPen_GetCap(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxPen_GetColour(_swigobj)  (_swigobj->GetColour())
static PyObject *_wrap_wxPen_GetColour(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxColour * _result;
    wxPen * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxPen_GetColour",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_GetColour. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxColour & _result_ref = wxPen_GetColour(_arg0);
    _result = (wxColour *) &_result_ref;

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxColour_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxPen_GetJoin(_swigobj)  (_swigobj->GetJoin())
static PyObject *_wrap_wxPen_GetJoin(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxPen * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxPen_GetJoin",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_GetJoin. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxPen_GetJoin(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxPen_GetStyle(_swigobj)  (_swigobj->GetStyle())
static PyObject *_wrap_wxPen_GetStyle(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxPen * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxPen_GetStyle",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_GetStyle. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxPen_GetStyle(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxPen_GetWidth(_swigobj)  (_swigobj->GetWidth())
static PyObject *_wrap_wxPen_GetWidth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxPen * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxPen_GetWidth",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_GetWidth. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxPen_GetWidth(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxPen_Ok(_swigobj)  (_swigobj->Ok())
static PyObject *_wrap_wxPen_Ok(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxPen * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxPen_Ok",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_Ok. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxPen_Ok(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxPen_SetCap(_swigobj,_swigarg0)  (_swigobj->SetCap(_swigarg0))
static PyObject *_wrap_wxPen_SetCap(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPen * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxPen_SetCap",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_SetCap. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxPen_SetCap(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxPen_SetColour(_swigobj,_swigarg0)  (_swigobj->SetColour(_swigarg0))
static PyObject *_wrap_wxPen_SetColour(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPen * _arg0;
    wxColour * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxPen_SetColour",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_SetColour. Expected _wxPen_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxPen_SetColour. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxPen_SetColour(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxPen_SetJoin(_swigobj,_swigarg0)  (_swigobj->SetJoin(_swigarg0))
static PyObject *_wrap_wxPen_SetJoin(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPen * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxPen_SetJoin",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_SetJoin. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxPen_SetJoin(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxPen_SetStyle(_swigobj,_swigarg0)  (_swigobj->SetStyle(_swigarg0))
static PyObject *_wrap_wxPen_SetStyle(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPen * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxPen_SetStyle",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_SetStyle. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxPen_SetStyle(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxPen_SetWidth(_swigobj,_swigarg0)  (_swigobj->SetWidth(_swigarg0))
static PyObject *_wrap_wxPen_SetWidth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPen * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxPen_SetWidth",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_SetWidth. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxPen_SetWidth(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxPen_GetDashes(_swigobj,_swigarg0)  (_swigobj->GetDashes(_swigarg0))
static PyObject *_wrap_wxPen_GetDashes(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxPen * _arg0;
    wxDash ** _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxPen_GetDashes",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_GetDashes. Expected _wxPen_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxDash_pp")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxPen_GetDashes. Expected _wxDash_pp.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxPen_GetDashes(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxPen_GetStipple(_swigobj)  (_swigobj->GetStipple())
static PyObject *_wrap_wxPen_GetStipple(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _result;
    wxPen * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxPen_GetStipple",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_GetStipple. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxBitmap *)wxPen_GetStipple(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxBitmap_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxPen_SetDashes(_swigobj,_swigarg0,_swigarg1)  (_swigobj->SetDashes(_swigarg0,_swigarg1))
static PyObject *_wrap_wxPen_SetDashes(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPen * _arg0;
    int  _arg1;
    wxDash * _arg2;
    char * _argc0 = 0;
    PyObject * _obj2 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sO:wxPen_SetDashes",&_argc0,&_obj2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_SetDashes. Expected _wxPen_p.");
        return NULL;
        }
    }
    if (_obj2)
{
    _arg2 = (unsigned long*)long_LIST_helper(_obj2);
    if (_arg2 == NULL) {
        return NULL;
    }
}
{
    if (_obj2) {
        _arg1 = PyList_Size(_obj2);
    }
    else {
        _arg1 = 0;
    }
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxPen_SetDashes(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    delete [] _arg2;
}
    return _resultobj;
}

#define wxPen_SetStipple(_swigobj,_swigarg0)  (_swigobj->SetStipple(_swigarg0))
static PyObject *_wrap_wxPen_SetStipple(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPen * _arg0;
    wxBitmap * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxPen_SetStipple",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPen_SetStipple. Expected _wxPen_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxPen_SetStipple. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxPen_SetStipple(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

static wxBrush *new_wxBrush(wxColour *colour,int style) {
            return wxTheBrushList->FindOrCreateBrush(*colour, style);
        }

static PyObject *_wrap_new_wxBrush(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBrush * _result;
    wxColour * _arg0;
    int  _arg1 = (wxSOLID);
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s|i:new_wxBrush",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of new_wxBrush. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxBrush *)new_wxBrush(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxBrush_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxBrush_GetColour(_swigobj)  (_swigobj->GetColour())
static PyObject *_wrap_wxBrush_GetColour(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxColour * _result;
    wxBrush * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBrush_GetColour",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBrush_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBrush_GetColour. Expected _wxBrush_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxColour & _result_ref = wxBrush_GetColour(_arg0);
    _result = (wxColour *) &_result_ref;

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxColour_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxBrush_GetStipple(_swigobj)  (_swigobj->GetStipple())
static PyObject *_wrap_wxBrush_GetStipple(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBitmap * _result;
    wxBrush * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBrush_GetStipple",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBrush_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBrush_GetStipple. Expected _wxBrush_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxBitmap *)wxBrush_GetStipple(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxBitmap_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxBrush_GetStyle(_swigobj)  (_swigobj->GetStyle())
static PyObject *_wrap_wxBrush_GetStyle(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxBrush * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBrush_GetStyle",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBrush_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBrush_GetStyle. Expected _wxBrush_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxBrush_GetStyle(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxBrush_Ok(_swigobj)  (_swigobj->Ok())
static PyObject *_wrap_wxBrush_Ok(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxBrush * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxBrush_Ok",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBrush_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBrush_Ok. Expected _wxBrush_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxBrush_Ok(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxBrush_SetColour(_swigobj,_swigarg0)  (_swigobj->SetColour(_swigarg0))
static PyObject *_wrap_wxBrush_SetColour(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBrush * _arg0;
    wxColour * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxBrush_SetColour",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBrush_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBrush_SetColour. Expected _wxBrush_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxBrush_SetColour. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBrush_SetColour(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxBrush_SetStipple(_swigobj,_swigarg0)  (_swigobj->SetStipple(_swigarg0))
static PyObject *_wrap_wxBrush_SetStipple(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBrush * _arg0;
    wxBitmap * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxBrush_SetStipple",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBrush_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBrush_SetStipple. Expected _wxBrush_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxBrush_SetStipple. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBrush_SetStipple(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxBrush_SetStyle(_swigobj,_swigarg0)  (_swigobj->SetStyle(_swigarg0))
static PyObject *_wrap_wxBrush_SetStyle(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBrush * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxBrush_SetStyle",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxBrush_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxBrush_SetStyle. Expected _wxBrush_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBrush_SetStyle(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define delete_wxDC(_swigobj) (delete _swigobj)
static PyObject *_wrap_delete_wxDC(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:delete_wxDC",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of delete_wxDC. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        delete_wxDC(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_BeginDrawing(_swigobj)  (_swigobj->BeginDrawing())
static PyObject *_wrap_wxDC_BeginDrawing(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_BeginDrawing",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_BeginDrawing. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_BeginDrawing(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_Blit(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5,_swigarg6,_swigarg7)  (_swigobj->Blit(_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5,_swigarg6,_swigarg7))
static PyObject *_wrap_wxDC_Blit(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    long  _arg3;
    long  _arg4;
    wxDC * _arg5;
    long  _arg6;
    long  _arg7;
    long  _arg8;
    char * _argc0 = 0;
    char * _argc5 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sllllslll:wxDC_Blit",&_argc0,&_arg1,&_arg2,&_arg3,&_arg4,&_argc5,&_arg6,&_arg7,&_arg8)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_Blit. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc5) {
        if (SWIG_GetPtr(_argc5,(void **) &_arg5,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 6 of wxDC_Blit. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxDC_Blit(_arg0,_arg1,_arg2,_arg3,_arg4,_arg5,_arg6,_arg7,_arg8);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxDC_Clear(_swigobj)  (_swigobj->Clear())
static PyObject *_wrap_wxDC_Clear(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_Clear",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_Clear. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_Clear(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_CrossHair(_swigobj,_swigarg0,_swigarg1)  (_swigobj->CrossHair(_swigarg0,_swigarg1))
static PyObject *_wrap_wxDC_CrossHair(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sll:wxDC_CrossHair",&_argc0,&_arg1,&_arg2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_CrossHair. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_CrossHair(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DestroyClippingRegion(_swigobj)  (_swigobj->DestroyClippingRegion())
static PyObject *_wrap_wxDC_DestroyClippingRegion(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_DestroyClippingRegion",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DestroyClippingRegion. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DestroyClippingRegion(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DeviceToLogicalX(_swigobj,_swigarg0)  (_swigobj->DeviceToLogicalX(_swigarg0))
static PyObject *_wrap_wxDC_DeviceToLogicalX(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    long  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sl:wxDC_DeviceToLogicalX",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DeviceToLogicalX. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_DeviceToLogicalX(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_DeviceToLogicalXRel(_swigobj,_swigarg0)  (_swigobj->DeviceToLogicalXRel(_swigarg0))
static PyObject *_wrap_wxDC_DeviceToLogicalXRel(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    long  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sl:wxDC_DeviceToLogicalXRel",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DeviceToLogicalXRel. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_DeviceToLogicalXRel(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_DeviceToLogicalY(_swigobj,_swigarg0)  (_swigobj->DeviceToLogicalY(_swigarg0))
static PyObject *_wrap_wxDC_DeviceToLogicalY(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    long  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sl:wxDC_DeviceToLogicalY",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DeviceToLogicalY. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_DeviceToLogicalY(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_DeviceToLogicalYRel(_swigobj,_swigarg0)  (_swigobj->DeviceToLogicalYRel(_swigarg0))
static PyObject *_wrap_wxDC_DeviceToLogicalYRel(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    long  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sl:wxDC_DeviceToLogicalYRel",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DeviceToLogicalYRel. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_DeviceToLogicalYRel(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_DrawArc(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5)  (_swigobj->DrawArc(_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5))
static PyObject *_wrap_wxDC_DrawArc(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    long  _arg3;
    long  _arg4;
    long  _arg5;
    long  _arg6;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sllllll:wxDC_DrawArc",&_argc0,&_arg1,&_arg2,&_arg3,&_arg4,&_arg5,&_arg6)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawArc. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawArc(_arg0,_arg1,_arg2,_arg3,_arg4,_arg5,_arg6);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DrawCircle(_swigobj,_swigarg0,_swigarg1,_swigarg2)  (_swigobj->DrawCircle(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_wxDC_DrawCircle(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    long  _arg3;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"slll:wxDC_DrawCircle",&_argc0,&_arg1,&_arg2,&_arg3)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawCircle. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawCircle(_arg0,_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DrawEllipse(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3)  (_swigobj->DrawEllipse(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_wxDC_DrawEllipse(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    long  _arg3;
    long  _arg4;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sllll:wxDC_DrawEllipse",&_argc0,&_arg1,&_arg2,&_arg3,&_arg4)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawEllipse. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawEllipse(_arg0,_arg1,_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DrawEllipticArc(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5)  (_swigobj->DrawEllipticArc(_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5))
static PyObject *_wrap_wxDC_DrawEllipticArc(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    long  _arg3;
    long  _arg4;
    long  _arg5;
    long  _arg6;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sllllll:wxDC_DrawEllipticArc",&_argc0,&_arg1,&_arg2,&_arg3,&_arg4,&_arg5,&_arg6)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawEllipticArc. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawEllipticArc(_arg0,_arg1,_arg2,_arg3,_arg4,_arg5,_arg6);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DrawIcon(_swigobj,_swigarg0,_swigarg1,_swigarg2)  (_swigobj->DrawIcon(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_wxDC_DrawIcon(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxIcon * _arg1;
    long  _arg2;
    long  _arg3;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ssll:wxDC_DrawIcon",&_argc0,&_argc1,&_arg2,&_arg3)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawIcon. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxDC_DrawIcon. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawIcon(_arg0,*_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DrawLine(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3)  (_swigobj->DrawLine(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_wxDC_DrawLine(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    long  _arg3;
    long  _arg4;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sllll:wxDC_DrawLine",&_argc0,&_arg1,&_arg2,&_arg3,&_arg4)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawLine. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawLine(_arg0,_arg1,_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DrawLines(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3)  (_swigobj->DrawLines(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_wxDC_DrawLines(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    int  _arg1;
    wxPoint * _arg2;
    long  _arg3 = 0;
    long  _arg4 = 0;
    char * _argc0 = 0;
    PyObject * _obj2 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sO|ll:wxDC_DrawLines",&_argc0,&_obj2,&_arg3,&_arg4)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawLines. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_obj2)
{
    _arg2 = wxPoint_LIST_helper(_obj2);
    if (_arg2 == NULL) {
        return NULL;
    }
}
{
    if (_obj2) {
        _arg1 = PyList_Size(_obj2);
    }
    else {
        _arg1 = 0;
    }
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawLines(_arg0,_arg1,_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    delete [] _arg2;
}
    return _resultobj;
}

#define wxDC_DrawPolygon(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4)  (_swigobj->DrawPolygon(_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4))
static PyObject *_wrap_wxDC_DrawPolygon(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    int  _arg1;
    wxPoint * _arg2;
    long  _arg3 = 0;
    long  _arg4 = 0;
    int  _arg5 = (wxODDEVEN_RULE);
    char * _argc0 = 0;
    PyObject * _obj2 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sO|lli:wxDC_DrawPolygon",&_argc0,&_obj2,&_arg3,&_arg4,&_arg5)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawPolygon. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_obj2)
{
    _arg2 = wxPoint_LIST_helper(_obj2);
    if (_arg2 == NULL) {
        return NULL;
    }
}
{
    if (_obj2) {
        _arg1 = PyList_Size(_obj2);
    }
    else {
        _arg1 = 0;
    }
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawPolygon(_arg0,_arg1,_arg2,_arg3,_arg4,_arg5);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    delete [] _arg2;
}
    return _resultobj;
}

#define wxDC_DrawPoint(_swigobj,_swigarg0,_swigarg1)  (_swigobj->DrawPoint(_swigarg0,_swigarg1))
static PyObject *_wrap_wxDC_DrawPoint(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sll:wxDC_DrawPoint",&_argc0,&_arg1,&_arg2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawPoint. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawPoint(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DrawRectangle(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3)  (_swigobj->DrawRectangle(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_wxDC_DrawRectangle(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    long  _arg3;
    long  _arg4;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sllll:wxDC_DrawRectangle",&_argc0,&_arg1,&_arg2,&_arg3,&_arg4)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawRectangle. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawRectangle(_arg0,_arg1,_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DrawRoundedRectangle(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4)  (_swigobj->DrawRoundedRectangle(_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4))
static PyObject *_wrap_wxDC_DrawRoundedRectangle(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    long  _arg3;
    long  _arg4;
    long  _arg5 = 20;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sllll|l:wxDC_DrawRoundedRectangle",&_argc0,&_arg1,&_arg2,&_arg3,&_arg4,&_arg5)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawRoundedRectangle. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawRoundedRectangle(_arg0,_arg1,_arg2,_arg3,_arg4,_arg5);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_DrawSpline(_swigobj,_swigarg0,_swigarg1)  (_swigobj->DrawSpline(_swigarg0,_swigarg1))
static PyObject *_wrap_wxDC_DrawSpline(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    int  _arg1;
    wxPoint * _arg2;
    char * _argc0 = 0;
    PyObject * _obj2 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sO:wxDC_DrawSpline",&_argc0,&_obj2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawSpline. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_obj2)
{
    _arg2 = wxPoint_LIST_helper(_obj2);
    if (_arg2 == NULL) {
        return NULL;
    }
}
{
    if (_obj2) {
        _arg1 = PyList_Size(_obj2);
    }
    else {
        _arg1 = 0;
    }
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawSpline(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    delete [] _arg2;
}
    return _resultobj;
}

#define wxDC_DrawText(_swigobj,_swigarg0,_swigarg1,_swigarg2)  (_swigobj->DrawText(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_wxDC_DrawText(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxString * _arg1;
    long  _arg2;
    long  _arg3;
    char * _argc0 = 0;
    PyObject * _obj1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sOll:wxDC_DrawText",&_argc0,&_obj1,&_arg2,&_arg3)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawText. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    if (!PyString_Check(_obj1)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg1 = new wxString(PyString_AsString(_obj1), PyString_Size(_obj1));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawText(_arg0,*_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    if (_obj1)
        delete _arg1;
}
    return _resultobj;
}

#define wxDC_EndDoc(_swigobj)  (_swigobj->EndDoc())
static PyObject *_wrap_wxDC_EndDoc(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_EndDoc",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_EndDoc. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_EndDoc(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_EndDrawing(_swigobj)  (_swigobj->EndDrawing())
static PyObject *_wrap_wxDC_EndDrawing(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_EndDrawing",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_EndDrawing. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_EndDrawing(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_EndPage(_swigobj)  (_swigobj->EndPage())
static PyObject *_wrap_wxDC_EndPage(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_EndPage",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_EndPage. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_EndPage(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_FloodFill(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3)  (_swigobj->FloodFill(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_wxDC_FloodFill(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    wxColour * _arg3;
    int  _arg4 = (wxFLOOD_SURFACE);
    char * _argc0 = 0;
    char * _argc3 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"slls|i:wxDC_FloodFill",&_argc0,&_arg1,&_arg2,&_argc3,&_arg4)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_FloodFill. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc3) {
        if (SWIG_GetPtr(_argc3,(void **) &_arg3,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 4 of wxDC_FloodFill. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_FloodFill(_arg0,_arg1,_arg2,*_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_GetBackground(_swigobj)  (_swigobj->GetBackground())
static PyObject *_wrap_wxDC_GetBackground(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBrush * _result;
    wxDC * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetBackground",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetBackground. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBrush & _result_ref = wxDC_GetBackground(_arg0);
    _result = (wxBrush *) &_result_ref;

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxBrush_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxDC_GetBrush(_swigobj)  (_swigobj->GetBrush())
static PyObject *_wrap_wxDC_GetBrush(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxBrush * _result;
    wxDC * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetBrush",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetBrush. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxBrush & _result_ref = wxDC_GetBrush(_arg0);
    _result = (wxBrush *) &_result_ref;

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxBrush_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxDC_GetCharHeight(_swigobj)  (_swigobj->GetCharHeight())
static PyObject *_wrap_wxDC_GetCharHeight(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetCharHeight",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetCharHeight. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_GetCharHeight(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_GetCharWidth(_swigobj)  (_swigobj->GetCharWidth())
static PyObject *_wrap_wxDC_GetCharWidth(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetCharWidth",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetCharWidth. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_GetCharWidth(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_GetClippingBox(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3)  (_swigobj->GetClippingBox(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_wxDC_GetClippingBox(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long * _arg1;
    long  temp;
    long * _arg2;
    long  temp0;
    long * _arg3;
    long  temp1;
    long * _arg4;
    long  temp2;
    char * _argc0 = 0;

    self = self;
{
  _arg1 = &temp;
}
{
  _arg2 = &temp0;
}
{
  _arg3 = &temp1;
}
{
  _arg4 = &temp2;
}
    if(!PyArg_ParseTuple(args,"s:wxDC_GetClippingBox",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetClippingBox. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_GetClippingBox(_arg0,_arg1,_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg1));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg2));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg3));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg4));
    _resultobj = t_output_helper(_resultobj, o);
}
    return _resultobj;
}

#define wxDC_GetFont(_swigobj)  (_swigobj->GetFont())
static PyObject *_wrap_wxDC_GetFont(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxFont * _result;
    wxDC * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetFont",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetFont. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxFont & _result_ref = wxDC_GetFont(_arg0);
    _result = (wxFont *) &_result_ref;

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxFont_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxDC_GetLogicalFunction(_swigobj)  (_swigobj->GetLogicalFunction())
static PyObject *_wrap_wxDC_GetLogicalFunction(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetLogicalFunction",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetLogicalFunction. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxDC_GetLogicalFunction(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxDC_GetMapMode(_swigobj)  (_swigobj->GetMapMode())
static PyObject *_wrap_wxDC_GetMapMode(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetMapMode",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetMapMode. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxDC_GetMapMode(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxDC_GetOptimization(_swigobj)  (_swigobj->GetOptimization())
static PyObject *_wrap_wxDC_GetOptimization(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetOptimization",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetOptimization. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxDC_GetOptimization(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxDC_GetPen(_swigobj)  (_swigobj->GetPen())
static PyObject *_wrap_wxDC_GetPen(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPen * _result;
    wxDC * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetPen",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetPen. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxPen & _result_ref = wxDC_GetPen(_arg0);
    _result = (wxPen *) &_result_ref;

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxPen_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static wxColour * wxDC_GetPixel(wxDC *self,long  x,long  y) {
            wxColour* wc = new wxColour();
            self->GetPixel(x, y, wc);
            return wc;
        }
static PyObject *_wrap_wxDC_GetPixel(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxColour * _result;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"sll:wxDC_GetPixel",&_argc0,&_arg1,&_arg2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetPixel. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxColour *)wxDC_GetPixel(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxColour_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxDC_GetSizeTuple(_swigobj,_swigarg0,_swigarg1)  (_swigobj->GetSize(_swigarg0,_swigarg1))
static PyObject *_wrap_wxDC_GetSizeTuple(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    int * _arg1;
    int  temp;
    int * _arg2;
    int  temp0;
    char * _argc0 = 0;

    self = self;
{
  _arg1 = &temp;
}
{
  _arg2 = &temp0;
}
    if(!PyArg_ParseTuple(args,"s:wxDC_GetSizeTuple",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetSizeTuple. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_GetSizeTuple(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg1));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg2));
    _resultobj = t_output_helper(_resultobj, o);
}
    return _resultobj;
}

#define wxDC_GetSize(_swigobj)  (_swigobj->GetSize())
static PyObject *_wrap_wxDC_GetSize(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxSize * _result;
    wxDC * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetSize",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetSize. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = new wxSize (wxDC_GetSize(_arg0));

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (void *) _result,"_wxSize_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxDC_GetTextBackground(_swigobj)  (_swigobj->GetTextBackground())
static PyObject *_wrap_wxDC_GetTextBackground(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxColour * _result;
    wxDC * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetTextBackground",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetTextBackground. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxColour & _result_ref = wxDC_GetTextBackground(_arg0);
    _result = (wxColour *) &_result_ref;

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxColour_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxDC_GetTextExtent(_swigobj,_swigarg0,_swigarg1,_swigarg2)  (_swigobj->GetTextExtent(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_wxDC_GetTextExtent(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxString * _arg1;
    long * _arg2;
    long  temp;
    long * _arg3;
    long  temp0;
    char * _argc0 = 0;
    PyObject * _obj1 = 0;

    self = self;
{
  _arg2 = &temp;
}
{
  _arg3 = &temp0;
}
    if(!PyArg_ParseTuple(args,"sO:wxDC_GetTextExtent",&_argc0,&_obj1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetTextExtent. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    if (!PyString_Check(_obj1)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg1 = new wxString(PyString_AsString(_obj1), PyString_Size(_obj1));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_GetTextExtent(_arg0,*_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg2));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg3));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    if (_obj1)
        delete _arg1;
}
    return _resultobj;
}

#define wxDC_GetFullTextExtent(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5)  (_swigobj->GetTextExtent(_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5))
static PyObject *_wrap_wxDC_GetFullTextExtent(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxString * _arg1;
    long * _arg2;
    long  temp;
    long * _arg3;
    long  temp0;
    long * _arg4;
    long  temp1;
    long * _arg5;
    long  temp2;
    wxFont * _arg6 = NULL;
    char * _argc0 = 0;
    PyObject * _obj1 = 0;
    char * _argc6 = 0;

    self = self;
{
  _arg2 = &temp;
}
{
  _arg3 = &temp0;
}
{
  _arg4 = &temp1;
}
{
  _arg5 = &temp2;
}
    if(!PyArg_ParseTuple(args,"sO|s:wxDC_GetFullTextExtent",&_argc0,&_obj1,&_argc6)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetFullTextExtent. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    if (!PyString_Check(_obj1)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg1 = new wxString(PyString_AsString(_obj1), PyString_Size(_obj1));
}
    if (_argc6) {
        if (SWIG_GetPtr(_argc6,(void **) &_arg6,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 7 of wxDC_GetFullTextExtent. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_GetFullTextExtent(_arg0,*_arg1,_arg2,_arg3,_arg4,_arg5,_arg6);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg2));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg3));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg4));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    PyObject *o;
    o = PyInt_FromLong((long) (*_arg5));
    _resultobj = t_output_helper(_resultobj, o);
}
{
    if (_obj1)
        delete _arg1;
}
    return _resultobj;
}

#define wxDC_GetTextForeground(_swigobj)  (_swigobj->GetTextForeground())
static PyObject *_wrap_wxDC_GetTextForeground(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxColour * _result;
    wxDC * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_GetTextForeground",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_GetTextForeground. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxColour & _result_ref = wxDC_GetTextForeground(_arg0);
    _result = (wxColour *) &_result_ref;

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxColour_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxDC_LogicalToDeviceX(_swigobj,_swigarg0)  (_swigobj->LogicalToDeviceX(_swigarg0))
static PyObject *_wrap_wxDC_LogicalToDeviceX(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    long  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sl:wxDC_LogicalToDeviceX",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_LogicalToDeviceX. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_LogicalToDeviceX(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_LogicalToDeviceXRel(_swigobj,_swigarg0)  (_swigobj->LogicalToDeviceXRel(_swigarg0))
static PyObject *_wrap_wxDC_LogicalToDeviceXRel(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    long  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sl:wxDC_LogicalToDeviceXRel",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_LogicalToDeviceXRel. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_LogicalToDeviceXRel(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_LogicalToDeviceY(_swigobj,_swigarg0)  (_swigobj->LogicalToDeviceY(_swigarg0))
static PyObject *_wrap_wxDC_LogicalToDeviceY(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    long  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sl:wxDC_LogicalToDeviceY",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_LogicalToDeviceY. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_LogicalToDeviceY(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_LogicalToDeviceYRel(_swigobj,_swigarg0)  (_swigobj->LogicalToDeviceYRel(_swigarg0))
static PyObject *_wrap_wxDC_LogicalToDeviceYRel(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    long  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sl:wxDC_LogicalToDeviceYRel",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_LogicalToDeviceYRel. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_LogicalToDeviceYRel(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_MaxX(_swigobj)  (_swigobj->MaxX())
static PyObject *_wrap_wxDC_MaxX(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_MaxX",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_MaxX. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_MaxX(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_MaxY(_swigobj)  (_swigobj->MaxY())
static PyObject *_wrap_wxDC_MaxY(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_MaxY",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_MaxY. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_MaxY(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_MinX(_swigobj)  (_swigobj->MinX())
static PyObject *_wrap_wxDC_MinX(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_MinX",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_MinX. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_MinX(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_MinY(_swigobj)  (_swigobj->MinY())
static PyObject *_wrap_wxDC_MinY(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    long  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_MinY",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_MinY. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (long )wxDC_MinY(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("l",_result);
    return _resultobj;
}

#define wxDC_Ok(_swigobj)  (_swigobj->Ok())
static PyObject *_wrap_wxDC_Ok(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_Ok",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_Ok. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxDC_Ok(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxDC_SetDeviceOrigin(_swigobj,_swigarg0,_swigarg1)  (_swigobj->SetDeviceOrigin(_swigarg0,_swigarg1))
static PyObject *_wrap_wxDC_SetDeviceOrigin(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sll:wxDC_SetDeviceOrigin",&_argc0,&_arg1,&_arg2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetDeviceOrigin. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetDeviceOrigin(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetBackground(_swigobj,_swigarg0)  (_swigobj->SetBackground(_swigarg0))
static PyObject *_wrap_wxDC_SetBackground(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxBrush * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxDC_SetBackground",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetBackground. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxBrush_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxDC_SetBackground. Expected _wxBrush_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetBackground(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetBackgroundMode(_swigobj,_swigarg0)  (_swigobj->SetBackgroundMode(_swigarg0))
static PyObject *_wrap_wxDC_SetBackgroundMode(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxDC_SetBackgroundMode",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetBackgroundMode. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetBackgroundMode(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetClippingRegion(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3)  (_swigobj->SetClippingRegion(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_wxDC_SetClippingRegion(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    long  _arg1;
    long  _arg2;
    long  _arg3;
    long  _arg4;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sllll:wxDC_SetClippingRegion",&_argc0,&_arg1,&_arg2,&_arg3,&_arg4)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetClippingRegion. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetClippingRegion(_arg0,_arg1,_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetPalette(_swigobj,_swigarg0)  (_swigobj->SetPalette(_swigarg0))
static PyObject *_wrap_wxDC_SetPalette(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxPalette * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxDC_SetPalette",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetPalette. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxPalette_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxDC_SetPalette. Expected _wxPalette_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetPalette(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetBrush(_swigobj,_swigarg0)  (_swigobj->SetBrush(_swigarg0))
static PyObject *_wrap_wxDC_SetBrush(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxBrush * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxDC_SetBrush",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetBrush. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxBrush_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxDC_SetBrush. Expected _wxBrush_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetBrush(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetFont(_swigobj,_swigarg0)  (_swigobj->SetFont(_swigarg0))
static PyObject *_wrap_wxDC_SetFont(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxFont * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxDC_SetFont",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetFont. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxFont_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxDC_SetFont. Expected _wxFont_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetFont(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetLogicalFunction(_swigobj,_swigarg0)  (_swigobj->SetLogicalFunction(_swigarg0))
static PyObject *_wrap_wxDC_SetLogicalFunction(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxDC_SetLogicalFunction",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetLogicalFunction. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetLogicalFunction(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetMapMode(_swigobj,_swigarg0)  (_swigobj->SetMapMode(_swigarg0))
static PyObject *_wrap_wxDC_SetMapMode(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxDC_SetMapMode",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetMapMode. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetMapMode(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetOptimization(_swigobj,_swigarg0)  (_swigobj->SetOptimization(_swigarg0))
static PyObject *_wrap_wxDC_SetOptimization(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    bool  _arg1;
    char * _argc0 = 0;
    int tempbool1;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxDC_SetOptimization",&_argc0,&tempbool1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetOptimization. Expected _wxDC_p.");
        return NULL;
        }
    }
    _arg1 = (bool ) tempbool1;
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetOptimization(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetPen(_swigobj,_swigarg0)  (_swigobj->SetPen(_swigarg0))
static PyObject *_wrap_wxDC_SetPen(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxPen * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxDC_SetPen",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetPen. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxPen_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxDC_SetPen. Expected _wxPen_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetPen(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetTextBackground(_swigobj,_swigarg0)  (_swigobj->SetTextBackground(_swigarg0))
static PyObject *_wrap_wxDC_SetTextBackground(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxColour * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxDC_SetTextBackground",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetTextBackground. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxDC_SetTextBackground. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetTextBackground(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetTextForeground(_swigobj,_swigarg0)  (_swigobj->SetTextForeground(_swigarg0))
static PyObject *_wrap_wxDC_SetTextForeground(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxColour * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxDC_SetTextForeground",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetTextForeground. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxDC_SetTextForeground. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetTextForeground(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_SetUserScale(_swigobj,_swigarg0,_swigarg1)  (_swigobj->SetUserScale(_swigarg0,_swigarg1))
static PyObject *_wrap_wxDC_SetUserScale(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    double  _arg1;
    double  _arg2;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sdd:wxDC_SetUserScale",&_argc0,&_arg1,&_arg2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_SetUserScale. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_SetUserScale(_arg0,_arg1,_arg2);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxDC_StartDoc(_swigobj,_swigarg0)  (_swigobj->StartDoc(_swigarg0))
static PyObject *_wrap_wxDC_StartDoc(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxDC * _arg0;
    wxString * _arg1;
    char * _argc0 = 0;
    PyObject * _obj1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sO:wxDC_StartDoc",&_argc0,&_obj1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_StartDoc. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    if (!PyString_Check(_obj1)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg1 = new wxString(PyString_AsString(_obj1), PyString_Size(_obj1));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxDC_StartDoc(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
{
    if (_obj1)
        delete _arg1;
}
    return _resultobj;
}

#define wxDC_StartPage(_swigobj)  (_swigobj->StartPage())
static PyObject *_wrap_wxDC_StartPage(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxDC_StartPage",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_StartPage. Expected _wxDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_StartPage(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

static void  wxDC_DrawBitmap(wxDC *self,wxBitmap & bitmap,long  x,long  y,bool  swapPalette) {
            wxMemoryDC* memDC = new wxMemoryDC;
            memDC->SelectObject(bitmap);
#ifdef __WXMSW__
            if (swapPalette)
                self->SetPalette(*bitmap.GetPalette());
#endif
            self->Blit(x, y, bitmap.GetWidth(), bitmap.GetHeight(), memDC,
                    0, 0, self->GetLogicalFunction());
            memDC->SelectObject(wxNullBitmap);
            delete memDC;
        }
static PyObject *_wrap_wxDC_DrawBitmap(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxDC * _arg0;
    wxBitmap * _arg1;
    long  _arg2;
    long  _arg3;
    bool  _arg4 = (1);
    char * _argc0 = 0;
    char * _argc1 = 0;
    int tempbool4;

    self = self;
    if(!PyArg_ParseTuple(args,"ssll|i:wxDC_DrawBitmap",&_argc0,&_argc1,&_arg2,&_arg3,&tempbool4)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxDC_DrawBitmap. Expected _wxDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxDC_DrawBitmap. Expected _wxBitmap_p.");
        return NULL;
        }
    }
    _arg4 = (bool ) tempbool4;
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxDC_DrawBitmap(_arg0,*_arg1,_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

static void *SwigwxMemoryDCTowxDC(void *ptr) {
    wxMemoryDC *src;
    wxDC *dest;
    src = (wxMemoryDC *) ptr;
    dest = (wxDC *) src;
    return (void *) dest;
}

#define new_wxMemoryDC() (new wxMemoryDC())
static PyObject *_wrap_new_wxMemoryDC(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxMemoryDC * _result;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,":new_wxMemoryDC")) 
        return NULL;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxMemoryDC *)new_wxMemoryDC();

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxMemoryDC_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxMemoryDC_SelectObject(_swigobj,_swigarg0)  (_swigobj->SelectObject(_swigarg0))
static PyObject *_wrap_wxMemoryDC_SelectObject(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxMemoryDC * _arg0;
    wxBitmap * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxMemoryDC_SelectObject",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxMemoryDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxMemoryDC_SelectObject. Expected _wxMemoryDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxMemoryDC_SelectObject. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        wxMemoryDC_SelectObject(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

static void *SwigwxScreenDCTowxDC(void *ptr) {
    wxScreenDC *src;
    wxDC *dest;
    src = (wxScreenDC *) ptr;
    dest = (wxDC *) src;
    return (void *) dest;
}

#define new_wxScreenDC() (new wxScreenDC())
static PyObject *_wrap_new_wxScreenDC(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxScreenDC * _result;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,":new_wxScreenDC")) 
        return NULL;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxScreenDC *)new_wxScreenDC();

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxScreenDC_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define wxScreenDC_StartDrawingOnTop(_swigobj,_swigarg0)  (_swigobj->StartDrawingOnTop(_swigarg0))
static PyObject *_wrap_wxScreenDC_StartDrawingOnTop(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxScreenDC * _arg0;
    wxWindow * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxScreenDC_StartDrawingOnTop",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxScreenDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxScreenDC_StartDrawingOnTop. Expected _wxScreenDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxWindow_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxScreenDC_StartDrawingOnTop. Expected _wxWindow_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxScreenDC_StartDrawingOnTop(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxScreenDC_StartDrawingOnTopRect(_swigobj,_swigarg0)  (_swigobj->StartDrawingOnTop(_swigarg0))
static PyObject *_wrap_wxScreenDC_StartDrawingOnTopRect(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxScreenDC * _arg0;
    wxRect * _arg1 = NULL;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s|s:wxScreenDC_StartDrawingOnTopRect",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxScreenDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxScreenDC_StartDrawingOnTopRect. Expected _wxScreenDC_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxRect_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxScreenDC_StartDrawingOnTopRect. Expected _wxRect_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxScreenDC_StartDrawingOnTopRect(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxScreenDC_EndDrawingOnTop(_swigobj)  (_swigobj->EndDrawingOnTop())
static PyObject *_wrap_wxScreenDC_EndDrawingOnTop(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxScreenDC * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxScreenDC_EndDrawingOnTop",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxScreenDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxScreenDC_EndDrawingOnTop. Expected _wxScreenDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxScreenDC_EndDrawingOnTop(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

static void *SwigwxClientDCTowxDC(void *ptr) {
    wxClientDC *src;
    wxDC *dest;
    src = (wxClientDC *) ptr;
    dest = (wxDC *) src;
    return (void *) dest;
}

#define new_wxClientDC(_swigarg0) (new wxClientDC(_swigarg0))
static PyObject *_wrap_new_wxClientDC(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxClientDC * _result;
    wxWindow * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:new_wxClientDC",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxWindow_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of new_wxClientDC. Expected _wxWindow_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxClientDC *)new_wxClientDC(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxClientDC_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static void *SwigwxPaintDCTowxDC(void *ptr) {
    wxPaintDC *src;
    wxDC *dest;
    src = (wxPaintDC *) ptr;
    dest = (wxDC *) src;
    return (void *) dest;
}

#define new_wxPaintDC(_swigarg0) (new wxPaintDC(_swigarg0))
static PyObject *_wrap_new_wxPaintDC(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPaintDC * _result;
    wxWindow * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:new_wxPaintDC",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxWindow_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of new_wxPaintDC. Expected _wxWindow_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxPaintDC *)new_wxPaintDC(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxPaintDC_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static void *SwigwxWindowDCTowxDC(void *ptr) {
    wxWindowDC *src;
    wxDC *dest;
    src = (wxWindowDC *) ptr;
    dest = (wxDC *) src;
    return (void *) dest;
}

#define new_wxWindowDC(_swigarg0) (new wxWindowDC(_swigarg0))
static PyObject *_wrap_new_wxWindowDC(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxWindowDC * _result;
    wxWindow * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:new_wxWindowDC",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxWindow_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of new_wxWindowDC. Expected _wxWindow_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxWindowDC *)new_wxWindowDC(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxWindowDC_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

static void *SwigwxPrinterDCTowxDC(void *ptr) {
    wxPrinterDC *src;
    wxDC *dest;
    src = (wxPrinterDC *) ptr;
    dest = (wxDC *) src;
    return (void *) dest;
}

#define new_wxPrinterDC(_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4) (new wxPrinterDC(_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4))
static PyObject *_wrap_new_wxPrinterDC(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPrinterDC * _result;
    wxString * _arg0;
    wxString * _arg1;
    wxString * _arg2;
    bool  _arg3 = (1);
    int  _arg4 = (wxPORTRAIT);
    PyObject * _obj0 = 0;
    PyObject * _obj1 = 0;
    PyObject * _obj2 = 0;
    int tempbool3;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"OOO|ii:new_wxPrinterDC",&_obj0,&_obj1,&_obj2,&tempbool3,&_arg4)) 
        return NULL;
{
    if (!PyString_Check(_obj0)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg0 = new wxString(PyString_AsString(_obj0), PyString_Size(_obj0));
}
{
    if (!PyString_Check(_obj1)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg1 = new wxString(PyString_AsString(_obj1), PyString_Size(_obj1));
}
{
    if (!PyString_Check(_obj2)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg2 = new wxString(PyString_AsString(_obj2), PyString_Size(_obj2));
}
    _arg3 = (bool ) tempbool3;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxPrinterDC *)new_wxPrinterDC(*_arg0,*_arg1,*_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxPrinterDC_p");
    _resultobj = Py_BuildValue("s",_ptemp);
{
    if (_obj0)
        delete _arg0;
}
{
    if (_obj1)
        delete _arg1;
}
{
    if (_obj2)
        delete _arg2;
}
    return _resultobj;
}

static void *SwigwxMetaFileDCTowxDC(void *ptr) {
    wxMetaFileDC *src;
    wxDC *dest;
    src = (wxMetaFileDC *) ptr;
    dest = (wxDC *) src;
    return (void *) dest;
}

#define new_wxMetaFileDC(_swigarg0) (new wxMetaFileDC(_swigarg0))
static PyObject *_wrap_new_wxMetaFileDC(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxMetaFileDC * _result;
    wxString * _arg0 = &wxPyEmptyStr;
    PyObject * _obj0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"|O:new_wxMetaFileDC",&_obj0)) 
        return NULL;
    if (_obj0)
{
    if (!PyString_Check(_obj0)) {
        PyErr_SetString(PyExc_TypeError, wxStringErrorMsg);
        return NULL;
    }
    _arg0 = new wxString(PyString_AsString(_obj0), PyString_Size(_obj0));
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxMetaFileDC *)new_wxMetaFileDC(*_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxMetaFileDC_p");
    _resultobj = Py_BuildValue("s",_ptemp);
{
    if (_obj0)
        delete _arg0;
}
    return _resultobj;
}

#define wxMetaFileDC_Close(_swigobj)  (_swigobj->Close())
static PyObject *_wrap_wxMetaFileDC_Close(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxMetaFile * _result;
    wxMetaFileDC * _arg0;
    char * _argc0 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxMetaFileDC_Close",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxMetaFileDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxMetaFileDC_Close. Expected _wxMetaFileDC_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxMetaFile *)wxMetaFileDC_Close(_arg0);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxMetaFile_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define new_wxPalette(_swigarg0,_swigarg1,_swigarg2,_swigarg3) (new wxPalette(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_new_wxPalette(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPalette * _result;
    int  _arg0;
    byte * _arg1;
    byte * _arg2;
    byte * _arg3;
    PyObject * _obj1 = 0;
    PyObject * _obj2 = 0;
    PyObject * _obj3 = 0;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"OOO:new_wxPalette",&_obj1,&_obj2,&_obj3)) 
        return NULL;
{
    _arg1 = byte_LIST_helper(_obj1);
    if (_arg1 == NULL) {
        return NULL;
    }
}
{
    _arg2 = byte_LIST_helper(_obj2);
    if (_arg2 == NULL) {
        return NULL;
    }
}
    if (_obj3)
{
    _arg3 = byte_LIST_helper(_obj3);
    if (_arg3 == NULL) {
        return NULL;
    }
}
{
    if (_obj1) {
        _arg0 = PyList_Size(_obj1);
    }
    else {
        _arg0 = 0;
    }
}
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxPalette *)new_wxPalette(_arg0,_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxPalette_p");
    _resultobj = Py_BuildValue("s",_ptemp);
{
    delete [] _arg1;
}
{
    delete [] _arg2;
}
{
    delete [] _arg3;
}
    return _resultobj;
}

#define delete_wxPalette(_swigobj) (delete _swigobj)
static PyObject *_wrap_delete_wxPalette(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxPalette * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:delete_wxPalette",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPalette_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of delete_wxPalette. Expected _wxPalette_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        delete_wxPalette(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxPalette_GetPixel(_swigobj,_swigarg0,_swigarg1,_swigarg2)  (_swigobj->GetPixel(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_wxPalette_GetPixel(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxPalette * _arg0;
    byte  _arg1;
    byte  _arg2;
    byte  _arg3;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sbbb:wxPalette_GetPixel",&_argc0,&_arg1,&_arg2,&_arg3)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPalette_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPalette_GetPixel. Expected _wxPalette_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxPalette_GetPixel(_arg0,_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxPalette_GetRGB(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3)  (_swigobj->GetRGB(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_wxPalette_GetRGB(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxPalette * _arg0;
    int  _arg1;
    byte * _arg2;
    byte * _arg3;
    byte * _arg4;
    char * _argc0 = 0;
    char * _argc2 = 0;
    char * _argc3 = 0;
    char * _argc4 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sisss:wxPalette_GetRGB",&_argc0,&_arg1,&_argc2,&_argc3,&_argc4)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPalette_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPalette_GetRGB. Expected _wxPalette_p.");
        return NULL;
        }
    }
    if (_argc2) {
        if (SWIG_GetPtr(_argc2,(void **) &_arg2,"_byte_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 3 of wxPalette_GetRGB. Expected _byte_p.");
        return NULL;
        }
    }
    if (_argc3) {
        if (SWIG_GetPtr(_argc3,(void **) &_arg3,"_byte_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 4 of wxPalette_GetRGB. Expected _byte_p.");
        return NULL;
        }
    }
    if (_argc4) {
        if (SWIG_GetPtr(_argc4,(void **) &_arg4,"_byte_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 5 of wxPalette_GetRGB. Expected _byte_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxPalette_GetRGB(_arg0,_arg1,_arg2,_arg3,_arg4);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxPalette_Ok(_swigobj)  (_swigobj->Ok())
static PyObject *_wrap_wxPalette_Ok(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxPalette * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxPalette_Ok",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxPalette_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxPalette_Ok. Expected _wxPalette_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxPalette_Ok(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define new_wxImageList(_swigarg0,_swigarg1,_swigarg2,_swigarg3) (new wxImageList(_swigarg0,_swigarg1,_swigarg2,_swigarg3))
static PyObject *_wrap_new_wxImageList(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxImageList * _result;
    int  _arg0;
    int  _arg1;
    bool  _arg2 = (1);
    int  _arg3 = 1;
    int tempbool2;
    char _ptemp[128];

    self = self;
    if(!PyArg_ParseTuple(args,"ii|ii:new_wxImageList",&_arg0,&_arg1,&tempbool2,&_arg3)) 
        return NULL;
    _arg2 = (bool ) tempbool2;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (wxImageList *)new_wxImageList(_arg0,_arg1,_arg2,_arg3);

    wxPy_END_ALLOW_THREADS;
}    SWIG_MakePtr(_ptemp, (char *) _result,"_wxImageList_p");
    _resultobj = Py_BuildValue("s",_ptemp);
    return _resultobj;
}

#define delete_wxImageList(_swigobj) (delete _swigobj)
static PyObject *_wrap_delete_wxImageList(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    wxImageList * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:delete_wxImageList",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of delete_wxImageList. Expected _wxImageList_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        delete_wxImageList(_arg0);

    wxPy_END_ALLOW_THREADS;
}    Py_INCREF(Py_None);
    _resultobj = Py_None;
    return _resultobj;
}

#define wxImageList_Add(_swigobj,_swigarg0,_swigarg1)  (_swigobj->Add(_swigarg0,_swigarg1))
static PyObject *_wrap_wxImageList_Add(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxImageList * _arg0;
    wxBitmap * _arg1;
    wxBitmap * _arg2 = &wxNullBitmap;
    char * _argc0 = 0;
    char * _argc1 = 0;
    char * _argc2 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss|s:wxImageList_Add",&_argc0,&_argc1,&_argc2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxImageList_Add. Expected _wxImageList_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxImageList_Add. Expected _wxBitmap_p.");
        return NULL;
        }
    }
    if (_argc2) {
        if (SWIG_GetPtr(_argc2,(void **) &_arg2,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 3 of wxImageList_Add. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxImageList_Add(_arg0,*_arg1,*_arg2);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxImageList_AddWithColourMask(_swigobj,_swigarg0,_swigarg1)  (_swigobj->Add(_swigarg0,_swigarg1))
static PyObject *_wrap_wxImageList_AddWithColourMask(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxImageList * _arg0;
    wxBitmap * _arg1;
    wxColour * _arg2;
    char * _argc0 = 0;
    char * _argc1 = 0;
    char * _argc2 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sss:wxImageList_AddWithColourMask",&_argc0,&_argc1,&_argc2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxImageList_AddWithColourMask. Expected _wxImageList_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxImageList_AddWithColourMask. Expected _wxBitmap_p.");
        return NULL;
        }
    }
    if (_argc2) {
        if (SWIG_GetPtr(_argc2,(void **) &_arg2,"_wxColour_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 3 of wxImageList_AddWithColourMask. Expected _wxColour_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxImageList_AddWithColourMask(_arg0,*_arg1,*_arg2);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxImageList_AddIcon(_swigobj,_swigarg0)  (_swigobj->Add(_swigarg0))
static PyObject *_wrap_wxImageList_AddIcon(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxImageList * _arg0;
    wxIcon * _arg1;
    char * _argc0 = 0;
    char * _argc1 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"ss:wxImageList_AddIcon",&_argc0,&_argc1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxImageList_AddIcon. Expected _wxImageList_p.");
        return NULL;
        }
    }
    if (_argc1) {
        if (SWIG_GetPtr(_argc1,(void **) &_arg1,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 2 of wxImageList_AddIcon. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxImageList_AddIcon(_arg0,*_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxImageList_Replace(_swigobj,_swigarg0,_swigarg1,_swigarg2)  (_swigobj->Replace(_swigarg0,_swigarg1,_swigarg2))
static PyObject *_wrap_wxImageList_Replace(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxImageList * _arg0;
    int  _arg1;
    wxBitmap * _arg2;
    wxBitmap * _arg3 = &wxNullBitmap;
    char * _argc0 = 0;
    char * _argc2 = 0;
    char * _argc3 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sis|s:wxImageList_Replace",&_argc0,&_arg1,&_argc2,&_argc3)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxImageList_Replace. Expected _wxImageList_p.");
        return NULL;
        }
    }
    if (_argc2) {
        if (SWIG_GetPtr(_argc2,(void **) &_arg2,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 3 of wxImageList_Replace. Expected _wxBitmap_p.");
        return NULL;
        }
    }
    if (_argc3) {
        if (SWIG_GetPtr(_argc3,(void **) &_arg3,"_wxBitmap_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 4 of wxImageList_Replace. Expected _wxBitmap_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxImageList_Replace(_arg0,_arg1,*_arg2,*_arg3);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxImageList_ReplaceIcon(_swigobj,_swigarg0,_swigarg1)  (_swigobj->Replace(_swigarg0,_swigarg1))
static PyObject *_wrap_wxImageList_ReplaceIcon(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxImageList * _arg0;
    int  _arg1;
    wxIcon * _arg2;
    char * _argc0 = 0;
    char * _argc2 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"sis:wxImageList_ReplaceIcon",&_argc0,&_arg1,&_argc2)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxImageList_ReplaceIcon. Expected _wxImageList_p.");
        return NULL;
        }
    }
    if (_argc2) {
        if (SWIG_GetPtr(_argc2,(void **) &_arg2,"_wxIcon_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 3 of wxImageList_ReplaceIcon. Expected _wxIcon_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxImageList_ReplaceIcon(_arg0,_arg1,*_arg2);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxImageList_Draw(_swigobj,_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5)  (_swigobj->Draw(_swigarg0,_swigarg1,_swigarg2,_swigarg3,_swigarg4,_swigarg5))
static PyObject *_wrap_wxImageList_Draw(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxImageList * _arg0;
    int  _arg1;
    wxDC * _arg2;
    int  _arg3;
    int  _arg4;
    int  _arg5 = (wxIMAGELIST_DRAW_NORMAL);
    bool  _arg6 = (0);
    char * _argc0 = 0;
    char * _argc2 = 0;
    int tempbool6;

    self = self;
    if(!PyArg_ParseTuple(args,"sisii|ii:wxImageList_Draw",&_argc0,&_arg1,&_argc2,&_arg3,&_arg4,&_arg5,&tempbool6)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxImageList_Draw. Expected _wxImageList_p.");
        return NULL;
        }
    }
    if (_argc2) {
        if (SWIG_GetPtr(_argc2,(void **) &_arg2,"_wxDC_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 3 of wxImageList_Draw. Expected _wxDC_p.");
        return NULL;
        }
    }
    _arg6 = (bool ) tempbool6;
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxImageList_Draw(_arg0,_arg1,*_arg2,_arg3,_arg4,_arg5,_arg6);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxImageList_GetImageCount(_swigobj)  (_swigobj->GetImageCount())
static PyObject *_wrap_wxImageList_GetImageCount(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    int  _result;
    wxImageList * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxImageList_GetImageCount",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxImageList_GetImageCount. Expected _wxImageList_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (int )wxImageList_GetImageCount(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxImageList_Remove(_swigobj,_swigarg0)  (_swigobj->Remove(_swigarg0))
static PyObject *_wrap_wxImageList_Remove(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxImageList * _arg0;
    int  _arg1;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"si:wxImageList_Remove",&_argc0,&_arg1)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxImageList_Remove. Expected _wxImageList_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxImageList_Remove(_arg0,_arg1);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

#define wxImageList_RemoveAll(_swigobj)  (_swigobj->RemoveAll())
static PyObject *_wrap_wxImageList_RemoveAll(PyObject *self, PyObject *args) {
    PyObject * _resultobj;
    bool  _result;
    wxImageList * _arg0;
    char * _argc0 = 0;

    self = self;
    if(!PyArg_ParseTuple(args,"s:wxImageList_RemoveAll",&_argc0)) 
        return NULL;
    if (_argc0) {
        if (SWIG_GetPtr(_argc0,(void **) &_arg0,"_wxImageList_p")) {
            PyErr_SetString(PyExc_TypeError,"Type error in argument 1 of wxImageList_RemoveAll. Expected _wxImageList_p.");
        return NULL;
        }
    }
{
    wxPy_BEGIN_ALLOW_THREADS;
        _result = (bool )wxImageList_RemoveAll(_arg0);

    wxPy_END_ALLOW_THREADS;
}    _resultobj = Py_BuildValue("i",_result);
    return _resultobj;
}

static PyMethodDef gdicMethods[] = {
	 { "wxImageList_RemoveAll", _wrap_wxImageList_RemoveAll, 1 },
	 { "wxImageList_Remove", _wrap_wxImageList_Remove, 1 },
	 { "wxImageList_GetImageCount", _wrap_wxImageList_GetImageCount, 1 },
	 { "wxImageList_Draw", _wrap_wxImageList_Draw, 1 },
	 { "wxImageList_ReplaceIcon", _wrap_wxImageList_ReplaceIcon, 1 },
	 { "wxImageList_Replace", _wrap_wxImageList_Replace, 1 },
	 { "wxImageList_AddIcon", _wrap_wxImageList_AddIcon, 1 },
	 { "wxImageList_AddWithColourMask", _wrap_wxImageList_AddWithColourMask, 1 },
	 { "wxImageList_Add", _wrap_wxImageList_Add, 1 },
	 { "delete_wxImageList", _wrap_delete_wxImageList, 1 },
	 { "new_wxImageList", _wrap_new_wxImageList, 1 },
	 { "wxPalette_Ok", _wrap_wxPalette_Ok, 1 },
	 { "wxPalette_GetRGB", _wrap_wxPalette_GetRGB, 1 },
	 { "wxPalette_GetPixel", _wrap_wxPalette_GetPixel, 1 },
	 { "delete_wxPalette", _wrap_delete_wxPalette, 1 },
	 { "new_wxPalette", _wrap_new_wxPalette, 1 },
	 { "wxMetaFileDC_Close", _wrap_wxMetaFileDC_Close, 1 },
	 { "new_wxMetaFileDC", _wrap_new_wxMetaFileDC, 1 },
	 { "new_wxPrinterDC", _wrap_new_wxPrinterDC, 1 },
	 { "new_wxWindowDC", _wrap_new_wxWindowDC, 1 },
	 { "new_wxPaintDC", _wrap_new_wxPaintDC, 1 },
	 { "new_wxClientDC", _wrap_new_wxClientDC, 1 },
	 { "wxScreenDC_EndDrawingOnTop", _wrap_wxScreenDC_EndDrawingOnTop, 1 },
	 { "wxScreenDC_StartDrawingOnTopRect", _wrap_wxScreenDC_StartDrawingOnTopRect, 1 },
	 { "wxScreenDC_StartDrawingOnTop", _wrap_wxScreenDC_StartDrawingOnTop, 1 },
	 { "new_wxScreenDC", _wrap_new_wxScreenDC, 1 },
	 { "wxMemoryDC_SelectObject", _wrap_wxMemoryDC_SelectObject, 1 },
	 { "new_wxMemoryDC", _wrap_new_wxMemoryDC, 1 },
	 { "wxDC_DrawBitmap", _wrap_wxDC_DrawBitmap, 1 },
	 { "wxDC_StartPage", _wrap_wxDC_StartPage, 1 },
	 { "wxDC_StartDoc", _wrap_wxDC_StartDoc, 1 },
	 { "wxDC_SetUserScale", _wrap_wxDC_SetUserScale, 1 },
	 { "wxDC_SetTextForeground", _wrap_wxDC_SetTextForeground, 1 },
	 { "wxDC_SetTextBackground", _wrap_wxDC_SetTextBackground, 1 },
	 { "wxDC_SetPen", _wrap_wxDC_SetPen, 1 },
	 { "wxDC_SetOptimization", _wrap_wxDC_SetOptimization, 1 },
	 { "wxDC_SetMapMode", _wrap_wxDC_SetMapMode, 1 },
	 { "wxDC_SetLogicalFunction", _wrap_wxDC_SetLogicalFunction, 1 },
	 { "wxDC_SetFont", _wrap_wxDC_SetFont, 1 },
	 { "wxDC_SetBrush", _wrap_wxDC_SetBrush, 1 },
	 { "wxDC_SetPalette", _wrap_wxDC_SetPalette, 1 },
	 { "wxDC_SetClippingRegion", _wrap_wxDC_SetClippingRegion, 1 },
	 { "wxDC_SetBackgroundMode", _wrap_wxDC_SetBackgroundMode, 1 },
	 { "wxDC_SetBackground", _wrap_wxDC_SetBackground, 1 },
	 { "wxDC_SetDeviceOrigin", _wrap_wxDC_SetDeviceOrigin, 1 },
	 { "wxDC_Ok", _wrap_wxDC_Ok, 1 },
	 { "wxDC_MinY", _wrap_wxDC_MinY, 1 },
	 { "wxDC_MinX", _wrap_wxDC_MinX, 1 },
	 { "wxDC_MaxY", _wrap_wxDC_MaxY, 1 },
	 { "wxDC_MaxX", _wrap_wxDC_MaxX, 1 },
	 { "wxDC_LogicalToDeviceYRel", _wrap_wxDC_LogicalToDeviceYRel, 1 },
	 { "wxDC_LogicalToDeviceY", _wrap_wxDC_LogicalToDeviceY, 1 },
	 { "wxDC_LogicalToDeviceXRel", _wrap_wxDC_LogicalToDeviceXRel, 1 },
	 { "wxDC_LogicalToDeviceX", _wrap_wxDC_LogicalToDeviceX, 1 },
	 { "wxDC_GetTextForeground", _wrap_wxDC_GetTextForeground, 1 },
	 { "wxDC_GetFullTextExtent", _wrap_wxDC_GetFullTextExtent, 1 },
	 { "wxDC_GetTextExtent", _wrap_wxDC_GetTextExtent, 1 },
	 { "wxDC_GetTextBackground", _wrap_wxDC_GetTextBackground, 1 },
	 { "wxDC_GetSize", _wrap_wxDC_GetSize, 1 },
	 { "wxDC_GetSizeTuple", _wrap_wxDC_GetSizeTuple, 1 },
	 { "wxDC_GetPixel", _wrap_wxDC_GetPixel, 1 },
	 { "wxDC_GetPen", _wrap_wxDC_GetPen, 1 },
	 { "wxDC_GetOptimization", _wrap_wxDC_GetOptimization, 1 },
	 { "wxDC_GetMapMode", _wrap_wxDC_GetMapMode, 1 },
	 { "wxDC_GetLogicalFunction", _wrap_wxDC_GetLogicalFunction, 1 },
	 { "wxDC_GetFont", _wrap_wxDC_GetFont, 1 },
	 { "wxDC_GetClippingBox", _wrap_wxDC_GetClippingBox, 1 },
	 { "wxDC_GetCharWidth", _wrap_wxDC_GetCharWidth, 1 },
	 { "wxDC_GetCharHeight", _wrap_wxDC_GetCharHeight, 1 },
	 { "wxDC_GetBrush", _wrap_wxDC_GetBrush, 1 },
	 { "wxDC_GetBackground", _wrap_wxDC_GetBackground, 1 },
	 { "wxDC_FloodFill", _wrap_wxDC_FloodFill, 1 },
	 { "wxDC_EndPage", _wrap_wxDC_EndPage, 1 },
	 { "wxDC_EndDrawing", _wrap_wxDC_EndDrawing, 1 },
	 { "wxDC_EndDoc", _wrap_wxDC_EndDoc, 1 },
	 { "wxDC_DrawText", _wrap_wxDC_DrawText, 1 },
	 { "wxDC_DrawSpline", _wrap_wxDC_DrawSpline, 1 },
	 { "wxDC_DrawRoundedRectangle", _wrap_wxDC_DrawRoundedRectangle, 1 },
	 { "wxDC_DrawRectangle", _wrap_wxDC_DrawRectangle, 1 },
	 { "wxDC_DrawPoint", _wrap_wxDC_DrawPoint, 1 },
	 { "wxDC_DrawPolygon", _wrap_wxDC_DrawPolygon, 1 },
	 { "wxDC_DrawLines", _wrap_wxDC_DrawLines, 1 },
	 { "wxDC_DrawLine", _wrap_wxDC_DrawLine, 1 },
	 { "wxDC_DrawIcon", _wrap_wxDC_DrawIcon, 1 },
	 { "wxDC_DrawEllipticArc", _wrap_wxDC_DrawEllipticArc, 1 },
	 { "wxDC_DrawEllipse", _wrap_wxDC_DrawEllipse, 1 },
	 { "wxDC_DrawCircle", _wrap_wxDC_DrawCircle, 1 },
	 { "wxDC_DrawArc", _wrap_wxDC_DrawArc, 1 },
	 { "wxDC_DeviceToLogicalYRel", _wrap_wxDC_DeviceToLogicalYRel, 1 },
	 { "wxDC_DeviceToLogicalY", _wrap_wxDC_DeviceToLogicalY, 1 },
	 { "wxDC_DeviceToLogicalXRel", _wrap_wxDC_DeviceToLogicalXRel, 1 },
	 { "wxDC_DeviceToLogicalX", _wrap_wxDC_DeviceToLogicalX, 1 },
	 { "wxDC_DestroyClippingRegion", _wrap_wxDC_DestroyClippingRegion, 1 },
	 { "wxDC_CrossHair", _wrap_wxDC_CrossHair, 1 },
	 { "wxDC_Clear", _wrap_wxDC_Clear, 1 },
	 { "wxDC_Blit", _wrap_wxDC_Blit, 1 },
	 { "wxDC_BeginDrawing", _wrap_wxDC_BeginDrawing, 1 },
	 { "delete_wxDC", _wrap_delete_wxDC, 1 },
	 { "wxBrush_SetStyle", _wrap_wxBrush_SetStyle, 1 },
	 { "wxBrush_SetStipple", _wrap_wxBrush_SetStipple, 1 },
	 { "wxBrush_SetColour", _wrap_wxBrush_SetColour, 1 },
	 { "wxBrush_Ok", _wrap_wxBrush_Ok, 1 },
	 { "wxBrush_GetStyle", _wrap_wxBrush_GetStyle, 1 },
	 { "wxBrush_GetStipple", _wrap_wxBrush_GetStipple, 1 },
	 { "wxBrush_GetColour", _wrap_wxBrush_GetColour, 1 },
	 { "new_wxBrush", _wrap_new_wxBrush, 1 },
	 { "wxPen_SetStipple", _wrap_wxPen_SetStipple, 1 },
	 { "wxPen_SetDashes", _wrap_wxPen_SetDashes, 1 },
	 { "wxPen_GetStipple", _wrap_wxPen_GetStipple, 1 },
	 { "wxPen_GetDashes", _wrap_wxPen_GetDashes, 1 },
	 { "wxPen_SetWidth", _wrap_wxPen_SetWidth, 1 },
	 { "wxPen_SetStyle", _wrap_wxPen_SetStyle, 1 },
	 { "wxPen_SetJoin", _wrap_wxPen_SetJoin, 1 },
	 { "wxPen_SetColour", _wrap_wxPen_SetColour, 1 },
	 { "wxPen_SetCap", _wrap_wxPen_SetCap, 1 },
	 { "wxPen_Ok", _wrap_wxPen_Ok, 1 },
	 { "wxPen_GetWidth", _wrap_wxPen_GetWidth, 1 },
	 { "wxPen_GetStyle", _wrap_wxPen_GetStyle, 1 },
	 { "wxPen_GetJoin", _wrap_wxPen_GetJoin, 1 },
	 { "wxPen_GetColour", _wrap_wxPen_GetColour, 1 },
	 { "wxPen_GetCap", _wrap_wxPen_GetCap, 1 },
	 { "new_wxPen", _wrap_new_wxPen, 1 },
	 { "wxColour_Get", _wrap_wxColour_Get, 1 },
	 { "wxColour_Set", _wrap_wxColour_Set, 1 },
	 { "wxColour_Ok", _wrap_wxColour_Ok, 1 },
	 { "wxColour_Blue", _wrap_wxColour_Blue, 1 },
	 { "wxColour_Green", _wrap_wxColour_Green, 1 },
	 { "wxColour_Red", _wrap_wxColour_Red, 1 },
	 { "delete_wxColour", _wrap_delete_wxColour, 1 },
	 { "new_wxColour", _wrap_new_wxColour, 1 },
	 { "wxFont_SetWeight", _wrap_wxFont_SetWeight, 1 },
	 { "wxFont_SetUnderlined", _wrap_wxFont_SetUnderlined, 1 },
	 { "wxFont_SetStyle", _wrap_wxFont_SetStyle, 1 },
	 { "wxFont_SetPointSize", _wrap_wxFont_SetPointSize, 1 },
	 { "wxFont_SetFamily", _wrap_wxFont_SetFamily, 1 },
	 { "wxFont_SetFaceName", _wrap_wxFont_SetFaceName, 1 },
	 { "wxFont_GetWeight", _wrap_wxFont_GetWeight, 1 },
	 { "wxFont_GetUnderlined", _wrap_wxFont_GetUnderlined, 1 },
	 { "wxFont_GetStyle", _wrap_wxFont_GetStyle, 1 },
	 { "wxFont_GetPointSize", _wrap_wxFont_GetPointSize, 1 },
	 { "wxFont_GetFontId", _wrap_wxFont_GetFontId, 1 },
	 { "wxFont_GetFamily", _wrap_wxFont_GetFamily, 1 },
	 { "wxFont_GetFaceName", _wrap_wxFont_GetFaceName, 1 },
	 { "new_wxFont", _wrap_new_wxFont, 1 },
	 { "wxCursor_Ok", _wrap_wxCursor_Ok, 1 },
	 { "delete_wxCursor", _wrap_delete_wxCursor, 1 },
	 { "new_wxCursor", _wrap_new_wxCursor, 1 },
	 { "wxIcon_SetWidth", _wrap_wxIcon_SetWidth, 1 },
	 { "wxIcon_SetHeight", _wrap_wxIcon_SetHeight, 1 },
	 { "wxIcon_SetDepth", _wrap_wxIcon_SetDepth, 1 },
	 { "wxIcon_Ok", _wrap_wxIcon_Ok, 1 },
	 { "wxIcon_LoadFile", _wrap_wxIcon_LoadFile, 1 },
	 { "wxIcon_GetWidth", _wrap_wxIcon_GetWidth, 1 },
	 { "wxIcon_GetHeight", _wrap_wxIcon_GetHeight, 1 },
	 { "wxIcon_GetDepth", _wrap_wxIcon_GetDepth, 1 },
	 { "delete_wxIcon", _wrap_delete_wxIcon, 1 },
	 { "new_wxIcon", _wrap_new_wxIcon, 1 },
	 { "delete_wxMask", _wrap_delete_wxMask, 1 },
	 { "new_wxMask", _wrap_new_wxMask, 1 },
	 { "wxBitmap_SetWidth", _wrap_wxBitmap_SetWidth, 1 },
	 { "wxBitmap_SetPalette", _wrap_wxBitmap_SetPalette, 1 },
	 { "wxBitmap_SetMask", _wrap_wxBitmap_SetMask, 1 },
	 { "wxBitmap_SetHeight", _wrap_wxBitmap_SetHeight, 1 },
	 { "wxBitmap_SetDepth", _wrap_wxBitmap_SetDepth, 1 },
	 { "wxBitmap_SaveFile", _wrap_wxBitmap_SaveFile, 1 },
	 { "wxBitmap_Ok", _wrap_wxBitmap_Ok, 1 },
	 { "wxBitmap_LoadFile", _wrap_wxBitmap_LoadFile, 1 },
	 { "wxBitmap_GetWidth", _wrap_wxBitmap_GetWidth, 1 },
	 { "wxBitmap_GetMask", _wrap_wxBitmap_GetMask, 1 },
	 { "wxBitmap_GetPalette", _wrap_wxBitmap_GetPalette, 1 },
	 { "wxBitmap_GetHeight", _wrap_wxBitmap_GetHeight, 1 },
	 { "wxBitmap_GetDepth", _wrap_wxBitmap_GetDepth, 1 },
	 { "wxBitmap_Create", _wrap_wxBitmap_Create, 1 },
	 { "delete_wxBitmap", _wrap_delete_wxBitmap, 1 },
	 { "new_wxBitmap", _wrap_new_wxBitmap, 1 },
	 { "wxMemoryDCFromDC", _wrap_wxMemoryDCFromDC, 1 },
	 { "wxNamedColour", _wrap_wxNamedColour, 1 },
	 { "wxStockCursor", _wrap_wxStockCursor, 1 },
	 { "wxMaskColour", _wrap_wxMaskColour, 1 },
	 { "wxBitmapFromData", _wrap_wxBitmapFromData, 1 },
	 { "wxNoRefBitmap", _wrap_wxNoRefBitmap, 1 },
	 { "wxEmptyBitmap", _wrap_wxEmptyBitmap, 1 },
	 { NULL, NULL }
};
static PyObject *SWIG_globals;
#ifdef __cplusplus
extern "C" 
#endif
SWIGEXPORT(void,initgdic)() {
	 PyObject *m, *d;
	 SWIG_globals = SWIG_newvarlink();
	 m = Py_InitModule("gdic", gdicMethods);
	 d = PyModule_GetDict(m);
	 PyDict_SetItemString(d,"cvar", SWIG_globals);
	 SWIG_addvarlink(SWIG_globals,"wxNORMAL_FONT",_wrap_wxNORMAL_FONT_get, _wrap_wxNORMAL_FONT_set);
	 SWIG_addvarlink(SWIG_globals,"wxSMALL_FONT",_wrap_wxSMALL_FONT_get, _wrap_wxSMALL_FONT_set);
	 SWIG_addvarlink(SWIG_globals,"wxITALIC_FONT",_wrap_wxITALIC_FONT_get, _wrap_wxITALIC_FONT_set);
	 SWIG_addvarlink(SWIG_globals,"wxSWISS_FONT",_wrap_wxSWISS_FONT_get, _wrap_wxSWISS_FONT_set);
	 SWIG_addvarlink(SWIG_globals,"wxRED_PEN",_wrap_wxRED_PEN_get, _wrap_wxRED_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxCYAN_PEN",_wrap_wxCYAN_PEN_get, _wrap_wxCYAN_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxGREEN_PEN",_wrap_wxGREEN_PEN_get, _wrap_wxGREEN_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxBLACK_PEN",_wrap_wxBLACK_PEN_get, _wrap_wxBLACK_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxWHITE_PEN",_wrap_wxWHITE_PEN_get, _wrap_wxWHITE_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxTRANSPARENT_PEN",_wrap_wxTRANSPARENT_PEN_get, _wrap_wxTRANSPARENT_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxBLACK_DASHED_PEN",_wrap_wxBLACK_DASHED_PEN_get, _wrap_wxBLACK_DASHED_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxGREY_PEN",_wrap_wxGREY_PEN_get, _wrap_wxGREY_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxMEDIUM_GREY_PEN",_wrap_wxMEDIUM_GREY_PEN_get, _wrap_wxMEDIUM_GREY_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxLIGHT_GREY_PEN",_wrap_wxLIGHT_GREY_PEN_get, _wrap_wxLIGHT_GREY_PEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxBLUE_BRUSH",_wrap_wxBLUE_BRUSH_get, _wrap_wxBLUE_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxGREEN_BRUSH",_wrap_wxGREEN_BRUSH_get, _wrap_wxGREEN_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxWHITE_BRUSH",_wrap_wxWHITE_BRUSH_get, _wrap_wxWHITE_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxBLACK_BRUSH",_wrap_wxBLACK_BRUSH_get, _wrap_wxBLACK_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxTRANSPARENT_BRUSH",_wrap_wxTRANSPARENT_BRUSH_get, _wrap_wxTRANSPARENT_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxCYAN_BRUSH",_wrap_wxCYAN_BRUSH_get, _wrap_wxCYAN_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxRED_BRUSH",_wrap_wxRED_BRUSH_get, _wrap_wxRED_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxGREY_BRUSH",_wrap_wxGREY_BRUSH_get, _wrap_wxGREY_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxMEDIUM_GREY_BRUSH",_wrap_wxMEDIUM_GREY_BRUSH_get, _wrap_wxMEDIUM_GREY_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxLIGHT_GREY_BRUSH",_wrap_wxLIGHT_GREY_BRUSH_get, _wrap_wxLIGHT_GREY_BRUSH_set);
	 SWIG_addvarlink(SWIG_globals,"wxBLACK",_wrap_wxBLACK_get, _wrap_wxBLACK_set);
	 SWIG_addvarlink(SWIG_globals,"wxWHITE",_wrap_wxWHITE_get, _wrap_wxWHITE_set);
	 SWIG_addvarlink(SWIG_globals,"wxRED",_wrap_wxRED_get, _wrap_wxRED_set);
	 SWIG_addvarlink(SWIG_globals,"wxBLUE",_wrap_wxBLUE_get, _wrap_wxBLUE_set);
	 SWIG_addvarlink(SWIG_globals,"wxGREEN",_wrap_wxGREEN_get, _wrap_wxGREEN_set);
	 SWIG_addvarlink(SWIG_globals,"wxCYAN",_wrap_wxCYAN_get, _wrap_wxCYAN_set);
	 SWIG_addvarlink(SWIG_globals,"wxLIGHT_GREY",_wrap_wxLIGHT_GREY_get, _wrap_wxLIGHT_GREY_set);
	 SWIG_addvarlink(SWIG_globals,"wxSTANDARD_CURSOR",_wrap_wxSTANDARD_CURSOR_get, _wrap_wxSTANDARD_CURSOR_set);
	 SWIG_addvarlink(SWIG_globals,"wxHOURGLASS_CURSOR",_wrap_wxHOURGLASS_CURSOR_get, _wrap_wxHOURGLASS_CURSOR_set);
	 SWIG_addvarlink(SWIG_globals,"wxCROSS_CURSOR",_wrap_wxCROSS_CURSOR_get, _wrap_wxCROSS_CURSOR_set);
	 SWIG_addvarlink(SWIG_globals,"wxNullBitmap",_wrap_wxNullBitmap_get, _wrap_wxNullBitmap_set);
	 SWIG_addvarlink(SWIG_globals,"wxNullIcon",_wrap_wxNullIcon_get, _wrap_wxNullIcon_set);
	 SWIG_addvarlink(SWIG_globals,"wxNullCursor",_wrap_wxNullCursor_get, _wrap_wxNullCursor_set);
	 SWIG_addvarlink(SWIG_globals,"wxNullPen",_wrap_wxNullPen_get, _wrap_wxNullPen_set);
	 SWIG_addvarlink(SWIG_globals,"wxNullBrush",_wrap_wxNullBrush_get, _wrap_wxNullBrush_set);
	 SWIG_addvarlink(SWIG_globals,"wxNullPalette",_wrap_wxNullPalette_get, _wrap_wxNullPalette_set);
	 SWIG_addvarlink(SWIG_globals,"wxNullFont",_wrap_wxNullFont_get, _wrap_wxNullFont_set);
	 SWIG_addvarlink(SWIG_globals,"wxNullColour",_wrap_wxNullColour_get, _wrap_wxNullColour_set);
	 PyDict_SetItemString(d,"wxIMAGELIST_DRAW_NORMAL", PyInt_FromLong((long) wxIMAGELIST_DRAW_NORMAL));
	 PyDict_SetItemString(d,"wxIMAGELIST_DRAW_TRANSPARENT", PyInt_FromLong((long) wxIMAGELIST_DRAW_TRANSPARENT));
	 PyDict_SetItemString(d,"wxIMAGELIST_DRAW_SELECTED", PyInt_FromLong((long) wxIMAGELIST_DRAW_SELECTED));
	 PyDict_SetItemString(d,"wxIMAGELIST_DRAW_FOCUSED", PyInt_FromLong((long) wxIMAGELIST_DRAW_FOCUSED));
	 PyDict_SetItemString(d,"wxIMAGE_LIST_NORMAL", PyInt_FromLong((long) wxIMAGE_LIST_NORMAL));
	 PyDict_SetItemString(d,"wxIMAGE_LIST_SMALL", PyInt_FromLong((long) wxIMAGE_LIST_SMALL));
	 PyDict_SetItemString(d,"wxIMAGE_LIST_STATE", PyInt_FromLong((long) wxIMAGE_LIST_STATE));
/*
 * These are the pointer type-equivalency mappings. 
 * (Used by the SWIG pointer type-checker).
 */
	 SWIG_RegisterMapping("_wxAcceleratorTable","_class_wxAcceleratorTable",0);
	 SWIG_RegisterMapping("_signed_long","_long",0);
	 SWIG_RegisterMapping("_wxPrintQuality","_int",0);
	 SWIG_RegisterMapping("_wxPrintQuality","_signed_int",0);
	 SWIG_RegisterMapping("_wxPrintQuality","_unsigned_int",0);
	 SWIG_RegisterMapping("_wxPrintQuality","_wxWindowID",0);
	 SWIG_RegisterMapping("_wxPrintQuality","_uint",0);
	 SWIG_RegisterMapping("_wxPrintQuality","_EBool",0);
	 SWIG_RegisterMapping("_wxPrintQuality","_size_t",0);
	 SWIG_RegisterMapping("_class_wxRegionIterator","_wxRegionIterator",0);
	 SWIG_RegisterMapping("_wxIndividualLayoutConstraint","_class_wxIndividualLayoutConstraint",0);
	 SWIG_RegisterMapping("_wxCursor","_class_wxCursor",0);
	 SWIG_RegisterMapping("_wxMask","_class_wxMask",0);
	 SWIG_RegisterMapping("_wxPen","_class_wxPen",0);
	 SWIG_RegisterMapping("_byte","_unsigned_char",0);
	 SWIG_RegisterMapping("_long","_wxDash",0);
	 SWIG_RegisterMapping("_long","_unsigned_long",0);
	 SWIG_RegisterMapping("_long","_signed_long",0);
	 SWIG_RegisterMapping("_wxImageList","_class_wxImageList",0);
	 SWIG_RegisterMapping("_class_wxAcceleratorTable","_wxAcceleratorTable",0);
	 SWIG_RegisterMapping("_wxDC","_class_wxMetaFileDC",SwigwxMetaFileDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_wxMetaFileDC",SwigwxMetaFileDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_class_wxPrinterDC",SwigwxPrinterDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_wxPrinterDC",SwigwxPrinterDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_class_wxWindowDC",SwigwxWindowDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_wxWindowDC",SwigwxWindowDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_class_wxPaintDC",SwigwxPaintDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_wxPaintDC",SwigwxPaintDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_class_wxClientDC",SwigwxClientDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_wxClientDC",SwigwxClientDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_class_wxScreenDC",SwigwxScreenDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_wxScreenDC",SwigwxScreenDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_class_wxMemoryDC",SwigwxMemoryDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_wxMemoryDC",SwigwxMemoryDCTowxDC);
	 SWIG_RegisterMapping("_wxDC","_class_wxDC",0);
	 SWIG_RegisterMapping("_size_t","_wxPrintQuality",0);
	 SWIG_RegisterMapping("_size_t","_unsigned_int",0);
	 SWIG_RegisterMapping("_size_t","_int",0);
	 SWIG_RegisterMapping("_size_t","_wxWindowID",0);
	 SWIG_RegisterMapping("_size_t","_uint",0);
	 SWIG_RegisterMapping("_class_wxRealPoint","_wxRealPoint",0);
	 SWIG_RegisterMapping("_wxPrinterDC","_class_wxPrinterDC",0);
	 SWIG_RegisterMapping("_class_wxMask","_wxMask",0);
	 SWIG_RegisterMapping("_wxColour","_class_wxColour",0);
	 SWIG_RegisterMapping("_wxBrush","_class_wxBrush",0);
	 SWIG_RegisterMapping("_uint","_wxPrintQuality",0);
	 SWIG_RegisterMapping("_uint","_size_t",0);
	 SWIG_RegisterMapping("_uint","_unsigned_int",0);
	 SWIG_RegisterMapping("_uint","_int",0);
	 SWIG_RegisterMapping("_uint","_wxWindowID",0);
	 SWIG_RegisterMapping("_wxRect","_class_wxRect",0);
	 SWIG_RegisterMapping("_wxPoint","_class_wxPoint",0);
	 SWIG_RegisterMapping("_wxBitmap","_class_wxCursor",SwigwxCursorTowxBitmap);
	 SWIG_RegisterMapping("_wxBitmap","_wxCursor",SwigwxCursorTowxBitmap);
	 SWIG_RegisterMapping("_wxBitmap","_class_wxIcon",SwigwxIconTowxBitmap);
	 SWIG_RegisterMapping("_wxBitmap","_wxIcon",SwigwxIconTowxBitmap);
	 SWIG_RegisterMapping("_wxBitmap","_class_wxBitmap",0);
	 SWIG_RegisterMapping("_wxPyTimer","_class_wxPyTimer",0);
	 SWIG_RegisterMapping("_wxWindowDC","_class_wxWindowDC",0);
	 SWIG_RegisterMapping("_class_wxIndividualLayoutConstraint","_wxIndividualLayoutConstraint",0);
	 SWIG_RegisterMapping("_EBool","_wxPrintQuality",0);
	 SWIG_RegisterMapping("_EBool","_signed_int",0);
	 SWIG_RegisterMapping("_EBool","_int",0);
	 SWIG_RegisterMapping("_EBool","_wxWindowID",0);
	 SWIG_RegisterMapping("_class_wxRegion","_wxRegion",0);
	 SWIG_RegisterMapping("_wxFont","_class_wxFont",0);
	 SWIG_RegisterMapping("_unsigned_long","_wxDash",0);
	 SWIG_RegisterMapping("_unsigned_long","_long",0);
	 SWIG_RegisterMapping("_class_wxRect","_wxRect",0);
	 SWIG_RegisterMapping("_class_wxDC","_class_wxMetaFileDC",SwigwxMetaFileDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_wxMetaFileDC",SwigwxMetaFileDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_class_wxPrinterDC",SwigwxPrinterDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_wxPrinterDC",SwigwxPrinterDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_class_wxWindowDC",SwigwxWindowDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_wxWindowDC",SwigwxWindowDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_class_wxPaintDC",SwigwxPaintDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_wxPaintDC",SwigwxPaintDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_class_wxClientDC",SwigwxClientDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_wxClientDC",SwigwxClientDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_class_wxScreenDC",SwigwxScreenDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_wxScreenDC",SwigwxScreenDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_class_wxMemoryDC",SwigwxMemoryDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_wxMemoryDC",SwigwxMemoryDCTowxDC);
	 SWIG_RegisterMapping("_class_wxDC","_wxDC",0);
	 SWIG_RegisterMapping("_class_wxPyTimer","_wxPyTimer",0);
	 SWIG_RegisterMapping("_wxAcceleratorEntry","_class_wxAcceleratorEntry",0);
	 SWIG_RegisterMapping("_signed_int","_wxPrintQuality",0);
	 SWIG_RegisterMapping("_signed_int","_EBool",0);
	 SWIG_RegisterMapping("_signed_int","_wxWindowID",0);
	 SWIG_RegisterMapping("_signed_int","_int",0);
	 SWIG_RegisterMapping("_wxLayoutConstraints","_class_wxLayoutConstraints",0);
	 SWIG_RegisterMapping("_wxMetaFileDC","_class_wxMetaFileDC",0);
	 SWIG_RegisterMapping("_wxScreenDC","_class_wxScreenDC",0);
	 SWIG_RegisterMapping("_WXTYPE","_short",0);
	 SWIG_RegisterMapping("_WXTYPE","_signed_short",0);
	 SWIG_RegisterMapping("_WXTYPE","_unsigned_short",0);
	 SWIG_RegisterMapping("_class_wxBrush","_wxBrush",0);
	 SWIG_RegisterMapping("_unsigned_short","_WXTYPE",0);
	 SWIG_RegisterMapping("_unsigned_short","_short",0);
	 SWIG_RegisterMapping("_class_wxFont","_wxFont",0);
	 SWIG_RegisterMapping("_wxClientDC","_class_wxClientDC",0);
	 SWIG_RegisterMapping("_class_wxPoint","_wxPoint",0);
	 SWIG_RegisterMapping("_wxRealPoint","_class_wxRealPoint",0);
	 SWIG_RegisterMapping("_signed_short","_WXTYPE",0);
	 SWIG_RegisterMapping("_signed_short","_short",0);
	 SWIG_RegisterMapping("_wxMemoryDC","_class_wxMemoryDC",0);
	 SWIG_RegisterMapping("_wxPaintDC","_class_wxPaintDC",0);
	 SWIG_RegisterMapping("_class_wxWindowDC","_wxWindowDC",0);
	 SWIG_RegisterMapping("_class_wxAcceleratorEntry","_wxAcceleratorEntry",0);
	 SWIG_RegisterMapping("_class_wxCursor","_wxCursor",0);
	 SWIG_RegisterMapping("_unsigned_char","_byte",0);
	 SWIG_RegisterMapping("_class_wxMetaFileDC","_wxMetaFileDC",0);
	 SWIG_RegisterMapping("_unsigned_int","_wxPrintQuality",0);
	 SWIG_RegisterMapping("_unsigned_int","_size_t",0);
	 SWIG_RegisterMapping("_unsigned_int","_uint",0);
	 SWIG_RegisterMapping("_unsigned_int","_wxWindowID",0);
	 SWIG_RegisterMapping("_unsigned_int","_int",0);
	 SWIG_RegisterMapping("_wxIcon","_class_wxIcon",0);
	 SWIG_RegisterMapping("_class_wxPen","_wxPen",0);
	 SWIG_RegisterMapping("_short","_WXTYPE",0);
	 SWIG_RegisterMapping("_short","_unsigned_short",0);
	 SWIG_RegisterMapping("_short","_signed_short",0);
	 SWIG_RegisterMapping("_class_wxImageList","_wxImageList",0);
	 SWIG_RegisterMapping("_wxWindowID","_wxPrintQuality",0);
	 SWIG_RegisterMapping("_wxWindowID","_size_t",0);
	 SWIG_RegisterMapping("_wxWindowID","_EBool",0);
	 SWIG_RegisterMapping("_wxWindowID","_uint",0);
	 SWIG_RegisterMapping("_wxWindowID","_int",0);
	 SWIG_RegisterMapping("_wxWindowID","_signed_int",0);
	 SWIG_RegisterMapping("_wxWindowID","_unsigned_int",0);
	 SWIG_RegisterMapping("_int","_wxPrintQuality",0);
	 SWIG_RegisterMapping("_int","_size_t",0);
	 SWIG_RegisterMapping("_int","_EBool",0);
	 SWIG_RegisterMapping("_int","_uint",0);
	 SWIG_RegisterMapping("_int","_wxWindowID",0);
	 SWIG_RegisterMapping("_int","_unsigned_int",0);
	 SWIG_RegisterMapping("_int","_signed_int",0);
	 SWIG_RegisterMapping("_wxSize","_class_wxSize",0);
	 SWIG_RegisterMapping("_wxRegionIterator","_class_wxRegionIterator",0);
	 SWIG_RegisterMapping("_class_wxPrinterDC","_wxPrinterDC",0);
	 SWIG_RegisterMapping("_class_wxPaintDC","_wxPaintDC",0);
	 SWIG_RegisterMapping("_class_wxLayoutConstraints","_wxLayoutConstraints",0);
	 SWIG_RegisterMapping("_class_wxIcon","_wxIcon",0);
	 SWIG_RegisterMapping("_class_wxColour","_wxColour",0);
	 SWIG_RegisterMapping("_class_wxScreenDC","_wxScreenDC",0);
	 SWIG_RegisterMapping("_wxPalette","_class_wxPalette",0);
	 SWIG_RegisterMapping("_wxRegion","_class_wxRegion",0);
	 SWIG_RegisterMapping("_class_wxClientDC","_wxClientDC",0);
	 SWIG_RegisterMapping("_class_wxSize","_wxSize",0);
	 SWIG_RegisterMapping("_class_wxBitmap","_class_wxCursor",SwigwxCursorTowxBitmap);
	 SWIG_RegisterMapping("_class_wxBitmap","_wxCursor",SwigwxCursorTowxBitmap);
	 SWIG_RegisterMapping("_class_wxBitmap","_class_wxIcon",SwigwxIconTowxBitmap);
	 SWIG_RegisterMapping("_class_wxBitmap","_wxIcon",SwigwxIconTowxBitmap);
	 SWIG_RegisterMapping("_class_wxBitmap","_wxBitmap",0);
	 SWIG_RegisterMapping("_class_wxMemoryDC","_wxMemoryDC",0);
	 SWIG_RegisterMapping("_wxDash","_unsigned_long",0);
	 SWIG_RegisterMapping("_wxDash","_long",0);
	 SWIG_RegisterMapping("_class_wxPalette","_wxPalette",0);
}
