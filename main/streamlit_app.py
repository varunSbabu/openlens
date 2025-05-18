import streamlit as st
import cv2
import numpy as np
import openai
import os
from dotenv import load_dotenv
from PIL import Image
import tempfile
import time

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Open Lens - AI Object Detection & Description",
    page_icon="🔍",
    layout="wide"
)

# OpenAI API credentials
api_key = os.getenv('OPENAI_API_KEY')
if not api_key or api_key == "your_openai_api_key_here":
    st.warning("Using dummy OpenAI responses for testing as no valid API key was provided. To use real OpenAI responses, set your OPENAI_API_KEY in the .env file")
    USE_DUMMY_RESPONSES = True
else:
    # Initialize OpenAI client
    openai.api_key = api_key
    USE_DUMMY_RESPONSES = False

# Check for YOLO model files
if os.path.exists("yolov8.weights") and os.path.exists("yolov8.cfg"):
    weights_file = "yolov8.weights"
    config_file = "yolov8.cfg"
elif os.path.exists("yolov3.weights") and os.path.exists("yolov3.cfg"):
    weights_file = "yolov3.weights"
    config_file = "yolov3.cfg"
else:
    st.error("YOLO model files not found. Please check the README for setup instructions.")
    st.stop()

# Load COCO class names
classes = []
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Function to get output layers
def get_output_layers(net):
    layer_names = net.getLayerNames()
    try:
        # OpenCV 4.5.4+
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    except:
        # Older OpenCV versions
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

# Function to draw bounding boxes
def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    color = (0, 255, 0)  # Green color for bounding boxes
    cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)
    cv2.putText(img, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return label

# Function to generate text using OpenAI API
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
        with st.spinner("Generating description..."):
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

# Function to process image
def process_image(image):
    # Load YOLO model
    net = cv2.dnn.readNet(weights_file, config_file)
    
    # Convert PIL Image to OpenCV format
    img = np.array(image)
    img = img[:, :, ::-1].copy()  # RGB to BGR
    
    height, width = img.shape[:2]
    
    # Create a blob from the image
    blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    
    # Perform object detection
    outs = net.forward(get_output_layers(net))
    
    # Initialize lists
    class_ids = []
    confidences = []
    boxes = []
    detected_objects = []
    
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
    
    # Apply non-maximum suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    
    # Draw bounding boxes
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = draw_prediction(img, class_ids[i], confidences[i], x, y, x + w, y + h)
            detected_objects.append(label)
    
    # Convert back to RGB for PIL
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result_image = Image.fromarray(img_rgb)
    
    return result_image, detected_objects

# Main Streamlit UI
st.title("🔍 Open Lens")
st.subheader("AI-Powered Object Detection & Description")

# Sidebar
st.sidebar.title("Options")
input_option = st.sidebar.radio("Select Input Source", ["Upload Image", "Webcam Capture"])

if input_option == "Upload Image":
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Process the uploaded image
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original Image")
            st.image(image, use_column_width=True)
        
        with col2:
            st.subheader("Processed Image")
            with st.spinner("Processing image..."):
                result_image, detected_objects = process_image(image)
                st.image(result_image, use_column_width=True)
        
        # Generate and display text
        if detected_objects:
            st.subheader("Detected Objects")
            st.write(", ".join(detected_objects))
            
            if st.button("Generate Description"):
                description = generate_text(detected_objects)
                st.subheader("AI Description")
                st.write(description)
        else:
            st.info("No objects detected in the image.")

elif input_option == "Webcam Capture":
    st.warning("Note: Webcam capture in Streamlit has some limitations and may not work on all systems.")
    
    if st.button("Take Photo"):
        # Use Streamlit's camera_input
        camera_image = st.camera_input("Take a photo")
        
        if camera_image is not None:
            # Process the camera image
            image = Image.open(camera_image)
            
            with st.spinner("Processing image..."):
                result_image, detected_objects = process_image(image)
                
                st.subheader("Processed Image")
                st.image(result_image, use_column_width=True)
                
                # Generate and display text
                if detected_objects:
                    st.subheader("Detected Objects")
                    st.write(", ".join(detected_objects))
                    
                    if st.button("Generate Description"):
                        description = generate_text(detected_objects)
                        st.subheader("AI Description")
                        st.write(description)
                else:
                    st.info("No objects detected in the image.")

# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    "Open Lens is an AI project that combines computer vision (YOLOv8) "
    "and natural language processing (GPT-3.5) to detect objects and generate descriptions."
)
st.sidebar.markdown("© 2023 Open Lens Project | [GitHub](https://github.com)") 