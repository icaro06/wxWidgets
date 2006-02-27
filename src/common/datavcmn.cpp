/////////////////////////////////////////////////////////////////////////////
// Name:        src/common/datavcmn.cpp
// Purpose:     wxDataViewCtrl base classes and common parts
// Author:      Robert Roebling
// Created:     2006/02/20
// RCS-ID:      $Id$
// Copyright:   (c) 2006, Robert Roebling
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

// For compilers that support precompilation, includes "wx.h".
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

#include "wx/defs.h"

#if wxUSE_DATAVIEWCTRL

#include "wx/object.h"
#include "wx/dataview.h"
#include "wx/log.h"
#include "wx/image.h"

// --------------------------------------------------------- 
// wxDataViewModel
// --------------------------------------------------------- 

IMPLEMENT_ABSTRACT_CLASS(wxDataViewModel, wxObject)

// --------------------------------------------------------- 
// wxDataViewListModel
// --------------------------------------------------------- 

class wxDataViewViewingColumn: public wxObject
{
public:
    wxDataViewViewingColumn( wxDataViewColumn *view_column, size_t model_column )
    {
        m_viewColumn = view_column;
        m_modelColumn = model_column;
    }
    
    wxDataViewColumn   *m_viewColumn;
    size_t              m_modelColumn;
};


IMPLEMENT_ABSTRACT_CLASS(wxDataViewListModel, wxDataViewModel)

wxDataViewListModel::wxDataViewListModel()
{
    m_notifier = NULL;
    m_viewingColumns.DeleteContents( true );
}

wxDataViewListModel::~wxDataViewListModel()
{
    if (m_notifier)
        delete m_notifier;
}

bool wxDataViewListModel::RowAppended()
{
    if (m_notifier)
        return m_notifier->RowAppended();
        
    return false;
}

bool wxDataViewListModel::RowPrepended()
{
    if (m_notifier)
        return m_notifier->RowPrepended();
        
    return false;
}

bool wxDataViewListModel::RowInserted( size_t before )
{
    if (m_notifier)
        return m_notifier->RowInserted( before );
        
    return false;
}

bool wxDataViewListModel::RowDeleted( size_t row )
{
    if (m_notifier)
        return m_notifier->RowDeleted( row );
        
    return false;
}

bool wxDataViewListModel::RowChanged( size_t row )
{
    if (m_notifier)
        return m_notifier->RowChanged( row );
        
    return false;
}

bool wxDataViewListModel::ValueChanged( size_t col, size_t row )
{
    bool ret = false;

    if (m_notifier)
        ret = m_notifier->ValueChanged( col, row );
        
    wxNode *node = m_viewingColumns.GetFirst();
    while (node)
    {
        wxDataViewViewingColumn* tmp = (wxDataViewViewingColumn*) node->GetData();
        
        if (tmp->m_modelColumn == col)
            m_notifier->ValueChanged( tmp->m_viewColumn, col, row );
    
        node = node->GetNext();
    }
    
    return ret;
}

bool wxDataViewListModel::Cleared()
{
    if (m_notifier)
        return m_notifier->Cleared();
        
    return false;
}

void wxDataViewListModel::AddViewingColumn( wxDataViewColumn *view_column, size_t model_column )
{
    m_viewingColumns.Append( new wxDataViewViewingColumn( view_column, model_column ) );
}

void wxDataViewListModel::RemoveViewingColumn( wxDataViewColumn *column )
{
    wxNode *node = m_viewingColumns.GetFirst();
    while (node)
    {
        wxDataViewViewingColumn* tmp = (wxDataViewViewingColumn*) node->GetData();
        
        if (tmp->m_viewColumn == column)
        {
            m_viewingColumns.DeleteObject( tmp );
            return;
        }
    
        node = node->GetNext();
    }
}

void wxDataViewListModel::SetNotifier( wxDataViewListModelNotifier *notifier )
{
    if (m_notifier)
        delete m_notifier;
        
   m_notifier = notifier;
}

