import os
import warnings
import pathlib
import sys

import numpy as np


package_directory = pathlib.Path().resolve()
print(package_directory)
sys.path.append(str(package_directory))
from pyTEM.Interface import Interface
print(dir(Interface))

