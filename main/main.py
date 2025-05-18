import cv2
import numpy as np
import openai
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API credentials
api_key = os.getenv('OPENAI_API_KEY')
if not api_key or api_key == "your_openai_api_key_here":
    print("Warning: Using dummy OpenAI responses for testing as no valid API key was provided.")
    print("To use real OpenAI responses, set your OPENAI_API_KEY in the .env file")
    USE_DUMMY_RESPONSES = True
else:
    # Initialize OpenAI client
    openai.api_key = api_key
    USE_DUMMY_RESPONSES = False

# Check if YOLO weights and config files exist
if not os.path.exists("yolov8.weights"):
    print("Warning: yolov8.weights file not found. Using yolov3.weights instead.")
    weights_file = "yolov3.weights"
    config_file = "yolov3.cfg"
else:
    weights_file = "yolov8.weights"
    config_file = "yolov8.cfg"

# Loading the YOLO model
net = cv2.dnn.readNet(weights_file, config_file)

# Loading the names of classes
classes = []
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Get output layer names
def get_output_layers(net):
    layer_names = net.getLayerNames()
    try:
        # OpenCV 4.5.4+
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    except:
        # Older OpenCV versions
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

# Draw prediction bounding box
def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    color = (0, 255, 0)  # Green color for bounding boxes
    cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)
    cv2.putText(img, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return label

# Generate text using OpenAI API
def generate_text(objects_list):
    if not objects_list:
        return "No objects detected."
    
    # Remove duplicates while preserving order
    unique_objects = []
    for obj in objects_list:
        if obj not in unique_objects:
            unique_objects.append(obj)
    
    # Create a prompt for GPT
    objects_str = ", ".join(unique_objects)
    
    if USE_DUMMY_RESPONSES:
        # Provide a dummy response for testing without API key
        return f"Detected objects: {objects_str}. This is a dummy response for testing without an OpenAI API key."
    
    try:
        prompt = f"I can see the following objects in my camera: {objects_str}. Please provide a brief description or interesting facts about these objects."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides concise and interesting information about objects detected by a computer vision system."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating text: {str(e)}"

def main():
    # Set up the video capture
    cap = cv2.VideoCapture(0)  # 0 for the default camera
    
    if not cap.isOpened():
        print("Error: Could not open video capture device.")
        return
    
    # Initialize variables
    detected_objects = []
    
    print("Press 's' to stop detection and generate text about detected objects")
    print("Press 'q' to quit without generating text")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
            
        # Get the frame's height and width
        height, width = frame.shape[:2]
        
        # Create a blob from the frame and set it as the input for YOLO
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        
        # Perform object detection
        outs = net.forward(get_output_layers(net))
        
        # Initializing lists to store detected class IDs, confidences, and bounding boxes
        class_ids = []
        confidences = []
        boxes = []
        
        # Process the outputs
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > 0.5:  # Only consider detections with confidence > 0.5
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    
                    # Calculate the top-left coordinates of the bounding box
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])
        
        # Apply non-maximum suppression to remove overlapping boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        
        # Draw bounding boxes and collect detected objects
        frame_objects = []
        
        if len(indices) > 0:
            for i in indices.flatten():
                x, y, w, h = boxes[i]
                label = draw_prediction(frame, class_ids[i], confidences[i], x, y, x + w, y + h)
                frame_objects.append(label)
        
        # Add detected objects to the list
        detected_objects.extend(frame_objects)
        
        # Display the frame with object detection
        cv2.imshow("Object Detection", frame)
        
        # Check for keypress
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            print("Generating text for detected objects...")
            generated_text = generate_text(detected_objects)
            print("\nGenerated Information:")
            print(generated_text)
            
            # Save the last frame with detections
            cv2.imwrite("output_detection.jpg", frame)
            print("Last frame saved as 'output_detection.jpg'")
            break
        elif key == ord('q'):
            print("Quitting without generating text")
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 