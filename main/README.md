# Open Lens: AI-Powered Object Detection and Description

Open Lens is a computer vision and natural language processing project that uses YOLOv8 for real-time object detection from a webcam feed and GPT-3.5 to generate descriptive text about the detected objects.

## Features

- Real-time object detection using YOLOv8/YOLOv3
- Visual display with bounding boxes and confidence scores
- Natural language descriptions of detected objects using OpenAI's GPT-3.5
- Simple keyboard controls for interaction
- Automatic saving of detection results
- Optional Streamlit web interface

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Webcam (for real-time detection)
- OpenAI API key (for generating descriptions)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/varunSbabu/OpenLense.git
   cd OpenLense
   ```

2. Download the YOLOv3 weights file:
   - On Windows: Run `download_weights.bat` in the root directory
   - On Linux/Mac: Run `./download_weights.sh` in the root directory
   - Or download manually from https://pjreddie.com/media/files/yolov3.weights and place in the `main` directory

3. Install the required packages:
   ```bash
   cd main
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the `main` directory with the following content:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## How to Run

### Command-line Interface

Run the main script:
```bash
python main.py
```

#### Controls
- Press 's' to stop detection and generate text about the detected objects
- Press 'q' to quit without generating text

### Streamlit Web Interface

Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

This provides a user-friendly web interface with:
- Image upload option
- Webcam capture option
- Object detection visualization
- Text generation for detected objects

## Project Structure

For details about the project structure and file descriptions, see [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md).

## Sample Output

When objects are detected, the program will:
1. Display the webcam feed with bounding boxes around detected objects
2. When you press 's', it will generate a description of the detected objects using GPT-3.5
3. Save the last frame with detections as `output_detection.jpg`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 