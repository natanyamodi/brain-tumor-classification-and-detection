---
title: Cerebroscan
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

![App Screenshot](https://github.com/user-attachments/assets/e8da60fd-5d15-4354-95cc-37789d4281db)

A deep learning system for detecting and classifying brain tumors in MRI scans using YOLOv8, deployed as a Gradio web application.

## 🌟 Features
- **Detection**: Fine-tuned YOLOv8 model for brain tumor identification
- **Multi-Class Classification**: Distinguishes between:
  - Glioma tumors
  - Meningioma tumors
  - Pituitary tumors
- **User-Friendly Interface**: Clean Gradio web interface with:
  - Image upload functionality
  - Sample test cases
  - Real-time visualization
- **Confidence Scoring**: Displays prediction confidence levels

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

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/natanyamodi/brain-tumor-classification-and-detection.git
cd cerebroscan
pip install -r requirements.txt
```

### 2. Run the Web App
```
python app.py
```

## 🎖️ Try it out
Use the interactive interface below to upload MRI scans and get instant predictions with confidence scores.
[cerebroscan](https://huggingface.co/spaces/natanyamodi/cerebroscan)
