"""
Created on February 26, 2020
@author: Trevor Kwan
Implementation of edge_detection function in the pymagine package.
"""
import numpy as np
from skimage.color import rgb2gray
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

def edge_detection(filename, color = 'Greys', is_grey = False):
    """
    Returns the given image with the user-specified
  edge detection applied.
  
  Parameters
  ----------
  image: string
    The local file path for image to which filter will be applied
    
  color: string
    Color of edge detection filter to be applied to the image 
    Options: 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds'
    Default: 'Greys'
    
  Returns
  -------
  image 
  image returned with desired edge detection color filter applied
    """
    if not isinstance(filename, str):
        raise TypeError("Image file path must be a string.")
    
    if not filename.endswith((".png", ".jpeg", ".jpg")):
        raise TypeError("Image format must be png, jpg, or jpeg.")
    
    if filename.startswith(("https:", "http:", "www.")):
        raise TypeError("Image file path can't be a URL, provide a local file path.")
        
    if color == "Greys" or color == "Purples" or color == "Blues" or color == "Greens" or color == "Oranges" or color == "Reds":
        True
    else:
        raise ValueError("Color can only be one of: 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds'")
    
    filt = np.ones((3,3))/8

    if is_grey:
        img = plt.imread(filename)
        I_filt = convolve2d(img,filt, boundary='symm', mode='same')

    else:
        img = plt.imread(filename)
        img = rgb2gray(img)
        I_filt = convolve2d(img,filt, boundary='symm', mode='same')
        
    return plt.imshow(I_filt, cmap = color)