"""
Created on February 28, 2020
@author: Brendon Campbell
Implementation of vignette_filter function in the pymagine package.
"""

import numpy as np
import cv2


def vignette_filter(image_path, strength=1.0, x=0.5, y=0.5):
    """
    Applies vignette filter to a given image at the specified strength
    and focal point then saves the result to the current working directory.

    Parameters
    ----------
    image: string
      The local file path to the image for which the
      filter will be applied.

    sigma: float
      Parameter for the strength of the dimming effect.
      Default: 1.0

    x: float
      Parameter for the centre point of the effect
      along the x axis.
      Default: 0.5

    y: float
      Parameter for the centre point of the effect
      along the y axis.
      Default: 0.5

    Returns
    -------
    numpy array
    altered image array with effect applied
    """
    if not isinstance(image_path, str):
        raise TypeError("Image file path must be a string.")

    if not image_path.endswith((".png", ".jpeg", ".jpg")):
        raise TypeError("Image format must be png, jpg, or jpeg.")

    if image_path.startswith(("https:", "http:", "www.")):
        raise TypeError(
            "Image file path can't be a URL, provide a local file path.")

    if strength <= 0.:
        raise ValueError("Vignette strength can't be negative.")

    if x < 0 or x > 1 or y < 0 or y > 1:
        raise ValueError("Centre points must be between 0 and 1.")

    # read in image file
    image = cv2.imread(image_path, 1)

    # extract image dimensions and define center/focus indices
    rows, cols = image.shape[:2]
    focus_x = int(cols * x)
    focus_y = int(rows * y)

    # calculate stdev of the gaussian based on strength parameter
    sigma = (rows + cols) / (((1 + strength) / 1))

    # generate gaussian filters for each axis
    filt_cols = cv2.getGaussianKernel(
        2 * cols, sigma)[cols - focus_x:2 * cols - focus_x]
    filt_rows = cv2.getGaussianKernel(
        2 * rows, sigma)[rows - focus_y:2 * rows - focus_y]

    # create and scale 2d vignette filter
    filt_2d = filt_rows * filt_cols.T
    filt_2d_scaled = filt_2d / filt_2d.max()

    # create output image of correct dimensions
    image_modified = np.copy(image)
    image_modified[:, :, :] = 0

    # apply filter to each layer of the input image
    image_modified[:, :, 0] = image[:, :, 0] * filt_2d_scaled
    image_modified[:, :, 1] = image[:, :, 1] * filt_2d_scaled
    image_modified[:, :, 2] = image[:, :, 2] * filt_2d_scaled

    # write image to disk
    cv2.imwrite('vignette.jpg', image_modified)
    print("The filtered image has been saved to the working directory")

    return image_modified
