$ErrorActionPreference = "Stop"
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Installer = Join-Path $Here "installer\aiverse_skills.py"

$Python = Get-Command python -ErrorAction SilentlyContinue
if (-not $Python) {
    $Python = Get-Command py -ErrorAction SilentlyContinue
    if (-not $Python) {
        throw "Python 3 is required to run AI-Verse Skills."
    }
    & $Python.Source -3 $Installer @args
    exit $LASTEXITCODE
}

& $Python.Source $Installer @args
exit $LASTEXITCODE
