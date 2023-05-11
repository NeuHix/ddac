import numpy as np
from astropy.io import fits

np.set_printoptions(threshold=np.inf)
# Due to "image data" array being very large, it is displayed using
# ellipses , but I don't want that, So this thing sets the print threshold
# to infinity , So I can see every row and column of the "image data" array.

fitslist = ['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits']

for file in fitslist:
	hduList = fits.open(file)  # fits.open() returns a list of HDUs
	print(f"{file} : {hduList[0].data} \n")  # Accessing the first element of the hdu list
	# .data returns the image data of the fits file in the form of Arrays

	print(f"Dimensions of {file}: {hduList[0].data.shape}")  # printing out the dimensions of the Array
