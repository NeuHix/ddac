The full catalogue of bright radio sources contains 320 objects.
The first few rows look like this:

###### bss.dat  
```
  1  00 04 35.65 -47 36 19.1   0.87 0.04 0.97 0.06  0.90 0.04                0.995 0.030            17.63 Q 1.F.11.C  PKS 0002-478
  2  00 10 35.92 -30 27 48.3   0.74 0.03 0.72 0.04  0.63 0.03  0.315 0.009   0.419 0.013 1.19  La01 19.59 Q 1.F.11..  PKS 0008-307
  3* 00 11 01.27 -26 12 33.1   0.64 0.07 0.82 0.07  0.69 0.03  0.210 0.006               1.096 Wr83 19.53 Q 4.F.44.C  PKS 0008-264
```

The catalogue is organised in *fixed-width* columns, with the format of the columns being:

* **1**: Object catalogue ID number (sometimes with an asterisk)
* **2-4**: Right ascension in HMS notation
* **5-7**: Declination in DMS notation
* **8-**: Other information, including spectral intensities

We only need coordinates for crossmatching. We can load specific columns with the `usecols` argument
in NumPy's `loadtxt` function:

```
import numpy as np
cat = np.loadtxt('bss.dat', usecols=range(1, 7))
print(cat[0])
```

We've skipped the ID column, since the ID number is always the same as the row number.
