"""
Created on February 26, 2020
@author: Sukriti Trehan
Implementation of colour_filters function in the pymagine package.
"""

def colour_filters(image, tone="sepia"):
  
  """
  Returns the given image with the user-specified
  color filter applied.
  
  Parameters
  ----------
  image: string
    The local file path for image to which filter will be applied
    
  tone: string
    Colour filter to be applied to the image 
    Options: 'sepia', 'grayscale', 'rose-tone', 'blue-tone'
    Default: 'sepia'
    
  Returns
  -------
  image 
  image returned with desired colour filter applied
  """
