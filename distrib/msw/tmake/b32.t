#!#############################################################################
#! File:    b32.t
#! Purpose: tmake template file from which makefile.b32 is generated by running
#!          tmake -t b32 wxwin.pro
#! Author:  Vadim Zeitlin
#! Created: 14.07.99
#! Version: $Id$
#!#############################################################################

#${
    #! include the code which parses filelist.txt file and initializes
    #! %wxCommon, %wxGeneric and %wxMSW hashes.
    IncludeTemplate("filelist.t");

    #! now transform these hashes into $project tags
    foreach $file (sort keys %wxGeneric) {
        my $tag = "";
        next if $wxGeneric{$file} =~ /\b(PS|G|16|U)\b/;

        $file =~ s/cp?p?$/obj/;
        $project{"WXGENERICOBJS"} .= "\$(MSWDIR)\\" . $file . " "
    }

    foreach $file (sort keys %wxCommon) {
        $isCFile = $file =~ /\.c$/;
        $file =~ s/cp?p?$/obj/;
        $obj = "\$(MSWDIR)\\" . $file . " ";
        $project{"WXCOMMONOBJS"} .= $obj;
        $project{"WXCOBJS"} .= $obj if $isCFile;
    }

    foreach $file (sort keys %wxMSW) {
        next if $wxMSW{$file} =~ /\b16\b/;

        if ( $file =~ /^automtn/ ) {
            #! comment in old makefile.b32 seems to imply that this file can't
            #! be compiled with Borland (leads to crash in oleauto sample)
            next;
        }

        $isCFile = $file =~ /\.c$/;

        my $isOleObj = $wxMSW{$file} =~ /\bO\b/;
        $file =~ s/cp?p?$/obj/;
        my $obj = "\$(MSWDIR)\\" . $file . " ";

        $project{"WXMSWOBJS"} .= $obj;
        if ( $isOleObj ) {
            #! remember that this file is in ole subdir
            $project{"WXOLEOBJS"} .= $obj;
        }
        $project{"WXCOBJS"} .= $obj if $isCFile;
    }
#$}

# This file was automatically generated by tmake at #$ Now()
# DO NOT CHANGE THIS FILE, YOUR CHANGES WILL BE LOST! CHANGE B32.T!

#
# File:     makefile.b32
# Author:   Julian Smart
# Created:  1998
# Updated:
# Copyright:
#
# "%W% %G%"
#
# Makefile : Builds wxWindows library wx.lib for MS Windows,
# and Borland C++ (32-bit).

!if "$(BCCDIR)" == ""
!error You must define the BCCDIR variable in autoexec.bat, e.g. BCCDIR=d:\bc4
!endif

!if "$(WXWIN)" == ""
!error You must define the WXWIN variable in autoexec.bat, e.g. WXWIN=c:\wx
!endif

WXDIR = $(WXWIN)

# Set all these to 1 if you want to build a dynamic library
!if "$(DLL)" == "1"
WXMAKINGDLL=1
WXBUILDDLL=1
!endif

!include $(WXDIR)\src\makeb32.env

# Please set these according to the settings in wx_setup.h, so we can include
# the appropriate libraries in wx.lib
USE_CTL3D=0
USE_XPM_IN_MSW=0

PERIPH_LIBS=
PERIPH_TARGET=
PERIPH_CLEAN_TARGET=

!if "$(USE_CTL3D)" == "1"
#Use WIN32S/WIN95 32 bit version ctl3d32.dll under win95 (Andre Beltman)
PERIPH_LIBS=$(WXDIR)\lib\ctl3d32.lib $(PERIPH_LIBS)
PERIPH_TARGET=ctl3d $(PERIPH_TARGET)
PERIPH_CLEAN_TARGET=clean_ctl3d $(PERIPH_CLEAN_TARGET)
!endif

!if "$(USE_XPM_IN_MSW)" == "1"
PERIPH_LIBS=$(WXLIB)\xpm.lib $(PERIPH_LIBS)
PERIPH_TARGET=xpm $(PERIPH_TARGET)
PERIPH_CLEAN_TARGET=clean_xpm $(PERIPH_CLEAN_TARGET)
!endif

