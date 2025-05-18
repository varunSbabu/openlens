#!/usr/bin/env python3
"""
Download YOLOv8 weights and convert to appropriate format for OpenCV.
"""

import os
import sys
from pathlib import Path

def main():
    try:
        # Check if ultralytics is installed
        import ultralytics
    except ImportError:
        print("Error: Ultralytics package not found.")
        print("Please install it first: pip install ultralytics")
        sys.exit(1)
    
    from ultralytics import YOLO
    
    print("Downloading YOLOv8n model...")
    
    # Create weights directory if it doesn't exist
    weights_dir = Path("weights")
    weights_dir.mkdir(exist_ok=True)
    
    # Download and export YOLOv8 model
    try:
        # Download YOLOv8n (nano) model
        model = YOLO("yolov8n.pt")
        
        # Export to ONNX format
        print("Converting to ONNX format...")
        success = model.export(format="onnx")
        
        if success:
            print(f"Model exported successfully to {success}")
            
            # Copy to main directory for compatibility with main.py
            import shutil
            source_path = Path("yolov8n.onnx")
            if source_path.exists():
                shutil.copy(source_path, ".")
                print(f"Copied {source_path} to current directory")
            
            print("\nNOTE: To use with OpenCV, you may need to convert the ONNX model to a format compatible with cv2.dnn.")
            print("For best results, consider using the ultralytics package directly in your code.")
        else:
            print("Failed to export model")
    except Exception as e:
        print(f"Error downloading or exporting model: {e}")
        sys.exit(1)
    
    print("\nSetup complete!")

if __name__ == "__main__":
    main() 