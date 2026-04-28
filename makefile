MAIN=Thesis

all:
	pdflatex $(MAIN).tex
	bibtex $(MAIN)
	pdflatex $(MAIN).tex
	pdflatex $(MAIN).tex

clean:
	rm -f *.aux *.bbl *.bcf *.blg *.log *.out *.run.xml *.toc *.lof *.lot *.lol *.loa *.acn *.acr *.alg *.glg *.glo *.gls *.ist *.synctex.gz
	find chapters frontmatter backmatter config -name "*.aux" -delete
