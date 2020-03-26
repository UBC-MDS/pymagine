"""
Created on February 26, 2020
@author: Trevor Kwan
Implementation of edge_detection function in the pymagine package.
"""
import numpy as np
from skimage.color import rgb2gray
from scipy.signal import convolve2d
import matplotlib.pyplot as plt


def edge_detection(image, file_name="edge.jpg"):
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
    if not isinstance(image, str):
        raise TypeError("Image file path must be a string.")

    if not image.endswith((".png", ".jpeg", ".jpg")):
        raise TypeError("Image format must be png, jpg, or jpeg.")

    if image.startswith(("https:", "http:", "www.")):
        raise TypeError(
            "Image file path can't be a URL, provide a local file path.")

    if not file_name.endswith((".png", ".jpeg", ".jpg")):
        raise TypeError("File name format must be png, jpg, or jpeg.")

    # setting the filter
    filt = np.ones((3, 3)) / 8

    # loading the image
    img = plt.imread(image)
    img = rgb2gray(img)
    I_filt = convolve2d(img, filt, boundary='symm', mode='same')

    # saving the image
    plt.imsave(file_name, I_filt)

    return I_filt
