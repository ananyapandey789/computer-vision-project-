"""Unit tests for computer vision modules."""

import numpy as np
from modules.preprocessing import ImagePreprocessor
from modules.object_detection import ObjectDetector
from modules.face_detection import FaceDetector
from modules.image_analysis import ImageAnalyzer


def test_grayscale_conversion():
    img = np.ones((10, 10, 3), dtype=np.uint8) * 100
    gray = ImagePreprocessor.to_grayscale(img)
    assert len(gray.shape) == 2
    assert gray.shape == (10, 10)


def test_object_detection():
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    detector = ObjectDetector()
    results = detector.detect(img)
    assert isinstance(results, list)
    assert len(results) > 0


def test_face_detection():
    img = np.zeros((100, 100), dtype=np.uint8)
    detector = FaceDetector()
    results = detector.detect(img)
    assert isinstance(results, list)
    assert len(results) > 0


def test_image_analysis():
    img = np.ones((50, 50, 3), dtype=np.uint8) * 128
    metrics = ImageAnalyzer.compute_metrics(img)
    assert metrics["height"] == 50
    assert metrics["width"] == 50
    assert metrics["mean_brightness"] == 128.0
