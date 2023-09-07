The SuperCOSMOS all-sky catalogue is a catalogue of galaxies generated from several **visible light** surveys.

The original data is available on this page in a package called *SCOS_XSC_mCl1_B21.5_R20_noStepWedges.csv.gz*.
Because this catalogue is so large, we've cut it down for these activities.
The cut down version of the file will be named **super.csv**.

The first few lines of **super.csv** look like this:

```super.csv
RA,Dec,sigRA,sigDec,epoch,muAcosD,muD,sigMuAcosD,sigMuD,chi2,classMagB,classMagR1,classMagR2,classMagI,meanClass,classB,classR1,classR2,classI,ellipB,ellipR1,ellipR2,ellipI,qualB,qualR1,qualR2,qualI
1.0583407,-52.9162402,1.2605071E-05,1.3178029E-05,1990.9344,-14.794838,-22.16756,7.242738,7.881182,5.027039,14.072,12.997,13.293,12.74,1,1,1,1,1,0.182453,0.234902,0.213206,0.19472,16,16,16,16
2.6084425,-41.5005753,2.0626481E-05,2.0626481E-05,1990.0508,-1.144597,-0.50977,10.397644,11.014809,0.245407,18.84,18.834,18.387,18.929,2,2,2,2,2,0.106605,0.112284,0.137899,0.091846,0,0,0,0
2.7302499,-27.706955,1.9480565E-05,1.8334649E-05,1982.9619,8.661513,1.872858,11.983931,11.506061,0.281173,19.188,18.723,18.74,18.993,2,2,2,2,1,0.117095,0.174671,0.020132,0.280859,0,0,0,0
```

The catalogue uses a comma-separated value (CSV) format. Aside from the first row, which contains column labels, the format is:

**1**: Right ascension in decimal degrees
**2**: Declination in decimal degrees
**3**: Other data, including magnitude and apparent shape
So now when loading this file in, we have to tell `np.loadtxt` to skip the first row and treat the commas as delimiters:

```python
import numpy as np
cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
print(cat)
```
