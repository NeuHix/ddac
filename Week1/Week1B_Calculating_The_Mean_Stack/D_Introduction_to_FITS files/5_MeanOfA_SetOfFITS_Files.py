from astropy.io import fits
import matplotlib.pyplot as plt

def mean_fits(fitsFiles):
	lenOfFiles = len(fitsFiles)
	fitsFile = fits.open(fitsFiles[0])
	imageDataArray = fitsFile[0].data
	fitsFile.close()
	if lenOfFiles > 0:
		for eachFile in range(1, lenOfFiles):
			openFits = fits.open(fitsFiles[eachFile])
			imageDataArray += openFits[0].data
			openFits.close()
		return imageDataArray / lenOfFiles


if __name__ == '__main__':
	image = mean_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits'])
	plt.imshow(image, cmap=plt.cm.viridis)

	plt.xlabel("RA")
	plt.ylabel("Dec")

	plt.colorbar()
	plt.show()
