$venv = $PSScriptRoot + '\.venv\Scripts'
$activate = $venv + '\activate.ps1'
$deactivate = $venv + '\deactivate.bat'

if (Test-Path -Path $venv) {
    $common = $PSScriptRoot + '\requirements\common.in'
    $dev = $PSScriptRoot + '\requirements\dev.in'
    $prod = $PSScriptRoot + '\requirements\prod.in'
    $requirements = $PSScriptRoot + '\requirements.in'

    & $activate

    python -m piptools compile $($common)
    python -m piptools compile $($dev)
    python -m piptools compile $($prod)
    python -m piptools compile $($requirements)

    & $deactivate
} else {
    "Virtual environment doesn't exist."
}