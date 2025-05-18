# Project Structure

```
OpenLense/
├── main.py                 # Main script for webcam-based object detection
├── streamlit_app.py        # Streamlit web interface
├── download_weights.py     # Script to download YOLOv8 weights
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables file
├── .env                    # Environment variables file (not in version control)
├── .gitignore              # Git ignore file
├── LICENSE                 # MIT License
├── README.md               # Project documentation
├── PROJECT_STRUCTURE.md    # This file, explaining the project structure
├── coco.names              # COCO dataset class names
├── yolov3.cfg              # YOLOv3 configuration file
├── weights/                # Directory for storing model weights
│   └── (model files)       # Downloaded model files
└── setup_git.ps1           # PowerShell script for Git setup
```

## File Descriptions

### Core Files
- **main.py**: The main Python script that uses OpenCV to access the webcam, YOLOv8/YOLOv3 for object detection, and OpenAI's GPT-3.5 for generating descriptions of detected objects.
- **streamlit_app.py**: A web interface built with Streamlit that provides a user-friendly way to interact with the object detection and description functionality.
- **download_weights.py**: Helper script to download and prepare YOLOv8 weights.

### Configuration Files
- **requirements.txt**: Lists all Python package dependencies.
- **.env.example**: Template for the .env file where users should add their OpenAI API key.
- **.env**: Contains the actual OpenAI API key (not committed to version control).
- **coco.names**: List of object classes that the YOLO model can detect.
- **yolov3.cfg**: Configuration file for the YOLOv3 model.

### Documentation
- **README.md**: Main documentation file with setup instructions and usage information.
- **LICENSE**: MIT License file.
- **PROJECT_STRUCTURE.md**: This file, explaining the project structure.

### Other
- **setup_git.ps1**: PowerShell script to initialize a Git repository for the project.
- **weights/**: Directory to store model weight files.
- **output_detection.jpg**: Sample output image generated when running the application (will be created when the app is run). 