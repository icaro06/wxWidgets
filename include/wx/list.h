/////////////////////////////////////////////////////////////////////////////
// Name:        list.h
// Purpose:     wxList, wxStringList classes
// Author:      Julian Smart
// Modified by: VZ at 16/11/98: WX_DECLARE_LIST() and typesafe lists added
// Created:     29/01/98
// RCS-ID:      $Id$
// Copyright:   (c) 1998 Julian Smart
// Licence:     wxWindows licence
/////////////////////////////////////////////////////////////////////////////

/*
  All this is quite ugly but serves two purposes:
    1. Be almost 100% compatible with old, untyped, wxList class
    2. Ensure compile-time type checking for the linked lists

  The idea is to have one base class (wxListBase) working with "void *" data,
  but to hide these untyped functions - i.e. make them protected, so they
  can only be used from derived classes which have inline member functions
  working with right types. This achieves the 2nd goal. As for the first one,
  we provide a special derivation of wxListBase called wxList which looks just
  like the old class.
*/

#ifndef _WX_LISTH__
#define _WX_LISTH__

#if defined(__GNUG__) && !defined(__APPLE__) && \
    !(defined(__MINGW32__) && __GNUC__ == 3 && __GNUC_MINOR__ == 2)
#pragma interface "list.h"
#endif

// -----------------------------------------------------------------------------
// headers
// -----------------------------------------------------------------------------

#include "wx/defs.h"
#include "wx/object.h"
#include "wx/string.h"

#if wxUSE_STL
    #include "wx/beforestd.h"
    #include <list>
    #include "wx/afterstd.h"
#endif

// ----------------------------------------------------------------------------
// types
// ----------------------------------------------------------------------------

// type of compare function for list sort operation (as in 'qsort'): it should
// return a negative value, 0 or positive value if the first element is less
// than, equal or greater than the second

extern "C"
{
typedef int (* LINKAGEMODE wxSortCompareFunction)(const void *elem1, const void *elem2);
}

class WXDLLIMPEXP_BASE wxObjectListNode;
typedef wxObjectListNode wxNode;

//
typedef int (* LINKAGEMODE wxListIterateFunction)(void *current);

// ----------------------------------------------------------------------------
// constants
// ----------------------------------------------------------------------------

#if !defined(wxENUM_KEY_TYPE_DEFINED)
#define wxENUM_KEY_TYPE_DEFINED

enum wxKeyType
{
    wxKEY_NONE,
    wxKEY_INTEGER,
    wxKEY_STRING
};

#endif

#if wxUSE_STL

#define wxLIST_COMPATIBILITY

#define WX_DECLARE_LIST_3(elT, dummy1, liT, dummy2, decl) \
    WX_DECLARE_LIST_X(elT, liT, decl)

#define WX_DECLARE_LIST_2(elT, liT, dummy, decl) \
    WX_DECLARE_LIST_X(elT, liT, decl)

#define WX_DECLARE_LIST_X(elT, liT, decl) \
    WX_DECLARE_LIST_XO(elT*, liT, decl)

#define WX_DECLARE_LIST_XO(elT, liT, decl) \
    decl liT : public std::list<elT>                                          \
    {                                                                         \
    public:                                                                   \
        class dummy;                                                          \
                                                                              \
        struct compatibility_iterator                                         \
        {                                                                     \
            typedef std::list<elT>::iterator iterator;                        \
            iterator m_iter;                                                  \
            liT * m_list;                                                     \
        public:                                                               \
            operator bool() const                                             \
                { return m_list && m_iter != m_list->end(); }                 \
            bool operator !() const                                           \
                { return !m_list || m_iter == m_list->end(); }                \
            compatibility_iterator( const liT* li, iterator it )              \
                : m_iter( it ), m_list( (liT*)li ) {}                         \
            compatibility_iterator( liT* li, iterator it )                    \
                : m_iter( it ), m_list( li ) {}                               \
            compatibility_iterator() : m_list( NULL ) { }                     \
            dummy* operator->() { return (dummy*)this; }                      \
            const dummy* operator->() const { return (const dummy*)this; }    \
        };                                                                    \
        typedef struct compatibility_iterator citer;                          \
                                                                              \
        class dummy                                                           \
        {                                                                     \
            typedef std::list<elT>::iterator it;                              \
            typedef compatibility_iterator citer;                             \
        public:                                                               \
            elT GetData() const                                               \
            {                                                                 \
                citer* i = (citer*)this;                                      \
                return *(i->m_iter);                                          \
            }                                                                 \
            citer GetNext() const                                             \
            {                                                                 \
                citer* i = (citer*)this;                                      \
                it lit = i->m_iter;                                           \
                return citer( i->m_list, ++lit );                             \
            }                                                                 \
            citer GetPrevious() const                                         \
            {                                                                 \
                citer* i = (citer*)this;                                      \
                it lit = i->m_iter;                                           \
                return citer( i->m_list, ++lit );                             \
            }                                                                 \
            void SetData( elT e )                                             \
            {                                                                 \
                citer* i = (citer*)this;                                      \
                *(i->m_iter) = e;                                             \
            }                                                                 \
        private:                                                              \
            dummy();                                                          \
        };                                                                    \
    protected:                                                                \
        iterator find( elT e )                                                \
        {                                                                     \
            iterator it, en;                                                  \
            for( it = begin(), en = end(); it != en; ++it )                   \
                if( *it == e )                                                \
                    return it;                                                \
            return it;                                                        \
        }                                                                     \
    public:                                                                   \
        liT() {};                                                             \
                                                                              \
        citer Append( elT e ) { push_back( e ); return GetLast(); }           \
        void Clear() { clear(); }                                             \
        size_t GetCount() const { return size(); }                            \
        citer GetFirst() const { return citer( this, ((liT*)this)->begin() ); } \
        citer GetLast() const { return citer( this, --(((liT*)this)->end()) ); } \
        bool IsEmpty() const { return empty(); }                              \
        bool DeleteObject( elT e )                                            \
        {                                                                     \
            iterator it = find( e );                                          \
            if( it != end() )                                                 \
            {                                                                 \
                erase( it );                                                  \
                return true;                                                  \
            }                                                                 \
            return false;                                                     \
        }                                                                     \
        void Erase( const compatibility_iterator& it )                        \
        {                                                                     \
            erase( it.m_iter );                                               \
        }                                                                     \
        citer Find( elT e ) const { return citer( this, ((liT*)this)->find( e ) ); } \
        citer Member( elT e ) const { return Find( e ); }                     \
        citer Insert( elT e )                                                 \
            { push_front( e ); return citer( this, begin() ); }               \
        citer Insert( size_t idx, elT e )                                     \
            { return Insert( Item( idx ), e ); }                              \
        citer Insert( citer idx, elT e )                                      \
            { return citer( this, insert( idx.m_iter, e ) ); }                \
        citer Item( size_t idx ) const                                        \
        {                                                                     \
            iterator it;                                                      \
            for( it = ((liT*)this)->begin(); idx; --idx )                     \
                ++it;                                                         \
            return citer( this, it );                                         \
        }                                                                     \
        int IndexOf( elT e ) const                                            \
        {                                                                     \
            const_iterator it, en;                                            \
            int idx;                                                          \
            for( idx = 0, it = begin(), en = end(); it != en; ++it, ++idx )   \
                if( *it == e )                                                \
                    return idx;                                               \
            return wxNOT_FOUND;                                               \
        }                                                                     \
    }

