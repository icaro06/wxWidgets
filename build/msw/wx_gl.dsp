# Microsoft Developer Studio Project File - Name="wx_gl" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** DO NOT EDIT **

# TARGTYPE "Win32 (x86) Static Library" 0x0104
# TARGTYPE "Win32 (x86) Dynamic-Link Library" 0x0102

CFG=gl - Win32 Debug USE_AUI_0
!MESSAGE This is not a valid makefile. To build this project using NMAKE,
!MESSAGE use the Export Makefile command and run
!MESSAGE 
!MESSAGE NMAKE /f "wx_gl.mak".
!MESSAGE 
!MESSAGE You can specify a configuration when running NMAKE
!MESSAGE by defining the macro CFG on the command line. For example:
!MESSAGE 
!MESSAGE NMAKE /f "wx_gl.mak" CFG="gl - Win32 Debug USE_AUI_0"
!MESSAGE 
!MESSAGE Possible choices for configuration are:
!MESSAGE 
!MESSAGE "gl - Win32 DLL Universal Unicode Release USE_AUI_1" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Universal Unicode Release USE_AUI_0" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Universal Unicode Debug USE_AUI_1" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Universal Unicode Debug USE_AUI_0" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Universal Release USE_AUI_1" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Universal Release USE_AUI_0" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Universal Debug USE_AUI_1" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Universal Debug USE_AUI_0" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Unicode Release USE_AUI_1" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Unicode Release USE_AUI_0" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Unicode Debug USE_AUI_1" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Unicode Debug USE_AUI_0" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Release USE_AUI_1" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Release USE_AUI_0" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Debug USE_AUI_1" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 DLL Debug USE_AUI_0" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "gl - Win32 Universal Unicode Release USE_AUI_1" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Universal Unicode Release USE_AUI_0" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Universal Unicode Debug USE_AUI_1" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Universal Unicode Debug USE_AUI_0" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Universal Release USE_AUI_1" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Universal Release USE_AUI_0" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Universal Debug USE_AUI_1" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Universal Debug USE_AUI_0" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Unicode Release USE_AUI_1" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Unicode Release USE_AUI_0" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Unicode Debug USE_AUI_1" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Unicode Debug USE_AUI_0" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Release USE_AUI_1" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Release USE_AUI_0" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Debug USE_AUI_1" (based on "Win32 (x86) Static Library")
!MESSAGE "gl - Win32 Debug USE_AUI_0" (based on "Win32 (x86) Static Library")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=cl.exe
RSC=rc.exe

