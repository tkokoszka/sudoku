# PowerShell 7 script to runs pre-commit checks.
# Meant for local manual usage. Execute it before doing commit or creating Pull Request, run from the project
# directory, i.e.:
# $ script\pre-commit.ps1

# Check if running from proper directory location.
if (-not (Test-Path -Path 'scripts' -PathType Container)) {
    Write-Error "This script must be run from the project root directory."
    exit 1
}

# Runs the command or dies, e.g.:
#   RunOrDie pip install "-r" backend\requirements.txt
# Caveat1: switches (i.e. "-name") must be wrapped in quotes. PowerShell insterprets arguments starting with
#          - (dash) as a switches and does not pass them to (ValueFromRemainingArguments). The only way around I
#          found is to wrap those in quotes.
function RunOrDie {
    param (
        [Parameter(ValueFromRemainingArguments=$true)]
        [string[]]$Cmd
    )
    Write-Output "================================================================================================"
    Write-Output "== $Cmd"
    Invoke-Expression $($Cmd -join " ")
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Command '$Cmd' failed"
        deactivate
        exit 1
    }
}

venv\Scripts\activate
RunOrDie pre-commit run "--all-files"
deactivate

Write-Output "All pre-commit checks completed."
