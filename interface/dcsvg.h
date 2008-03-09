/////////////////////////////////////////////////////////////////////////////
// Name:        dcsvg.h
// Purpose:     documentation for wxSVGFileDC class
// Author:      wxWidgets team
// RCS-ID:      $Id$
// Licence:     wxWindows license
/////////////////////////////////////////////////////////////////////////////

/**
    @class wxSVGFileDC
    @wxheader{dcsvg.h}

    A wxSVGFileDC is a @e device context onto which graphics and text can be drawn,
    and the output
    produced as a vector file, in the SVG format
    (see W3C specifications).
    This format can be read by a range of programs, including a Netscape plugin
    (Adobe), full details
    in the SVG Implementation and Resource Directory.
    Vector formats may often be smaller than raster formats.

    The intention behind wxSVGFileDC is that it can be used to produce a file
    corresponding
    to the screen display context, wxSVGFileDC, by passing the wxSVGFileDC as a
    parameter instead of a wxSVGFileDC. Thus the wxSVGFileDC is a write-only class.

    As the wxSVGFileDC is a vector format, raster operations like GetPixel are
    unlikely to be supported.
    However, the SVG specification allows for PNG format raster files to be
    embedded in the SVG, and so
    bitmaps, icons and blit operations into the wxSVGFileDC are supported.

    A more substantial SVG library (for reading and writing) is available at the
    wxArt2D website.

    @library{wxcore}
    @category{FIXME}

    @seealso
    @b Members
*/
class wxSVGFileDC : public wxDC
{
public:
    //@{
    /**
        Constructors:
        a filename @a f with default size 340x240 at 72.0 dots per inch (a frequent
        screen resolution).
        a filename @a f with size @a Width by @a Height at 72.0 dots per inch
        a filename @a f with size @a Width by @a Height at @a dpi resolution.
    */
    wxSVGFileDC(wxString f);
    wxSVGFileDC(wxString f, int Width, int Height);
    wxSVGFileDC(wxString f, int Width, int Height, float dpi);
    //@}

    /**
        Destructor.
    */
    ~wxSVGFileDC();

    /**
        Does nothing
    */


    /**
        As wxDC: Copy from a source DC to this DC, specifying the destination
        coordinates, size of area to copy, source DC, source coordinates,
        logical function, whether to use a bitmap mask, and mask source position.
    */
    bool Blit(wxCoord xdest, wxCoord ydest, wxCoord width,
              wxCoord height, wxSVGFileDC* source,
              wxCoord xsrc, wxCoord ysrc,
              int logicalFunc = wxCOPY,
              bool useMask = FALSE,
              wxCoord xsrcMask = -1,
              wxCoord ysrcMask = -1);

    /**
        Adds the specified point to the bounding box which can be retrieved with
        wxDC::MinX, wxDC::MaxX and
        wxDC::MinY, wxDC::MaxY functions.
    */
    void CalcBoundingBox(wxCoord x, wxCoord y);

    /**
        This makes no sense in wxSVGFileDC and does nothing
    */
    void Clear();

    /**
        Not Implemented
    */
    void CrossHair(wxCoord x, wxCoord y);

    /**
        Not Implemented
    */
    void DestroyClippingRegion();

    /**
        Convert device X coordinate to logical coordinate, using the current
        mapping mode.
    */
    wxCoord DeviceToLogicalX(wxCoord x);

    /**
        Convert device X coordinate to relative logical coordinate, using the current
        mapping mode but ignoring the x axis orientation.
        Use this function for converting a width, for example.
    */
    wxCoord DeviceToLogicalXRel(wxCoord x);

    /**
        Converts device Y coordinate to logical coordinate, using the current
        mapping mode.
    */
    wxCoord DeviceToLogicalY(wxCoord y);

    /**
        Convert device Y coordinate to relative logical coordinate, using the current
        mapping mode but ignoring the y axis orientation.
        Use this function for converting a height, for example.
    */
    wxCoord DeviceToLogicalYRel(wxCoord y);

