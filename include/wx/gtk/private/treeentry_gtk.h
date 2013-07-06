/* ///////////////////////////////////////////////////////////////////////////
// Name:        wx/gtk/private/treeentry_gtk.h
// Purpose:     GtkTreeEntry - a string/userdata combo for use with treeview
// Author:      Ryan Norton
// Id:          $Id$
// Copyright:   (c) 2006 Ryan Norton
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////// */

#ifndef _WX_GTK_TREE_ENTRY_H_
#define _WX_GTK_TREE_ENTRY_H_

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

#include <gtk/gtk.h> /* for gpointer and gchar* etc. */

#define GTK_TYPE_TREE_ENTRY          (gtk_tree_entry_get_type())
#define GTK_TREE_ENTRY(obj)          (G_TYPE_CHECK_INSTANCE_CAST (obj, gtk_tree_entry_get_type (), GtkTreeEntry))
#define GTK_IS_TREE_ENTRY(obj)       (G_TYPE_CHECK_INSTANCE_TYPE (obj, gtk_tree_entry_get_type ()))

typedef struct _GtkTreeEntry        GtkTreeEntry;

typedef void (*GtkTreeEntryDestroy) (GtkTreeEntry* entry, gpointer context);

struct _GtkTreeEntry
{
    GObject parent;                     /* object instance */
    gchar*  label;                      /* label - always copied by this object except on get */
    gchar*  collate_key;                /* collate key used for string comparisons/sorting */
    gpointer userdata;                  /* untouched userdata */
    GtkTreeEntryDestroy destroy_func;   /* called upon destruction - use for freeing userdata etc. */
    gpointer destroy_func_data;         /* context passed to destroy_func */
};

GtkTreeEntry* gtk_tree_entry_new        (void);

GType    gtk_tree_entry_get_type      (void);

gchar*     gtk_tree_entry_get_collate_key     (GtkTreeEntry* entry);

gchar*     gtk_tree_entry_get_label     (GtkTreeEntry* entry);

gpointer   gtk_tree_entry_get_userdata  (GtkTreeEntry* entry);

void     gtk_tree_entry_set_label       (GtkTreeEntry* entry, const gchar* label);

void   gtk_tree_entry_set_userdata      (GtkTreeEntry* entry, gpointer userdata);

void   gtk_tree_entry_set_destroy_func (GtkTreeEntry* entry,
                                        GtkTreeEntryDestroy destroy_func,
                                        gpointer destroy_func_data);

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif /* _WX_GTK_TREE_ENTRY_H_ */
