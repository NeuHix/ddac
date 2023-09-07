import sys
import numpy
from astropy.io import fits



file = fits.open('image0.fits')
arr = file[0].data
print(arr)

print(f"sys -> {sys.getsizeof(arr) / (1024)} KB")
print(arr.nbytes)