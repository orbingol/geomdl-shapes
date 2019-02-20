""" Shapes Module for NURBS-Python (geomdl)

.. moduleauthor:: Onur Rauf Bingol <orbingol@gmail.com>

"""

# Module version
__version__ = "1.1.0"

# Author and license
__author__ = "Onur Rauf Bingol"
__license__ = "MIT"

# Common imports
from geomdl.exceptions import GeomdlException

# Support for "from geomdl.shapes import *"
__all__ = [
    'curve2d',
    'surface',
    'analytic'
]
