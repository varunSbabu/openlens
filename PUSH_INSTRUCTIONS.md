# Instructions for Pushing OpenLens to GitHub

Since there was an issue with Git configuration on your system, I've prepared two methods for you to push your project to GitHub:

## Method 1: Using GitHub Desktop (Recommended)

1. Download and install [GitHub Desktop](https://desktop.github.com/)
2. Open GitHub Desktop and sign in with your GitHub account
3. Click on "File" > "Add local repository"
4. Browse to your project folder: `D:/openlens/openlens`
5. Click "Add Repository"
6. You'll see all your changes in the left panel
7. Add a summary (commit message) like "Initial commit of OpenLens project"
8. Click "Commit to main"
9. Click "Publish repository" at the top
10. Make sure the repository name is "OpenLense" and the GitHub account is "varunSbabu"
11. Click "Publish Repository"

## Method 2: Manual Upload via GitHub Website

1. Go to your repository: https://github.com/varunSbabu/OpenLense
2. Click on "Add file" > "Upload files"
3. Drag and drop all files from your project directory, or click "choose your files" to select them
4. Add a commit message like "Initial commit of OpenLens project"
5. Click "Commit changes"

## Important Notes

1. The large weights file (yolov3.weights) is excluded in the .gitignore file to avoid uploading large files to GitHub
2. Users can download the weights file using the provided scripts (download_weights.bat or download_weights.sh)
3. Make sure to maintain the current project structure:
   - Root directory: Contains runner scripts and README
   - `main/` directory: Contains all the core project files

## Files Ready for Upload

1. Project code files in the `main/` directory
2. Runner scripts (run_project.bat and run_project.ps1) in the root directory
3. Weight download scripts (download_weights.bat and download_weights.sh) in the root directory
4. README.md files with clear instructions
5. .gitignore files to exclude large binary files and virtual environments

Good luck with your project! 