!IF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswunivudll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswunivudll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswunivu" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivudll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmswuniv270u_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswunivu" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivudll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmswuniv270u_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswunivu" /i "..\..\include" /d WXDLLNAME=wxmswuniv270u_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswunivu" /i "..\..\include" /d WXDLLNAME=wxmswuniv270u_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregexu.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27u_core.lib wxbase27u.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270u_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27u_gl.lib"
# ADD LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregexu.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27u_core.lib wxbase27u.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270u_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27u_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswunivudll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswunivudll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswunivu" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivudll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmswuniv270u_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswunivu" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivudll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmswuniv270u_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswunivu" /i "..\..\include" /d WXDLLNAME=wxmswuniv270u_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswunivu" /i "..\..\include" /d WXDLLNAME=wxmswuniv270u_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregexu.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27u_core.lib wxbase27u.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270u_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27u_gl.lib"
# ADD LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregexu.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27u_core.lib wxbase27u.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270u_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27u_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswunivuddll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswunivuddll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswunivud" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivuddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmswuniv270ud_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswunivud" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivuddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmswuniv270ud_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "__WXDEBUG__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswunivud" /i "..\..\include" /d WXDLLNAME=wxmswuniv270ud_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "__WXDEBUG__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswunivud" /i "..\..\include" /d WXDLLNAME=wxmswuniv270ud_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexud.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27ud_core.lib wxbase27ud.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270ud_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27ud_gl.lib" /debug
# ADD LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexud.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27ud_core.lib wxbase27ud.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270ud_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27ud_gl.lib" /debug

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswunivuddll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswunivuddll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswunivud" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivuddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmswuniv270ud_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswunivud" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivuddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmswuniv270ud_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "__WXDEBUG__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswunivud" /i "..\..\include" /d WXDLLNAME=wxmswuniv270ud_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "__WXDEBUG__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswunivud" /i "..\..\include" /d WXDLLNAME=wxmswuniv270ud_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexud.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27ud_core.lib wxbase27ud.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270ud_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27ud_gl.lib" /debug
# ADD LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexud.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27ud_core.lib wxbase27ud.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270ud_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27ud_gl.lib" /debug

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswunivdll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswunivdll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswuniv" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivdll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmswuniv270_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswuniv" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivdll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmswuniv270_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "__WXMSW__" /d "__WXUNIVERSAL__" /i "..\..\lib\vc_dll\mswuniv" /i "..\..\include" /d WXDLLNAME=wxmswuniv270_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "__WXMSW__" /d "__WXUNIVERSAL__" /i "..\..\lib\vc_dll\mswuniv" /i "..\..\include" /d WXDLLNAME=wxmswuniv270_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregex.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27_core.lib wxbase27.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27_gl.lib"
# ADD LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregex.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27_core.lib wxbase27.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswunivdll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswunivdll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswuniv" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivdll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmswuniv270_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswuniv" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivdll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmswuniv270_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "__WXMSW__" /d "__WXUNIVERSAL__" /i "..\..\lib\vc_dll\mswuniv" /i "..\..\include" /d WXDLLNAME=wxmswuniv270_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "__WXMSW__" /d "__WXUNIVERSAL__" /i "..\..\lib\vc_dll\mswuniv" /i "..\..\include" /d WXDLLNAME=wxmswuniv270_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregex.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27_core.lib wxbase27.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27_gl.lib"
# ADD LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregex.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27_core.lib wxbase27.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswunivddll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswunivddll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswunivd" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmswuniv270d_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswunivd" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmswuniv270d_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "__WXDEBUG__" /i "..\..\lib\vc_dll\mswunivd" /i "..\..\include" /d WXDLLNAME=wxmswuniv270d_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "__WXDEBUG__" /i "..\..\lib\vc_dll\mswunivd" /i "..\..\include" /d WXDLLNAME=wxmswuniv270d_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexd.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27d_core.lib wxbase27d.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270d_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27d_gl.lib" /debug
# ADD LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexd.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27d_core.lib wxbase27d.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270d_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27d_gl.lib" /debug

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswunivddll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswunivddll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswunivd" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmswuniv270d_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswunivd" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswunivddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmswuniv270d_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "__WXDEBUG__" /i "..\..\lib\vc_dll\mswunivd" /i "..\..\include" /d WXDLLNAME=wxmswuniv270d_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXUNIVERSAL__" /d "__WXDEBUG__" /i "..\..\lib\vc_dll\mswunivd" /i "..\..\include" /d WXDLLNAME=wxmswuniv270d_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexd.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27d_core.lib wxbase27d.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270d_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27d_gl.lib" /debug
# ADD LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexd.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmswuniv27d_core.lib wxbase27d.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmswuniv270d_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmswuniv27d_gl.lib" /debug

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswudll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswudll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswu" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswudll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmsw270u_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswu" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswudll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmsw270u_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "__WXMSW__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswu" /i "..\..\include" /d WXDLLNAME=wxmsw270u_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "__WXMSW__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswu" /i "..\..\include" /d WXDLLNAME=wxmsw270u_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregexu.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27u_core.lib wxbase27u.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270u_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27u_gl.lib"
# ADD LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregexu.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27u_core.lib wxbase27u.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270u_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27u_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswudll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswudll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswu" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswudll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmsw270u_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\mswu" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswudll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmsw270u_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "__WXMSW__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswu" /i "..\..\include" /d WXDLLNAME=wxmsw270u_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "__WXMSW__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswu" /i "..\..\include" /d WXDLLNAME=wxmsw270u_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregexu.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27u_core.lib wxbase27u.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270u_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27u_gl.lib"
# ADD LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregexu.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27u_core.lib wxbase27u.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270u_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27u_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswuddll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswuddll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswud" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswuddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmsw270ud_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswud" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswuddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmsw270ud_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXDEBUG__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswud" /i "..\..\include" /d WXDLLNAME=wxmsw270ud_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXDEBUG__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswud" /i "..\..\include" /d WXDLLNAME=wxmsw270ud_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexud.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27ud_core.lib wxbase27ud.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270ud_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27ud_gl.lib" /debug
# ADD LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexud.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27ud_core.lib wxbase27ud.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270ud_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27ud_gl.lib" /debug

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswuddll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswuddll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswud" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswuddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmsw270ud_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswud" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswuddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmsw270ud_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXDEBUG__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswud" /i "..\..\include" /d WXDLLNAME=wxmsw270ud_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXDEBUG__" /d "_UNICODE" /i "..\..\lib\vc_dll\mswud" /i "..\..\include" /d WXDLLNAME=wxmsw270ud_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexud.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27ud_core.lib wxbase27ud.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270ud_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27ud_gl.lib" /debug
# ADD LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexud.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27ud_core.lib wxbase27ud.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270ud_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27ud_gl.lib" /debug

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswdll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswdll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\msw" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswdll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmsw270_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\msw" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswdll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmsw270_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "__WXMSW__" /i "..\..\lib\vc_dll\msw" /i "..\..\include" /d WXDLLNAME=wxmsw270_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "__WXMSW__" /i "..\..\lib\vc_dll\msw" /i "..\..\include" /d WXDLLNAME=wxmsw270_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregex.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27_core.lib wxbase27.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27_gl.lib"
# ADD LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregex.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27_core.lib wxbase27.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswdll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswdll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\msw" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswdll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmsw270_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_dll\msw" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswdll\wxprec_gldll.pch" /Fd..\..\lib\vc_dll\wxmsw270_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "__WXMSW__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "__WXMSW__" /i "..\..\lib\vc_dll\msw" /i "..\..\include" /d WXDLLNAME=wxmsw270_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "__WXMSW__" /i "..\..\lib\vc_dll\msw" /i "..\..\include" /d WXDLLNAME=wxmsw270_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregex.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27_core.lib wxbase27.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27_gl.lib"
# ADD LINK32 wxtiff.lib wxjpeg.lib wxpng.lib wxzlib.lib wxregex.lib wxexpat.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27_core.lib wxbase27.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswddll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswddll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswd" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmsw270d_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswd" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmsw270d_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXDEBUG__" /i "..\..\lib\vc_dll\mswd" /i "..\..\include" /d WXDLLNAME=wxmsw270d_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXDEBUG__" /i "..\..\lib\vc_dll\mswd" /i "..\..\include" /d WXDLLNAME=wxmsw270d_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexd.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27d_core.lib wxbase27d.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270d_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27d_gl.lib" /debug
# ADD LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexd.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27d_core.lib wxbase27d.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270d_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27d_gl.lib" /debug

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_dll"
# PROP BASE Intermediate_Dir "vc_mswddll\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_dll"
# PROP Intermediate_Dir "vc_mswddll\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswd" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmsw270d_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_dll\mswd" /I "..\..\include" /W4 /Yu"wx/wxprec.h" /Fp"vc_mswddll\wxprec_gldll.pch" /Zi /Gm /GZ /Fd..\..\lib\vc_dll\wxmsw270d_gl_vc_custom.pdb /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /c
# ADD BASE MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD MTL /nologo /D "WIN32" /D "_USRDLL" /D "DLL_EXPORTS" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "WXUSINGDLL" /D "WXMAKINGDLL_GL" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXDEBUG__" /i "..\..\lib\vc_dll\mswd" /i "..\..\include" /d WXDLLNAME=wxmsw270d_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
# ADD RSC /l 0x409 /d "_DEBUG" /d "__WXMSW__" /d "__WXDEBUG__" /i "..\..\lib\vc_dll\mswd" /i "..\..\include" /d WXDLLNAME=wxmsw270d_gl_vc_custom /i "..\..\src\tiff" /i "..\..\src\jpeg" /i "..\..\src\png" /i "..\..\src\zlib" /i "..\..\src\regex" /i "..\..\src\expat\lib" /d "WXUSINGDLL" /d WXMAKINGDLL_GL
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexd.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27d_core.lib wxbase27d.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270d_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27d_gl.lib" /debug
# ADD LINK32 wxtiffd.lib wxjpegd.lib wxpngd.lib wxzlibd.lib wxregexd.lib wxexpatd.lib kernel32.lib user32.lib gdi32.lib comdlg32.lib winspool.lib winmm.lib shell32.lib comctl32.lib ole32.lib oleaut32.lib uuid.lib rpcrt4.lib advapi32.lib wsock32.lib odbc32.lib wxmsw27d_core.lib wxbase27d.lib opengl32.lib glu32.lib /nologo /dll /machine:i386 /out:"..\..\lib\vc_dll\wxmsw270d_gl_vc_custom.dll" /libpath:"..\..\lib\vc_dll" /implib:"..\..\lib\vc_dll\wxmsw27d_gl.lib" /debug

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswunivu\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswunivu\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswunivu" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmswuniv27u_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivu\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswunivu" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmswuniv27u_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivu\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27u_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27u_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswunivu\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswunivu\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswunivu" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmswuniv27u_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivu\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswunivu" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmswuniv27u_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivu\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "_UNICODE" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27u_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27u_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswunivud\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswunivud\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswunivud" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmswuniv27ud_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivud\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswunivud" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmswuniv27ud_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivud\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27ud_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27ud_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswunivud\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswunivud\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswunivud" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmswuniv27ud_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivud\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswunivud" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmswuniv27ud_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivud\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /D "_UNICODE" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27ud_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27ud_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswuniv\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswuniv\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswuniv" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmswuniv27_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswuniv\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "__WXUNIVERSAL__" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswuniv" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmswuniv27_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswuniv\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "__WXUNIVERSAL__" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswuniv\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswuniv\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswuniv" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmswuniv27_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswuniv\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "__WXUNIVERSAL__" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswuniv" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmswuniv27_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswuniv\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "__WXUNIVERSAL__" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswunivd\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswunivd\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswunivd" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmswuniv27d_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivd\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswunivd" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmswuniv27d_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivd\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27d_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27d_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswunivd\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswunivd\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswunivd" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmswuniv27d_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivd\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswunivd" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmswuniv27d_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswunivd\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXUNIVERSAL__" /D "__WXDEBUG__" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27d_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmswuniv27d_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswu\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswu\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswu" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmsw27u_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswu\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "_UNICODE" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswu" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmsw27u_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswu\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "_UNICODE" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27u_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27u_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswu\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswu\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswu" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmsw27u_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswu\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "_UNICODE" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\mswu" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmsw27u_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswu\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /D "_UNICODE" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27u_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27u_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswud\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswud\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswud" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmsw27ud_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswud\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswud" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmsw27ud_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswud\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27ud_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27ud_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswud\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswud\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswud" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmsw27ud_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswud\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswud" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmsw27ud_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswud\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /D "_UNICODE" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27ud_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27ud_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_msw\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_msw\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\msw" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmsw27_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_msw\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\msw" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmsw27_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_msw\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_msw\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_msw\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\msw" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmsw27_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_msw\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /c
# ADD CPP /nologo /FD /MD /O2 /GR /EHsc /I "..\..\lib\vc_lib\msw" /I "..\..\include" /W4 /Fd..\..\lib\vc_lib\wxmsw27_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_msw\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "__WXMSW__" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_1"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswd\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswd\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswd" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmsw27d_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswd\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswd" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmsw27d_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswd\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27d_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27d_gl.lib"

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_0"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "..\..\lib\vc_lib"
# PROP BASE Intermediate_Dir "vc_mswd\gl"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "..\..\lib\vc_lib"
# PROP Intermediate_Dir "vc_mswd\gl"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswd" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmsw27d_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswd\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /c
# ADD CPP /nologo /FD /MDd /Od /GR /EHsc /I "..\..\lib\vc_lib\mswd" /I "..\..\include" /W4 /Zi /Gm /GZ /Fd..\..\lib\vc_lib\wxmsw27d_gl.pdb /Yu"wx/wxprec.h" /Fp"vc_mswd\wxprec_gllib.pch" /I "..\..\src\tiff" /I "..\..\src\jpeg" /I "..\..\src\png" /I "..\..\src\zlib" /I "..\..\src\regex" /I "..\..\src\expat\lib" /D "WIN32" /D "_LIB" /D "_DEBUG" /D "__WXMSW__" /D "__WXDEBUG__" /c
# ADD BASE RSC /l 0x409
# ADD RSC /l 0x409
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27d_gl.lib"
# ADD LIB32 /nologo /out:"..\..\lib\vc_lib\wxmsw27d_gl.lib"

