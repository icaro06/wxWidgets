/////////////////////////////////////////////////////////////////////////////
// Name:        wizard.h
// Purpose:     interface of wxWizardPage
// Author:      wxWidgets team
// RCS-ID:      $Id$
// Licence:     wxWindows license
/////////////////////////////////////////////////////////////////////////////

/**
    @class wxWizardPage

    wxWizardPage is one of the screens in wxWizard: it must
    know what are the following and preceding pages (which may be @NULL for the
    first/last page). Except for this extra knowledge, wxWizardPage is just a
    panel, so the controls may be placed directly on it in the usual way.

    This class allows the programmer to decide the order of pages in the wizard
    dynamically (during run-time) and so provides maximal flexibility. Usually,
    however, the order of pages is known in advance in which case
    wxWizardPageSimple class is enough and it is simpler
    to use.

    @library{wxadv}
    @category{miscwnd}

    @see wxWizard, @ref overview_samplewizard "wxWizard sample"
*/
class wxWizardPage : public wxPanel
{
public:
    /**
        Constructor accepts an optional bitmap which will be used for this page
        instead of the default one for this wizard (note that all bitmaps used should
        be of the same size). Notice that no other parameters are needed because the
        wizard will resize and reposition the page anyhow.

        @param parent
            The parent wizard
        @param bitmap
            The page-specific bitmap if different from the global one
    */
    wxWizardPage(wxWizard* parent,
                 const wxBitmap& bitmap = wxNullBitmap);

    /**
        This method is called by wxWizard to get the bitmap to display alongside the
        page. By default, @c m_bitmap member variable which was set in the
        @ref wxwizardpage() constructor.
        If the bitmap was not explicitly set (i.e. if @c wxNullBitmap is returned),
        the default bitmap for the wizard should be used.
        The only cases when you would want to override this function is if the page
        bitmap depends dynamically on the user choices, i.e. almost never.
    */
    wxBitmap GetBitmap() const;

    /**
        Get the page which should be shown when the user chooses the @c "Next"
        button: if @NULL is returned, this button will be disabled. The last
        page of the wizard will usually return @NULL from here, but the others
        will not.

        @see GetPrev()
    */
    wxWizardPage* GetNext() const;

    /**
        Get the page which should be shown when the user chooses the @c "Back"
        button: if @NULL is returned, this button will be disabled. The first
        page of the wizard will usually return @NULL from here, but the others
        will not.

        @see GetNext()
    */
    wxWizardPage* GetPrev() const;
};



/**
    @class wxWizardEvent

    wxWizardEvent class represents an event generated by the
    wizard(): this event is first sent to the page itself and,
    if not processed there, goes up the window hierarchy as usual.

    @library{wxadv}
    @category{events}

    @see wxWizard, @ref overview_samplewizard "wxWizard sample"
*/
class wxWizardEvent : public wxNotifyEvent
{
public:
    /**
        Constructor. It is not normally used by the user code as the objects of this
        type are constructed by wxWizard.
    */
    wxWizardEvent(wxEventType type = wxEVT_NULL, int id = -1,
                  bool direction = true);

    /**
        Return the direction in which the page is changing: for @c
        EVT_WIZARD_PAGE_CHANGING, return @true if we're going forward or
        @false otherwise and for @c EVT_WIZARD_PAGE_CHANGED return @true if
        we came from the previous page and @false if we returned from the next
        one.
    */
    bool GetDirection() const;

    /**
        Returns the wxWizardPage which was active when this
        event was generated.
    */
    wxWizardPage* GetPage() const;
};



/**
    @class wxWizardPageSimple

    wxWizardPageSimple is the simplest possible
    wxWizardPage implementation: it just returns the
    pointers given to its constructor from GetNext() and GetPrev() functions.

    This makes it very easy to use the objects of this class in the wizards where
    the pages order is known statically - on the other hand, if this is not the
    case you must derive your own class from wxWizardPage
    instead.

    @library{wxadv}
    @category{miscwnd}

    @see wxWizard, @ref overview_samplewizard "wxWizard sample"
*/
class wxWizardPageSimple : public wxWizardPage
{
public:
    /**
        Constructor takes the previous and next pages. They may be modified later by
        SetPrev() or
        SetNext().
    */
    wxWizardPageSimple(wxWizard* parent = NULL,
                       wxWizardPage* prev = NULL,
                       wxWizardPage* next = NULL,
                       const wxBitmap& bitmap = wxNullBitmap);

    /**
        A convenience function to make the pages follow each other.
        Example:
    */
    static void Chain(wxWizardPageSimple* first,
                      wxWizardPageSimple* second);

    /**
        Sets the next page.
    */
    void SetNext(wxWizardPage* next);

    /**
        Sets the previous page.
    */
    void SetPrev(wxWizardPage* prev);
};



