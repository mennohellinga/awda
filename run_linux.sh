#!/bin/sh

python3 analysis.py
cd LaTeX
xelatex master.tex
xelatex master.tex