    /**
        Draws an arc of a circle, centred on (@e xc, yc), with starting point (@e x1,
        y1)
        and ending at (@e x2, y2).   The current pen is used for the outline
        and the current brush for filling the shape.
        The arc is drawn in an anticlockwise direction from the start point to the end
        point.
    */
    void DrawArc(wxCoord x1, wxCoord y1, wxCoord x2, wxCoord y2,
                 wxCoord xc, wxCoord yc);

    /**
        Draw a bitmap on the device context at the specified point. If @a transparent
        is @true and the bitmap has
        a transparency mask, the bitmap will be drawn transparently.
        When drawing a mono-bitmap, the current text foreground colour will be used to
        draw the foreground
        of the bitmap (all bits set to 1), and the current text background colour to
        draw the background
        (all bits set to 0). See also wxDC::SetTextForeground,
        wxDC::SetTextBackground and wxMemoryDC.
    */
    void DrawBitmap(const wxBitmap& bitmap, wxCoord x, wxCoord y,
                    bool transparent);

    //@{
    /**
        Draws a check mark inside the given rectangle.
    */
    void DrawCheckMark(wxCoord x, wxCoord y, wxCoord width,
                       wxCoord height);
    void DrawCheckMark(const wxRect& rect);
    //@}

    //@{
    /**
        Draws a circle with the given centre and radius.
        
        @see wxDC::DrawEllipse
    */
    void DrawCircle(wxCoord x, wxCoord y, wxCoord radius);
    void DrawCircle(const wxPoint& pt, wxCoord radius);
    //@}

    //@{
    /**
        Draws an ellipse contained in the rectangle specified either with the given top
        left corner and the given size or directly. The current pen is used for the
        outline and the current brush for filling the shape.
        
        @see wxDC::DrawCircle
    */
    void DrawEllipse(wxCoord x, wxCoord y, wxCoord width,
                     wxCoord height);
    void DrawEllipse(const wxPoint& pt, const wxSize& size);
    void DrawEllipse(const wxRect& rect);
    //@}

    /**
        Draws an arc of an ellipse. The current pen is used for drawing the arc and
        the current brush is used for drawing the pie.
        @a x and @a y specify the x and y coordinates of the upper-left corner of the
        rectangle that contains
        the ellipse.
        @a width and @a height specify the width and height of the rectangle that
        contains
        the ellipse.
        @a start and @a end specify the start and end of the arc relative to the
        three-o'clock
        position from the center of the rectangle. Angles are specified
        in degrees (360 is a complete circle). Positive values mean
        counter-clockwise motion. If @a start is equal to @e end, a
        complete ellipse will be drawn.
    */
    void DrawEllipticArc(wxCoord x, wxCoord y, wxCoord width,
                         wxCoord height,
                         double start,
                         double end);

    /**
        Draw an icon on the display (does nothing if the device context is PostScript).
        This can be the simplest way of drawing bitmaps on a window.
    */
    void DrawIcon(const wxIcon& icon, wxCoord x, wxCoord y);

    /**
        Draws a line from the first point to the second. The current pen is used
        for drawing the line.
    */
    void DrawLine(wxCoord x1, wxCoord y1, wxCoord x2, wxCoord y2);

    //@{
    /**
        Draws lines using an array of @a points of size @e n, or list of
        pointers to points, adding the optional offset coordinate. The current
        pen is used for drawing the lines.  The programmer is responsible for
        deleting the list of points.
    */
    void DrawLines(int n, wxPoint points[], wxCoord xoffset = 0,
                   wxCoord yoffset = 0);
    void DrawLines(wxList* points, wxCoord xoffset = 0,
                   wxCoord yoffset = 0);
    //@}

    /**
        Draws a point using the current pen.
    */
    void DrawPoint(wxCoord x, wxCoord y);

