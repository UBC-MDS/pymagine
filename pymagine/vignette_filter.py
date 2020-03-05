"""
Created on February 28, 2020
@author: Brendon Campbell
Implementation of vignette_filter function in the pymagine package.
"""

def vignette_filter(image, a=1.0):
  """
  Returns the given image with the vignette filter applied 
  at the specified strength.
  
  Parameters
  ----------
  image: string
    The local file path to the image for which the
    filter will be applied.
  
  a: float
    Parameter for the strength of the dimming effect.
    Default: 1.0
  
  Returns
  -------
  image
    image returned with the desired filter applied
  """