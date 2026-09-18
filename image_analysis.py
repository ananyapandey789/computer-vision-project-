"""Image analysis and metrics calculation module."""

from typing import Dict, Any
import numpy as np


class ImageAnalyzer:
    """Computes qualitative and quantitative metrics from image arrays."""

    @staticmethod
    def compute_metrics(image: np.ndarray) -> Dict[str, Any]:
        """Compute key statistics such as brightness, contrast, and dimension details."""
        if image is None or image.size == 0:
            return {}

        brightness = float(np.mean(image))
        std_contrast = float(np.std(image))
        shape = image.shape

        return {
            "height": shape[0],
            "width": shape[1],
            "channels": shape[2] if len(shape) > 2 else 1,
            "mean_brightness": round(brightness, 2),
            "std_contrast": round(std_contrast, 2),
        }
