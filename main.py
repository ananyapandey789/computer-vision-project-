"""Main pipeline script for image processing, analysis, and report generation."""

import numpy as np
from modules.preprocessing import ImagePreprocessor
from modules.object_detection import ObjectDetector
from modules.face_detection import FaceDetector
from modules.image_analysis import ImageAnalyzer
from modules.report_generator import ReportGenerator


def run_pipeline():
    print("=== Starting Computer Vision Pipeline ===")

    # Create dummy synthetic image (100x100x3)
    sample_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

    # 1. Preprocessing
    print("[1/4] Preprocessing image...")
    gray_img = ImagePreprocessor.to_grayscale(sample_image)

    # 2. Object Detection
    print("[2/4] Running object detection...")
    obj_detector = ObjectDetector()
    detected_objects = obj_detector.detect(sample_image)

    # 3. Face Detection
    print("[3/4] Running face detection...")
    face_detector = FaceDetector()
    detected_faces = face_detector.detect(gray_img)

    # 4. Image Analysis
    print("[4/4] Analyzing image metrics...")
    metrics = ImageAnalyzer.compute_metrics(sample_image)

    # Compile results
    pipeline_results = {
        "metrics": metrics,
        "objects": detected_objects,
        "faces": detected_faces
    }

    # Generate Report
    report_gen = ReportGenerator("report/REPORT_CONTENT.md")
    report_file = report_gen.save_report(pipeline_results)

    print(f"Pipeline executed successfully!")
    print(f"Report generated at: {report_file}")


if __name__ == "__main__":
    run_pipeline()
