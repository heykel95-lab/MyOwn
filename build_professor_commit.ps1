[CmdletBinding()]
param(
  [string]$Message,
  [switch]$Push
)

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$BuildScript = Join-Path $Root "build_professor.ps1"

& $BuildScript
if ($LASTEXITCODE -ne 0) {
  exit $LASTEXITCODE
}

$status = git -C $Root status --porcelain
if (-not $status) {
  Write-Host "Build succeeded. No saved Git changes to commit."
  exit 0
}

git -C $Root add -A
if ($LASTEXITCODE -ne 0) {
  exit $LASTEXITCODE
}

$status = git -C $Root status --porcelain
if (-not $status) {
  Write-Host "Build succeeded. No saved Git changes to commit."
  exit 0
}

if (-not $Message) {
  $stamp = Get-Date -Format "yyyy-MM-dd HH:mm"
  $Message = "Build professor draft $stamp"
}

git -C $Root commit -m $Message
if ($LASTEXITCODE -ne 0) {
  exit $LASTEXITCODE
}

if ($Push) {
  git -C $Root push
  if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
  }
}