!ENDIF

# Begin Target

# Name "gl - Win32 DLL Universal Unicode Release USE_AUI_1"
# Name "gl - Win32 DLL Universal Unicode Release USE_AUI_0"
# Name "gl - Win32 DLL Universal Unicode Debug USE_AUI_1"
# Name "gl - Win32 DLL Universal Unicode Debug USE_AUI_0"
# Name "gl - Win32 DLL Universal Release USE_AUI_1"
# Name "gl - Win32 DLL Universal Release USE_AUI_0"
# Name "gl - Win32 DLL Universal Debug USE_AUI_1"
# Name "gl - Win32 DLL Universal Debug USE_AUI_0"
# Name "gl - Win32 DLL Unicode Release USE_AUI_1"
# Name "gl - Win32 DLL Unicode Release USE_AUI_0"
# Name "gl - Win32 DLL Unicode Debug USE_AUI_1"
# Name "gl - Win32 DLL Unicode Debug USE_AUI_0"
# Name "gl - Win32 DLL Release USE_AUI_1"
# Name "gl - Win32 DLL Release USE_AUI_0"
# Name "gl - Win32 DLL Debug USE_AUI_1"
# Name "gl - Win32 DLL Debug USE_AUI_0"
# Name "gl - Win32 Universal Unicode Release USE_AUI_1"
# Name "gl - Win32 Universal Unicode Release USE_AUI_0"
# Name "gl - Win32 Universal Unicode Debug USE_AUI_1"
# Name "gl - Win32 Universal Unicode Debug USE_AUI_0"
# Name "gl - Win32 Universal Release USE_AUI_1"
# Name "gl - Win32 Universal Release USE_AUI_0"
# Name "gl - Win32 Universal Debug USE_AUI_1"
# Name "gl - Win32 Universal Debug USE_AUI_0"
# Name "gl - Win32 Unicode Release USE_AUI_1"
# Name "gl - Win32 Unicode Release USE_AUI_0"
# Name "gl - Win32 Unicode Debug USE_AUI_1"
# Name "gl - Win32 Unicode Debug USE_AUI_0"
# Name "gl - Win32 Release USE_AUI_1"
# Name "gl - Win32 Release USE_AUI_0"
# Name "gl - Win32 Debug USE_AUI_1"
# Name "gl - Win32 Debug USE_AUI_0"
# Begin Group "Common Sources"

