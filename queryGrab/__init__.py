"""{{ cookiecutter.package_name }} - {{ cookiecutter.package_description }}"""

from .Presto import queryPr, pushPr
from .geoConverter import convert_polygon_to_geohash
from .GoogleSheets import readGs

<<<<<<< HEAD
__version__ = '1.1.0'
=======
__version__ = '1.2.0'
>>>>>>> f81134a9c235f4fe2eb2f080b6f3d5ab894faf73

def sample(N,e):
	from math import ceil
	return int(ceil(N*1.0/(1+N*e*e)))