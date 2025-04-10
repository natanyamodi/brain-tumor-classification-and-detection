---
title: Cerebroscan-Brain Tumor Detection and Classification App
emoji: 🌖
colorFrom: yellow
colorTo: blue
sdk: gradio
sdk_version: 5.24.0
app_file: app.py
pinned: false
short_description: This app detects and classifies brain tumors in MRI scans
---

# 🧠 Brain Tumor Detection and Classification with YOLOv8
### A deep learning system for detecting and classifying brain tumors in MRI scans using YOLOv8, deployed as a Gradio web application.

![App Screenshot](https://github.com/user-attachments/assets/e8da60fd-5d15-4354-95cc-37789d4281db)

## 🌟 Features
- **Real-Time Detection**: Identifies tumor regions using bounding boxes.
- **Multi-class Classification**:
  - Glioma
  - Meningioma
  - Pituitary tumors
- **Interactive UI**: Upload images, view detections, and see confidence levels.
- **Lightweight & Fast**: Optimized using YOLOv8 for speed and accuracy.

## 🧪 Model Training

The model was trained using **Ultralytics YOLOv8** for brain tumor detection and classification. Training was performed in a **Kaggle notebook** with GPU support, and the complete workflow is documented in:

```
training/brain-tumor-classification-and-detection-yolov8.ipynb
```

You can follow this notebook to visualize the data, perform training, evaluate performance, and export the trained model weights.

### 💻 Training Environment

- **Platform**: Kaggle Notebook
- **Framework**: Ultralytics YOLOv8
- **Hardware**: Free GPU T4 x2 (via Kaggle)

### 🧠 Dataset Overview

The dataset was sourced from **Roboflow Universe**:  
🔗 [Roboflow Dataset - Brain Tumor](https://universe.roboflow.com/computer-vision-kbzhg/brain_tumor-gxibq/dataset/1)

The following were already applied on the dataset, so you can skip doing these steps.
**Preprocessing:**
- Auto-Orient: ✅
- Resize: Stretched to 640x640

**Augmentations:**
- Outputs per training example: 3
- Flip: Horizontal & Vertical ✅


### 🛠️ Train Your Own Model

To train your own model from scratch:

1. Download the dataset using the Roboflow code snippet:
   ```python
   !pip install roboflow
   from roboflow import Roboflow
   rf = Roboflow(api_key="your_api_key")
   project = rf.workspace("computer-vision-kbzhg").project("brain_tumor-gxibq")
   version = project.version(1)
   dataset = version.download("yolov8")
   ```

2. Run the cells in the notebook:
   ```
   training/brain-tumor-classification-and-detection-yolov8.ipynb
   ```

3. After training, you’ll find your model weights at:
   ```
   runs/detect/train/weights/best.pt
   ```

4. Download the `best.pt` file to the `models/` directory:
   ```
   models/best.pt
   ```

### ✅ Skip Training? Use Pretrained Weights

If you’d like to skip training and directly use a pretrained model:
- The `models/best.pt` file is already included in this repository.
- These weights were trained using the steps described above on the Roboflow dataset.


### 📊 YOLOv8 Evaluation Results

| Class             | Images | Instances | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|-------------------|--------|-----------|-----------|--------|--------|--------------|
| All Classes       | 1450   | 1467      | 0.977     | 0.965  | 0.987  | 0.915        |
| Glioma Tumor      | 472    | 487       | 0.966     | 0.922  | 0.974  | 0.882        |
| Meningioma Tumor  | 522    | 524       | 0.987     | 0.993  | 0.993  | 0.952        |
| Pituitary Tumor   | 456    | 456       | 0.979     | 0.980  | 0.993  | 0.912        |


## 🚀 Local Setup & Installation

To run the app locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/natanyamodi/brain-tumor-classification-and-detection.git
   ```
2. **Create a Virtual Environment**
   ```
   python -m venv venv
   venv/Scripts/activate  # or `source venv/bin/activate` on Mac
   ```
3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Run the App**
   ```
   python app.py
   ```
* You can now access the app at http://localhost:7860

## 🌐 Try it out
Use the interactive interface below to upload MRI scans and get instant predictions with confidence scores.

[🔗 Launch Cerebroscan in Browser](https://huggingface.co/spaces/natanyamodi/cerebroscan)

## 🔍 Intended Use
- Educational and demonstration purposes.
- Showcase of YOLOv8 in medical imaging.
- Assist developers and researchers exploring computer vision capabilities in healthcare and medical imaging research.

## 📌 Limitations
- Not suitable for clinical use.
- MRI quality, noise, and uncommon tumor types may impact accuracy.
- The model does not detect "no tumor" cases — it assumes one of the three tumor types if anything is detected.
- This tool is a research prototype and should never be used as a substitute for professional medical advice.

**Always consult a licensed radiologist or medical professional for diagnostic decisions.**

## 📂 Project Structure
```
cerebroscan/
├── training/
│ └── brain-tumor-classification-and-detection-yolov8.ipynb # Training notebook
├── models/
│ └── best.pt # Trained weights
├── images/ # Sample scans
│ ├── glioma.jpeg
│ ├── meningioma.jpeg
│ └── pituitary.jpeg
├── app.py # Gradio application
├── requirements.txt # Dependencies
└── README.md
```
