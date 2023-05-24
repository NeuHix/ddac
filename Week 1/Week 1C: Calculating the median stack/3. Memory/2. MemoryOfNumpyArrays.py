import sys
import numpy

arrayy = numpy.random.rand(10)

print(f"Python -> {sys.getsizeof(arrayy)} - This includes everything, from metadata to the array itself \n"
      f"Numpy ->  {arrayy.nbytes} - This only includes the actual array \n")