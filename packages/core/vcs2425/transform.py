import numpy as np
from .colormap import colormap

class ApplyColormap:
    def __init__(self, cmap='Spectral'):
        self.cmap = cmap

    def __call__(self, img):
        """
        Args:
            img (PIL Image or numpy.ndarray): Grayscale image.
        Returns:
            numpy.ndarray: Colormapped image.
        """
        # Convert PIL Image to numpy array if needed
        if hasattr(img, 'numpy'):
            img_np = img.numpy()
        else:
            img_np = np.array(img)

        if (self.cmap == "stacked"):
            img_np = (img_np / 256).astype(np.uint8)  # Ensure the image is in the range [0, 255]
            return np.stack([img_np] * 3, axis=-1)
        else:
            colored = colormap(img_np, cmap=self.cmap)
            return colored
