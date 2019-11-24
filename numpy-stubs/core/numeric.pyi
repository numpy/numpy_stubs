from types import ModuleType
from typing import (
    Sequence,
    Optional,
    TypeVar,
    Union,
    Tuple,
    List,
    Iterable,
    Callable,
    Any,
)

from numpy import ndarray, dtype, _ArrayLike, _ShapeLike

_T = TypeVar("_T")

def zeros_like(
    a: _ArrayLike,
    dtype: Optional[dtype] = ...,
    order: str = ...,
    subok: bool = ...,
    shape: Optional[Union[int, Sequence[int]]] = ...,
) -> ndarray[int]: ...
def ones(
    shape: _ShapeLike, dtype: Optional[dtype] = ..., order: str = ...
) -> ndarray[int]: ...
def ones_like(
    a: _ArrayLike,
    dtype: Optional[dtype] = ...,
    order: str = ...,
    subok: bool = ...,
    shape: Optional[_ShapeLike] = ...,
) -> ndarray[int]: ...
def full(
    shape: _ShapeLike, fill_value: _T, dtype: Optional[dtype] = ..., order: str = ...
) -> ndarray[_T]: ...
def full_like(
    a: _ArrayLike,
    fill_value: _T,
    dtype: Optional[dtype] = ...,
    order: str = ...,
    subok: bool = ...,
    shape: Optional[_ShapeLike] = ...,
) -> ndarray[_T]: ...
def count_nonzero(
    a: _ArrayLike, axis: Optional[Union[int, Tuple[int], Tuple[int, int]]] = ...
) -> Union[int, ndarray[int]]: ...
def isfortran(a: ndarray) -> bool: ...
def argwhere(a: _ArrayLike) -> ndarray: ...
def flatnonzero(a: _ArrayLike) -> ndarray: ...
def correlate(a: _ArrayLike, v: _ArrayLike, mode: str = ...) -> ndarray: ...
def convolve(a: _ArrayLike, v: _ArrayLike, mode: str = ...) -> ndarray: ...
def outer(a: _ArrayLike, b: _ArrayLike, out: ndarray = ...) -> ndarray: ...
def tensordot(
    a: _ArrayLike,
    b: _ArrayLike,
    axes: Union[
        int, Tuple[int, int], Tuple[Tuple[int, int], ...], Tuple[List[int, int], ...]
    ] = ...,
) -> ndarray: ...
def roll(
    a: _ArrayLike,
    shift: Union[int, Tuple[int, ...]],
    axis: Optional[Union[int, Tuple[int, ...]]] = ...,
) -> _T: ...
def rollaxis(a: _ArrayLike, axis: int, start: int = ...) -> ndarray: ...
def normalize_axis_tuple(
    axis: Union[int, Iterable[int]],
    ndim: int,
    argname: Optional[str] = ...,
    allow_duplicate: bool = ...,
) -> Tuple[int, ...]: ...
def moveaxis(
    a: ndarray,
    source: Union[int, Sequence[int]],
    destination: Union[int, Sequence[int]],
) -> ndarray: ...
def cross(
    a: _ArrayLike,
    b: _ArrayLike,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: Optional[int] = ...,
) -> ndarray: ...
def indices(
    dimensions: Sequence[int], dtype: dtype = ..., sparse: bool = ...
) -> Union[ndarray, Tuple[ndarray, ...]]: ...
def fromfunction(function: Callable, shape: Tuple[int, int], **kwargs) -> Any: ...
def isscalar(element: Any) -> bool: ...
def binary_repr(num: int, width: Optional[int] = ...) -> str: ...
def base_repr(number: int, base: int = ..., padding: int = ...) -> str: ...
def identity(n: int, dtype: Optional[dtype] = ...) -> ndarray: ...
def allclose(
    a: _ArrayLike,
    b: _ArrayLike,
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
) -> bool: ...
def isclose(
    a: _ArrayLike,
    b: _ArrayLike,
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
) -> _ArrayLike: ...
def array_equal(a1: _ArrayLike, a2: _ArrayLike) -> bool: ...
def array_equiv(a1: _ArrayLike, a2: _ArrayLike) -> bool: ...
def extend_all(module: ModuleType): ...