# PROP Default_Filter ""
# Begin Source File

SOURCE=..\..\src\common\dummy.cpp
# ADD BASE CPP /Yc"wx/wxprec.h"
# ADD CPP /Yc"wx/wxprec.h"
# End Source File
# End Group
# Begin Group "MSW Sources"

# PROP Default_Filter ""
# Begin Source File

SOURCE=..\..\src\msw\glcanvas.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\msw\version.rc

!IF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_1"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_0"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_1"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_0"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_1"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_0"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_1"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_0"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_1"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_0"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_1"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_0"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_1"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_0"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_1"


!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_0"


!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_1"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_0"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_1"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_0"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_1"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_0"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_1"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_0"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_1"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_0"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_1"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_0"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_1"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_0"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_1"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_0"

# PROP Exclude_From_Build 1

!ENDIF

# End Source File
# End Group
# Begin Group "Setup Headers"

# PROP Default_Filter ""
# Begin Source File

SOURCE=..\..\include\wx\univ\setup.h

!IF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivu\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_dll\mswunivu\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswunivu\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivu\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_dll\mswunivu\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswunivu\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivud\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_dll\mswunivud\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswunivud\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivud\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_dll\mswunivud\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswunivud\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswuniv\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_dll\mswuniv\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswuniv\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswuniv\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_dll\mswuniv\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswuniv\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivd\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_dll\mswunivd\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswunivd\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivd\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_dll\mswunivd\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswunivd\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivu\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_lib\mswunivu\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswunivu\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivu\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_lib\mswunivu\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswunivu\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivud\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_lib\mswunivud\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswunivud\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivud\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_lib\mswunivud\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswunivud\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswuniv\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_lib\mswuniv\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswuniv\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswuniv\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_lib\mswuniv\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswuniv\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivd\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_lib\mswunivd\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswunivd\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivd\wx\setup.h
InputPath=..\include\wx\univ\setup.h

