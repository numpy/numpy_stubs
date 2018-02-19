# very simple, just enough to start running tests
#
import builtins
from typing import Any, Mapping, List, Optional, Tuple, Union

from numpy.core._internal import _ctypes

_Shape = Tuple[int, ...]

class dtype:
    names: Optional[Tuple[str, ...]]

    @property
    def alignment(self) -> int: ...

    @property
    def base(self) -> dtype: ...

    @property
    def byteorder(self) -> str: ...

    @property
    def char(self) -> str: ...

    @property
    def descr(self) -> List[Union[
        Tuple[str, str],
        Tuple[str, str, _Shape]]]: ...

    @property
    def fields(self) -> Optional[Mapping[
        str,
        Union[Tuple[dtype, int],
              Tuple[dtype, int, Any]]]]: ...

    @property
    def flags(self) -> int: ...

    @property
    def hasobject(self) -> bool: ...

    @property
    def isbuiltin(self) -> int: ...

    @property
    def isnative(self) -> bool: ...

    @property
    def isalignedstruct(self) -> bool: ...

    @property
    def itemsize(self) -> int: ...

    @property
    def kind(self) -> str: ...

    @property
    def metadata(self) -> Optional[Mapping[str, Any]]: ...

    @property
    def name(self) -> str: ...

    @property
    def num(self) -> int: ...

    @property
    def shape(self) -> _Shape: ...

    @property
    def ndim(self) -> int: ...

    @property
    def subdtype(self) -> Optional[Tuple[dtype, _Shape]]: ...

    def newbyteorder(self, new_order: str = ...) -> dtype: ...

    # Leave str and type for end to avoid having to use `builtins.str`
    # everywhere. See https://github.com/python/mypy/issues/3775
    @property
    def str(self) -> builtins.str: ...

    @property
    def type(self) -> builtins.type: ...


_dtype_class = dtype      # for ndarray type


class _flagsobj:
    aligned: bool
    updateifcopy: bool
    writeable: bool
    writebackifcopy: bool

    @property
    def behaved(self) -> bool: ...

    @property
    def c_contiguous(self) -> bool: ...

    @property
    def carray(self) -> bool: ...

    @property
    def contiguous(self) -> bool: ...

    @property
    def f_contiguous(self) -> bool: ...

    @property
    def farray(self) -> bool: ...

    @property
    def fnc(self) -> bool: ...

    @property
    def forc(self) -> bool: ...

    @property
    def fortran(self) -> bool: ...

    @property
    def num(self) -> int: ...

    @property
    def owndata(self) -> bool: ...

    def __getitem__(self, key: str) -> bool: ...
    def __setitem__(self, key: str, value: bool) -> None: ...


class flatiter:
    @property
    def base(self) -> ndarray: ...

    @property
    def coords(self) -> _Shape: ...

    @property
    def index(self) -> int: ...

    def copy(self) -> ndarray: ...
    def __iter__(self) -> flatiter: ...
    def __next__(self) -> Any: ...


class ndarray:
    dtype: _dtype_class
    imag: ndarray
    real: ndarray
    shape: _Shape
    strides: Tuple[int, ...]

    @property
    def T(self) -> ndarray: ...

    @property
    def base(self) -> Optional[ndarray]: ...

    @property
    def ctypes(self) -> _ctypes: ...

    @property
    def data(self) -> memoryview: ...

    @property
    def flags(self) -> _flagsobj: ...

    @property
    def flat(self) -> flatiter: ...

    @property
    def size(self) -> int: ...

    @property
    def itemsize(self) -> int: ...

    @property
    def nbytes(self) -> int: ...

    @property
    def ndim(self) -> int: ...

    def __getattr__(self, name) -> Any: ...


def array(
    object: object,
    dtype: dtype = ...,
    copy: bool = ...,
    subok: bool = ...,
    ndmin: int = ...) -> ndarray: ...
