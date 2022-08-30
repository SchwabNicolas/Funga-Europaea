$venv = $PSScriptRoot + '\.venv\Scripts'
$piptools = $PSScriptRoot + '\.venv\Lib\piptools\__ini__.py'
$activate = $venv + '\activate.ps1'
$deactivate = $venv + '\deactivate.bat'

if (Test-Path -Path $venv) {
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
        "Package pip-tools is missing. Please install it with " + $venv + 'pip.exe install -m pip-tools'
    }
} else {
    "Virtual environment doesn't exist."
}