/**
    @class wxWizard

    wxWizard is the central class for implementing 'wizard-like' dialogs. These
    dialogs are mostly familiar to Windows users and are nothing other than a
    sequence of 'pages', each displayed inside a dialog which has the
    buttons to navigate to the next (and previous) pages.

    The wizards are typically used to decompose a complex dialog into several
    simple steps and are mainly useful to the novice users, hence it is important
    to keep them as simple as possible.

    To show a wizard dialog, you must first create an instance of the wxWizard class
    using either the non-default constructor or a default one followed by call to
    the
    wxWizard::Create function. Then you should add all pages you
    want the wizard to show and call wxWizard::RunWizard.
    Finally, don't forget to call @c wizard-Destroy(), otherwise your application
    will hang on exit due to an undestroyed window.

    You can supply a bitmap to display on the left of the wizard, either for all
    pages
    or for individual pages. If you need to have the bitmap resize to the height of
    the wizard,
    call wxWizard::SetBitmapPlacement and if necessary,
    wxWizard::SetBitmapBackgroundColour and wxWizard::SetMinimumBitmapWidth.

    To make wizard pages scroll when the display is too small to fit the whole
    dialog, you can switch
    layout adaptation on globally with wxDialog::EnableLayoutAdaptation or
    per dialog with wxDialog::SetLayoutAdaptationMode. For more
    about layout adaptation, see @ref overview_autoscrollingdialogs "Automatic
    scrolling dialogs".

    @library{wxadv}
    @category{cmndlg}

    @see wxWizardEvent, wxWizardPage, @ref overview_samplewizard "wxWizard sample"
*/
class wxWizard : public wxDialog
{
public:
    //@{
    /**
        Constructor which really creates the wizard -- if you use this constructor, you
        shouldn't call Create().
        Notice that unlike almost all other wxWidgets classes, there is no @e size
        parameter in the wxWizard constructor because the wizard will have a predefined
        default size by default. If you want to change this, you should use the
        GetPageAreaSizer() function.

        @param parent
            The parent window, may be @NULL.
        @param id
            The id of the dialog, will usually be just -1.
        @param title
            The title of the dialog.
        @param bitmap
            The default bitmap used in the left side of the wizard. See
            also GetBitmap.
        @param pos
            The position of the dialog, it will be centered on the screen
            by default.
        @param style
            Window style is passed to wxDialog.
    */
    wxWizard();
    wxWizard(wxWindow* parent, int id = -1,
             const wxString& title = wxEmptyString,
             const wxBitmap& bitmap = wxNullBitmap,
             const wxPoint& pos = wxDefaultPosition,
             long style = wxDEFAULT_DIALOG_STYLE);
    //@}

    /**
        Creates the wizard dialog. Must be called if the default constructor had been
        used to create the object.
        Notice that unlike almost all other wxWidgets classes, there is no @e size
        parameter in the wxWizard constructor because the wizard will have a predefined
        default size by default. If you want to change this, you should use the
        GetPageAreaSizer() function.

        @param parent
            The parent window, may be @NULL.
        @param id
            The id of the dialog, will usually be just -1.
        @param title
            The title of the dialog.
        @param bitmap
            The default bitmap used in the left side of the wizard. See
            also GetBitmap.
        @param pos
            The position of the dialog, it will be centered on the screen
            by default.
        @param style
            Window style is passed to wxDialog.
    */
    bool Create(wxWindow* parent, int id = -1,
                const wxString& title = wxEmptyString,
                const wxBitmap& bitmap = wxNullBitmap,
                const wxPoint& pos = wxDefaultPosition,
                long style = wxDEFAULT_DIALOG_STYLE);

    /**
        This method is obsolete, use
        GetPageAreaSizer() instead.
        Sets the page size to be big enough for all the pages accessible via the
        given @e firstPage, i.e. this page, its next page and so on.
        This method may be called more than once and it will only change the page size
        if the size required by the new page is bigger than the previously set one.
        This is useful if the decision about which pages to show is taken during
        run-time, as in this case, the wizard won't be able to get to all pages starting
        from a single one and you should call @e Fit separately for the others.
    */
    void FitToPage(const wxWizardPage* firstPage);

    /**
        Returns the bitmap used for the wizard.
    */
    const wxBitmap GetBitmap() const;

    /**
        Returns the colour that should be used to fill the area not taken up by the
        wizard or page bitmap,
        if a non-zero bitmap placement flag has been set.
        See also SetBitmapPlacement().
    */
    const wxColour GetBitmapBackgroundColour() const;

    /**
        Returns the flags indicating how the wizard or page bitmap should be expanded
        and positioned to fit the
        page height. By default, placement is 0 (no expansion is done).
        See also SetBitmapPlacement() for the possible values.
    */
    int GetBitmapPlacement();

    /**
        Get the current page while the wizard is running. @NULL is returned if
        RunWizard() is not being executed now.
    */
    wxWizardPage* GetCurrentPage() const;

    /**
        Returns the minimum width for the bitmap that will be constructed to contain
        the actual wizard or page bitmap
        if a non-zero bitmap placement flag has been set.
        See also SetBitmapPlacement().
    */
    int GetMinimumBitmapWidth() const;

