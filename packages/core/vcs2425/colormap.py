import numpy as np
import matplotlib.cm as cm

def colormap(img, cmap='Spectral'):
    """
    Apply a colormap to a grayscale image.
    
    Parameters:
        img (numpy.ndarray): Grayscale image array. (1 channel of uint16). The 16-bit PNG file stores the single channel values mapped linearly from the [0, 1] range into [0, 65535]. This comes from the MarigoldImageProcessor function called "export_depth_to_16bit_png".
        cmap (str): Colormap name.
        
    Returns:
        numpy.ndarray: Colormapped RGB image.
    """
    # Normalize the image to [0, 1]
    normalized = img.astype(np.float32) / 65535.0
    
    # Apply the colormap
    custom_colormap = cm.get_cmap(cmap)
    colored_image = custom_colormap(normalized)  # Returns RGBA
    
    # Convert RGBA to RGB (drop alpha channel)
    rgb_image = (colored_image[:, :, :3] * 255).astype(np.uint8)
    
    return rgb_image