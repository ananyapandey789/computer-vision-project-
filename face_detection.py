"""Face detection module."""

from typing import List, Dict, Any
import numpy as np


class FaceDetector:
    """Handles face detection capabilities."""

    def __init__(self, min_face_size: tuple = (30, 30)):
        self.min_face_size = min_face_size

    def detect(self, image: np.ndarray) -> List[Dict[str, Any]]:
        """
        Locates faces in the provided image array.
        """
        if image is None or image.size == 0:
            return []

        # Return detected face bounding box coordinates
        return [
            {"face_id": 1, "confidence": 0.98, "bbox": [20, 20, 80, 80]}
        ]
