/////////////////////////////////////////////////////////////////////////////
// Name:        palette.h
// Purpose:     wxPalette class
// Author:      AUTHOR
// Modified by:
// Created:     ??/??/98
// RCS-ID:      $Id$
// Copyright:   (c) AUTHOR
// Licence:   	wxWindows licence
/////////////////////////////////////////////////////////////////////////////

#ifndef _WX_PALETTE_H_
#define _WX_PALETTE_H_

#ifdef __GNUG__
#pragma interface "palette.h"
#endif

#include "wx/colour.h"
#include "wx/gdiobj.h"

class WXDLLEXPORT wxPalette;

class WXDLLEXPORT wxPaletteRefData: public wxGDIRefData
{
    friend class WXDLLEXPORT wxPalette;
public:
    wxPaletteRefData();
    ~wxPaletteRefData();
protected:
 		wxColour* m_palette;
 		wxInt32		m_count ;
};

#define M_PALETTEDATA ((wxPaletteRefData *)m_refData)

class WXDLLEXPORT wxPalette: public wxGDIObject
{
  DECLARE_DYNAMIC_CLASS(wxPalette)

public:
  wxPalette();
  inline wxPalette(const wxPalette& palette) { Ref(palette); }

  wxPalette(int n, const unsigned char *red, const unsigned char *green, const unsigned char *blue);
  ~wxPalette();
  bool Create(int n, const unsigned char *red, const unsigned char *green, const unsigned char *blue);
  int GetPixel(const unsigned char red, const unsigned char green, const unsigned char blue) const;
  bool GetRGB(int pixel, unsigned char *red, unsigned char *green, unsigned char *blue) const;

  virtual bool Ok() const { return (m_refData != NULL) ; }

  inline wxPalette& operator = (const wxPalette& palette) { if (*this == palette) return (*this); Ref(palette); return *this; }
  inline bool operator == (const wxPalette& palette) { return m_refData == palette.m_refData; }
  inline bool operator != (const wxPalette& palette) { return m_refData != palette.m_refData; }

/* TODO: implementation
  inline WXHPALETTE GetHPALETTE() const { return (M_PALETTEDATA ? M_PALETTEDATA->m_hPalette : 0); }
  void SetHPALETTE(WXHPALETTE pal);
*/
};

#endif
    // _WX_PALETTE_H_
