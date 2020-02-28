"""
Created on February 28, 2020
@author: Katie Birchard
Implementation of fishbowl_filter function in the pymagine package.
"""


def fishbowl_filter(image, a=0.3, b=0.3, c=0.3, d=1.0, w=500, h=500):
  """
  Returns the given image with the user-specified
  barrel or pincushion distortion applied.
  
  Parameters
  ----------
  image: string
    The local file path to the image for which the
    filter will be applied
  
  a: float
    Parameter for correction, affects the outermost
    pixels
    Default: 0.3
  
  b: float
    Parameter for correction
    Default: 0.3
    
  c: float
    Parameter for correction
    Default: 0.3
    
  d: float
    Linear scaling of the image
    Default: 1.0
  
  w: integer
    Scaled width of the image
    Default: 500
    
  h: integer
    Scaled height of the image
    Default: 500
  
  Returns
  -------
  image
    image returned with the desired distortion filter 
    applied
  """
