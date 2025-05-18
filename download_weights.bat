@echo off
echo Downloading YOLOv3 weights file...
mkdir main\weights 2>nul

powershell -Command "Invoke-WebRequest -Uri https://pjreddie.com/media/files/yolov3.weights -OutFile main\yolov3.weights"

if %ERRORLEVEL% EQU 0 (
    echo Weights file downloaded successfully to main\yolov3.weights
) else (
    echo Error downloading weights file. Please download manually from:
    echo https://pjreddie.com/media/files/yolov3.weights
    echo and place it in the main directory.
)

pause 