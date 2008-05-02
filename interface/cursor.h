/////////////////////////////////////////////////////////////////////////////
// Name:        cursor.h
// Purpose:     interface of wxCursor
// Author:      wxWidgets team
// RCS-ID:      $Id$
// Licence:     wxWindows license
/////////////////////////////////////////////////////////////////////////////

/**
    @class wxCursor
    @wxheader{cursor.h}

    A cursor is a small bitmap usually used for denoting where the mouse
    pointer is, with a picture that might indicate the interpretation of a
    mouse click. As with icons, cursors in X and MS Windows are created in a
    different manner. Therefore, separate cursors will be created for the
    different environments.  Platform-specific methods for creating a wxCursor
    object are catered for, and this is an occasion where conditional
    compilation will probably be required (see wxIcon for an example).

    A single cursor object may be used in many windows (any subwindow type).
    The wxWidgets convention is to set the cursor for a window, as in X, rather
    than to set it globally as in MS Windows, although a global wxSetCursor()
    function is also available for MS Windows use.

    @section cursor_custom Creating a Custom Cursor

    The following is an example of creating a cursor from 32x32 bitmap data
    (down_bits) and a mask (down_mask) where 1 is black and 0 is white for the
    bits, and 1 is opaque and 0 is transparent for the mask. It works on
    Windows and GTK+.

    @code
    static char down_bits[] = { 255, 255, 255, 255, 31,
        255, 255, 255, 31, 255, 255, 255, 31, 255, 255, 255,
        31, 255, 255, 255, 31, 255, 255, 255, 31, 255, 255,
        255, 31, 255, 255, 255, 31, 255, 255, 255, 25, 243,
        255, 255, 19, 249, 255, 255, 7, 252, 255, 255, 15, 254,
        255, 255, 31, 255, 255, 255, 191, 255, 255, 255, 255,
        255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
        255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
        255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
        255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
        255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
        255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
        255 };

    static char down_mask[] = { 240, 1, 0, 0, 240, 1,
        0, 0, 240, 1, 0, 0, 240, 1, 0, 0, 240, 1, 0, 0, 240, 1,
        0, 0, 240, 1, 0, 0, 240, 1, 0, 0, 255, 31, 0, 0, 255,
        31, 0, 0, 254, 15, 0, 0, 252, 7, 0, 0, 248, 3, 0, 0,
        240, 1, 0, 0, 224, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0 };

    #ifdef __WXMSW__
        wxBitmap down_bitmap(down_bits, 32, 32);
        wxBitmap down_mask_bitmap(down_mask, 32, 32);

        down_bitmap.SetMask(new wxMask(down_mask_bitmap));
        wxImage down_image = down_bitmap.ConvertToImage();
        down_image.SetOption(wxIMAGE_OPTION_CUR_HOTSPOT_X, 6);
        down_image.SetOption(wxIMAGE_OPTION_CUR_HOTSPOT_Y, 14);
        wxCursor down_cursor = wxCursor(down_image);
    #else
        wxCursor down_cursor = wxCursor(down_bits, 32, 32, 6, 14,
                                        down_mask, wxWHITE, wxBLACK);
    #endif
    @endcode

    @library{wxcore}
    @category{gdi}

    @stdobjects
    - ::wxNullCursor
    - ::wxSTANDARD_CURSOR
    - ::wxHOURGLASS_CURSOR
    - ::wxCROSS_CURSOR

    @see wxBitmap, wxIcon, wxWindow::SetCursor(), wxSetCursor(),
         ::wxStockCursor
*/
class wxCursor : public wxBitmap
{
public:
    /**
        Default constructor.
    */
    wxCursor();
    /**
        Constructs a cursor by passing an array of bits (Motif and GTK+ only).
        @a maskBits is used only under Motif and GTK+. The parameters @a fg and
        @a bg are only present on GTK+, and force the cursor to use particular
        background and foreground colours.

        If either @a hotSpotX or @a hotSpotY is -1, the hotspot will be the
        centre of the cursor image (Motif only).

        @param bits
            An array of bits.
        @param maskBits
            Bits for a mask bitmap.
        @param width
            Cursor width.
        @param height
            Cursor height.
        @param hotSpotX
            Hotspot x coordinate.
        @param hotSpotY
            Hotspot y coordinate.
    */
    wxCursor(const char bits[], int width, int height,
             int hotSpotX = -1, int hotSpotY = -1,
             const char maskBits[] = NULL,
             wxColour* fg = NULL, wxColour* bg = NULL);
    /**
        Constructs a cursor by passing a string resource name or filename.

        On MacOS when specifying a string resource name, first the color
        cursors 'crsr' and then the black/white cursors 'CURS' in the resource
        chain are scanned through.

        @a hotSpotX and @a hotSpotY are currently only used under Windows when
        loading from an icon file, to specify the cursor hotspot relative to
        the top left of the image.

        @param type
            Icon type to load. Under Motif, type defaults to wxBITMAP_TYPE_XBM.
            Under Windows, it defaults to wxBITMAP_TYPE_CUR_RESOURCE. Under
            MacOS, it defaults to wxBITMAP_TYPE_MACCURSOR_RESOURCE.
            Under X, the permitted cursor types are:
            <ul>
            <li>wxBITMAP_TYPE_XBM - Load an X bitmap file.</li>
            </ul>
            Under Windows, the permitted types are:
            - wxBITMAP_TYPE_CUR - Load a cursor from a .cur cursor file (only
                                  if USE_RESOURCE_LOADING_IN_MSW is enabled in
                                  setup.h).
            - wxBITMAP_TYPE_CUR_RESOURCE - Load a Windows resource (as
                                           specified in the .rc file).
            - wxBITMAP_TYPE_ICO - Load a cursor from a .ico icon file (only if
                                  USE_RESOURCE_LOADING_IN_MSW is enabled in
                                  setup.h). Specify @a hotSpotX and @a hotSpotY.
        @param hotSpotX
            Hotspot x coordinate.
        @param hotSpotY
            Hotspot y coordinate.
    */
    wxCursor(const wxString& cursorName, long type,
             int hotSpotX = 0, int hotSpotY = 0);
    /**
        Constructs a cursor using a cursor identifier.

        @param cursorId
            A stock cursor identifier. See ::wxStockCursor.
    */
    wxCursor(wxStockCursor cursorId);
    /**
        Constructs a cursor from a wxImage. If cursor are monochrome on the
        current platform, colors with the RGB elements all greater than 127
        will be foreground, colors less than this background. The mask (if any)
        will be used to specify the transparent area.

        In wxMSW the foreground will be white and the background black. If the
        cursor is larger than 32x32 it is resized.

        In wxGTK, colour cursors and alpha channel are supported (starting from
        GTK+ 2.2). Otherwise the two most frequent colors will be used for
        foreground and background. In any case, the cursor will be displayed at
        the size of the image.

        In wxMac, if the cursor is larger than 16x16 it is resized and
        currently only shown as black/white (mask respected).
    */
    wxCursor(const wxImage& image);
    /**
        Copy constructor, uses @ref overview_refcount "reference counting".

        @param cursor
            Pointer or reference to a cursor to copy.
    */
    wxCursor(const wxCursor& cursor);

    /**
        Destroys the cursor. See
        @ref overview_refcount_destruct "reference-counted object destruction"
        for more info.

        A cursor can be reused for more than one window, and does not get
        destroyed when the window is destroyed. wxWidgets destroys all cursors
        on application exit, although it is best to clean them up explicitly.
    */
    ~wxCursor();

    /**
        Returns @true if cursor data is present.
    */
    bool IsOk() const;

    /**
        Assignment operator, using @ref overview_refcount "reference counting".
    */
    wxCursor operator =(const wxCursor& cursor);
};


/**
    @name Predefined cursors.

    @see wxStockCursor
*/
//@{
wxCursor wxNullCursor;
wxCursor* wxSTANDARD_CURSOR;
wxCursor* wxHOURGLASS_CURSOR;
wxCursor* wxCROSS_CURSOR;
//@}

