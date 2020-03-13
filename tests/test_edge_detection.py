import sys
import os
import pytest

import numpy as np
import pandas as pd

from pymagine import edge_detection as ed

fname = os.path.join(os.path.dirname(__file__), '../tests/imgs/coronado_beach.jpeg')
bad_ftype = 'imgs/coronado_beach.csv'
url_fname = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg'

def test_inputs():
   """
   Runs tests to ensure edge_detection function is working properly.
   """
   with pytest.raises(TypeError):
       ed.edge_detection(True) # Not a string for the file path
   with pytest.raises(TypeError):
       ed.edge_detection(bad_ftype) # Filetype is not image
   with pytest.raises(TypeError):
       ed.edge_detection(url_fname) # Filepath can't be URL

   with pytest.raises(ValueError):
       ed.edge_detection(fname, color = "Pinks") # Invalid color value
   with pytest.raises(ValueError):
       ed.edge_detection(fname, color = "Greys", is_grey = "Greys") # Invalid is_grey input

def test_outputs():
    """
    Applies tests to the function output
    """
    test_array = plt.imread(fname)

    # verify output image is the same dimensions as the input image
    returned_arr_edge_detection = ed.edge_detection(fname)
    assert returned_arr_edge_detection.shape == test_array.shape