/////////////////////////////////////////////////////////////////////////////
// Name:        textfile.h
// Purpose:     interface of wxTextFile
// Author:      wxWidgets team
// RCS-ID:      $Id$
// Licence:     wxWindows license
/////////////////////////////////////////////////////////////////////////////

/**
    @class wxTextFile
    @wxheader{textfile.h}

    The wxTextFile is a simple class which allows to work with text files on line by
    line basis. It also understands the differences in line termination characters
    under different platforms and will not do anything bad to files with "non
    native" line termination sequences - in fact, it can be also used to modify the
    text files and change the line termination characters from one type (say DOS) to
    another (say Unix).

    One word of warning: the class is not at all optimized for big files and thus
    it will load the file entirely into memory when opened. Of course, you should
    not
    work in this way with large files (as an estimation, anything over 1 Megabyte is
    surely too big for this class). On the other hand, it is not a serious
    limitation for small files like configuration files or program sources
    which are well handled by wxTextFile.

    The typical things you may do with wxTextFile in order are:

     Create and open it: this is done with either
    wxTextFile::Create or wxTextFile::Open
    function which opens the file (name may be specified either as the argument to
    these functions or in the constructor), reads its contents in memory (in the
    case of @c Open()) and closes it.
     Work with the lines in the file: this may be done either with "direct
    access" functions like wxTextFile::GetLineCount and
    wxTextFile::GetLine (@e operator[] does exactly the same
    but looks more like array addressing) or with "sequential access" functions
    which include wxTextFile::GetFirstLine/
    wxTextFile::GetNextLine and also
    wxTextFile::GetLastLine/wxTextFile::GetPrevLine.
    For the sequential access functions the current line number is maintained: it is
    returned by wxTextFile::GetCurrentLine and may be
    changed with wxTextFile::GoToLine.
     Add/remove lines to the file: wxTextFile::AddLine and
    wxTextFile::InsertLine add new lines while
    wxTextFile::RemoveLine deletes the existing ones.
    wxTextFile::Clear resets the file to empty.
     Save your changes: notice that the changes you make to the file will @b not be
    saved automatically; calling wxTextFile::Close or doing
    nothing discards them! To save the changes you must explicitly call
    wxTextFile::Write - here, you may also change the line
    termination type if you wish.


    @library{wxbase}
    @category{file}

    @see wxFile
*/
class wxTextFile
{
public:
    /**
        Constructor does not load the file into memory, use Open() to do it.
    */
    wxTextFile(const wxString& strFile) const;

    /**
        Destructor does nothing.
    */
    ~wxTextFile() const;

    /**
        Adds a line to the end of file.
    */
    void AddLine(const wxString& str,
                 wxTextFileType type = typeDefault) const;

    /**
        Delete all lines from the file, set current line number to 0.
    */
    void Clear() const;

    /**
        Closes the file and frees memory, @b losing all changes. Use Write()
        if you want to save them.
    */
    bool Close() const;

    //@{
    /**
        Creates the file with the given name or the name which was given in the
        @ref ctor() constructor. The array of file lines is initially
        empty.
        It will fail if the file already exists, Open() should
        be used in this case.
    */
    bool Create() const;
    const bool Create(const wxString& strFile) const;
    //@}

    /**
        Returns @true if the current line is the last one.
    */
    bool Eof() const;

    /**
        Return @true if file exists - the name of the file should have been specified
        in the constructor before calling Exists().
    */
    bool Exists() const;

    /**
        Returns the current line: it has meaning only when you're using
        GetFirstLine()/GetNextLine() functions, it doesn't get updated when
        you're using "direct access" functions like GetLine(). GetFirstLine() and
        GetLastLine() also change the value of the current line, as well as
        GoToLine().
    */
    size_t GetCurrentLine() const;

    /**
        Get the line termination string corresponding to given constant. @e typeDefault
        is
        the value defined during the compilation and corresponds to the native format
        of the platform, i.e. it will be wxTextFileType_Dos under Windows,
        wxTextFileType_Unix under Unix (including Mac OS X when compiling with the
        Apple Developer Tools) and wxTextFileType_Mac under Mac OS (including
        Mac OS X when compiling with CodeWarrior).
    */
    static const char* GetEOL(wxTextFileType type = typeDefault) const;

    /**
        This method together with GetNextLine()
        allows more "iterator-like" traversal of the list of lines, i.e. you may
        write something like:
    */
    wxString GetFirstLine() const;

    /**
        Gets the last line of the file. Together with
        GetPrevLine() it allows to enumerate the lines
        in the file from the end to the beginning like this:
    */
    wxString GetLastLine();

    /**
        Retrieves the line number @a n from the file. The returned line may be
        modified but you shouldn't add line terminator at the end - this will be done
        by wxTextFile.
    */
    wxString GetLine(size_t n) const;

    /**
        Get the number of lines in the file.
    */
    size_t GetLineCount() const;

    /**
        Get the type of the line (see also wxTextFile::GetEOL)
    */
    wxTextFileType GetLineType(size_t n) const;

    /**
        Get the name of the file.
    */
    const char* GetName() const;

    /**
        Gets the next line (see GetFirstLine() for
        the example).
    */
    wxString GetNextLine();

    /**
        Gets the previous line in the file.
    */
    wxString GetPrevLine();

    /**
        Changes the value returned by GetCurrentLine()
        and used by wxTextFile::GetFirstLine/GetNextLine().
    */
    void GoToLine(size_t n) const;

    /**
        Guess the type of file (which is supposed to be opened). If sufficiently
        many lines of the file are in DOS/Unix/Mac format, the corresponding value will
        be returned. If the detection mechanism fails wxTextFileType_None is returned.
    */
    wxTextFileType GuessType() const;

    /**
        Insert a line before the line number @e n.
    */
    void InsertLine(const wxString& str, size_t n,
                    wxTextFileType type = typeDefault) const;

    /**
        Returns @true if the file is currently opened.
    */
    bool IsOpened() const;

    //@{
    /**
        )
        Open() opens the file with the given name or the name which was given in the
        @ref ctor() constructor and also loads file in memory on
        success. It will fail if the file does not exist,
        Create() should be used in this case.
        The @e conv argument is only meaningful in Unicode build of wxWidgets when
        it is used to convert the file to wide character representation.
    */
    bool Open() const;
    const bool Open(const wxString& strFile) const;
    //@}

    /**
        Delete line number @a n from the file.
    */
    void RemoveLine(size_t n) const;

    /**
        )
        Change the file on disk. The @a typeNew parameter allows you to change the
        file format (default argument means "don't change type") and may be used to
        convert, for example, DOS files to Unix.
        The @e conv argument is only meaningful in Unicode build of wxWidgets when
        it is used to convert all lines to multibyte representation before writing them
        them to physical file.
        Returns @true if operation succeeded, @false if it failed.
    */
    bool Write(wxTextFileType typeNew = wxTextFileType_None) const;

    /**
        The same as GetLine().
    */
    wxString operator[](size_t n) const;
};

