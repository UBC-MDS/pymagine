"""
Created on February 28, 2020
@author: Katie Birchard
Implementation of tunnel_filter function in the pymagine package.
"""
import math
from PIL import Image
import numpy as np
import cv2


def tunnel_filter(image_path, rot=0.5, file_name="tunnel.jpg"):
    """
    Returns the given image with the user-specified
    pincushion distortion applied.

    Parameters
    ----------
    image_path: string
      The local file path to the image for which the
      filter will be applied

    rot: float
      Value between -0.5 and 0.5, specifies rotation of
      the tunnel image
      Default: 0.5

    file_name: string
        The output file path (including file name) to 
        the saved image
        Default: "tunnel.jpg"

    Returns
    -------
    numpy array
    Altered image array returned for the input tunnel
    filter

    Example
    -------
    >>> tunnel_filter("img/picture.jpeg", rot=0.2, 
            file_name="folder/output.jpg")
    """
    if not isinstance(image_path, str):
        raise TypeError("Image file path must be a string.")

    if not image_path.endswith((".png", ".jpeg", ".jpg")):
        raise TypeError("Image format must be png, jpg, or jpeg.")

    if image_path.startswith(("https:", "http:", "www.")):
        raise TypeError(
            "Image file path can't be a URL, provide a local file path.")

    if not isinstance(rot, float):
        raise TypeError("Rotation degree must be a float.")

    if rot > 0.5 or rot < -0.5:
        raise ValueError("Rotation degree must be within -0.5 and 0.5.")

    if not file_name.endswith((".png", ".jpeg", ".jpg")):
        raise TypeError("File name format must be png, jpg, or jpeg.")

    # Read in the image file and convert to array
    pic = Image.open(image_path)
    pic_array = np.array(pic)

    # Get height and width
    h, w = pic.size

    # Calculate max radius for normalization
    max_radius = math.sqrt(w**2 + h**2) / 2

    # Create new array to fill with distorted data points
    tunnel_array = pic_array.copy()

    # Loops through all pixels and adds distortion
    for x in range(0, w):
        for y in range(0, h):

            norm_y = (2 * y - h) / h
            norm_x = (2 * x - w) / w

            # Calculating radius and normalizing
            r = np.sqrt(norm_x**2 + norm_y**2) / max_radius

            # Adding distortion strength
            x2 = norm_x / (1 + (0.5 * (r**4) + 0.5 * (r**2) + 0.5 * r))
            y2 = norm_y / (1 + (0.5 * (r**4) + 0.5 * (r**2) + 0.5 * r))

            # Adding distortion and rotation
            t = math.atan2(x2, y2)
            nx = rot * math.cos(t)
            ny = rot * math.sin(t)
            x3 = ((nx + 1) * w) / 2.0
            y3 = ((ny + 1) * h) / 2.0

            # Applying distortion to new image array
            tunnel_array[x, y] = pic_array[int(x3), int(y3)]

    cv2.imwrite(file_name, cv2.UMat(tunnel_array))
    return tunnel_array
