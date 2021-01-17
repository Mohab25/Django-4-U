# this is a file just to test pathlib
from pathlib import Path

path = Path(__file__).parent.joinpath('data/shp1')
print(path)