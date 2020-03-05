"""
Created on February 28, 2020
@author: Katie Birchard
Implementation of tunnel_filter function in the pymagine package.
"""

def tunnel_filter(image_path, k=0.5, rot=0.5):
  """
  Returns the given image with the user-specified
  pincushion distortion applied.
  
  Parameters
  ----------
  image_path: string
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
  if not isinstance(image_path, str):
    raise TypeError("Image file path must be a string.")
    
  if not image_path.endswith((".png", ".jpeg", ".jpg")):
    raise TypeError("Image format must be png, jpg, or jpeg.")
    
  if image_path.startswith(("https:", "http:", "www.")):
    raise TypeError("Image file path can't be a URL, provide a local file path.")
    
  if not isinstance(k, float):
    raise TypeError("Distortion coefficient must be a float.")
    
  if not isinstance(rot, float):
    raise TypeError("Rotation degree must be a float.")
    
  if rot > 0.5 or rot < -0.5:
    raise ValueError("Rotation degree must be within -0.5 and 0.5.")
  
  # Read in the image file and convert to array 
  pic = PIL.Image.open(image_path) 
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
                    
  return PIL.Image.fromarray(tunnel_array).show() 
  
