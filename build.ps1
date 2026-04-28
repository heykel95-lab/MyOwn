$MAIN = "Thesis"

# Clean auxiliary files first to avoid corrupted .aux errors.
Remove-Item -Force -ErrorAction SilentlyContinue *.aux,*.bbl,*.bcf,*.blg,*.log,*.out,*.run.xml,*.toc,*.lof,*.lot,*.lol,*.loa,*.acn,*.acr,*.alg,*.glg,*.glo,*.gls,*.ist,*.synctex.gz
Get-ChildItem -Recurse -Include *.aux | Remove-Item -Force -ErrorAction SilentlyContinue

pdflatex "$MAIN.tex"
bibtex $MAIN
pdflatex "$MAIN.tex"
pdflatex "$MAIN.tex"