    //@{
    /**
        Draws a filled polygon using an array of @a points of size @e n,
        or list of pointers to points, adding the optional offset coordinate.
        The last argument specifies the fill rule: @b wxODDEVEN_RULE (the
        default) or @b wxWINDING_RULE.
        The current pen is used for drawing the outline, and the current brush
        for filling the shape.  Using a transparent brush suppresses filling.
        The programmer is responsible for deleting the list of points.
        Note that wxWindows automatically closes the first and last points.
    */
    void DrawPolygon(int n, wxPoint points[], wxCoord xoffset = 0,
                     wxCoord yoffset = 0,
                     int fill_style = wxODDEVEN_RULE);
    void DrawPolygon(wxList* points, wxCoord xoffset = 0,
                     wxCoord yoffset = 0,
                     int fill_style = wxODDEVEN_RULE);
    //@}

    /**
        Draws a rectangle with the given top left corner, and with the given
        size.  The current pen is used for the outline and the current brush
        for filling the shape.
    */
    void DrawRectangle(wxCoord x, wxCoord y, wxCoord width,
                       wxCoord height);

    /**
        Draws the text rotated by @a angle degrees.
        The wxMSW wxDC and wxSVGFileDC rotate the text around slightly different
        points, depending on the size of the font
    */
    void DrawRotatedText(const wxString& text, wxCoord x, wxCoord y,
                         double angle);

    /**
        Draws a rectangle with the given top left corner, and with the given
        size.  The corners are quarter-circles using the given radius. The
        current pen is used for the outline and the current brush for filling
        the shape.
        If @a radius is positive, the value is assumed to be the
        radius of the rounded corner. If @a radius is negative,
        the absolute value is assumed to be the @e proportion of the smallest
        dimension of the rectangle. This means that the corner can be
        a sensible size relative to the size of the rectangle, and also avoids
        the strange effects X produces when the corners are too big for
        the rectangle.
    */
    void DrawRoundedRectangle(wxCoord x, wxCoord y, wxCoord width,
                              wxCoord height,
                              double radius = 20);

    //@{
    /**
        Draws a three-point spline using the current pen.
    */
    void DrawSpline(wxList* points);
    void DrawSpline(wxCoord x1, wxCoord y1, wxCoord x2,
                    wxCoord y2,
                    wxCoord x3,
                    wxCoord y3);
    //@}

    /**
        Draws a text string at the specified point, using the current text font,
        and the current text foreground and background colours.
        The coordinates refer to the top-left corner of the rectangle bounding
        the string. See GetTextExtent() for how
        to get the dimensions of a text string, which can be used to position the
        text more precisely.
    */
    void DrawText(const wxString& text, wxCoord x, wxCoord y);

    /**
        Does nothing
    */
    void EndDoc();

    /**
        Does nothing
    */
    void EndDrawing();

    /**
        Does nothing
    */
    void EndPage();

    /**
        Not implemented
    */
    void FloodFill(wxCoord x, wxCoord y, const wxColour& colour,
                   int style = wxFLOOD_SURFACE);

    //@{
    /**
        Gets the brush used for painting the background (see
        wxSVGFileDC::SetBackground).
    */
    wxBrush GetBackground();
    const wxBrush GetBackground();
    //@}

    /**
        Returns the current background mode: @c wxSOLID or @c wxTRANSPARENT.
        
        @see wxDC::SetBackgroundMode
    */
    int GetBackgroundMode();

    //@{
    /**
        Gets the current brush (see wxSVGFileDC::SetBrush).
    */
    wxBrush GetBrush();
    const wxBrush GetBrush();
    //@}

    /**
        Gets the character height of the currently set font.
    */
    wxCoord GetCharHeight();

    /**
        Gets the average character width of the currently set font.
    */
    wxCoord GetCharWidth();

    /**
        Not implemented
    */
    void GetClippingBox(wxCoord x, wxCoord y, wxCoord width,
                        wxCoord height);