"..\..\lib\vc_lib\mswunivd\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswunivd\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ENDIF

# End Source File
# Begin Source File

SOURCE=..\..\include\wx\msw\setup.h

!IF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswu\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_dll\mswu\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswu\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswu\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_dll\mswu\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswu\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswud\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_dll\mswud\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswud\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswud\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_dll\mswud\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswud\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\msw\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_dll\msw\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\msw\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\msw\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_dll\msw\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\msw\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswd\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_dll\mswd\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswd\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswd\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_dll\mswd\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_dll\mswd\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_1"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_0"

# Begin Custom Build - 

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswu\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_lib\mswu\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswu\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswu\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_lib\mswu\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswu\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswud\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_lib\mswud\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswud\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswud\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_lib\mswud\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswud\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\msw\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_lib\msw\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\msw\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\msw\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_lib\msw\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\msw\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswd\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_lib\mswd\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswd\wx\setup.h

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswd\wx\setup.h
InputPath=..\include\wx\msw\setup.h

"..\..\lib\vc_lib\mswd\wx\setup.h" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy "$(InputPath)" ..\..\lib\vc_lib\mswd\wx\setup.h

# End Custom Build

!ENDIF

# End Source File
# End Group
# Begin Group "MSW Headers"

# PROP Default_Filter ""
# Begin Source File

