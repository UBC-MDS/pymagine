import os
import pytest
import matplotlib.pyplot as plt
import numpy as np

from pymagine import tunnel_filter as tun

fname = os.path.join(
    os.path.dirname(__file__),
    '../tests/imgs/coronado_beach.jpg')
bad_ftype = 'imgs/coronado_beach.csv'
url_fname = 'https://pic.svg'


def test_tunnel():
    """
    Applies tests to the colour_filters function
    to ensure proper usage.
    """
    # File path must be a string
    with pytest.raises(TypeError):
        tun.tunnel_filter(20)
    # File type must be an image
    with pytest.raises(TypeError):
        tun.tunnel_filter(bad_ftype)
    # File path cannot be a URL
    with pytest.raises(TypeError):
        tun.tunnel_filter(url_fname)
    # Invalid rotation type
    with pytest.raises(TypeError):
        tun.tunnel_filter(fname, rot="180")
    # Invalid rotation value
    with pytest.raises(ValueError):
        tun.tunnel_filter(fname, rot=0.6)


def test_outputs():
    """
    Applies tests to the tunnel_filter function
    output.
    """
    test_array = plt.imread(fname)

    returned_arr = tun.tunnel_filter(fname)

    assert returned_arr.shape == test_array.shape

    assert all(isinstance(x, np.uint8) for x in returned_arr.ravel())
