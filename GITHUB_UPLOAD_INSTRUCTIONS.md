# GitHub Upload Instructions

Since there seems to be an issue with Git configuration on your system, here are two alternative methods to upload your project to GitHub:

## Method 1: Using GitHub Desktop

1. Download and install [GitHub Desktop](https://desktop.github.com/) if you haven't already
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

**Note**: If your project is large (especially with the YOLOv3 weights file), you might want to add the weights file to your `.gitignore` and provide instructions in your README on how to download it instead.

## Recommended Structure for Upload

Make sure to maintain the current project structure:
- Root directory: Contains runner scripts and README
- `main/` directory: Contains all the core project files

This structure makes it easy for users to run your project while keeping all the implementation details organized. 