#PERIPH_LIBS=$(WXDIR)\lib\zlib.lib $(WXDIR)\lib\winpng.lib $(WXDIR)\lib\jpeg.lib $(PERIPH_LIBS)
PERIPH_LIBS=
PERIPH_TARGET=zlib png jpeg $(PERIPH_TARGET)
PERIPH_CLEAN_TARGET=clean_zlib clean_png clean_jpeg $(PERIPH_CLEAN_TARGET)

!if "$(DLL)" == "0"
DUMMY=dummy
!else
DUMMY=dummydll
LIBS= cw32 import32 ole2w32
!endif

LIBTARGET=$(WXLIB)

GENDIR=..\generic
COMMDIR=..\common
OLEDIR=.\ole
MSWDIR=.

DOCDIR = $(WXDIR)\docs

GENERICOBJS= #$ ExpandList("WXGENERICOBJS");

# Not needed:
#  $(MSWDIR)\colrdlgg.obj \
#  $(MSWDIR)\fontdlgg.obj \
#  $(MSWDIR)\helpxlp.obj \
#  $(MSWDIR)\msgdlgg.obj \
#  $(MSWDIR)\printps.obj \
#  $(MSWDIR)\prntdlgg.obj \
#  $(MSWDIR)\listctrl.obj \
#  $(MSWDIR)\notebook.obj \
#  $(MSWDIR)\treectrl.obj

COMMONOBJS = \
		$(MSWDIR)\y_tab.obj \
		#$ ExpandList("WXCOMMONOBJS");

MSWOBJS = #$ ExpandList("WXMSWOBJS");

OBJECTS = $(COMMONOBJS) $(GENERICOBJS) $(MSWOBJS)

default:	wx

wx:    $(CFG) $(DUMMY).obj $(OBJECTS) $(PERIPH_TARGET) $(LIBTARGET)

all:	all_libs all_execs

!if "$(DLL)" == "0"

$(LIBTARGET): $(DUMMY).obj $(OBJECTS)
        -erase $(LIBTARGET)
	tlib $(LIBTARGET) /P1024 @&&!
+$(OBJECTS:.obj =.obj +) +$(PERIPH_LIBS:.lib =.lib +)
!

!else

$(LIBTARGET): $(DUMMY).obj $(OBJECTS)
	-erase $(LIBTARGET)
	-erase $(WXLIBDIR)\wx.dll
        tlink32 $(LINK_FLAGS) /v @&&!
c0d32.obj $(OBJECTS)
$(WXLIBDIR)\wx
nul
$(PERIPH_LIBS) $(LIBS)
wxb32
!
        implib -c $(LIBTARGET) $(WXLIBDIR)\wx.dll

!endif

dummy.obj: dummy.$(SRCSUFF) $(LOCALHEADERS) $(BASEHEADERS) $(WXDIR)\include\wx\wx.h
dummydll.obj: dummydll.$(SRCSUFF) $(LOCALHEADERS) $(BASEHEADERS) $(WXDIR)\include\wx\wx.h

$(MSWDIR)\y_tab.obj:     $(COMMDIR)\y_tab.c $(COMMDIR)\lex_yy.c

#        cl @<<
# $(CPPFLAGS2) /c $*.c -DUSE_DEFINE -DYY_USE_PROTOS /Fo$@
# <<

$(COMMDIR)\y_tab.c:     $(COMMDIR)\dosyacc.c
        copy $(COMMDIR)\dosyacc.c $(COMMDIR)\y_tab.c

$(COMMDIR)\lex_yy.c:    $(COMMDIR)\doslex.c
    copy $(COMMDIR)\doslex.c $(COMMDIR)\lex_yy.c

# $(OBJECTS):	$(WXDIR)\include\wx\setup.h

#${
    $_ = $project{"WXMSWOBJS"};
    my @objs = split;
    foreach (@objs) {
        $text .= $_ . ": ";
        if ( $project{"WXOLEOBJS"} =~ /\Q$_/ ) { s/MSWDIR/OLEDIR/; }
        $suffix = $project{"WXCOBJS"} =~ /\Q$_/ ? "c" : '$(SRCSUFF)';
        s/obj$/$suffix/;
        $text .= $_ . "\n\n";
    }
#$}

