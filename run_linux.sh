#!/bin/sh

if [ -f LaTeX ] || [ -d LaTeX ]
then
	rm -rf LaTeX
fi

mkdir LaTeX

python3 analysis.py
cd LaTeX
pdflatex master.tex
pdflatex master.tex
