# Regenerates each CLAUDE.md from the AGENTS.md beside it, so both files carry
# the identical rule set and neither has to be updated by hand.
#
# AGENTS.md is the file to edit. CLAUDE.md is overwritten from it, here and by
# the pre-commit hook in .githooks/.
#
# .NET file I/O is used rather than Get-Content/Set-Content because Windows
# PowerShell 5.1 reads UTF-8 as the ANSI codepage by default, which corrupts
# every em dash, times sign and Greek letter in these files.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

$pairs = @(
    @{ Source = "AGENTS.md";      Target = "CLAUDE.md" },
    @{ Source = "code/AGENTS.md"; Target = "code/CLAUDE.md" }
)

$changed = @()

foreach ($pair in $pairs) {
    $source = Join-Path $root $pair.Source
    $target = Join-Path $root $pair.Target

    if (-not (Test-Path $source)) {
        Write-Error "missing source: $($pair.Source)"
    }

    $banner = "<!-- GENERATED FILE - DO NOT EDIT.`n" +
              "     Regenerated from $($pair.Source) by sync_agent_docs.ps1 and by the`n" +
              "     pre-commit hook. Edit $($pair.Source) instead; any change made here`n" +
              "     is overwritten on the next commit. The two files are kept identical`n" +
              "     so that an agent reading either one gets the same rules. -->`n`n"

    $body = [System.IO.File]::ReadAllText($source)
    $new = $banner + $body

    $old = if (Test-Path $target) { [System.IO.File]::ReadAllText($target) } else { "" }

    if ($old -ne $new) {
        [System.IO.File]::WriteAllText($target, $new, $utf8NoBom)
        $changed += $pair.Target
    }
}

if ($changed.Count -gt 0) {
    Write-Host "synced: $($changed -join ', ')"
} else {
    Write-Host "already in sync"
}
