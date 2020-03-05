"""
Created on February 28, 2020
@author: Katie Birchard
Implementation of tunnel_filter function in the pymagine package.
"""


def tunnel_filter(image, k=0.5, rot=0.5):
  """
  Returns the given image with the user-specified
  pincushion distortion applied.
  
  Parameters
  ----------
  image: string
    The local file path to the image for which the
    filter will be applied
  
  k: float
    Distortion coefficient
    Default: 0.5
  
  rot: float
    Value between -0.5 and 0.5, specifies rotation of 
    the tunnel image
    Default: 0.5
  
  Returns
  -------
  image
    image returned with the desired distortion filter 
    applied
  """
  
  # Read in the image file and convert to array 
  pic = Image.open(image) 
  pic_array = np.array(pic)
  
  # Get height and width
  h, w = pic.size
  print(pic.size)
  
  # Calculate max radius for normalization
  max_radius = math.sqrt(w**2 + h**2)/2
  
  # Create new array to fill with distorted data points
  tunnel_array = pic_array.copy()
  
  # Loops through all pixels and adds distortion  
  for x in range(0,w):
      for y in range(0,h):
        
          norm_y = (2*y - h)/h 
          norm_x = (2*x - w)/w  
          
          # Calculating radius and normalizing
          r = np.sqrt(norm_x**2 + norm_y**2)/max_radius
          
          # Adding distortion strength  
          x2 = norm_x / (1 + (k*(r**4) + k*(r**2) * k*r))
          y2 = norm_y/ (1 + (k*(r**4) + k*(r**2) + k*r))
          
          # Adding distortion and rotation
          t = math.atan2(x2, y2)
          nx = rot*math.cos(t)
          ny = rot*math.sin(t)
          x3 = ((nx + 1)*w)/2.0
          y3 = ((ny + 1)*h)/2.0
          
          # Applying distortion to new image array
          tunnel_array[x, y] = pic_array[int(x3), int(y3)]
                    
  return Image.fromarray(tunnel_array).show() 
  
