"""
Created on February 26, 2020
@author: Trevor Kwan
Implementation of edge_detection function in the pymagine package.
"""

def edge_detection(image, color="Greys"):
  
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