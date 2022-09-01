$venv = $PSScriptRoot + '\.venv\Scripts'
$piptools = $PSScriptRoot + '\.venv\Lib\piptools\__ini__.py'
$activate = $venv + '\activate.ps1'
$deactivate = $venv + '\deactivate.bat'

# Check if required files are present
if (Test-Path -Path $venv) {
    if (Test-Path -Path $piptools) {
        $common = $PSScriptRoot + '\requirements\common.in'
        $dev = $PSScriptRoot + '\requirements\dev.in'
        $prod = $PSScriptRoot + '\requirements\prod.in'
        $requirements = $PSScriptRoot + '\requirements.in'

        # Activate environment
        & $activate

        # Compile all requirements files
        python -m piptools compile $($common)
        python -m piptools compile $($dev)
        python -m piptools compile $($prod)
        python -m piptools compile $($requirements)

        # Deactivate environment
        & $deactivate
    } else {
        "Package pip-tools is missing. Please install it with " + $venv + "pip.exe install -m pip-tools"
    }
} else {
    "Virtual environment doesn't exist."
}