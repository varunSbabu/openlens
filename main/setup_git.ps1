# OpenLens Git Setup Script

Write-Host "===== OpenLens Git Setup =====" -ForegroundColor Cyan

# Check if Git is installed
try {
    $gitVersion = git --version
    Write-Host "Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "Git is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/downloads" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Initialize Git repository
Write-Host "Initializing Git repository..." -ForegroundColor Cyan
git init .

# Configure Git locally
Write-Host "Setting up local Git configuration..." -ForegroundColor Cyan
git config --local user.name "Varun"
git config --local user.email "your.email@example.com"

# Add files to Git
Write-Host "Adding files to Git..." -ForegroundColor Cyan
git add .

# Commit changes
Write-Host "Committing changes..." -ForegroundColor Cyan
git commit -m "Initial commit for OpenLens project"

# Add remote repository
Write-Host "Adding remote repository..." -ForegroundColor Cyan
git remote add origin https://github.com/varunSbabu/OpenLense.git

Write-Host "===== Setup Complete =====" -ForegroundColor Green
Write-Host ""
Write-Host "Your repository has been initialized and files committed." -ForegroundColor White
Write-Host ""
Write-Host "To push to GitHub, run:" -ForegroundColor Yellow
Write-Host "git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "Make sure you have access rights to the repository." -ForegroundColor Yellow
Read-Host "Press Enter to exit" 