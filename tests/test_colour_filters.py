import sys
import os
import pytest

from pymagine import colour_filters as cf

fname = os.path.join(os.path.dirname(__file__), '../tests/imgs/coronado_beach.jpeg')
bad_ftype = 'imgs/coronado_beach.csv'
url_fname = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg'

def test_inputs():
    with pytest.raises(TypeError):
       cf.colour_filters(2) # Not a string for the file path
    with pytest.raises(TypeError):
       cf.colour_filters(bad_ftype) # Filetype is not image
    with pytest.raises(TypeError):
       cf.colour_filters(url_fname) # Filepath can't be URL
    with pytest.raises(ValueError):
        cf.colour_filters(fname, tone = "pink") # Invalid tone value
