"""
Created on February 26, 2020
@author: Trevor Kwan
Implementation of edge_detection function in the pymagine package.
"""
import numpy as np
from skimage.color import rgb2gray
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import cv2


def edge_detection(filename):
    """
    Returns the given image with the greyscale
  edge detection applied.

  Parameters
  ----------
  image: string
    The local file path for image to which filter will be applied

  Returns
  -------
  numpy array
  Altered image array returned for the input edge_detection filter

  Example
  -------
  >>> edge_detection("img/picture.jpg")
    """
    if not isinstance(filename, str):
        raise TypeError("Image file path must be a string.")

    if not filename.endswith((".png", ".jpeg", ".jpg")):
        raise TypeError("Image format must be png, jpg, or jpeg.")

    if filename.startswith(("https:", "http:", "www.")):
        raise TypeError(
            "Image file path can't be a URL, provide a local file path.")

    filt = np.ones((3, 3)) / 8

    img = plt.imread(filename)
    img = rgb2gray(img)
    I_filt = convolve2d(img, filt, boundary='symm', mode='same')

    cv2.imwrite('edge_detection.jpg', I_filt)

    print("The filtered image has been saved to the working directory")
    return I_filt
