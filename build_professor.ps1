$MAIN = "Professor_Draft"
$PDF = "$MAIN.pdf"
$ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path
$CLEANUP_SCRIPT = Join-Path $ROOT "cleanup_build.ps1"

function Invoke-BuildCleanup {
  if (Test-Path -LiteralPath $CLEANUP_SCRIPT) {
    & $CLEANUP_SCRIPT
    if (-not $?) {
      exit 1
    }
  }
}

function Close-PdfViewerForFile {
  param([string]$FileName)

  $escapedName = [regex]::Escape($FileName)
  $viewerNames = @(
    "Acrobat",
    "AcroRd32",
    "SumatraPDF",
    "FoxitPDFReader",
    "PDFXEdit"
  )

  Get-Process -ErrorAction SilentlyContinue |
    Where-Object {
      $viewerNames -contains $_.ProcessName -and
      ($_.MainWindowTitle -match $escapedName -or $_.MainWindowTitle -match "Professor_Draft")
    } |
    ForEach-Object {
      $null = $_.CloseMainWindow()
      if (-not $_.WaitForExit(3000)) {
        Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
      }
    }
}

function Test-FileLocked {
  param([string]$Path)

  if (-not (Test-Path $Path)) {
    return $false
  }

  try {
    $stream = [System.IO.File]::Open($Path, "Open", "ReadWrite", "None")
    $stream.Close()
    return $false
  } catch {
    return $true
  }
}

function Remove-BuildOutputs {
  param([string]$BaseName)

  Remove-Item -Force -ErrorAction SilentlyContinue `
    "$BaseName.aux", `
    "$BaseName.bbl", `
    "$BaseName.blg", `
    "$BaseName.log", `
    "$BaseName.out", `
    "$BaseName.toc", `
    "$BaseName.lof", `
    "$BaseName.lot", `
    "$BaseName.pdf", `
    "$BaseName.synctex.gz"
}

function Open-PdfInVSCode {
  param([string]$Path)

  $codeCommand = Get-Command code.cmd -ErrorAction SilentlyContinue
  if (-not $codeCommand) {
    $codeCommand = Get-Command code -ErrorAction SilentlyContinue
  }

  $codeExeCandidates = @(
    "$env:LOCALAPPDATA\Programs\Microsoft VS Code\Code.exe",
    "$env:ProgramFiles\Microsoft VS Code\Code.exe"
  )
  $codeExe = $codeExeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1

  if ($codeCommand) {
    Write-Host "Opening $Path in VS Code."
    Start-Process -FilePath $codeCommand.Source -ArgumentList @("--reuse-window", $Path)
  } elseif ($codeExe) {
    Write-Host "Opening $Path in VS Code."
    Start-Process -FilePath $codeExe -ArgumentList @("--reuse-window", $Path)
  } else {
    Write-Host "VS Code command 'code' was not found. Opening with the default PDF application."
    Start-Process -FilePath $Path
  }
}

Close-PdfViewerForFile $PDF
Invoke-BuildCleanup

$buildMain = $MAIN
if (Test-FileLocked $PDF) {
  $stamp = Get-Date -Format "yyyyMMdd_HHmmss"
  $buildMain = "${MAIN}_current_$stamp"
  Write-Host "$PDF is locked by a PDF viewer. Building $buildMain.pdf instead."
} else {
  Remove-BuildOutputs $MAIN
}

# Clean old timestamped draft builds when they are not open.
Get-ChildItem -File -Filter "${MAIN}_current_*.pdf" -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -ne "$buildMain.pdf" -and -not (Test-FileLocked $_.FullName) } |
  Remove-Item -Force -ErrorAction SilentlyContinue

Remove-BuildOutputs $buildMain

pdflatex "-interaction=nonstopmode" "-halt-on-error" "-jobname=$buildMain" "$MAIN.tex"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$aux = Get-Content "$buildMain.aux" -Raw
if ($aux.Contains('\citation') -and $aux.Contains('\bibdata')) {
  bibtex $buildMain
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

pdflatex "-interaction=nonstopmode" "-halt-on-error" "-jobname=$buildMain" "$MAIN.tex"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

pdflatex "-interaction=nonstopmode" "-halt-on-error" "-jobname=$buildMain" "$MAIN.tex"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$builtPdf = (Resolve-Path "$buildMain.pdf").ProviderPath
Invoke-BuildCleanup
Open-PdfInVSCode $builtPdf