#define WX_DECLARE_LIST(elementtype, listname)                              \
    WX_DECLARE_LIST_X(elementtype, listname, class)

#define WX_DECLARE_EXPORTED_LIST(elementtype, listname)                     \
    WX_DECLARE_LIST_X(elementtype, listname, class WXDLLEXPORT)

#define WX_DECLARE_USER_EXPORTED_LIST(elementtype, listname, usergoo)       \
    WX_DECLARE_LIST_X(elementtype, listname, class usergoo)

// this macro must be inserted in your program after
//      #include <wx/listimpl.cpp>
#define WX_DEFINE_LIST(name)    "don't forget to include listimpl.cpp!"

#define WX_DEFINE_EXPORTED_LIST(name)      WX_DEFINE_LIST(name)
#define WX_DEFINE_USER_EXPORTED_LIST(name) WX_DEFINE_LIST(name)

#else // if !wxUSE_STL

// due to circular header dependencies this function has to be declared here
// (normally it's found in utils.h which includes itself list.h...)
extern WXDLLIMPEXP_BASE wxChar* copystring(const wxChar *s);

class WXDLLEXPORT wxObjectListNode;
typedef wxObjectListNode wxNode;

// undef it to get rid of old, deprecated functions
#define wxLIST_COMPATIBILITY

// -----------------------------------------------------------------------------
// key stuff: a list may be optionally keyed on integer or string key
// -----------------------------------------------------------------------------

union wxListKeyValue
{
    long integer;
    wxChar *string;
};

// a struct which may contain both types of keys
//
// implementation note: on one hand, this class allows to have only one function
// for any keyed operation instead of 2 almost equivalent. OTOH, it's needed to
// resolve ambiguity which we would otherwise have with wxStringList::Find() and
// wxList::Find(const char *).
class WXDLLIMPEXP_BASE wxListKey
{
public:
    // implicit ctors
    wxListKey() : m_keyType(wxKEY_NONE)
        { }
    wxListKey(long i) : m_keyType(wxKEY_INTEGER)
        { m_key.integer = i; }
    wxListKey(const wxChar *s) : m_keyType(wxKEY_STRING)
        { m_key.string = wxStrdup(s); }
    wxListKey(const wxString& s) : m_keyType(wxKEY_STRING)
        { m_key.string = wxStrdup(s.c_str()); }

    // accessors
    wxKeyType GetKeyType() const { return m_keyType; }
    const wxChar *GetString() const
        { wxASSERT( m_keyType == wxKEY_STRING ); return m_key.string; }
    long GetNumber() const
        { wxASSERT( m_keyType == wxKEY_INTEGER ); return m_key.integer; }

    // comparison
    // Note: implementation moved to list.cpp to prevent BC++ inline
    // expansion warning.
    bool operator==(wxListKeyValue value) const ;

    // dtor
    ~wxListKey()
    {
        if ( m_keyType == wxKEY_STRING )
            free(m_key.string);
    }

private:
    wxKeyType m_keyType;
    wxListKeyValue m_key;
};

// -----------------------------------------------------------------------------
// wxNodeBase class is a (base for) node in a double linked list
// -----------------------------------------------------------------------------

