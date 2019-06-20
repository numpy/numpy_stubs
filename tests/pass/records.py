import numpy as np
import numpy.core.records as records

# Example data from numpy docs
x1 = np.array([1, 2, 3, 4])
x2 = np.array(['a', 'dd', 'xyz', '12'])
x3 = np.array([1.1, 2, 3, 4])
names = ['a', 'b', 'c']

# Testing various parameter types
records.fromarrays([x1, x2, x3])
records.fromarrays([x1, x2, x3], dtype=None)
records.fromarrays([x1, x2, x3], dtype=[('a', np.int32), ('b', np.str_), ('c', np.float32)])
records.fromarrays([x1, x2, x3], shape=None)
records.fromarrays([x1, x2, x3], shape=(4,))
records.fromarrays([x1, x2, x3], formats=None)
records.fromarrays([x1, x2, x3], formats=['i', 'U', 'f'])
records.fromarrays([x1, x2, x3], names=None)
records.fromarrays([x1, x2, x3], names=names)
records.fromarrays([x1, x2, x3], titles=None)
records.fromarrays([x1, x2, x3], titles=names)
records.fromarrays([x1, x2, x3], aligned=True)
records.fromarrays([x1, x2, x3], aligned=False)
records.fromarrays([x1, x2, x3], byteorder=None)
records.fromarrays([x1, x2, x3], byteorder='L')
