#!/bin/python3
# Module: LT_strings.py

################################################################################
# LT_string.py
#
# contains all fixed LaTeX strings used by awda, as well as functions to
# generate some barely-procedural LaTeX-strings
################################################################################

master_open = r'''\documentclass[a4paper, 10pt]{hitec}

\usepackage[british]{babel}

\usepackage{booktabs,fontspec,longtable,mdframed,arabxetex}

\setmainfont{Linux Libertine O}

\newcommand{\awd}{\textsc{awd}}

\title{GE3V17043 — Soldiers, Guerrillas, Terrorists\\Data Analysis Report}
\author{Menno Hellinga}
\confidential{github.com/mennohellinga/awda}

\setcounter{tocdepth}{2}

\begin{document}

\maketitle
\tableofcontents

'''

master_close = r'''\end{document}'''

table_header = r'''% in order to use this table in your own document, place the following code in the preamble:
%\usepackage{booktabs,fontspec,longtable,arabtext}
%\setmainfont{Linux Libertine O} % or another font with good unicode support
% and compile with xelatex

'''

def thread_open(title):
    '''
        thread_open(title):

        Takes a thread title, and creates a LaTeX header for it.
    '''

    return r'''% in order to use this thread in you own document, place the following code in the preamble:
%\usepackage{fontspec,mdframed,arabtext}
%\setmainfont{Linux Libertine O} % or another font with good unicode support
% and compile with xelatex

        \section{'''+title+r'''}
    
    '''

def table_start(spec, names):
    '''
        LT_table_start (spec, names)

        Takes a LaTeX column specification, spec, and a list of header names,
        names, and creates a table header for it.
    '''
    
    result = r'''\begin{longtable}{'''+spec+r'''}
    \toprule
    '''
    
    for i, name in enumerate(names):
        result = result + r'\textbf{' + name + r'}    '
        if i != len(names) - 1:
            result = result + '&'
    result = result + r'''\\
    \midrule
    \endhead
    '''
    
    return result

table_end = r'''\bottomrule
\end{longtable}
'''