SOURCE=..\..\include\wx\msw\genrcdefs.h

!IF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivu\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswunivu\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswunivu\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivu\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswunivu\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswunivu\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivud\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswunivud\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswunivud\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Unicode Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivud\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswunivud\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswunivud\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswuniv\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswuniv\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswuniv\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswuniv\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswuniv\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswuniv\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivd\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswunivd\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswunivd\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Universal Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswunivd\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswunivd\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswunivd\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswu\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswu\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswu\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswu\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswu\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswu\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswud\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswud\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswud\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Unicode Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswud\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswud\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswud\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\msw\wx\msw\rcdefs.h

"..\..\lib\vc_dll\msw\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\msw\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\msw\wx\msw\rcdefs.h

"..\..\lib\vc_dll\msw\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\msw\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswd\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswd\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswd\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 DLL Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_dll\mswd\wx\msw\rcdefs.h

"..\..\lib\vc_dll\mswd\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_dll\mswd\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivu\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswunivu\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswunivu\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivu\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswunivu\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswunivu\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivud\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswunivud\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswunivud\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Unicode Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivud\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswunivud\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswunivud\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswuniv\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswuniv\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswuniv\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswuniv\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswuniv\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswuniv\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivd\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswunivd\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswunivd\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Universal Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswunivd\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswunivd\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswunivd\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswu\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswu\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswu\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswu\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswu\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswu\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswud\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswud\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswud\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Unicode Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswud\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswud\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswud\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\msw\wx\msw\rcdefs.h

"..\..\lib\vc_lib\msw\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\msw\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Release USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\msw\wx\msw\rcdefs.h

"..\..\lib\vc_lib\msw\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\msw\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_1"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswd\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswd\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswd\wx\msw\rcdefs.h"

# End Custom Build

!ELSEIF  "$(CFG)" == "gl - Win32 Debug USE_AUI_0"

# Begin Custom Build - Creating ..\..\lib\vc_lib\mswd\wx\msw\rcdefs.h

"..\..\lib\vc_lib\mswd\wx\msw\rcdefs.h" : "$(SOURCE)" "$(SETUPHDIR)\wx\msw"
	cl /EP /nologo "$(InputPath)" > "..\..\lib\vc_lib\mswd\wx\msw\rcdefs.h"

# End Custom Build

!ENDIF

# End Source File
# Begin Source File

SOURCE=..\..\include\wx\msw\glcanvas.h
# End Source File
# End Group
# End Target
# End Project

