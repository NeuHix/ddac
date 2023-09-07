## Median is memory hungry

Calculating the median requires all the data to be in memory _**at once**_. This is an issue in typical astrophysics calculations, which may use hundreds of thousands of FITS files.

Through the previous activities, you have hopefully noticed that even with a machine with lots of RAM, it's not going to be possible to find the median of more than a few tens of thousands of images.

## Mean is relatively light

This isn’t an issue for calculating the mean, since the sum only requires one image to be added at a time. You can load an image, add it to the sum, and then reuse the memory. Since the sum is only ever the size of a single image, you’ll never run out of memory.
