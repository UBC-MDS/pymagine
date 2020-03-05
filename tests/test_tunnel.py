import sys
import os
import pytest

import numpy as np
import pandas as pd
import cv2
import math

from pymagine import tunnel_filter as tun

fname = os.path.join(os.path.dirname(__file__), '../tests/imgs/coronado_beach.jpg')
bad_ftype = 'imgs/coronado_beach.csv'
url_fname = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg'

def test_tunnel():
  # File path must be a string
  with pytest.raises(TypeError):
    tun.tunnel_filter(20)
  # File type must be an image
  with pytest.raises(TypeError):
    tun.tunnel_filter(bad_ftype)
  # File path cannot be a URL
  with pytest.raises(TypeError):
    tun.tunnel_filter(url_fname)
  # Invalid distortion coefficient type
  with pytest.raises(TypeError):
    tun.tunnel_filter(fname, k=1L)
  # Invalid rotation type
  with pytest.raises(TypeError):
    tun.tunnel_filter(fname, rot="180")    
  # Invalid rotation value
  with pytest.raises(ValueError):
    tun.tunnel_filter(fname, rot=0.6)
  