    //@{
    /**
        Gets the current font (see wxSVGFileDC::SetFont).
    */
    wxFont GetFont();
    const wxFont GetFont();
    //@}

    /**
        Gets the current logical function (see wxSVGFileDC::SetLogicalFunction).
    */
    int GetLogicalFunction();

    /**
        Gets the @e mapping mode for the device context (see wxSVGFileDC::SetMapMode).
    */
    int GetMapMode();

    //@{
    /**
        Gets the current pen (see wxSVGFileDC::SetPen).
    */
    wxPen GetPen();
    const wxPen GetPen();
    //@}

    /**
        Not implemented
    */
    bool GetPixel(wxCoord x, wxCoord y, wxColour* colour);

    /**
        For a Windows printer device context, this gets the horizontal and vertical
        resolution.
    */
    void GetSize(wxCoord* width, wxCoord* height);

    //@{
    /**
        Gets the current text background colour (see wxSVGFileDC::SetTextBackground).
    */
    wxColour GetTextBackground();
    const wxColour GetTextBackground();
    //@}

    /**
        Gets the dimensions of the string using the currently selected font.
        @a string is the text string to measure, @a w and @a h are
        the total width and height respectively, @a descent is the
        dimension from the baseline of the font to the bottom of the
        descender, and @a externalLeading is any extra vertical space added
        to the font by the font designer (usually is zero).
        The optional parameter @a font specifies an alternative
        to the currently selected font: but note that this does not
        yet work under Windows, so you need to set a font for
        the device context first.
        See also wxFont, SetFont().
    */
    void GetTextExtent(const wxString& string, wxCoord* w,
                       wxCoord* h,
                       wxCoord* descent = NULL,
                       wxCoord* externalLeading = NULL,
                       wxFont* font = NULL);

    //@{
    /**
        Gets the current text foreground colour (see wxSVGFileDC::SetTextForeground).
    */
    wxColour GetTextForeground();
    const wxColour GetTextForeground();
    //@}

    /**
        Gets the current user scale factor (set by wxDC::SetUserScale).
    */
    void GetUserScale(double x, double y);

    /**
        Converts logical X coordinate to device coordinate, using the current
        mapping mode.
    */
    wxCoord LogicalToDeviceX(wxCoord x);

    /**
        Converts logical X coordinate to relative device coordinate, using the current
        mapping mode but ignoring the x axis orientation.
        Use this for converting a width, for example.
    */
    wxCoord LogicalToDeviceXRel(wxCoord x);

    /**
        Converts logical Y coordinate to device coordinate, using the current
        mapping mode.
    */
    wxCoord LogicalToDeviceY(wxCoord y);

    /**
        Converts logical Y coordinate to relative device coordinate, using the current
        mapping mode but ignoring the y axis orientation.
        Use this for converting a height, for example.
    */
    wxCoord LogicalToDeviceYRel(wxCoord y);

    /**
        Gets the maximum horizontal extent used in drawing commands so far.
    */
    wxCoord MaxX();

    /**
        Gets the maximum vertical extent used in drawing commands so far.
    */
    wxCoord MaxY();

    /**
        Gets the minimum horizontal extent used in drawing commands so far.
    */
    wxCoord MinX();

    /**
        Gets the minimum vertical extent used in drawing commands so far.
    */
    wxCoord MinY();

    /**
        Returns @true if the DC is ok to use; False values arise from being unable to
        write the file
    */
    bool Ok();

    /**
        Resets the bounding box: after a call to this function, the bounding box
        doesn't contain anything.
        
        @see wxDC::CalcBoundingBox
    */
    void ResetBoundingBox();

    /**
        Sets the x and y axis orientation (i.e., the direction from lowest to
        highest values on the axis). The default orientation is the natural
        orientation, e.g. x axis from left to right and y axis from bottom up.
        
        @param xLeftRight
            True to set the x axis orientation to the natural
            left to right orientation, @false to invert it.
        @param yBottomUp
            True to set the y axis orientation to the natural
            bottom up orientation, @false to invert it.
    */
    void SetAxisOrientation(bool xLeftRight, bool yBottomUp);

