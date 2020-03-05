"""
Created on February 26, 2020
@author: Trevor Kwan
Implementation of edge_detection function in the pymagine package.
"""
import numpy as np
from skimage.color import rgb2gray
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

def edge_detection(filename, color, is_grey = False):
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
    filt = np.ones((3,3))/8

    if is_grey:
        img = plt.imread(filename)
        I_filt = convolve2d(img,filt, boundary='symm', mode='same')

    else:
        img = plt.imread(filename)
        img = rgb2gray(img)
        I_filt = convolve2d(img,filt, boundary='symm', mode='same')
        
    return plt.imshow(I_filt, cmap = color)