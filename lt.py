#!/bin/python3
# Module: lt.py

################################################################################
# lt.py
#
# contains all functions that write LaTeX output to files
################################################################################

import re

import lt_strings

path_ns = './LaTeX'
path = path_ns+'/'

def safe_enc (string):
    '''
        returns <string>, converted to a LaTeX string with valid character encoding;
        removes all instances of U200B;
        does not escape special characters
    '''

    string = string.replace('\u200b', '')

    # Regex looks for instances of a non-arabic character followed by an arabic
    # character. Then, \textarabic{ is placed between them. That means every
    # arabic word is in its own \textarabic{} block: this avoid problems with
    # paragraph breaks within \textarabic{}
    #
    # \uxxxx represents the unicode character with the hexadecimal code xxxx.
    # The ranges in the regex are arabic characters and presentation forms.
    p = re.compile('([^\u0600-\u06ff\u0750-\u07ff\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff])([\u0600-\u06ff\u0750-\u07ff\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff])')
    string = p.sub(r'\1\\textarab{\2', string)

    # Similar to the substitution above: looks for instances of an arabic
    # character followed by a non-arabic, and puts } between them
    p = re.compile('([\u0600-\u06ff\u0750-\u07ff\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff])([^\u0600-\u06ff\u0750-\u07ff\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff])')
    string = p.sub(r'\1}\2', string)

    return string

def safe (string):
    '''
        escapes all special LaTeX-character in <string>, and then returns
        safe_enc(string)
    '''

    p = re.compile(r'&..;')
    string = p.sub("", string)

    string = string.replace('\\', "")

    p = re.compile(r'([_$%#&{}])')
    string = p.sub(r'\\\1', string)

    string = string.replace('^', r'\^{}')

    string = safe_enc(string)

    return string

def master_open():
    '''
        writes the header of the LaTeX master document
    '''

    f = open(path+'master.tex', 'w+')
    f.write(lt_strings.master_open)

def master_close():
    '''
        Writes the footer of the LaTeX master document
    '''

    f = open(path+'master.tex', 'a')
    f.write(lt_strings.master_close)
    f.close()

def thread_open(filename, title):
    '''
        Writes the header for a thread, with title <title>, to
        path+<filename>.tex and adds mention of the thread to the master doc

        Returns the threadfile, for use with thread_post and thread_close
    '''

    threadfile = open(path+filename+".tex", "w+")
    threadfile.write(lt_strings.thread_open(title))

    f = open(path+'master.tex', 'a')
    f.write('''
                \include{'''+filename+'''}
    ''')
    f.close()

    return threadfile

def thread_post(threadfile, title, author, date, content):
    '''
        Writes a post to an already opened thread.
    '''

    threadfile.write(r'''\subsubsection*{'''+title+r'''}
        \begin{mdframed}
            \emph{written by '''+author+''' on '''+date+'''}

            '''+content+r'''
        \end{mdframed}

    ''')

def thread_close(threadfile):
    '''
        Writes the footer for the current thread, and closes threadfile
    '''

    threadfile.close()

def print_table (filename, name, description, colspec, header, table):
    r'''
        print_table(filename, name, description, header, table)

        Prints a table with \section <name>, text <description>, header
        <header> and contents <table> to path+<filename>+".tex".

        All input strings except <filename> must consist of properly sanitised
        and charset-safe LaTeX code.
    '''

    f = open(path+filename+'.tex', "w")

    f.write(lt_strings.table_header)
    f.write(r'''\section{'''+name+'''}
        '''+description+'''
        '''+lt_strings.table_start(colspec, header))

    for row in table:
        for i, item in enumerate(row):
            f.write(item+"\t")
            if i != len(row) - 1:
                f.write("&\t")
        f.write(r'''\\
                ''')

    f.write(lt_strings.table_end)

    f.close()

    f = open(path+"master.tex", 'a')
    f.write(r'''\include{'''+filename+'''}
            ''')
    f.close()
