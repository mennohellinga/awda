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
        returns <string>, converted to a LaTeX string with valid character encoding
    '''

    if bool(re.search('[\u0400-\u04ff]', string)):
        string = r'''\fontencoding{T2A}\selectfont '''+string+r'''\fontencoding{T1}\selectfont'''

    return string

def safe (string):
    '''
        escapes all special LaTeX-character in <string>, and then return
        safe_enc(string)
    '''

    p = re.compile(r'([\\_$^{}])')
    return safe_enc(p.sub(r'\\\1', string))

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

def print_table (filename, name, description, colspec, header, table):
    r'''
        print_table(filename, name, description, header, table)

        Prints a table with \section <name>, text <description>, header
        <header> and contents <table> to path+<filename>.

        All input strings except filename must consist of properly sanitised
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
