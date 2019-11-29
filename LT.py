#!/bin/python3
# Module: LT.py

################################################################################
# LT.py
#
# contains all functions that write LaTeX output to files
################################################################################

import LT_strings

LT_path_ns = './LaTeX'
LT_path = LT_path_ns+'/'

def master_open():
    '''
        writes the header of the LaTeX master document
    '''

    f = open(LT_path+'master.tex', 'w+')
    f.write(LT_strings.master_open)

def master_close():
    '''
        Writes the footer of the LaTeX master document
    '''

    f = open(LT_path+'master.tex', 'a')
    f.write(LT_strings.master_close)
    f.close()

def print_table (filename, name, description, colspec, header, table):
    r'''
        print_table(filename, name, description, header, table)

        Prints a table with \section <name>, text <description>, header
        <header> and contents <table> to LT_path+<filename>.

        All input strings except filename must consist of properly sanitised
        and charset-safe LaTeX code.
    '''

    f = open(LT_path+filename+'.tex', "w")

    f.write(LT_strings.table_header)
    f.write(r'''\section{'''+name+'''}
        '''+description+'''
        '''+LT_strings.table_start(colspec, header))

    for row in table:
        for i, item in enumerate(row):
            f.write(item+"\t")
            if i != len(row) - 1:
                f.write("&\t")
        f.write(r'''\\
                ''')

    f.write(LT_strings.table_end)

    f.close()

    f = open(LT_path+"master.tex", 'a')
    f.write(r'''\include{'''+filename+'''}
            ''')
    f.close()
