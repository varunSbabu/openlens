Write-Host "===== OpenLens Project Runner =====" -ForegroundColor Cyan
Write-Host ""
Write-Host "This script will navigate to the main directory and run the OpenLens project."
Write-Host ""
Write-Host "Choose an option:" -ForegroundColor Yellow
Write-Host "1. Run main.py (Command-line interface)"
Write-Host "2. Run streamlit_app.py (Web interface)"
Write-Host "3. Exit"
Write-Host ""

$option = Read-Host "Enter your choice (1-3)"

Set-Location -Path "main"

switch ($option) {
    "1" {
        Write-Host ""
        Write-Host "Running main.py..." -ForegroundColor Green
        Write-Host ""
        python main.py
    }
    "2" {
        Write-Host ""
        Write-Host "Running streamlit_app.py..." -ForegroundColor Green
        Write-Host ""
        streamlit run streamlit_app.py
    }
    "3" {
        Write-Host ""
        Write-Host "Exiting..." -ForegroundColor Yellow
        exit 0
    }
    default {
        Write-Host ""
        Write-Host "Invalid option. Please run the script again and choose a valid option." -ForegroundColor Red
        exit 1
    }
}

Read-Host "Press Enter to exit" 