# numpy-stubs: experimental typing stubs for NumPy

[![Build Status](https://travis-ci.org/numpy/numpy-stubs.svg?branch=master)](https://travis-ci.org/numpy/numpy-stubs)

**We are currently focused on moving these type stubs into the
NumPy main repo. We look forward to your contributions once the
migration is complete!**

This repository exists for developing [PEP 484](https://www.python.org/dev/peps/pep-0484/)
compatible typing annotations for [NumPy](https://github.com/numpy/numpy).

The plan:

1. Write basic type stubs for `numpy.ndarray` without dtypes or shapes.
2. Add support for dtypes in ndarray type-annotations.
   - This might be as simple as writing `np.ndarray[np.float64]`, but will need a
     decision about appropriate syntax for shape typing to ensure that this is
     forwards compatible with typing shapes.
   - This will likely require minor changes to NumPy itself, e.g., to add
     `ndarray.__class_getitem__` per PEP 560.
3. Add support for shapes in ndarray type-annotations.
   - This will first require defining a broader (Python wide) standard for
     typing array shapes, and likely entail writing a PEP.
