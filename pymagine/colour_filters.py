"""
Created on February 26, 2020
@author: Sukriti Trehan
Implementation of colour_filters function in the pymagine package.
"""

import matplotlib.pyplot as plt
import numpy as np

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
  if not isinstance(image, str):
    raise TypeError("File path must be a string")

  if not image.lower().endswith(('.png', '.jpg', '.jpeg')):
    raise TypeError("Path given must be point to an image of .png, .jpg, or .jpeg format")

  if image.lower().startswith(('http', 'www')):
    raise TypeError("Local path for image must be given")
  
  if not tone.lower() in ["grayscale", "negative", "blue_tone", "red_tone", "green_tone", "sepia"]:
    raise ValueError("Invalid tone value. Tone must be a string: 'grayscale', 'negative', 'blue_tone', 'green_tone', 'red_tone', or 'sepia'")
    
  # Loading the image
  image = plt.imread(image)
    
  ### define common function to extract RGB pixels
    
  red = list()
  blue = list()
  green = list()
    
  def return_pixel(image):

      for i in range(image.shape[0]):
        for j in range(image.shape[1]):
          red.append(image[i, j, 0])
          blue.append(image[i, j, 2])
          green.append(image[i, j, 1])
      return np.asarray(red), np.asarray(green), np.asarray(blue)

  pixels = return_pixel(image)
  red_pixel = pixels[0]
  green_pixel = pixels[1]
  blue_pixel = pixels[2]
    
  ### end of finding R,G,B pixels
  
  if tone.lower() == 'grayscale':
      image_2d = image[:, :, 0]
        
      transformed_red = red_pixel*0.2989
      transformed_blue = blue_pixel*0.1140
      transformed_green = green_pixel*0.5870
          
      new_pixel = transformed_blue + transformed_green + transformed_red
      
      gray_image = np.reshape(new_pixel, image_2d.shape)
      final_image = plt.imshow(gray_image, cmap='gray')
  
  elif tone.lower() == 'negative':
      image_2d = image[:, :, 0]
      
      negative_image = image_2d.copy()
      negative_image = 255 - image_2d
      final_image = plt.imshow(negative_image, cmap="gray")
      
  elif tone.lower() == 'red_tone':
      transformed_red = red_pixel*0.75
      transformed_blue = blue_pixel*0.125
      transformed_green = green_pixel*0.125

      transformed_red = (np.where(transformed_red > 255, 255, transformed_red)).astype(int)
      transformed_green = (np.where(transformed_green > 255, 255, transformed_green)).astype(int)
      transformed_blue = (np.where(transformed_blue > 255, 255, transformed_blue)).astype(int)
      
      final_image_array = np.dstack((np.reshape(transformed_red, n), np.reshape(transformed_green, n), np.reshape(transformed_blue, n)))
      final_image = plt.imshow(final_image_array)
      
  elif tone.lower() == 'blue_tone':
      transformed_red = red_pixel*0.12
      transformed_blue = blue_pixel*0.70
      transformed_green = green_pixel*0.17

      transformed_red = (np.where(transformed_red > 255, 255, transformed_red)).astype(int)
      transformed_green = (np.where(transformed_green > 255, 255, transformed_green)).astype(int)
      transformed_blue = (np.where(transformed_blue > 255, 255, transformed_blue)).astype(int)
      
      final_image_array = np.dstack((np.reshape(transformed_red, n), np.reshape(transformed_green, n), np.reshape(transformed_blue, n)))
      final_image = plt.imshow(final_image_array)
      
  elif tone.lower() == 'green_tone':
      transformed_red = red_pixel*0.12
      transformed_blue = blue_pixel*0.17
      transformed_green = green_pixel*0.70

      transformed_red = (np.where(transformed_red > 255, 255, transformed_red)).astype(int)
      transformed_green = (np.where(transformed_green > 255, 255, transformed_green)).astype(int)
      transformed_blue = (np.where(transformed_blue > 255, 255, transformed_blue)).astype(int)
      
      final_image_array = np.dstack((np.reshape(transformed_red, n), np.reshape(transformed_green, n), np.reshape(transformed_blue, n)))
      final_image = plt.imshow(final_image_array)
  
  else:
      transformed_red = red_pixel*0.393 + green_pixel*0.769 + blue_pixel*0.189
      transformed_blue = red_pixel*0.272 + green_pixel*0.534 + blue_pixel*0.131
      transformed_green = red_pixel*0.349 + green_pixel*0.686 + blue_pixel*0.168

      transformed_red = (np.where(transformed_red > 255, 255, transformed_red)).astype(int)
      transformed_green = (np.where(transformed_green > 255, 255, transformed_green)).astype(int)
      transformed_blue = (np.where(transformed_blue > 255, 255, transformed_blue)).astype(int)
      
      n = image[:,:,0].shape
      
      final_image_array = np.dstack((np.reshape(transformed_red, n), np.reshape(transformed_green, n), np.reshape(transformed_blue, n)))
      final_image = plt.imshow(final_image_array)
  
  return final_image
