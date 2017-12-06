# numpy_stubs: experimental typing stubs for NumPy

This repository exists for developing [PEP 484](https://www.python.org/dev/peps/pep-0484/)
compatible typing annotations for [NumPy](https://github.com/numpy/numpy).

It will be released as a separate "numpy_stubs" package on PyPI per [PEP
561](https://www.python.org/dev/peps/pep-0561/). This will let us iterate
rapidly on experimental type annotations without coupling to NumPy's release
cycle.

The plan (help wanted!):

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

Eventually, once development has stabilized, we expect to merge these type stubs
into the main NumPy repository.