WXDLLIMPEXP_DATA_BASE(extern wxListKey) wxDefaultListKey;

class WXDLLIMPEXP_BASE wxListBase;

class WXDLLIMPEXP_BASE wxNodeBase
{
friend class wxListBase;
public:
    // ctor
    wxNodeBase(wxListBase *list = (wxListBase *)NULL,
               wxNodeBase *previous = (wxNodeBase *)NULL,
               wxNodeBase *next = (wxNodeBase *)NULL,
               void *data = NULL,
               const wxListKey& key = wxDefaultListKey);

    virtual ~wxNodeBase();

    // FIXME no check is done that the list is really keyed on strings
    const wxChar *GetKeyString() const { return m_key.string; }
    long GetKeyInteger() const { return m_key.integer; }

    // Necessary for some existing code
    void SetKeyString(wxChar* s) { m_key.string = s; }
    void SetKeyInteger(long i) { m_key.integer = i; }

#ifdef wxLIST_COMPATIBILITY
    // compatibility methods, use Get* instead.
    wxDEPRECATED( wxNode *Next() const );
    wxDEPRECATED( wxNode *Previous() const );
    wxDEPRECATED( wxObject *Data() const );
#endif // wxLIST_COMPATIBILITY

protected:
    // all these are going to be "overloaded" in the derived classes
    wxNodeBase *GetNext() const { return m_next; }
    wxNodeBase *GetPrevious() const { return m_previous; }

    void *GetData() const { return m_data; }
    void SetData(void *data) { m_data = data; }

    // get 0-based index of this node within the list or wxNOT_FOUND
    int IndexOf() const;

    virtual void DeleteData() { }
public:
    // for wxList::iterator
    void** GetDataPtr() const { return &(((wxNodeBase*)this)->m_data); }
private:
    // optional key stuff
    wxListKeyValue m_key;

    void        *m_data;        // user data
    wxNodeBase  *m_next,        // next and previous nodes in the list
                *m_previous;

    wxListBase  *m_list;        // list we belong to

    DECLARE_NO_COPY_CLASS(wxNodeBase)
};

// -----------------------------------------------------------------------------
// a double-linked list class
// -----------------------------------------------------------------------------

class wxList;

class WXDLLIMPEXP_BASE wxListBase : public wxObject
{
friend class WXDLLIMPEXP_BASE wxNodeBase; // should be able to call DetachNode()
friend class wxHashTableBase;   // should be able to call untyped Find()
private:
        // common part of all ctors
    void Init(wxKeyType keyType = wxKEY_NONE); // Must be declared before it's used (for VC++ 1.5)
public:
    // default ctor & dtor
    wxListBase(wxKeyType keyType = wxKEY_NONE)
        { Init(keyType); }
    virtual ~wxListBase();

    // accessors
        // count of items in the list
    size_t GetCount() const { return m_count; }

        // return TRUE if this list is empty
    bool IsEmpty() const { return m_count == 0; }

    // operations

        // delete all nodes
    void Clear();

        // instruct it to destroy user data when deleting nodes
    void DeleteContents(bool destroy) { m_destroy = destroy; }

       // query if to delete
    bool GetDeleteContents() const
        { return m_destroy; }

      // get the keytype
    wxKeyType GetKeyType() const
        { return m_keyType; }

      // set the keytype (required by the serial code)
    void SetKeyType(wxKeyType keyType)
        { wxASSERT( m_count==0 ); m_keyType = keyType; }

#ifdef wxLIST_COMPATIBILITY
    // compatibility methods from old wxList
    wxDEPRECATED( int Number() const );             // use GetCount instead.
    wxDEPRECATED( wxNode *First() const );          // use GetFirst
    wxDEPRECATED( wxNode *Last() const );           // use GetLast
    wxDEPRECATED( wxNode *Nth(size_t n) const );    // use Item

    // kludge for typesafe list migration in core classes.
    wxDEPRECATED( operator wxList&() const );
#endif // wxLIST_COMPATIBILITY

protected:

    // all methods here are "overloaded" in derived classes to provide compile
    // time type checking

    // create a node for the list of this type
    virtual wxNodeBase *CreateNode(wxNodeBase *prev, wxNodeBase *next,
                                   void *data,
                                   const wxListKey& key = wxDefaultListKey) = 0;

// Can't access these from derived classes otherwise (bug in Salford C++?)
#ifdef __SALFORDC__
public:
#endif

    // ctors
        // from an array
    wxListBase(size_t count, void *elements[]);
        // from a sequence of objects
    wxListBase(void *object, ... /* terminate with NULL */);

protected:
        // copy ctor and assignment operator
    wxListBase(const wxListBase& list) : wxObject()
        { Init(); DoCopy(list); }
    wxListBase& operator=(const wxListBase& list)
        { Clear(); DoCopy(list); return *this; }

        // get list head/tail
    wxNodeBase *GetFirst() const { return m_nodeFirst; }
    wxNodeBase *GetLast() const { return m_nodeLast; }

        // by (0-based) index
    wxNodeBase *Item(size_t index) const;

        // get the list item's data
    void *operator[](size_t n) const
    {
        wxNodeBase *node = Item(n);

        return node ? node->GetData() : (wxNodeBase *)NULL;
    }

