import pytest
import os
import matplotlib.pyplot as plt

from pymagine import vignette_filter as vig

fname = os.path.join(
    os.path.dirname(__file__),
    '../tests/imgs/coronado_beach.jpeg')
bad_ftype = 'imgs/coronado_beach.csv'
url_fname = 'https://upload.wikimedia.org/wikipedia/Python-logo-notext.svg'


def test_inputs():
    """
    Applies tests to the vignette function to confirm handling of valid inputs
    """
    with pytest.raises(TypeError):
        vig.vignette_filter(True)  # Not a string for the file path
    with pytest.raises(TypeError):
        vig.vignette_filter(bad_ftype)  # Filetype is not image
    with pytest.raises(TypeError):
        vig.vignette_filter(url_fname)  # Filepath can't be URL

    with pytest.raises(ValueError):
        vig.vignette_filter(fname, strength=-1.0)  # Invalid strength value
    with pytest.raises(ValueError):
        vig.vignette_filter(fname, x=2.0)  # Invalid x axis value
    with pytest.raises(ValueError):
        vig.vignette_filter(fname, y=-1.0)  # Invalid y axis value


def test_outputs():
    """
    Applies tests to the function output
    """
    test_array = plt.imread(fname)

    # verify output image is the same dimensions as the input image
    returned_arr_vignette = vig.vignette_filter(fname)
    assert returned_arr_vignette.shape == test_array[:, :, 0].shape
