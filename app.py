import gradio as gr
from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("models/best.pt") 
class_labels = ["glioma", "meningioma", "pituitary"]
# print(model.names)

def predict(input_img):
    # Convert PIL image to OpenCV format
    image_cv = np.array(input_img)
    image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)
    
    # Run prediction
    results = model.predict(source=image_cv, conf=0.5)
    boxes = results[0].boxes
    
    if boxes is not None and boxes.data.shape[0] > 0:
        # Draw bounding boxes
        for box in boxes.data:
            x1, y1, x2, y2 = map(int, box[:4])
            class_id = int(box[5])
            confidence = float(box[4])
            label = class_labels[class_id]
            
            cv2.rectangle(image_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        image_annotated = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
        return image_annotated, {label:confidence}
    else:
        return input_img, {"No tumor detected": 1.0}
    

css = """
.gradio-share-link-button-0 {display: none !important}
"""

brain_app = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload Brain MRI Scan"),
    outputs=[
        gr.Image(label="Detection Results"), 
        gr.Label(label="Confidence Scores")
    ],
    title="🧠 Brain Tumor Detection and Classification",
    description="""This app detects and classifies brain tumors in MRI scans.
    Upload an image or try the examples below.""",
    examples=[
        "images/glioma.jpeg",
        "images/meningioma.jpeg",
        "images/pituitary.jpeg"
    ],
    flagging_mode="never",
    css=css
)

if __name__ == '__main__':
    brain_app.launch(share=False)