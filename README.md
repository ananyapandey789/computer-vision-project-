# Automated Computer Vision & Report Generation Pipeline

An end-to-end Python application for image preprocessing, object detection, face detection, image analysis, and automated Markdown report generation.

## Features
- **Preprocessing:** Resizing, normalization, noise reduction, and contrast enhancement.
- **Object Detection:** Detect objects within images using modern computer vision workflows.
- **Face Detection:** Identify and locate faces within image inputs.
- **Image Analysis:** Calculate brightness, contrast, aspect ratios, and color histograms.
- **Report Generation:** Automatically aggregate analysis results into structured Markdown reports.
- **Architecture & Diagrams:** Includes architecture, class, sequence, use case, and workflow documentation.

## Project Structure
```
.
├── README.md
├── requirements.txt
├── main.py
├── statement.md
├── diagrams/
│   ├── architecture.md
│   ├── class_diagram.md
│   ├── use_case.md
│   ├── sequence.md
│   └── workflow.md
├── input/
│   └── README.txt
├── models/
│   └── README.txt
├── output/
│   └── .gitkeep
├── report/
│   └── REPORT_CONTENT.md
├── modules/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── object_detection.py
│   ├── face_detection.py
│   ├── image_analysis.py
│   └── report_generator.py
└── tests/
    └── test_validation.py
```

## Setup & Installation

1. **Clone or Extract the repository:**
   ```bash
   cd project_root
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

5. **Run tests:**
   ```bash
   pytest
   ```