wxDataViewListModelNotifier* wxDataViewListModel::GetNotifier()
{
    return m_notifier;
}

// --------------------------------------------------------- 
// wxDataViewCellBase
// --------------------------------------------------------- 

IMPLEMENT_ABSTRACT_CLASS(wxDataViewCellBase, wxObject)

wxDataViewCellBase::wxDataViewCellBase( const wxString &varianttype, wxDataViewCellMode mode )
{
    m_variantType = varianttype;
    m_mode = mode;
}
    
// --------------------------------------------------------- 
// wxDataViewColumnBase
// --------------------------------------------------------- 

IMPLEMENT_ABSTRACT_CLASS(wxDataViewColumnBase, wxObject)

wxDataViewColumnBase::wxDataViewColumnBase( const wxString &title, wxDataViewCell *cell, size_t model_column, int flags)
{
    m_cell = cell;
    m_model_column = model_column;
    m_flags = flags;
    m_title = title;
    m_owner = NULL;
    m_cell->SetOwner( (wxDataViewColumn*) this );
}

wxDataViewColumnBase::~wxDataViewColumnBase()
{
    if (m_cell)
        delete m_cell;
        
    if (GetOwner())
    {
        GetOwner()->GetModel()->RemoveViewingColumn( (wxDataViewColumn*) this );
    }
}

void wxDataViewColumnBase::SetTitle( const wxString &title )
{
    m_title = title;
}

wxString wxDataViewColumnBase::GetTitle()
{
    return m_title;
}

// --------------------------------------------------------- 
// wxDataViewCtrlBase
// --------------------------------------------------------- 

IMPLEMENT_ABSTRACT_CLASS(wxDataViewCtrlBase, wxControl)

wxDataViewCtrlBase::wxDataViewCtrlBase()
{
    m_model = NULL;
    m_cols.DeleteContents( true );
}

wxDataViewCtrlBase::~wxDataViewCtrlBase()
{
    if (m_model)
        delete m_model;
}

bool wxDataViewCtrlBase::AssociateModel( wxDataViewListModel *model )
{
    if (m_model)
        delete m_model;
        
    m_model = model;
    
    return true;
}

wxDataViewListModel* wxDataViewCtrlBase::GetModel()
{
    return m_model;
}

bool wxDataViewCtrlBase::AppendTextColumn( const wxString &label, size_t model_column )
{
    return AppendColumn( new wxDataViewColumn( label, new wxDataViewTextCell(), model_column ) );
}

bool wxDataViewCtrlBase::AppendToggleColumn( const wxString &label, size_t model_column )
{
    return AppendColumn( new wxDataViewColumn( label, new wxDataViewToggleCell(), model_column ) );
}

bool wxDataViewCtrlBase::AppendProgressColumn( const wxString &label, size_t model_column )
{
    return AppendColumn( new wxDataViewColumn( label, new wxDataViewProgressCell(), model_column ) );
}

bool wxDataViewCtrlBase::AppendDateColumn( const wxString &label, size_t model_column )
{
    return AppendColumn( new wxDataViewColumn( label, new wxDataViewDateCell(), model_column ) );
}

bool wxDataViewCtrlBase::AppendColumn( wxDataViewColumn *col )
{
    m_cols.Append( (wxObject*) col );
    col->SetOwner( (wxDataViewCtrl*) this );
    m_model->AddViewingColumn( col, col->GetModelColumn() );
    return true;
}

size_t wxDataViewCtrlBase::GetNumberOfColumns()
{
    return m_cols.GetCount();
}

bool wxDataViewCtrlBase::DeleteColumn( size_t pos )
{
    return false;
}

bool wxDataViewCtrlBase::ClearColumns()
{
    return false;
}

wxDataViewColumn* wxDataViewCtrlBase::GetColumn( size_t pos )
{
    return (wxDataViewColumn*) m_cols[ pos ];
}

#endif
