# very simple, just enough to start running tests
#
import builtins
from typing import Any, Mapping, List, Optional, Tuple, Union

from numpy.core._internal import _ctypes

class dtype:
    alignment: int
    byteorder: str
    char: str
    descr: List[Tuple[str, str]]
    fields: Optional[Mapping[str, Union[Tuple[dtype, int], Tuple[dtype, int, str]]]]
    flags: int
    hasobject: bool
    isbuiltin: int
    isnative: bool
    isalignedstruct: bool
    itemsize: int
    kind: str
    name: str
    names: Optional[Tuple[str, ...]]
    num: int
    shape: Tuple[int, ...]
    ndim: int
    subdtype: Optional[Tuple[dtype, Tuple[int, ...]]]


    def newbyteoder(self, new_order:str = ...): dtype

    str: builtins.str
    type: builtins.type

    @property
    def base(self) -> dtype: ...


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
    ctypes: _ctypes
    base: Optional[ndarray]


def array(
    object: object,
    dtype: dtype = ...,
    copy: bool = ...,
    subok: bool = ...,
    ndmin: int = ...) -> ndarray: ...