    // operations
        // append to end of list
    wxNodeBase *Prepend(void *object)
        { return (wxNodeBase *)wxListBase::Insert(object); }
        // append to beginning of list
    wxNodeBase *Append(void *object);
        // insert a new item at the beginning of the list
    wxNodeBase *Insert(void *object) { return Insert( (wxNodeBase*)NULL, object); }
        // insert a new item at the given position
    wxNodeBase *Insert(size_t pos, void *object)
        { return pos == GetCount() ? Append(object)
                                   : Insert(Item(pos), object); }
        // insert before given node or at front of list if prev == NULL
    wxNodeBase *Insert(wxNodeBase *prev, void *object);

        // keyed append
    wxNodeBase *Append(long key, void *object);
    wxNodeBase *Append(const wxChar *key, void *object);

        // removes node from the list but doesn't delete it (returns pointer
        // to the node or NULL if it wasn't found in the list)
    wxNodeBase *DetachNode(wxNodeBase *node);
        // delete element from list, returns FALSE if node not found
    bool DeleteNode(wxNodeBase *node);
        // finds object pointer and deletes node (and object if DeleteContents
        // is on), returns FALSE if object not found
    bool DeleteObject(void *object);

    // search (all return NULL if item not found)
        // by data
    wxNodeBase *Find(void *object) const;

        // by key
    wxNodeBase *Find(const wxListKey& key) const;

    // get 0-based index of object or wxNOT_FOUND
    int IndexOf( void *object ) const;

    // this function allows the sorting of arbitrary lists by giving
    // a function to compare two list elements. The list is sorted in place.
    void Sort(const wxSortCompareFunction compfunc);

    // functions for iterating over the list
    void *FirstThat(wxListIterateFunction func);
    void ForEach(wxListIterateFunction func);
    void *LastThat(wxListIterateFunction func);

    // for STL interface, "last" points to one after the last node
    // of the controlled sequence (NULL for the end of the list)
    void Reverse();
    void DeleteNodes(wxNodeBase* first, wxNodeBase* last);
private:
    // helpers
        // common part of copy ctor and assignment operator
    void DoCopy(const wxListBase& list);
        // common part of all Append()s
    wxNodeBase *AppendCommon(wxNodeBase *node);
        // free node's data and node itself
    void DoDeleteNode(wxNodeBase *node);

    size_t m_count;             // number of elements in the list
    bool m_destroy;             // destroy user data when deleting list items?
    wxNodeBase *m_nodeFirst,    // pointers to the head and tail of the list
               *m_nodeLast;

    wxKeyType m_keyType;        // type of our keys (may be wxKEY_NONE)
};

// -----------------------------------------------------------------------------
// macros for definition of "template" list type
// -----------------------------------------------------------------------------

// and now some heavy magic...

// declare a list type named 'name' and containing elements of type 'T *'
// (as a by product of macro expansion you also get wx##name##Node
// wxNode-derived type)
//
// implementation details:
//  1. We define _WX_LIST_ITEM_TYPE_##name typedef to save in it the item type
//     for the list of given type - this allows us to pass only the list name
//     to WX_DEFINE_LIST() even if it needs both the name and the type
//
//  2. We redefine all non-type-safe wxList functions with type-safe versions
//     which don't take any space (everything is inline), but bring compile
//     time error checking.
//
//  3. The macro which is usually used (WX_DECLARE_LIST) is defined in terms of
//     a more generic WX_DECLARE_LIST_2 macro which, in turn, uses the most
//     generic WX_DECLARE_LIST_3 one. The last macro adds a sometimes
//     interesting capability to store polymorphic objects in the list and is
//     particularly useful with, for example, "wxWindow *" list where the
//     wxWindowBase pointers are put into the list, but wxWindow pointers are
//     retrieved from it.

