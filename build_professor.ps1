$MAIN = "Professor_Draft"

# Clean only the professor draft outputs.
Remove-Item -Force -ErrorAction SilentlyContinue "$MAIN.aux","$MAIN.bbl","$MAIN.blg","$MAIN.log","$MAIN.out","$MAIN.toc","$MAIN.pdf","$MAIN.synctex.gz"

pdflatex "$MAIN.tex"
$aux = Get-Content "$MAIN.aux" -Raw
if ($aux -match "\\citation" -and $aux -match "\\bibdata") {
  bibtex $MAIN
}
pdflatex "$MAIN.tex"
pdflatex "$MAIN.tex"
