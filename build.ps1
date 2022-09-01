$venv = $PSScriptRoot + '\.venv\Scripts'
$manage = $PSScriptRoot + '\manage.py'
$activate = $venv + '\activate.ps1'
$deactivate = $venv + '\deactivate.bat'

# Check if required files are present
if (Test-Path -Path $venv) {
    if (Test-Path -Path $manage) {
        # Activate environment
        & $activate

        # Build Tailwind CSS
        python .\manage.py tailwind build

        # Deactivate environment
        & $deactivate
    } else {
        "Couldn't locate manage.py file. Please check if Django is installed."
    }
} else {
    "Virtual environment doesn't exist."
}