#define WX_DECLARE_LIST_3(T, Tbase, name, nodetype, classexp)               \
    typedef int (*wxSortFuncFor_##name)(const T **, const T **);            \
                                                                            \
    classexp nodetype : public wxNodeBase                                   \
    {                                                                       \
    public:                                                                 \
        nodetype(wxListBase *list = (wxListBase *)NULL,                     \
                 nodetype *previous = (nodetype *)NULL,                     \
                 nodetype *next = (nodetype *)NULL,                         \
                 T *data = (T *)NULL,                                       \
                 const wxListKey& key = wxDefaultListKey)                   \
            : wxNodeBase(list, previous, next, data, key) { }               \
                                                                            \
        nodetype *GetNext() const                                           \
            { return (nodetype *)wxNodeBase::GetNext(); }                   \
        nodetype *GetPrevious() const                                       \
            { return (nodetype *)wxNodeBase::GetPrevious(); }               \
                                                                            \
        T *GetData() const                                                  \
            { return (T *)wxNodeBase::GetData(); }                          \
        void SetData(T *data)                                               \
            { wxNodeBase::SetData(data); }                                  \
                                                                            \
        virtual void DeleteData();                                          \
    };                                                                      \
                                                                            \
    classexp name : public wxListBase                                       \
    {                                                                       \
    public:                                                                 \
        typedef nodetype Node;                                              \
        typedef Node* compatibility_iterator;                               \
                                                                            \
        name(wxKeyType keyType = wxKEY_NONE) : wxListBase(keyType)          \
            { }                                                             \
        name(size_t count, T *elements[])                                   \
            : wxListBase(count, (void **)elements) { }                      \
                                                                            \
        name& operator=(const name& list)                                   \
            { (void) wxListBase::operator=(list); return *this; }           \
                                                                            \
        nodetype *GetFirst() const                                          \
            { return (nodetype *)wxListBase::GetFirst(); }                  \
        nodetype *GetLast() const                                           \
            { return (nodetype *)wxListBase::GetLast(); }                   \
                                                                            \
        nodetype *Item(size_t index) const                                  \
            { return (nodetype *)wxListBase::Item(index); }                 \
                                                                            \
        T *operator[](size_t index) const                                   \
        {                                                                   \
            nodetype *node = Item(index);                                   \
            return node ? (T*)(node->GetData()) : (T*)NULL;                 \
        }                                                                   \
                                                                            \
        nodetype *Append(Tbase *object)                                     \
            { return (nodetype *)wxListBase::Append(object); }              \
        nodetype *Insert(Tbase *object)                                     \
            { return (nodetype *)Insert((nodetype*)NULL, object); }         \
        nodetype *Insert(size_t pos, Tbase *object)                         \
            { return (nodetype *)wxListBase::Insert(pos, object); }         \
        nodetype *Insert(nodetype *prev, Tbase *object)                     \
            { return (nodetype *)wxListBase::Insert(prev, object); }        \
                                                                            \
        nodetype *Append(long key, void *object)                            \
            { return (nodetype *)wxListBase::Append(key, object); }         \
        nodetype *Append(const wxChar *key, void *object)                   \
            { return (nodetype *)wxListBase::Append(key, object); }         \
                                                                            \
        nodetype *DetachNode(nodetype *node)                                \
            { return (nodetype *)wxListBase::DetachNode(node); }            \
        bool DeleteNode(nodetype *node)                                     \
            { return wxListBase::DeleteNode(node); }                        \
        bool DeleteObject(Tbase *object)                                    \
            { return wxListBase::DeleteObject(object); }                    \
        void Erase(compatibility_iterator it)                               \
            { DeleteNode(it); }                                             \
                                                                            \
        nodetype *Find(Tbase *object) const                                 \
            { return (nodetype *)wxListBase::Find(object); }                \
                                                                            \
        virtual nodetype *Find(const wxListKey& key) const                  \
            { return (nodetype *)wxListBase::Find(key); }                   \
                                                                            \
        int IndexOf(Tbase *object) const                                    \
            { return wxListBase::IndexOf(object); }                         \
                                                                            \
        void Sort(wxSortFuncFor_##name func)                                \
            { wxListBase::Sort((wxSortCompareFunction)func); }              \
                                                                            \
    protected:                                                              \
        virtual wxNodeBase *CreateNode(wxNodeBase *prev, wxNodeBase *next,  \
                               void *data,                                  \
                               const wxListKey& key = wxDefaultListKey)     \
            {                                                               \
                return new nodetype(this,                                   \
                                    (nodetype *)prev, (nodetype *)next,     \
                                    (T *)data, key);                        \
            }                                                               \
        /* STL interface */                                                 \
    public:                                                                 \
        typedef size_t size_type;                                           \
        typedef int difference_type;                                        \
        typedef T* value_type;                                              \
        typedef Tbase* base_value_type;                                     \
        typedef value_type& reference;                                      \
        typedef const value_type& const_reference;                          \
        typedef base_value_type& base_reference;                            \
        typedef const base_value_type& const_base_reference;                \
                                                                            \
        class iterator                                                      \
        {                                                                   \
            typedef name list;                                              \
        public:                                                             \
            typedef nodetype Node;                                          \
            typedef iterator itor;                                          \
            typedef T* value_type;                                          \
            typedef value_type* ptr_type;                                   \
            typedef value_type& reference;                                  \
                                                                            \
            Node* m_node;                                                   \
            Node* m_init;                                                   \
        public:                                                             \
            typedef reference reference_type;                               \
            typedef ptr_type pointer_type;                                  \
                                                                            \
            iterator(Node* node, Node* init) : m_node(node), m_init(init) {}\
            iterator() : m_node(NULL), m_init(NULL) { }                     \
            reference_type operator*() const                                \
                { return *(pointer_type)m_node->GetDataPtr(); }             \
            pointer_type operator->() const                                 \
                { return (pointer_type)m_node->GetDataPtr(); }              \
            itor& operator++() { m_node = m_node->GetNext(); return *this; }\
            itor operator++(int)                                            \
                { itor tmp = *this; m_node = m_node->GetNext(); return tmp; }\
            itor& operator--()                                              \
            {                                                               \
                m_node = m_node ? m_node->GetPrevious() : m_init;           \
                return *this;                                               \
            }                                                               \
            itor operator--(int)                                            \
            {                                                               \
                itor tmp = *this;                                           \
                m_node = m_node ? m_node->GetPrevious() : m_init;           \
                return tmp;                                                 \
            }                                                               \
            bool operator!=(const itor& it) const                           \
                { return it.m_node != m_node; }                             \
            bool operator==(const itor& it) const                           \
                { return it.m_node == m_node; }                             \
        };                                                                  \
        class const_iterator                                                \
        {                                                                   \
            typedef name list;                                              \
        public:                                                             \
            typedef nodetype Node;                                          \
            typedef T* value_type;                                          \
            typedef const value_type& const_reference;                      \
            typedef const_iterator itor;                                    \
            typedef value_type* ptr_type;                                   \
                                                                            \
            Node* m_node;                                                   \
            Node* m_init;                                                   \
        public:                                                             \
            typedef const_reference reference_type;                         \
            typedef const ptr_type pointer_type;                            \
                                                                            \
            const_iterator(Node* node, Node* init)                          \
                : m_node(node), m_init(init) { }                            \
            const_iterator() : m_node(NULL), m_init(NULL) { }               \
            const_iterator(const iterator& it)                              \
                : m_node(it.m_node), m_init(it.m_init) { }                  \
            reference_type operator*() const                                \
                { return *(pointer_type)m_node->GetDataPtr(); }             \
            pointer_type operator->() const                                 \
                { return (pointer_type)m_node->GetDataPtr(); }              \
            itor& operator++() { m_node = m_node->GetNext(); return *this; }\
            itor operator++(int)                                            \
                { itor tmp = *this; m_node = m_node->GetNext(); return tmp; }\
            itor& operator--()                                              \
            {                                                               \
                m_node = m_node ? m_node->GetPrevious() : m_init;           \
                return *this;                                               \
            }                                                               \
            itor operator--(int)                                            \
            {                                                               \
                itor tmp = *this;                                           \
                m_node = m_node ? m_node->GetPrevious() : m_init;           \
                return tmp;                                                 \
            }                                                               \
            bool operator!=(const itor& it) const                           \
                { return it.m_node != m_node; }                             \
            bool operator==(const itor& it) const                           \
                { return it.m_node == m_node; }                             \
        };                                                                  \
        class reverse_iterator                                              \
        {                                                                   \
            typedef name list;                                              \
        public:                                                             \
            typedef nodetype Node;                                          \
            typedef T* value_type;                                          \
            typedef reverse_iterator itor;                                  \
            typedef value_type* ptr_type;                                   \
            typedef value_type& reference;                                  \
                                                                            \
            Node* m_node;                                                   \
            Node* m_init;                                                   \
        public:                                                             \
            typedef reference reference_type;                               \
            typedef ptr_type pointer_type;                                  \
                                                                            \
            reverse_iterator(Node* node, Node* init)                        \
                : m_node(node), m_init(init) { }                            \
            reverse_iterator() : m_node(NULL), m_init(NULL) { }             \
            reference_type operator*() const                                \
                { return *(pointer_type)m_node->GetDataPtr(); }             \
            pointer_type operator->() const                                 \
                { return (pointer_type)m_node->GetDataPtr(); }              \
            itor& operator++()                                              \
                { m_node = m_node->GetPrevious(); return *this; }           \
            itor operator++(int)                                            \
            { itor tmp = *this; m_node = m_node->GetPrevious(); return tmp; }\
            itor& operator--()                                              \
            { m_node = m_node ? m_node->GetNext() : m_init; return *this; } \
            itor operator--(int)                                            \
            {                                                               \
                itor tmp = *this;                                           \
                m_node = m_node ? m_node->GetNext() : m_init;               \
                return tmp;                                                 \
            }                                                               \
            bool operator!=(const itor& it) const                           \
                { return it.m_node != m_node; }                             \
            bool operator==(const itor& it) const                           \
                { return it.m_node == m_node; }                             \
        };                                                                  \
        class const_reverse_iterator                                        \
        {                                                                   \
            typedef name list;                                              \
        public:                                                             \
            typedef nodetype Node;                                          \
            typedef T* value_type;                                          \
            typedef const_reverse_iterator itor;                            \
            typedef value_type* ptr_type;                                   \
            typedef const value_type& const_reference;                      \
                                                                            \
            Node* m_node;                                                   \
            Node* m_init;                                                   \
        public:                                                             \
            typedef const_reference reference_type;                         \
            typedef const ptr_type pointer_type;                            \
                                                                            \
            const_reverse_iterator(Node* node, Node* init)                  \
                : m_node(node), m_init(init) { }                            \
            const_reverse_iterator() : m_node(NULL), m_init(NULL) { }       \
            const_reverse_iterator(const reverse_iterator& it)              \
                : m_node(it.m_node), m_init(it.m_init) { }                  \
            reference_type operator*() const                                \
                { return *(pointer_type)m_node->GetDataPtr(); }             \
            pointer_type operator->() const                                 \
                { return (pointer_type)m_node->GetDataPtr(); }              \
            itor& operator++()                                              \
                { m_node = m_node->GetPrevious(); return *this; }           \
            itor operator++(int)                                            \
            { itor tmp = *this; m_node = m_node->GetPrevious(); return tmp; }\
            itor& operator--()                                              \
                { m_node = m_node ? m_node->GetNext() : m_init; return *this;}\
            itor operator--(int)                                            \
            {                                                               \
                itor tmp = *this;                                           \
                m_node = m_node ? m_node->GetNext() : m_init;               \
                return tmp;                                                 \
            }                                                               \
            bool operator!=(const itor& it) const                           \
                { return it.m_node != m_node; }                             \
            bool operator==(const itor& it) const                           \
                { return it.m_node == m_node; }                             \
        };                                                                  \
                                                                            \
        wxEXPLICIT name(size_type n, const_reference v = value_type())      \
            { assign(n, v); }                                               \
        name(const_iterator first, const_iterator last)                     \
            { assign(first, last); }                                        \
        iterator begin() { return iterator(GetFirst(), GetLast()); }        \
        const_iterator begin() const                                        \
            { return const_iterator(GetFirst(), GetLast()); }               \
        iterator end() { return iterator(NULL, GetLast()); }                \
        const_iterator end() const { return const_iterator(NULL, GetLast()); }\
        reverse_iterator rbegin()                                           \
            { return reverse_iterator(GetLast(), GetFirst()); }             \
        const_reverse_iterator rbegin() const                               \
            { return const_reverse_iterator(GetLast(), GetFirst()); }       \
        reverse_iterator rend() { return reverse_iterator(NULL, GetFirst()); }\
        const_reverse_iterator rend() const                                 \
            { return const_reverse_iterator(NULL, GetFirst()); }            \
        void resize(size_type n, value_type v = value_type())               \
        {                                                                   \
            if(n < size())                                                  \
                for(; n < size(); pop_back());                              \
            else if(n > size())                                             \
                for(; n > size(); push_back(v));                            \
        }                                                                   \
        size_type size() const { return GetCount(); }                       \
        size_type max_size() const { return INT_MAX; }                      \
        bool empty() const { return IsEmpty(); }                            \
        reference front() { return *begin(); }                              \
        const_reference front() const { return *begin(); }                  \
        reference back() { return *--end(); }                               \
        const_reference back() const { return *--end(); }                   \
        void push_front(const_reference v = value_type())                   \
            { Insert(GetFirst(), (const_base_reference)v); }                \
        void pop_front() { DeleteNode(GetFirst()); }                        \
        void push_back(const_reference v = value_type())                    \
            { Append((const_base_reference)v); }                            \
        void pop_back() { DeleteNode(GetLast()); }                          \
        void assign(const_iterator first, const_iterator last)              \
        {                                                                   \
            clear();                                                        \
            for(; first != last; ++first)                                   \
                Append((const_base_reference)*first);                       \
        }                                                                   \
        void assign(size_type n, const_reference v = value_type())          \
        {                                                                   \
            clear();                                                        \
            for(size_type i = 0; i < n; ++i)                                \
                Append((const_base_reference)v);                            \
        }                                                                   \
        iterator insert(iterator it, const_reference v = value_type())      \
        {                                                                   \
            Insert(it.m_node, (const_base_reference)v);                     \
            return iterator(it.m_node->GetPrevious(), GetLast());           \
        }                                                                   \
        void insert(iterator it, size_type n, const_reference v = value_type())\
        {                                                                   \
            for(size_type i = 0; i < n; ++i)                                \
                Insert(it.m_node, (const_base_reference)v);                 \
        }                                                                   \
        void insert(iterator it, const_iterator first, const_iterator last) \
        {                                                                   \
            for(; first != last; ++first)                                   \
                Insert(it.m_node, (const_base_reference)*first);            \
        }                                                                   \
        iterator erase(iterator it)                                         \
        {                                                                   \
            iterator next = iterator(it.m_node->GetNext(), GetLast());      \
            DeleteNode(it.m_node); return next;                             \
        }                                                                   \
        iterator erase(iterator first, iterator last)                       \
        {                                                                   \
            iterator next = last; ++next;                                   \
            DeleteNodes(first.m_node, last.m_node);                         \
            return next;                                                    \
        }                                                                   \
        void clear() { Clear(); }                                           \
        void splice(iterator it, name& l, iterator first, iterator last)    \
            { insert(it, first, last); l.erase(first, last); }              \
        void splice(iterator it, name& l)                                   \
            { splice(it, l, l.begin(), l.end() ); }                         \
        void splice(iterator it, name& l, iterator first)                   \
        {                                                                   \
            iterator tmp = first; ++tmp;                                    \
            if(it == first || it == tmp) return;                            \
            insert(it, *first);                                             \
            l.erase(first);                                                 \
        }                                                                   \
        void remove(const_reference v)                                      \
            { DeleteObject((const_base_reference)v); }                      \
        void reverse()                                                      \
            { Reverse(); }                                                  \
     /* void swap(name& l)                                                  \
        {                                                                   \
            { size_t t = m_count; m_count = l.m_count; l.m_count = t; }     \
            { bool t = m_destroy; m_destroy = l.m_destroy; l.m_destroy = t; }\
            { wxNodeBase* t = m_nodeFirst; m_nodeFirst = l.m_nodeFirst; l.m_nodeFirst = t; }\
            { wxNodeBase* t = m_nodeLast; m_nodeLast = l.m_nodeLast; l.m_nodeLast = t; }\
            { wxKeyType t = m_keyType; m_keyType = l.m_keyType; l.m_keyType = t; }\
        } */                                                                \
    }

#define WX_DECLARE_LIST_2(elementtype, listname, nodename, classexp)        \
    WX_DECLARE_LIST_3(elementtype, elementtype, listname, nodename, classexp)

#define WX_DECLARE_LIST(elementtype, listname)                              \
    typedef elementtype _WX_LIST_ITEM_TYPE_##listname;                      \
    WX_DECLARE_LIST_2(elementtype, listname, wx##listname##Node, class)

#define WX_DECLARE_EXPORTED_LIST(elementtype, listname)                     \
    typedef elementtype _WX_LIST_ITEM_TYPE_##listname;                      \
    WX_DECLARE_LIST_2(elementtype, listname, wx##listname##Node, class WXDLLEXPORT)

#define WX_DECLARE_USER_EXPORTED_LIST(elementtype, listname, usergoo)       \
    typedef elementtype _WX_LIST_ITEM_TYPE_##listname;                      \
    WX_DECLARE_LIST_2(elementtype, listname, wx##listname##Node, class usergoo)

// this macro must be inserted in your program after
//      #include <wx/listimpl.cpp>
#define WX_DEFINE_LIST(name)    "don't forget to include listimpl.cpp!"

#define WX_DEFINE_EXPORTED_LIST(name)      WX_DEFINE_LIST(name)
#define WX_DEFINE_USER_EXPORTED_LIST(name) WX_DEFINE_LIST(name)

#endif // !wxUSE_STL

// =============================================================================
// now we can define classes 100% compatible with the old ones
// =============================================================================

// ----------------------------------------------------------------------------
// commonly used list classes
// ----------------------------------------------------------------------------

#ifdef wxLIST_COMPATIBILITY

// define this to make a lot of noise about use of the old wxList classes.
//#define wxWARN_COMPAT_LIST_USE

// -----------------------------------------------------------------------------
// wxList compatibility class: in fact, it's a list of wxObjects
// -----------------------------------------------------------------------------
WX_DECLARE_LIST_2(wxObject, wxObjectList, wxObjectListNode, class WXDLLIMPEXP_BASE);

class WXDLLIMPEXP_BASE wxList : public wxObjectList
{
public:
#if defined(wxWARN_COMPAT_LIST_USE) && !wxUSE_STL
    wxDEPRECATED( wxList(int key_type = wxKEY_NONE) );
#elif !wxUSE_STL
    wxList(int key_type = wxKEY_NONE);
#endif

    // this destructor is required for Darwin
   ~wxList() { }

#if !wxUSE_STL
    wxList& operator=(const wxList& list)
        { (void) wxListBase::operator=(list); return *this; }

    // compatibility methods
    void Sort(wxSortCompareFunction compfunc) { wxListBase::Sort(compfunc); }
#endif

#if wxUSE_STL
#else
    wxNode *Member(wxObject *object) const { return (wxNode *)Find(object); }
#endif

private:
#if !wxUSE_STL
    DECLARE_DYNAMIC_CLASS(wxList)
#endif
};

#if !wxUSE_STL

// -----------------------------------------------------------------------------
// wxStringList class for compatibility with the old code
// -----------------------------------------------------------------------------
WX_DECLARE_LIST_2(wxChar, wxStringListBase, wxStringListNode, class WXDLLIMPEXP_BASE);

class WXDLLIMPEXP_BASE wxStringList : public wxStringListBase
{
public:
    // ctors and such
        // default
#ifdef wxWARN_COMPAT_LIST_USE
    wxDEPRECATED( wxStringList() );
    wxDEPRECATED( wxStringList(const wxChar *first ...) );
#else
    wxStringList();
    wxStringList(const wxChar *first ...);
#endif

        // copying the string list: the strings are copied, too (extremely
        // inefficient!)
    wxStringList(const wxStringList& other) : wxStringListBase() { DeleteContents(TRUE); DoCopy(other); }
    wxStringList& operator=(const wxStringList& other)
        { Clear(); DoCopy(other); return *this; }

    // operations
        // makes a copy of the string
    wxNode *Add(const wxChar *s);
        
        // Append to beginning of list
    wxNode *Prepend(const wxChar *s);

    bool Delete(const wxChar *s);

    wxChar **ListToArray(bool new_copies = FALSE) const;
    bool Member(const wxChar *s) const;

    // alphabetic sort
    void Sort();

private:
    void DoCopy(const wxStringList&); // common part of copy ctor and operator=

    DECLARE_DYNAMIC_CLASS(wxStringList)
};

#else // if wxUSE_STL

WX_DECLARE_LIST_XO(wxString, wxStringListBase, class WXDLLEXPORT);

class WXDLLEXPORT wxStringList : public wxStringListBase
{
public:
    compatibility_iterator Append(wxChar* s)
        { wxString tmp = s; delete[] s; return wxStringListBase::Append(tmp); }
    compatibility_iterator Insert(wxChar* s)
        { wxString tmp = s; delete[] s; return wxStringListBase::Insert(tmp); }
    compatibility_iterator Insert(size_t pos, wxChar* s)
    {
        wxString tmp = s;
        delete[] s;
        return wxStringListBase::Insert(pos, tmp);
    }
    compatibility_iterator Add(const wxChar* s)
        { push_back(s); return GetLast(); }
    compatibility_iterator Prepend(const wxChar* s)
        { push_front(s); return GetFirst(); }
};

#endif // wxUSE_STL

#endif // wxLIST_COMPATIBILITY

// delete all list elements
//
// NB: the class declaration of the list elements must be visible from the
//     place where you use this macro, otherwise the proper destructor may not
//     be called (a decent compiler should give a warning about it, but don't
//     count on it)!
#define WX_CLEAR_LIST(type, list)                                            \
    {                                                                        \
        type::iterator it, en;                                               \
        for( it = (list).begin(), en = (list).end(); it != en; ++it )        \
            delete *it;                                                      \
        (list).clear();                                                      \
    }

#endif
    // _WX_LISTH__
