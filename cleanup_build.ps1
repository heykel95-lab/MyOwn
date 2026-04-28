[CmdletBinding(SupportsShouldProcess = $true)]
param(
  [switch]$RemoveGeneratedPdfs,
  [switch]$KeepLogs
)

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Workspace = (Resolve-Path $Root).ProviderPath
$Separator = [System.IO.Path]::DirectorySeparatorChar

function Get-SafeRootFiles {
  param([string[]]$Patterns)

  foreach ($pattern in $Patterns) {
    Get-ChildItem -LiteralPath $Workspace -File -Filter $pattern -ErrorAction SilentlyContinue |
      Where-Object { $_.FullName.StartsWith($Workspace + $Separator) }
  }
}

$extensions = @(
  "aux",
  "bbl",
  "bcf",
  "blg",
  "fdb_latexmk",
  "fls",
  "lof",
  "log",
  "lot",
  "out",
  "run.xml",
  "synctex.gz",
  "toc"
)

if ($KeepLogs) {
  $extensions = $extensions | Where-Object { $_ -ne "log" }
}

$buildBases = @(
  "Thesis",
  "Thesis_*",
  "Professor_Draft",
  "Professor_Draft_*"
)

$artifactPatterns = foreach ($base in $buildBases) {
  foreach ($extension in $extensions) {
    "$base.$extension"
  }
}

$files = @(Get-SafeRootFiles $artifactPatterns)

if ($RemoveGeneratedPdfs) {
  $generatedPdfPatterns = @(
    "Thesis_*.pdf",
    "Thesis*_preview.pdf",
    "Professor_Draft_*.pdf"
  )

  $files += Get-SafeRootFiles $generatedPdfPatterns |
    Where-Object { $_.Name -notin @("Thesis.pdf", "Professor_Draft.pdf") }
}

$files = @($files | Sort-Object FullName -Unique)

if ($files.Count -eq 0) {
  Write-Host "No LaTeX build artifacts found."
  return
}

Write-Host "Cleaning $($files.Count) LaTeX build artifact(s)."
foreach ($file in $files) {
  if ($PSCmdlet.ShouldProcess($file.FullName, "Remove")) {
    Remove-Item -LiteralPath $file.FullName -Force
  }
}
