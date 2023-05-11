from astropy.io import fits
import matplotlib.pyplot as plt

hduList = fits.open("image0.fits")

imageDataArray = hduList[0].data

plt.imshow(imageDataArray, cmap=plt.cm.viridis)

plt.xlabel("RA")
plt.ylabel("Dec")

plt.colorbar()
plt.show()
