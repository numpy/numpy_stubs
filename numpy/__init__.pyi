# very simple, just enough to start running tests
#
from typing import Any, Tuple, Optional

class dtype: pass
_dtype = dtype      # for ndarray type


class flagsobj:
    aligned: bool
    behaved: bool
    c_contiguous: bool
    carray: bool
    contiguous: bool
    f_contiguous: bool
    farray: bool
    fnc: bool
    forc: bool
    fortran: bool
    num: bool
    owndata: bool
    updateifcopy: bool
    writeable: bool
    writebackifcopy: bool

    def __getitem__(self, key: str) -> bool: ...
    def __setitem__(self, key: str, value: bool) -> None: ...


class flatiter:
    base: ndarray
    coords: Tuple[int, ...]
    index: int

    def copy(self) -> ndarray: ...
    def __iter__(self) -> flatiter: ...
    def __next__(self) -> Any: ...


class ndarray:
    T: ndarray
    data: memoryview
    dtype: _dtype
    flags: flagsobj
    flat: Any
    imag: ndarray
    real: ndarray
    size: int
    itemsize: int
    nbytes: int
    ndim: int
    shape: Tuple[int, ...]
    strides: Tuple[int, ...]
    ctypes: Any
    base: Optional[ndarray]


def array(
    object: object,
    dtype: dtype = ...,
    copy: bool = ...,
    subok: bool = ...,
    ndmin: int = ...) -> ndarray: ...
