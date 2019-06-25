import numpy as np
import numpy.core.records as records

# Example data from numpy docs
x1 = np.array([1, 2, 3, 4])
x2 = np.array(['a', 'dd', 'xyz', '12'])
x3 = np.array([1.1, 2, 3, 4])
names = ['a', 'b', 'c']

# Testing various parameter types for fromarrays
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

# Testing various parameter types for fromrecords
rec1 = (1, 2, 3)
rec2 = (456, 'dbe', 1.2)
rec3 = (2, 'de', 1.3)

# Test basics
records.fromrecords([rec1], names=names)
records.fromrecords([rec2, rec3], names=names)

# Test other params
records.fromrecords([rec2, rec3], dtype=None)
records.fromrecords([rec2, rec3], dtype=[('a', np.int32), ('b', np.str_), ('c', np.float32)])
records.fromrecords([rec2, rec3], shape=None)
records.fromrecords([rec2, rec3], shape=(4,))
records.fromrecords([rec2, rec3], formats=None)
records.fromrecords([rec2, rec3], formats=['i', 'U', 'f'])
records.fromrecords([rec2, rec3], names=None)
records.fromrecords([rec2, rec3], names=names)
records.fromrecords([rec2, rec3], titles=None)
records.fromrecords([rec2, rec3], titles=names)
records.fromrecords([rec2, rec3], aligned=True)
records.fromrecords([rec2, rec3], aligned=False)
records.fromrecords([rec2, rec3], byteorder=None)
records.fromrecords([rec2, rec3], byteorder='L')
