## Pymagine 

![](https://github.com/katieb1/pymagine/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/katieb1/pymagine/branch/master/graph/badge.svg)](https://codecov.io/gh/katieb1/pymagine) ![Release](https://github.com/katieb1/pymagine/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pymagine/badge/?version=latest)](https://pymagine.readthedocs.io/en/latest/?badge=latest)

Python package that allows the user to apply filters to images

### Installation:

```
pip install -i https://test.pypi.org/simple/ pymagine
```

### Features

### Dependencies

The following python packages are required to run `pymagine`:
* numpy==1.18.1
* scikit-image==0.16.1
* scipy==1.2.3
* matplotlib==3.1.3
* cv2==4.2.0
* math==3.8.2
* PIL==7.0.0
* testpypi==1.3.0

### Usage

Load the pymagine library:

`from pymagine import pymagine`

Apply a vignette filter to an image:

`vignette_filter("~\image.jpg", strength=0.5, x=0.2, y=0.8)`

Apply a colour filter to an image:

`colour_filter("~\image.jpg", tone="blue_tone")`

Apply a tunnel filter to an image:

`tunnel_filter("~\image.jpg", k=0.5, rot=-0.2)`

Apply an edge detection filter to an image:

`edge_detection("~\image.jpg", color="Purples", is_grey=False)`

### Documentation
The official documentation is hosted on Read the Docs: <https://pymagine.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
