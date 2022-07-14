import pathlib
import sys


package_directory = pathlib.Path().resolve()
sys.path.append(str(package_directory))
from pyTEM.Interface import Interface
print('\n'.join(map(str, dir(Interface))))
