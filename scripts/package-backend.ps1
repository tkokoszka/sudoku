# PowerShell 7 script to package the backend for deploying on AWS Lambda as .zip.
# Meant for local manual usage, run from the project directory, i.e.:
# $ script\package-backend.ps1

# Check if running from proper directory location.
if (-not (Test-Path -Path 'scripts' -PathType Container)) {
    Write-Error "This script must be run from the project root directory."
    exit 1
}

# Based on https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

$outDir = "out\backend"
$outPackageFile = "out\backend_deploy.zip"

# Preare the directory:
Remove-Item -Path "$outDir" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "$outPackageFile" -Force -ErrorAction SilentlyContinue
New-Item -Path "$outDir" -Force -ItemType Directory

# Copy the source.
Copy-Item -Path "backend\src\*.py" -Destination "$outDir\"

# Install packages.
pip install -r "backend\requirements.txt" --target "$outDir\"

# Create zip package.
Compress-Archive -Path "$outDir\*" -DestinationPath "$outPackageFile"

Write-Output "Backend package created: $outPackageFile"