########################################################
# Common objects (always compiled)

#${
    $_ = $project{"WXCOMMONOBJS"};
    my @objs = split;
    foreach (@objs) {
        $text .= $_ . ": ";
        $suffix = $project{"WXCOBJS"} =~ /\Q$_/ ? "c" : '$(SRCSUFF)';
        s/MSWDIR/COMMDIR/;
        s/obj$/$suffix/;
        $text .= $_ . "\n\n";
    }
#$}

########################################################
# Generic objects (not always compiled, depending on
# whether platforms have native implementations)

#${
    $_ = $project{"WXGENERICOBJS"};
    my @objs = split;
    foreach (@objs) {
        $text .= $_ . ": ";
        s/MSWDIR/GENDIR/;
        s/obj$/\$(SRCSUFF)/;
        $text .= $_ . "\n\n";
    }
#$}


all_utils:
    cd $(WXDIR)\utils
    make -f makefile.b32
    cd $(WXDIR)\src\msw

all_samples:
    cd $(WXDIR)\samples
    make -f makefile.b32
    cd $(WXDIR)\src\msw

all_execs:
    cd $(WXDIR)\utils
    make -f makefile.b32 all_execs
    cd $(WXDIR)\src\msw

wxxpm:	$(CFG)
	cd $(WXDIR)\src\xpm
	make -f makefile.b32 -DCFG=$(CFG) -DFINAL=$(FINAL) -DWXWIN=$(WXDIR) -DDEBUG=$(DEBUG)
	cd $(WXDIR)\src\msw

clean_wxxpm:	$(CFG)
	cd $(WXDIR)\src\xpm
	make -f makefile.b32 clean
	cd $(WXDIR)\src\msw

png:    $(CFG)
        cd $(WXDIR)\src\png
        make -f makefile.b32
        cd $(WXDIR)\src\msw

clean_png:
        cd $(WXDIR)\src\png
        make -f makefile.b32 clean
        cd $(WXDIR)\src\msw

zlib:   $(CFG)
        cd $(WXDIR)\src\zlib
        make -f makefile.b32 lib
        cd $(WXDIR)\src\msw

clean_zlib:
        cd $(WXDIR)\src\zlib
        make -f makefile.b32 clean
        cd $(WXDIR)\src\msw

jpeg:    $(CFG)
        cd $(WXDIR)\src\jpeg
        make -f makefile.b32
        cd $(WXDIR)\src\msw

clean_jpeg:
        cd $(WXDIR)\src\jpeg
        make -f makefile.b32 clean
        cd $(WXDIR)\src\msw

$(CFG): makefile.b32
	copy &&!
-H=$(WXDIR)\src\msw\wx32.csm
-3
-d
-R-
-X
-w-par
-w-aus
-w-hid # virtual function A hides virtual function B
-WE
-tWM

-I$(WXINC);$(BCCDIR)\include;$(WXDIR)/src/png;$(WXDIR)/src/jpeg;$(WXDIR)/src/zlib;$(WXDIR)/src/xpm
-I$(WXDIR)\include\wx\msw\gnuwin32

-L$(BCCDIR)\lib
-D__WXWIN__
-D__WXMSW__
-D__WINDOWS__
-DWIN32
$(OPT)
$(DEBUG_FLAGS)
$(WIN95FLAG)
! $(CFG)

#-I$(WXDIR)\src\common\wxxpm\libxpm.34b\lib
# -Oxt

clean: $(PERIPH_CLEAN_TARGET)
    -erase $(LIBTARGET)
    -erase *.obj
    -erase *.pch
    -erase *.csm
    -erase *.cfg
    -erase ..\common\y_tab.c
    -erase ..\common\lex_yy.c

cleanall: clean


MFTYPE=b32
# Can't use this or we'll have to distribute all tmake files with wxWindows
# makefile.$(MFTYPE) : $(WXWIN)\distrib\msw\tmake\filelist.txt $(WXWIN)\distrib\msw\tmake\$(MFTYPE).t

self:
	cd $(WXWIN)\distrib\msw\tmake
	tmake -t $(MFTYPE) wxwin.pro -o makefile.$(MFTYPE)
	copy makefile.$(MFTYPE) $(WXWIN)\src\msw

