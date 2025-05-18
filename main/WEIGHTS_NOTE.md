# Note About YOLOv3 Weights

The YOLOv3 weights file (`yolov3.weights`) is a large file (approximately 237MB) and is not included in the Git repository. 

## Options to Get the Weights File

1. **Use the download_weights.py script**:
   ```bash
   python download_weights.py
   ```
   This will download YOLOv8 weights and convert them to the appropriate format.

2. **Download YOLOv3 weights manually**:
   ```bash
   # Download YOLOv3 weights
   curl -L https://pjreddie.com/media/files/yolov3.weights -o yolov3.weights
   ```

3. **Copy from another location**:
   If you already have the weights file in another location, simply copy it to the project root directory.

The application is configured to look for the weights file in the project root directory. 