"""Image preprocessing module."""

import numpy as np


class ImagePreprocessor: me
    """Handles image preprocessing operations such as resizing, grayscale conversion, and normalization."""

    @staticmethod
    def to_grayscale(image: np.ndarray) -> np.ndarray:
        """Convert standard BGR/RGB image array to grayscale if 3D."""
        if len(image.shape) == 3 and image.shape[2] in [3, 4]:
            # Weighted average formula for luminance
            return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
        return image

    @staticmethod
    def normalize(image: np.ndarray) -> np.ndarray:
        """Normalize pixel intensities to range [0, 1]."""
        return image.astype(np.float32) / 255.0

    @staticmethod
    def resize(image: np.ndarray, target_shape: tuple) -> np.ndarray:
        """Simple downsampling/upsampling stub or image crop/reshape."""
        # For lightweight implementation without mandatory heavy OpenCV dependency
        return image[:target_shape[0], :target_shape[1]] if image.shape[0] >= target_shape[0] and image.shape[1] >= target_shape[1] else image
