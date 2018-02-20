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
array + 1
-array

array_scalar = np.array(1)
int(array_scalar)
float(array_scalar)
complex(array_scalar)
bytes(array_scalar)
abs(array_scalar)
operator.index(array_scalar)
bool(array_scalar)

# Other methods
np.array([1, 2]).transpose()
