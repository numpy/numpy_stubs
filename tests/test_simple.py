"""Simple expression that should pass with mypy."""
import operator

import numpy as np
from typing import Iterable

# Basic checks
array = np.array([1, 2])
def ndarray_func(x: np.ndarray) -> np.ndarray:
    return x
ndarray_func(np.array([1, 2]))
array == 1
array.dtype == float

# Dtype construction
np.dtype(float)
np.dtype(np.float64)
np.dtype(None)
np.dtype('float64')
np.dtype(np.dtype(float))
np.dtype(('U', 10))
np.dtype((np.int32, (2, 2)))
np.dtype([('R', 'u1'), ('G', 'u1'), ('B', 'u1')])
np.dtype([('R', 'u1', 1)])
np.dtype([('R', 'u1', (2, 2))])
np.dtype({'col1': ('U10', 0), 'col2': ('float32', 10)})
np.dtype((np.int32, {'real': (np.int16, 0), 'imag': (np.int16, 2)}))
np.dtype((np.int32, (np.int8, 4)))

# Iteration and indexing
def iterable_func(x: Iterable) -> Iterable:
    return x
iterable_func(array)
[element for element in array]
iter(array)
zip(array, array)
array[1]
array[:]
array[...]
array[:] = 0

array_2d = np.ones((3, 3))
array_2d[:2, :2]
array_2d[..., 0]
array_2d[:2, :2] = 0

# Other special methods
len(array)
str(array)
array_scalar = np.array(1)
int(array_scalar)
float(array_scalar)
# currently does not work due to https://github.com/python/typeshed/issues/1904
# complex(array_scalar)
bytes(array_scalar)
operator.index(array_scalar)
bool(array_scalar)

# comparisons
array < 1
array <= 1
array == 1
array != 1
array > 1
array >= 1
1 < array
1 <= array
1 == array
1 != array
1 > array
1 >= array

# binary arithmetic
array + 1
1 + array
array += 1

array - 1
1 - array
array -= 1

array * 1
1 * array
array *= 1

array / 1
1 / array
array /= 1

array // 1
1 // array
array //= 1

array % 1
1 % array
array %= 1

divmod(array, 1)
divmod(1, array)

array ** 1
1 ** array
array **= 1

array << 1
1 << array
array <<= 1

array >> 1
1 >> array
array >>= 1

array & 1
1 & array
array &= 1

array ^ 1
1 ^ array
array ^= 1

array | 1
1 | array
array |= 1

array @ array

# unary arithmetic
-array
+array
abs(array)
~array

# Other methods
np.array([1, 2]).transpose()
