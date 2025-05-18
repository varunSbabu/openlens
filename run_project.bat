@echo off
echo ===== OpenLens Project Runner =====
echo.
echo This script will navigate to the main directory and run the OpenLens project.
echo.
echo Choose an option:
echo 1. Run main.py (Command-line interface)
echo 2. Run streamlit_app.py (Web interface)
echo 3. Exit
echo.

set /p option="Enter your choice (1-3): "

cd main

if "%option%"=="1" (
    echo.
    echo Running main.py...
    echo.
    python main.py
) else if "%option%"=="2" (
    echo.
    echo Running streamlit_app.py...
    echo.
    streamlit run streamlit_app.py
) else if "%option%"=="3" (
    echo.
    echo Exiting...
    exit /b 0
) else (
    echo.
    echo Invalid option. Please run the script again and choose a valid option.
    exit /b 1
)

pause 