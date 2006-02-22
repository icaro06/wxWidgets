/////////////////////////////////////////////////////////////////////////////
// Name:        wx/dataview.h
// Purpose:     wxDataViewCtrl base classes
// Author:      Robert Roebling
// Modified by:
// Created:     08.01.06
// RCS-ID:      $Id$
// Copyright:   (c) Robert Roebling
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

#ifndef _WX_DATAVIEW_H_BASE_
#define _WX_DATAVIEW_H_BASE_

#include "wx/defs.h"

#if wxUSE_DATAVIEWCTRL

#include "wx/control.h"
#include "wx/textctrl.h"
#include "wx/bitmap.h"
#include "wx/variant.h"

// ----------------------------------------------------------------------------
// wxDataViewCtrl flags 
// ----------------------------------------------------------------------------

// ----------------------------------------------------------------------------
// wxDataViewCtrl globals
// ----------------------------------------------------------------------------

class WXDLLIMPEXP_CORE wxDataViewCtrl;
class WXDLLIMPEXP_CORE wxDataViewColumn;

extern WXDLLEXPORT_DATA(const wxChar) wxDataViewCtrlNameStr[];

// --------------------------------------------------------- 
// wxDataViewModel
// --------------------------------------------------------- 

class wxDataViewModel: public wxObject
{
public:
    wxDataViewModel() { }
    virtual ~wxDataViewModel() { }
    
protected:
    DECLARE_DYNAMIC_CLASS_NO_COPY(wxDataViewModel)
};

// --------------------------------------------------------- 
// wxDataViewListModelNotifier
// --------------------------------------------------------- 

class wxDataViewListModelNotifier
{
public:
    wxDataViewListModelNotifier() { }
    virtual ~wxDataViewListModelNotifier() { }
    
    virtual bool RowAppended() = 0;
    virtual bool RowPrepended() = 0;
    virtual bool RowInserted( size_t before ) = 0;
    virtual bool RowDeleted( size_t row ) = 0;
    virtual bool RowChanged( size_t row ) = 0;
    virtual bool ValueChanged( size_t row, size_t col ) = 0;
    virtual bool Cleared() = 0;
};

// --------------------------------------------------------- 
// wxDataViewListModel
// --------------------------------------------------------- 

class wxDataViewListModel: public wxDataViewModel
{
public:
    wxDataViewListModel();
    virtual ~wxDataViewListModel();

    virtual size_t GetNumberOfRows() = 0;
    virtual size_t GetNumberOfCols() = 0;
    // as reported by wxVariant
    virtual wxString GetColType( size_t col ) = 0;
    virtual wxVariant GetValue( size_t col, size_t row ) = 0;

    // delegated notifiers
    bool RowAppended();
    bool RowPrepended();
    bool RowInserted( size_t before );
    bool RowDeleted( size_t row );
    bool RowChanged( size_t row );
    bool ValueChanged( size_t row, size_t col );
    bool Cleared();
    
    void SetNotifier( wxDataViewListModelNotifier *notifier );
    wxDataViewListModelNotifier* GetNotifier();
    
private:
    wxDataViewListModelNotifier *m_notifier;

protected:
    DECLARE_DYNAMIC_CLASS_NO_COPY(wxDataViewListModel)
};

// --------------------------------------------------------- 
// wxDataViewColumn
// --------------------------------------------------------- 

enum wxDataViewColumnType
{
    wxDATAVIEW_COL_TEXT,
    wxDATAVIEW_COL_ICON,
    wxDATAVIEW_COL_ICONTEXT,
    wxDATAVIEW_COL_CHECK,
    wxDATAVIEW_COL_DATETIME,
    wxDATAVIEW_COL_PROGRESS,
    wxDATAVIEW_COL_CHOICE,
    wxDATAVIEW_COL_CUSTOM
};

enum wxDataViewColumnFlags
{
    wxDATAVIEW_COL_RESIZABLE  = 1,
    wxDATAVIEW_COL_SORTABLE   = 2,
    wxDATAVIEW_COL_HIDDEN     = 4
};

class wxDataViewColumnBase: public wxObject
{
public:
    wxDataViewColumnBase( const wxString &title, wxDataViewCtrl *ctrl, 
            wxDataViewColumnType kind, int flags = 0 );

    virtual void SetTitle( const wxString &title );
    virtual wxString GetTitle();

private:
    wxDataViewCtrl          *m_ctrl;
    wxDataViewColumnType     m_kind;
    int                      m_flags;
    wxString                 m_title;

protected:
    DECLARE_DYNAMIC_CLASS_NO_COPY(wxDataViewColumnBase)
};

// --------------------------------------------------------- 
// wxDataViewCtrlBase
// --------------------------------------------------------- 

class wxDataViewCtrlBase: public wxControl
{
public:
    wxDataViewCtrlBase();
    ~wxDataViewCtrlBase();

    
    virtual bool AssociateModel( wxDataViewListModel *model );
    wxDataViewListModel* GetModel();
    
    virtual bool AppendStringColumn( const wxString &label );
    virtual bool AppendColumn( wxDataViewColumn *col );    
    virtual size_t GetNumberOfColumns();
    virtual bool DeleteColumn( size_t pos );
    virtual bool ClearColumns();
    virtual wxDataViewColumn* GetColumn( size_t pos );
    
private:
    wxDataViewListModel    *m_model;
    wxList                  m_cols;

protected:
    DECLARE_DYNAMIC_CLASS_NO_COPY(wxDataViewCtrlBase)
};

#if defined(__WXGTK20__)
    #include "wx/gtk/dataview.h"
#elif defined(__WXMAC__)
    #include "wx/mac/dataview.h"
#else
    #include "wx/generic/dataview.h"
#endif

#endif // wxUSE_DATAVIEWCTRL

#endif
    // _WX_DATAVIEW_H_BASE_
