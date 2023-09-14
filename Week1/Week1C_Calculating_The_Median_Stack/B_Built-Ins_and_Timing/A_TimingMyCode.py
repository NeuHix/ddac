import numpy as np
import time

"""
Numpy's Mean vs Python's Mean
"""

fluxes = np.random.randn(10**2)

# Time Start -> Python's mean
pytimeStart = time.perf_counter()
pymean = sum(fluxes) / len(fluxes)
pytimeOver = time.perf_counter()
pyMean = pytimeOver - pytimeStart

# Time start -> Np's mean
nptimeStart = time.perf_counter()
npmean = np.mean(fluxes)
nptimeOver = time.perf_counter()
npMean = nptimeOver - nptimeStart


if npMean > pyMean:
    print(
        f"Py's Mean Won! \n" f"It took just {pyMean}s \n" f"While Np took {npMean}s \n"
    )
elif pyMean > npMean:
    print(
        f"NP's mean Won! \n" f"It took just {npMean}s \n" f"While Py took {pyMean}s \n"
    )
else:
    print(f"Draw!")

data = fluxes

start = time.perf_counter()
mean = sum(data) / len(data)
seconds = time.perf_counter() - start

print("Python -> That took {:.2f} seconds.".format(seconds))

start = time.perf_counter()
meanN = np.mean(data)
seconds = time.perf_counter() - start

print("Numpy -> That took {:.1f} seconds.".format(seconds))

"""
Python is winning for array of sizes up to 100.
Over that, Numpy takes over python.
"""
