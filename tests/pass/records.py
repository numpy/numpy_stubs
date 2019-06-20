import numpy as np

# Example data from numpy docs
x1 = np.array([1, 2, 3, 4])
x2 = np.array(['a', 'dd', 'xyz', '12'])
x3 = np.array([1.1, 2, 3, 4])
names = ['a', 'b', 'c']

# Testing various parameter types
np.core.records.fromarrays([x1, x2, x3])
np.core.records.fromarrays([x1, x2, x3], dtype=None)
np.core.records.fromarrays([x1, x2, x3],
                           dtype=[('a', np.int32), ('b', np.str_), ('c', np.float32)])
np.core.records.fromarrays([x1, x2, x3], shape=None)
np.core.records.fromarrays([x1, x2, x3], shape=(4,))
np.core.records.fromarrays([x1, x2, x3], formats=None)
np.core.records.fromarrays([x1, x2, x3], formats=['i', 'U', 'f'])
np.core.records.fromarrays([x1, x2, x3], names=None)
np.core.records.fromarrays([x1, x2, x3], names=names)
np.core.records.fromarrays([x1, x2, x3], titles=None)
np.core.records.fromarrays([x1, x2, x3], titles=names)
np.core.records.fromarrays([x1, x2, x3], aligned=True)
np.core.records.fromarrays([x1, x2, x3], aligned=False)
np.core.records.fromarrays([x1, x2, x3], byteorder=None)
np.core.records.fromarrays([x1, x2, x3], byteorder='L')
