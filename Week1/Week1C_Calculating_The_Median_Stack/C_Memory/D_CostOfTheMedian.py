from astropy.io import fits
import numpy
import time

def median_fits(fitsfiles):
	fitsArrays = []
	timestart = time.perf_counter()  # Start the time counter

	for eachfile in fitsfiles:  # For every file in fitsFiles, DO:
		file = fits.open(eachfile)  # open it through fits, this returns a hdu List
		imageArray = file[0].data   # the Array is usually at first element of the hdu list
		file.close()  # Closing the file to save memory
		fitsArrays.append(imageArray)  # inserting the array in the Array List

	fitsstack = numpy.dstack(fitsArrays)    # Sorting the Arrays
	median = numpy.median(fitsstack, axis=2)    # Calculating the Median
	memory = fitsstack.nbytes / 1024    # Calculating the memory the entire list of Arrays occupy in kB

	timelapse = time.perf_counter() - timestart  # End the Time counter and calculate timelapsed

	return median, timelapse, memory

if __name__ == '__main__':
	print(median_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits']))