    /**
        Returns pointer to page area sizer. The wizard is laid out using sizers and
        the page area sizer is the place-holder for the pages. All pages are resized
        before
        being shown to match the wizard page area.
        Page area sizer has a minimal size that is the maximum of several values. First,
        all pages (or other objects) added to the sizer. Second, all pages reachable
        by repeatedly applying
        wxWizardPage::GetNext to
        any page inserted into the sizer. Third,
        the minimal size specified using SetPageSize() and
        FitToPage(). Fourth, the total wizard height may
        be increased to accommodate the bitmap height. Fifth and finally, wizards are
        never smaller than some built-in minimal size to avoid wizards that are too
        small.
        The caller can use wxSizer::SetMinSize to enlarge it
        beyond the minimal size. If @c wxRESIZE_BORDER was passed to constructor, user
        can resize wizard and consequently the page area (but not make it smaller than
        the
        minimal size).
        It is recommended to add the first page to the page area sizer. For simple
        wizards,
        this will enlarge the wizard to fit the biggest page. For non-linear wizards,
        the first page of every separate chain should be added. Caller-specified size
        can be accomplished using wxSizer::SetMinSize.
        Adding pages to the page area sizer affects the default border width around page
        area that can be altered with SetBorder().
    */
    virtual wxSizer* GetPageAreaSizer() const;

    /**
        Returns the size available for the pages.
    */
    wxSize GetPageSize() const;

    /**
        Return @true if this page is not the last one in the wizard. The base
        class version implements this by calling
        @ref wxWizardPage::getnext page-GetNext but this could be undesirable if,
        for example, the pages are created on demand only.

        @see HasPrevPage()
    */
    virtual bool HasNextPage(wxWizardPage* page);

    /**
        Returns @true if this page is not the last one in the wizard. The base
        class version implements this by calling
        @ref wxWizardPage::getprev page-GetPrev but this could be undesirable if,
        for example, the pages are created on demand only.

        @see HasNextPage()
    */
    virtual bool HasPrevPage(wxWizardPage* page);

    /**
        Executes the wizard starting from the given page, returning @true if it was
        successfully finished or @false if user cancelled it. The @a firstPage
        can not be @NULL.
    */
    bool RunWizard(wxWizardPage* firstPage);

    /**
        Sets the bitmap used for the wizard.
    */
    void SetBitmap(const wxBitmap& bitmap);

    /**
        Sets the colour that should be used to fill the area not taken up by the wizard
        or page bitmap,
        if a non-zero bitmap placement flag has been set.
        See also SetBitmapPlacement().
    */
    void SetBitmapBackgroundColour(const wxColour& colour);

    /**
        Sets the flags indicating how the wizard or page bitmap should be expanded and
        positioned to fit the
        page height. By default, placement is 0 (no expansion is done). @a placement is
        a bitlist with the
        following possible values:

        @b wxWIZARD_VALIGN_TOP

        Aligns the bitmap at the top.

        @b wxWIZARD_VALIGN_CENTRE

        Centres the bitmap vertically.

        @b wxWIZARD_VALIGN_BOTTOM

        Aligns the bitmap at the bottom.

        @b wxWIZARD_HALIGN_LEFT

        Left-aligns the bitmap.

        @b wxWIZARD_HALIGN_CENTRE

        Centres the bitmap horizontally.

        @b wxWIZARD_HALIGN_RIGHT

        Right-aligns the bitmap.

        @b wxWIZARD_TILE


        See also SetMinimumBitmapWidth().
    */
    void SetBitmapPlacement(int placement);

    /**
        Sets width of border around page area. Default is zero. For backward
        compatibility, if there are no pages in
        GetPageAreaSizer(), the default is 5 pixels.
        If there is a five point border around all controls in a page and the border
        around
        page area is left as zero, a five point white space along all dialog borders
        will be added to the control border in order to space page controls ten points
        from the dialog
        border and non-page controls.
    */
    void SetBorder(int border);

    /**
        Sets the minimum width for the bitmap that will be constructed to contain the
        actual wizard or page bitmap
        if a non-zero bitmap placement flag has been set. If this is not set when using
        bitmap placement, the initial
        layout may be incorrect.
        See also SetBitmapPlacement().
    */
    void SetMinimumBitmapWidth(int width);

    /**
        This method is obsolete, use
        GetPageAreaSizer() instead.
        Sets the minimal size to be made available for the wizard pages. The wizard
        will take into account the size of the bitmap (if any) itself. Also, the
        wizard will never be smaller than the default size.
        The recommended way to use this function is to lay out all wizard pages using
        the sizers (even though the wizard is not resizeable) and then use
        wxSizer::CalcMin in a loop to calculate the maximum
        of minimal sizes of the pages and pass it to SetPageSize().
    */
    void SetPageSize(const wxSize& sizePage);
};

