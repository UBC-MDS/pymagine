import sys
import os
import pytest
import matplotlib.pyplot as plt
import numpy as np

from pymagine import colour_filters as cf

fname = os.path.join(os.path.dirname(__file__), '../tests/imgs/coronado_beach.jpeg')
bad_ftype = 'imgs/coronado_beach.csv'
url_fname = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg'

def test_inputs():
    """
    Applies tests to the colour_filters function to ensure proper usage.
    """
    with pytest.raises(TypeError):
       cf.colour_filters(2) # Not a string for the file path
    with pytest.raises(TypeError):
       cf.colour_filters(bad_ftype) # Filetype is not image
    with pytest.raises(TypeError):
       cf.colour_filters(url_fname) # Filepath can't be URL
    with pytest.raises(ValueError):
        cf.colour_filters(fname, tone = "pink") # Invalid tone value


def test_outputs():
    """
    Applies tests to the colour_filters function output
    """
    test_array = plt.imread(fname)
    
    returned_arr_grayscale = cf.colour_filters(fname, tone="grayscale")
    returned_arr_negative = cf.colour_filters(fname, tone="negative")
    returned_arr_red = cf.colour_filters(fname, tone="red_tone")
    returned_arr_green = cf.colour_filters(fname, tone="green_tone")
    returned_arr_blue = cf.colour_filters(fname, tone="blue_tone")
    returned_arr_sepia = cf.colour_filters(fname, tone="sepia")
    
    assert returned_arr_grayscale.shape == test_array[:,:,0].shape
    assert returned_arr_negative.shape == test_array[:,:,0].shape
    assert returned_arr_red.shape == test_array.shape
    assert returned_arr_blue.shape == test_array.shape
    assert returned_arr_green.shape == test_array.shape
    assert returned_arr_sepia.shape == test_array.shape
    
    assert all(isinstance(x, np.uint8) for x in returned_arr_red.ravel())
    assert all(isinstance(x, np.uint8) for x in returned_arr_blue.ravel())
    assert all(isinstance(x, np.uint8) for x in returned_arr_green.ravel())
    assert all(isinstance(x, np.uint8) for x in returned_arr_sepia.ravel())
