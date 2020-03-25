## Pymagine 


[![codecov](https://codecov.io/gh/UBC-MDS/pymagine/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pymagine) 
![build](https://github.com/UBC-MDS/pymagine/workflows/build/badge.svg?branch=master)
![Release](https://github.com/UBC-MDS/pymagine/workflows/Release/badge.svg?branch=master)
[![Documentation Status](https://readthedocs.org/projects/pymagine/badge/?version=latest)](https://pymagine.readthedocs.io/en/latest/?badge=latest)

### Package Overview & Scope

This package includes functions that provide several different types of visual manipulations to an input image.

### Installation:

```
pip install -i https://test.pypi.org/simple/ pymagine
```

### Features

This package includes four main functions that accept an image as input and apply different types of manipulations and provide a new output image as summarized below:

1. **Tunnel distortion**: produces an image with strong visual distortion intended to create a tunnel or pincushion effect
2. **Colour filters**: produces an image with different user-specified colour distortions (ex: blue tone)
3. **Edge detection**: identifies edges by looking at where the image brightness changes sharply, and produces a black and white image highlighting the locations of these edges
4. **Vignetting**: produces an image with reduced brightness around the periphery compared to the image center, while allowing the user to specify a focal point location around which the effect should be centered

**Package data:** A small set of example photos are included with the package for testing the functions, with some usage examples outlined below.

### Our Package in the Python Ecosystem

A variety of image processing packages providing some similar functionality already exist within the Python ecosystem, including [Pillow](https://github.com/python-pillow/Pillow), [scikit-image](https://github.com/scikit-image/scikit-image), and the more advanced computer vision oriented [OpenCV](https://github.com/opencv/opencv). The purpose of our package is to provide functions that apply some common artistic filter transformations to a given input image.



### Dependencies

The following python packages are required to run `pymagine`:
* numpy==1.18.1
* pandas==1.0.1
* scikit-image==0.16.1
* scipy==1.2.3
* matplotlib==3.1.3
* opencv-python==4.2.0
* flake8==3.7.9
* Pillow==7.0.0
* testpypi==1.3.0

### Usage

Load the pymagine library:

`from pymagine import vignette_filter as vignette_filter`
`from pymagine import colour_filters as colour_filters`
`from pymagine import tunnel_filter as tunnel_filter`
`from pymagine import edge_detection as edge_detection`

Example photo taken at Coronado Beach, San Diego:

![Sample Image](docs/img/coronado_beach.jpeg)

Apply a vignette filter to an image:

`vignette_filter("~\image.jpg", strength=1.0, x=0.5, y=0.5)`
![Vignette Effect](docs/img/vignette.jpeg)


Apply a colour filter to an image:

`colour_filters("~\image.jpg", tone="blue_tone")`
![Colour Effect](docs/img/colour_filter.jpeg)

Apply a tunnel filter to an image:

`tunnel_filter("~\image.jpg", rot=-0.2)`
![Tunnel Effect](docs/img/tunnel.jpg)

Apply an edge detection filter to an image:

`edge_detection("~\image.jpg")`
![Edge Detection Effect](docs/img/edge_detection_image.jpg)

### Documentation
The official documentation is hosted on Read the Docs: <https://pymagine.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
