from astropy.io import fits

# Reader Header info of a FITS file

fitsFile = fits.open('image0.fits')
fitsFile.info()
# no need of a print statement !!!
