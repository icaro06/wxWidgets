#!/bin/sh
#
# File:      makeall.sh
# Purpose:   create wxWindows makefiles for all compilers
# Author:    Michael Bedward
# Created:   29 Aug 1999
# Copyright: (c) 1999 Michael Bedward
# Version:   $Id$
#
# This creates the makefiles for all compilers from the templates using
# tmake. The tmake executable should be in the path.  

# Assume we are in distrib/msw/tmake
#
topdir="../../.."
mswdir="$topdir/src/msw"

for tname in `ls *.t` 
do
    case $tname in
	b32.t)
	    echo "Generating $mswdir/makefile.b32 for Borland C++ (32 bits)..."
	    tmake -t b32 wxwin.pro -o $mswdir/makefile.b32 ;;

	bcc.t)
	    echo "Generating $mswdir/makefile.bcc for Borland C++ (16 bits)..."
	    tmake -t bcc wxwin.pro -o $mswdir/makefile.bcc;;

	dos.t)
	    echo "Generating $mswdir/makefile.dos for Visual C++ 1.52..."
	    tmake -t dos wxwin.pro -o $mswdir/makefile.dos;;

	g95.t)
	    echo "Generating $mswdir/makefile.g95 for Cygwin/Mingw32..."
	    tmake -t g95 wxwin.pro -o $mswdir/makefile.g95;;

	sc.t)
	    echo "Generating $mswdir/makefile.sc for Symantec C++..."
	    tmake -t sc wxwin.pro -o $mswdir/makefile.sc;;

	vc.t) 
	    echo "Generating $mswdir/makefile.vc for Visual C++ 4.0..."
	    tmake -t vc wxwin.pro -o $mswdir/makefile.vc;;

	wat.t)
	    echo "Generating $mswdir/makefile.wat for Watcom C++..."
	    tmake -t wat wxwin.pro -o $mswdir/makefile.wat;;

	unx.t)
	    echo "Generating $topdir/Makefile.in for Unix and Configure..."
	    tmake -t unx wxwin.pro -o $topdir/Makefile.in;;
    esac
done