    /**
        Sets the current background brush for the DC.
    */
    void SetBackground(const wxBrush& brush);

    /**
        @a mode may be one of wxSOLID and wxTRANSPARENT. This setting determines
        whether text will be drawn with a background colour or not.
    */
    void SetBackgroundMode(int mode);

    /**
        Sets the current brush for the DC.
        If the argument is wxNullBrush, the current brush is selected out of the device
        context, and the original brush restored, allowing the current brush to
        be destroyed safely.
        See also wxBrush.
        See also wxMemoryDC for the interpretation of colours
        when drawing into a monochrome bitmap.
    */
    void SetBrush(const wxBrush& brush);

    //@{
    /**
        Not implemented
    */
    void SetClippingRegion(wxCoord x, wxCoord y, wxCoord width,
                           wxCoord height);
    void SetClippingRegion(const wxPoint& pt, const wxSize& sz);
    void SetClippingRegion(const wxRect& rect);
    void SetClippingRegion(const wxRegion& region);
    //@}

    /**
        Sets the device origin (i.e., the origin in pixels after scaling has been
        applied).
        This function may be useful in Windows printing
        operations for placing a graphic on a page.
    */
    void SetDeviceOrigin(wxCoord x, wxCoord y);

    /**
        Sets the current font for the DC. It must be a valid font, in particular you
        should not pass @c wxNullFont to this method.
        See also wxFont.
    */
    void SetFont(const wxFont& font);

    /**
        Only wxCOPY is avalaible; trying to set one of the othe values will fail
    */
    void SetLogicalFunction(int function);

    /**
        The @e mapping mode of the device context defines the unit of
        measurement used to convert logical units to device units. Note that
        in X, text drawing isn't handled consistently with the mapping mode; a
        font is always specified in point size. However, setting the @e user scale (see
        wxSVGFileDC::SetUserScale) scales the text appropriately. In
        Windows, scaleable TrueType fonts are always used; in X, results depend
        on availability of fonts, but usually a reasonable match is found.
        Note that the coordinate origin should ideally be selectable, but for
        now is always at the top left of the screen/printer.
        Drawing to a Windows printer device context under UNIX
        uses the current mapping mode, but mapping mode is currently ignored for
        PostScript output.
        The mapping mode can be one of the following:
        
        wxMM_TWIPS
        
        Each logical unit is 1/20 of a point, or 1/1440 of
          an inch.
        
        wxMM_POINTS
        
        Each logical unit is a point, or 1/72 of an inch.
        
        wxMM_METRIC
        
        Each logical unit is 1 mm.
        
        wxMM_LOMETRIC
        
        Each logical unit is 1/10 of a mm.
        
        wxMM_TEXT
        
        Each logical unit is 1 pixel.
    */
    void SetMapMode(int int);

    /**
        Not implemented
    */
    void SetPalette(const wxPalette& palette);

    /**
        Sets the current pen for the DC.
        If the argument is wxNullPen, the current pen is selected out of the device
        context, and the original pen restored.
        See also wxMemoryDC for the interpretation of colours
        when drawing into a monochrome bitmap.
    */
    void SetPen(const wxPen& pen);

    /**
        Sets the current text background colour for the DC.
    */
    void SetTextBackground(const wxColour& colour);

    /**
        Sets the current text foreground colour for the DC.
        See also wxMemoryDC for the interpretation of colours
        when drawing into a monochrome bitmap.
    */
    void SetTextForeground(const wxColour& colour);

    /**
        Sets the user scaling factor, useful for applications which require
        'zooming'.
    */
    void SetUserScale(double xScale, double yScale);

    /**
        Does nothing
    */
    bool StartDoc(const wxString& message);
};
