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

T = TypeVar("T")

def zeros_like(
    a: _ArrayLike,
    dtype: Optional[dtype] = None,
    order: str = "K",
    subok: bool = True,
    shape: Optional[Union[int, Sequence[int]]] = None,
) -> ndarray[int]: ...
def ones(
    shape: _ShapeLike, dtype: Optional[dtype] = None, order: str = "C"
) -> ndarray[int]: ...
def ones_like(
    a: _ArrayLike,
    dtype: Optional[dtype] = None,
    order: str = "K",
    subok: bool = True,
    shape: Optional[_ShapeLike] = None,
) -> ndarray[int]: ...
def full(
    shape: _ShapeLike, fill_value: T, dtype: Optional[dtype] = None, order: str = "C"
) -> ndarray[T]: ...
def full_like(
    a: _ArrayLike,
    fill_value: T,
    dtype: Optional[dtype] = None,
    order: str = "K",
    subok: bool = True,
    shape: Optional[_ShapeLike] = None,
) -> ndarray[T]: ...
def count_nonzero(
    a: _ArrayLike, axis: Optional[Union[int, Tuple[int], Tuple[int, int]]] = None
) -> Union[int, ndarray[int]]: ...
def isfortran(a: ndarray) -> bool: ...
def argwhere(a: _ArrayLike) -> ndarray: ...
def flatnonzero(a: _ArrayLike) -> ndarray: ...
def correlate(a: _ArrayLike, v: _ArrayLike, mode: str = "valid") -> ndarray: ...
def convolve(a: _ArrayLike, v: _ArrayLike, mode: str = "full") -> ndarray: ...
def outer(a: _ArrayLike, b: _ArrayLike, out: ndarray = None) -> ndarray: ...
def tensordot(
    a: _ArrayLike,
    b: _ArrayLike,
    axes: Union[
        int, Tuple[int, int], Tuple[Tuple[int, int], ...], Tuple[List[int, int], ...]
    ] = 2,
) -> ndarray: ...
def roll(
    a: _ArrayLike,
    shift: Union[int, Tuple[int, ...]],
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
) -> T: ...
def rollaxis(a: _ArrayLike, axis: int, start: int = 0) -> ndarray: ...
def normalize_axis_tuple(
    axis: Union[int, Iterable[int]],
    ndim: int,
    argname: Optional[str] = None,
    allow_duplicate: bool = False,
) -> Tuple[int, ...]: ...
def moveaxis(
    a: ndarray,
    source: Union[int, Sequence[int]],
    destination: Union[int, Sequence[int]],
) -> ndarray: ...
def cross(
    a: _ArrayLike,
    b: _ArrayLike,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: Optional[int] = None,
) -> ndarray: ...
def indices(
    dimensions: Sequence[int], dtype: dtype = int, sparse: bool = False
) -> Union[ndarray, Tuple[ndarray, ...]]: ...
def fromfunction(function: Callable, shape: Tuple[int, int], **kwargs) -> Any: ...
def isscalar(element: Any) -> bool: ...
def binary_repr(num: int, width: Optional[int] = None) -> str: ...
def base_repr(number: int, base: int = 2, padding: int = 0) -> str: ...
def identity(n: int, dtype: Optional[dtype] = None) -> ndarray: ...
def allclose(
    a: _ArrayLike,
    b: _ArrayLike,
    rtol: float = 1.0e-5,
    atol: float = 1.0e-8,
    equal_nan: bool = False,
) -> bool: ...
def isclose(
    a: _ArrayLike,
    b: _ArrayLike,
    rtol: float = 1.0e-5,
    atol: float = 1.0e-8,
    equal_nan: bool = False,
) -> _ArrayLike: ...
def array_equal(a1: _ArrayLike, a2: _ArrayLike) -> bool: ...
def array_equiv(a1: _ArrayLike, a2: _ArrayLike) -> bool: ...
def extend_all(module: ModuleType): ...
