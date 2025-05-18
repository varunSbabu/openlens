#!/bin/bash

echo "Downloading YOLOv3 weights file..."
mkdir -p main/weights
wget -O main/yolov3.weights https://pjreddie.com/media/files/yolov3.weights

echo "Weights file downloaded successfully to main/yolov3.weights" 