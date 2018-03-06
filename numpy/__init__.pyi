import builtins

from typing import (
    Any, Dict, Iterable, List, Optional, Mapping, Sized,
    SupportsInt, SupportsFloat, SupportsComplex, SupportsBytes, SupportsAbs,
    Tuple, Union,
)

import sys

from numpy.core._internal import _ctypes

_Shape = Tuple[int, ...]

# Anything that can be coerced into numpy.dtype. To avoid recursive
# definitions, any nested fields are required to be castable to a dtype object
# are typed as Any.
# Reference: https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
_ConvertibleToDtype = Union[
    type,  # TODO: enumerate np.generic types and Python scalars
    # TODO: add a protocol for anything with a dtype attribute?
    None,
    str,
    Tuple[Any, int],
    Tuple[Any, _Shape],
    List[Union[Tuple[Union[str, Tuple[str, str]], Any],
               Tuple[Union[str, Tuple[str, str]], Any, _Shape]]],
    Dict[str, Any],
    Tuple[Any, Any]]


class dtype:
    names: Optional[Tuple[str, ...]]

    def __init__(self,
                 obj: Union[dtype, _ConvertibleToDtype],
                 align: bool = ...,
                 copy: bool = ...) -> None: ...

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


_DtypeLike = Union[dtype, _ConvertibleToDtype]
_Dtype = dtype  # to avoid name conflicts with ndarray.dtype


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


class ndarray(Iterable, Sized, SupportsInt, SupportsFloat, SupportsComplex,
              SupportsBytes, SupportsAbs[Any]):

    dtype: _Dtype
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

    # Many of these special methods are irrelevant currently, since protocols
    # aren't supported yet. That said, I'm adding them for completeness.
    # https://docs.python.org/3/reference/datamodel.html
    def __len__(self) -> int: ...
    def __getitem__(self, key) -> Any: ...
    def __setitem__(self, key, value): ...
    def __iter__(self) -> Any: ...
    def __contains__(self, key) -> bool: ...

    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __complex__(self) -> complex: ...
    if sys.version_info[0] < 3:
        def __oct__(self) -> str: ...
        def __hex__(self) -> str: ...
        def __nonzero__(self) -> bool: ...
    else:
        def __bool__(self) -> bool: ...
    def __bytes__(self) -> bytes: ...

    def __index__(self) -> int: ...

    def __copy__(self, order: str = ...) -> ndarray: ...
    def __deepcopy__(self, memo: dict) -> ndarray: ...

    # https://github.com/numpy/numpy/blob/v1.13.0/numpy/lib/mixins.py#L63-L181

    # TODO(shoyer): add overloads (returning ndarray) for cases where other is
    # known not to define __array_priority__ or __array_ufunc__, such as for
    # numbers or other numpy arrays. Or even better, use protocols (once they
    # work).

    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __iadd__(self, other): ...

    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __isub__(self, other): ...

    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __imul__(self, other): ...

    if sys.version_info[0] < 3:
        def __div__(self, other): ...
        def __rdiv__(self, other): ...
        def __idiv__(self, other): ...

    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __itruediv__(self, other): ...

    def __floordiv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __ifloordiv__(self, other): ...

    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __imod__(self, other): ...

    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...

    # NumPy's __pow__ doesn't handle a third argument
    def __pow__(self, other): ...
    def __rpow__(self, other): ...
    def __ipow__(self, other): ...

    def __lshift__(self, other): ...
    def __rlshift__(self, other): ...
    def __ilshift__(self, other): ...

    def __rshift__(self, other): ...
    def __rrshift__(self, other): ...
    def __irshift__(self, other): ...

    def __and__(self, other): ...
    def __rand__(self, other): ...
    def __iand__(self, other): ...

    def __xor__(self, other): ...
    def __rxor__(self, other): ...
    def __ixor__(self, other): ...

    def __or__(self, other): ...
    def __ror__(self, other): ...
    def __ior__(self, other): ...

    if sys.version_info[:2] >= (3, 5):
        def __matmul__(self, other): ...
        def __rmatmul__(self, other): ...

    def __neg__(self) -> ndarray: ...
    def __pos__(self) -> ndarray: ...
    def __abs__(self) -> ndarray: ...
    def __invert__(self) -> ndarray: ...

    # TODO(shoyer): remove when all methods are defined
    def __getattr__(self, name) -> Any: ...


def array(
    object: object,
    dtype: _DtypeLike = ...,
    copy: bool = ...,
    subok: bool = ...,
    ndmin: int = ...) -> ndarray: ...


# TODO(shoyer): remove when the full numpy namespace is defined
def __getattr__(name: str) -> Any: ...
