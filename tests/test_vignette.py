import sys
import os
import pytest

import numpy as np
import pandas as pd
import cv2

from pymagine import vignette_filter as vig

fname = os.path.join(os.path.dirname(__file__), '../tests/imgs/coronado_beach.jpeg')
bad_ftype = 'imgs/coronado_beach.csv'
url_fname = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg'

def test_inputs():
    with pytest.raises(TypeError):
       vig.vignette_filter(True) # Not a string for the file path
    with pytest.raises(TypeError):
       vig.vignette_filter(bad_ftype) # Filetype is not image
    with pytest.raises(TypeError):
       vig.vignette_filter(url_fname) # Filepath can't be URL

    with pytest.raises(ValueError):
        vig.vignette_filter(fname, strength=-1.0) # Invalid strength value
    with pytest.raises(ValueError):
        vig.vignette_filter(fname, x=2.0) # Invalid x axis value
    with pytest.raises(ValueError):
        vig.vignette_filter(fname, y=-1.0) # Invalid y axis value