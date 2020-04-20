import builtins
import sys
import datetime as dt

from numpy.core._internal import _ctypes
from typing import (
    Any,
    ByteString,
    Callable,
    Container,
    Callable,
    Dict,
    IO,
    Iterable,
    List,
    Mapping,
    Optional,
    overload,
    Sequence,
    Sized,
    SupportsAbs,
    SupportsComplex,
    SupportsFloat,
    SupportsInt,
    Text,
    Tuple,
    Type,
    TypeVar,
    Union,
)

if sys.version_info[0] < 3:
    class SupportsBytes: ...

else:
    from typing import SupportsBytes

if sys.version_info >= (3, 8):
    from typing import Literal, Protocol
else:
    from typing_extensions import Literal, Protocol

_Shape = Tuple[int, ...]

# Anything that can be coerced to a shape tuple
_ShapeLike = Union[int, Sequence[int]]

_DtypeLikeNested = Any  # TODO: wait for support for recursive types

# Anything that can be coerced into numpy.dtype.
# Reference: https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
_DtypeLike = Union[
    dtype,
    # default data type (float64)
    None,
    # array-scalar types and generic types
    type,  # TODO: enumerate these when we add type hints for numpy scalars
    # TODO: add a protocol for anything with a dtype attribute
    # character codes, type strings or comma-separated fields, e.g., 'float64'
    str,
    # (flexible_dtype, itemsize)
    Tuple[_DtypeLikeNested, int],
    # (fixed_dtype, shape)
    Tuple[_DtypeLikeNested, _ShapeLike],
    # [(field_name, field_dtype, field_shape), ...]
    #
    # The type here is quite broad because NumPy accepts quite a wide
    # range of inputs inside the list; see the tests for some
    # examples.
    List[Any],
    # {'names': ..., 'formats': ..., 'offsets': ..., 'titles': ...,
    #  'itemsize': ...}
    # TODO: use TypedDict when/if it's officially supported
    Dict[
        str,
        Union[
            Sequence[str],  # names
            Sequence[_DtypeLikeNested],  # formats
            Sequence[int],  # offsets
            Sequence[Union[bytes, Text, None]],  # titles
            int,  # itemsize
        ],
    ],
    # {'field1': ..., 'field2': ..., ...}
    Dict[str, Tuple[_DtypeLikeNested, int]],
    # (base_dtype, new_dtype)
    Tuple[_DtypeLikeNested, _DtypeLikeNested],
]

# Can be used as such `Union[Sequence[T], _ArrayLikeSeq]` as ndarray
# is not a proper Sequence
# TODO: Specify the to-be returned array type once ndarray is a Generic
class _ArrayLikeSeq(Protocol):
    shape: Tuple[int, ...]
    def __array__(self, dtype: _DtypeLike = ...) -> ndarray: ...

_NdArraySubClass = TypeVar("_NdArraySubClass", bound=ndarray)

_ArrayLike = TypeVar("_ArrayLike")

_Generic = TypeVar("_Generic", bound=generic)
_Number = TypeVar("_Number", bound=number)

# In principle the SupportsInt, SupportsFloat, etc. protocols
# would be more suited here but they have one significant disadvatange:
# all these methods are also defined available in ndarray,
# which has no guarantee of being scalar-esque (i.e. a 0D array)
_ScalarNumeric = Union[int, float, complex, bool, bool_, number]

# Any scalar besides object, as the latter may or may not be a scalar
_ScalarAny = Union[_ScalarNumeric, str, bytes, dt.datetime, flexible, datetime64]

# TODO: Refine the _ArrayLikeSeq type once ndarray is a Generic
_ArrayLikeInt = TypeVar(
    "_ArrayLikeInt",
    bound=Union[int, integer, Sequence[Union[int, integer]], _ArrayLikeSeq],
)
_ArrayLikeBool = TypeVar(
    "_ArrayLikeBool",
    bound=Union[bool, bool_, Sequence[Union[bool, bool_]], _ArrayLikeSeq],
)

class dtype:
    names: Optional[Tuple[str, ...]]
    def __init__(
        self, obj: _DtypeLike, align: bool = ..., copy: bool = ...
    ) -> None: ...
    @property
    def alignment(self) -> int: ...
    @property
    def base(self) -> dtype: ...
    @property
    def byteorder(self) -> str: ...
    @property
    def char(self) -> str: ...
    @property
    def descr(self) -> List[Union[Tuple[str, str], Tuple[str, str, _Shape]]]: ...
    @property
    def fields(
        self,
    ) -> Optional[Mapping[str, Union[Tuple[dtype, int], Tuple[dtype, int, Any]]]]: ...
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
    def type(self) -> Type[generic]: ...

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

_ArraySelf = TypeVar("_ArraySelf", bound=_ArrayOrScalarCommon)

class _ArrayOrScalarCommon(
    SupportsInt, SupportsFloat, SupportsComplex, SupportsBytes, SupportsAbs[Any]
):
    @property
    def T(self: _ArraySelf) -> _ArraySelf: ...
    @property
    def base(self) -> Optional[ndarray]: ...
    @property
    def dtype(self) -> _Dtype: ...
    @property
    def data(self) -> memoryview: ...
    @property
    def flags(self) -> _flagsobj: ...
    @property
    def size(self) -> int: ...
    @property
    def itemsize(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    @property
    def ndim(self) -> int: ...
    @property
    def shape(self) -> _Shape: ...
    @property
    def strides(self) -> _Shape: ...
    def __array__(self, dtype: _DtypeLike = ...) -> ndarray: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __complex__(self) -> complex: ...
    if sys.version_info[0] < 3:
        def __oct__(self) -> str: ...
        def __hex__(self) -> str: ...
        def __nonzero__(self) -> bool: ...
        def __unicode__(self) -> Text: ...
    else:
        def __bool__(self) -> bool: ...
        def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __copy__(self: _ArraySelf, order: str = ...) -> _ArraySelf: ...
    def __deepcopy__(self: _ArraySelf, memo: dict) -> _ArraySelf: ...
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
    def __neg__(self: _ArraySelf) -> _ArraySelf: ...
    def __pos__(self: _ArraySelf) -> _ArraySelf: ...
    def __abs__(self: _ArraySelf) -> _ArraySelf: ...
    def __invert__(self: _ArraySelf) -> _ArraySelf: ...
    # TODO(shoyer): remove when all methods are defined
    def __getattr__(self, name) -> Any: ...

_BufferType = Union[ndarray, bytes, bytearray, memoryview]

class ndarray(_ArrayOrScalarCommon, Iterable, Sized, Container):
    real: ndarray
    imag: ndarray
    def __new__(
        cls,
        shape: Sequence[int],
        dtype: Union[_DtypeLike, str] = ...,
        buffer: _BufferType = ...,
        offset: int = ...,
        strides: _ShapeLike = ...,
        order: Optional[str] = ...,
    ) -> ndarray: ...
    @property
    def dtype(self) -> _Dtype: ...
    @property
    def ctypes(self) -> _ctypes: ...
    @property
    def shape(self) -> _Shape: ...
    @shape.setter
    def shape(self, value: _ShapeLike): ...
    @property
    def flat(self) -> flatiter: ...
    @property
    def strides(self) -> _Shape: ...
    @strides.setter
    def strides(self, value: _ShapeLike): ...
    # Array conversion
    @overload
    def item(self, *args: int) -> Any: ...
    @overload
    def item(self, args: Tuple[int, ...]) -> Any: ...
    def tolist(self) -> List[Any]: ...
    @overload
    def itemset(self, __value: Any) -> None: ...
    @overload
    def itemset(self, __item: _ShapeLike, __value: Any) -> None: ...
    def tostring(self, order: Optional[str] = ...) -> bytes: ...
    def tobytes(self, order: Optional[str] = ...) -> bytes: ...
    def tofile(
        self, fid: Union[IO[bytes], str], sep: str = ..., format: str = ...
    ) -> None: ...
    def dump(self, file: str) -> None: ...
    def dumps(self) -> bytes: ...
    def astype(
        self,
        dtype: _DtypeLike,
        order: str = ...,
        casting: str = ...,
        subok: bool = ...,
        copy: bool = ...,
    ) -> ndarray: ...
    def byteswap(self, inplace: bool = ...) -> ndarray: ...
    def copy(self, order: str = ...) -> ndarray: ...
    @overload
    def view(self, dtype: Type[_NdArraySubClass]) -> _NdArraySubClass: ...
    @overload
    def view(self, dtype: _DtypeLike = ...) -> ndarray: ...
    @overload
    def view(
        self, dtype: _DtypeLike, type: Type[_NdArraySubClass]
    ) -> _NdArraySubClass: ...
    @overload
    def view(self, *, type: Type[_NdArraySubClass]) -> _NdArraySubClass: ...
    def getfield(self, dtype: Union[_DtypeLike, str], offset: int = ...) -> ndarray: ...
    def setflags(
        self, write: bool = ..., align: bool = ..., uic: bool = ...
    ) -> None: ...
    def fill(self, value: Any) -> None: ...
    # Shape manipulation
    @overload
    def reshape(self, shape: Sequence[int], *, order: str = ...) -> ndarray: ...
    @overload
    def reshape(self, *shape: int, order: str = ...) -> ndarray: ...
    @overload
    def resize(self, new_shape: Sequence[int], *, refcheck: bool = ...) -> None: ...
    @overload
    def resize(self, *new_shape: int, refcheck: bool = ...) -> None: ...
    @overload
    def transpose(self, axes: Sequence[int]) -> ndarray: ...
    @overload
    def transpose(self, *axes: int) -> ndarray: ...
    def swapaxes(self, axis1: int, axis2: int) -> ndarray: ...
    def flatten(self, order: str = ...) -> ndarray: ...
    def ravel(self, order: str = ...) -> ndarray: ...
    def squeeze(self, axis: Union[int, Tuple[int, ...]] = ...) -> ndarray: ...
    # Many of these special methods are irrelevant currently, since protocols
    # aren't supported yet. That said, I'm adding them for completeness.
    # https://docs.python.org/3/reference/datamodel.html
    def __len__(self) -> int: ...
    def __getitem__(self, key) -> Any: ...
    def __setitem__(self, key, value): ...
    def __iter__(self) -> Any: ...
    def __contains__(self, key) -> bool: ...
    def __index__(self) -> int: ...

class generic(_ArrayOrScalarCommon):
    def __init__(self, value: Any = ...) -> None: ...
    @property
    def base(self) -> None: ...

class _real_generic(generic):
    @property
    def real(self: _ArraySelf) -> _ArraySelf: ...
    @property
    def imag(self: _ArraySelf) -> _ArraySelf: ...

class number(generic):
    def __init__(self, value: Union[SupportsInt, SupportsFloat] = ...) -> None: ...

class bool_(_real_generic): ...
class object_(generic): ...

class datetime64:
    @overload
    def __init__(
        self, _data: Union[datetime64, str, dt.datetime] = ..., _format: str = ...
    ) -> None: ...
    @overload
    def __init__(self, _data: int, _format: str) -> None: ...
    def __add__(self, other: Union[timedelta64, int]) -> datetime64: ...
    def __sub__(self, other: Union[timedelta64, datetime64, int]) -> timedelta64: ...

class integer(number, _real_generic): ...
class signedinteger(integer): ...
class int8(signedinteger): ...
class int16(signedinteger): ...
class int32(signedinteger): ...
class int64(signedinteger): ...

class timedelta64(signedinteger):
    def __init__(self, _data: Any = ..., _format: str = ...) -> None: ...
    @overload
    def __add__(self, other: Union[timedelta64, int]) -> timedelta64: ...
    @overload
    def __add__(self, other: datetime64) -> datetime64: ...
    def __sub__(self, other: Union[timedelta64, int]) -> timedelta64: ...
    if sys.version_info[0] < 3:
        @overload
        def __div__(self, other: timedelta64) -> float: ...
        @overload
        def __div__(self, other: float) -> timedelta64: ...
    @overload
    def __truediv__(self, other: timedelta64) -> float: ...
    @overload
    def __truediv__(self, other: float) -> timedelta64: ...
    def __mod__(self, other: timedelta64) -> timedelta64: ...

class unsignedinteger(integer): ...
class uint8(unsignedinteger): ...
class uint16(unsignedinteger): ...
class uint32(unsignedinteger): ...
class uint64(unsignedinteger): ...
class inexact(number): ...
class floating(inexact, _real_generic): ...
class float16(floating): ...
class float32(floating): ...
class float64(floating): ...

class complexfloating(inexact):
    def __init__(
        self, value: Union[SupportsInt, SupportsFloat, SupportsComplex, complex] = ...
    ) -> None: ...

class complex64(complexfloating):
    @property
    def real(self) -> float32: ...
    @property
    def imag(self) -> float32: ...

class complex128(complexfloating):
    @property
    def real(self) -> float64: ...
    @property
    def imag(self) -> float64: ...

class flexible(_real_generic): ...
class void(flexible): ...
class character(_real_generic): ...
class bytes_(character): ...
class str_(character): ...

# TODO(alan): Platform dependent types
# longcomplex, longdouble, longfloat
# bytes, short, intc, intp, longlong
# half, single, double, longdouble
# uint_, int_, float_, complex_
# float128, complex256
# float96

def array(
    object: object,
    dtype: _DtypeLike = ...,
    copy: bool = ...,
    subok: bool = ...,
    ndmin: int = ...,
) -> ndarray: ...
def zeros(
    shape: _ShapeLike, dtype: _DtypeLike = ..., order: Optional[str] = ...
) -> ndarray: ...
def ones(
    shape: _ShapeLike, dtype: _DtypeLike = ..., order: Optional[str] = ...
) -> ndarray: ...
def zeros_like(
    a: _ArrayLike,
    dtype: Optional[dtype] = ...,
    order: str = ...,
    subok: bool = ...,
    shape: Optional[Union[int, Sequence[int]]] = ...,
) -> ndarray: ...
def ones_like(
    a: _ArrayLike,
    dtype: Optional[dtype] = ...,
    order: str = ...,
    subok: bool = ...,
    shape: Optional[_ShapeLike] = ...,
) -> ndarray[int]: ...
def full(
    shape: _ShapeLike, fill_value: Any, dtype: Optional[dtype] = ..., order: str = ...
) -> ndarray: ...
def full_like(
    a: _ArrayLike,
    fill_value: Any,
    dtype: Optional[dtype] = ...,
    order: str = ...,
    subok: bool = ...,
    shape: Optional[_ShapeLike] = ...,
) -> ndarray: ...
def count_nonzero(
    a: _ArrayLike, axis: Optional[Union[int, Tuple[int], Tuple[int, int]]] = ...
) -> Union[int, ndarray]: ...
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
) -> ndarray: ...
def rollaxis(a: _ArrayLike, axis: int, start: int = ...) -> ndarray: ...
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
) -> Union[bool_, ndarray]: ...
def array_equal(a1: _ArrayLike, a2: _ArrayLike) -> bool: ...
def array_equiv(a1: _ArrayLike, a2: _ArrayLike) -> bool: ...

#
# Constants
#

Inf: float
Infinity: float
NAN: float
NINF: float
NZERO: float
NaN: float
PINF: float
PZERO: float
e: float
euler_gamma: float
inf: float
infty: float
nan: float
pi: float

ALLOW_THREADS: int
BUFSIZE: int
CLIP: int
ERR_CALL: int
ERR_DEFAULT: int
ERR_IGNORE: int
ERR_LOG: int
ERR_PRINT: int
ERR_RAISE: int
ERR_WARN: int
FLOATING_POINT_SUPPORT: int
FPE_DIVIDEBYZERO: int
FPE_INVALID: int
FPE_OVERFLOW: int
FPE_UNDERFLOW: int
MAXDIMS: int
MAY_SHARE_BOUNDS: int
MAY_SHARE_EXACT: int
RAISE: int
SHIFT_DIVIDEBYZERO: int
SHIFT_INVALID: int
SHIFT_OVERFLOW: int
SHIFT_UNDERFLOW: int
UFUNC_BUFSIZE_DEFAULT: int
WRAP: int
little_endian: int
tracemalloc_domain: int

class ufunc:
    @property
    def __name__(self) -> str: ...
    def __call__(
        self,
        *args: _ArrayLike,
        out: Optional[Union[ndarray, Tuple[ndarray, ...]]] = ...,
        where: Optional[ndarray] = ...,
        # The list should be a list of tuples of ints, but since we
        # don't know the signature it would need to be
        # Tuple[int, ...]. But, since List is invariant something like
        # e.g. List[Tuple[int, int]] isn't a subtype of
        # List[Tuple[int, ...]], so we can't type precisely here.
        axes: List[Any] = ...,
        axis: int = ...,
        keepdims: bool = ...,
        # TODO: make this precise when we can use Literal.
        casting: str = ...,
        # TODO: make this precise when we can use Literal.
        order: Optional[str] = ...,
        dtype: Optional[_DtypeLike] = ...,
        subok: bool = ...,
        signature: Union[str, Tuple[str]] = ...,
        # In reality this should be a length of list 3 containing an
        # int, an int, and a callable, but there's no way to express
        # that.
        extobj: List[Union[int, Callable]] = ...,
    ) -> Union[ndarray, generic]: ...
    @property
    def nin(self) -> int: ...
    @property
    def nout(self) -> int: ...
    @property
    def nargs(self) -> int: ...
    @property
    def ntypes(self) -> int: ...
    @property
    def types(self) -> List[str]: ...
    # Broad return type because it has to encompass things like
    #
    # >>> np.logical_and.identity is True
    # True
    # >>> np.add.identity is 0
    # True
    # >>> np.sin.identity is None
    # True
    #
    # and any user-defined ufuncs.
    @property
    def identity(self) -> Any: ...
    # This is None for ufuncs and a string for gufuncs.
    @property
    def signature(self) -> Optional[str]: ...
    # The next four methods will always exist, but they will just
    # raise a ValueError ufuncs with that don't accept two input
    # arguments and return one output argument. Because of that we
    # can't type them very precisely.
    @property
    def reduce(self) -> Any: ...
    @property
    def accumulate(self) -> Any: ...
    @property
    def reduceat(self) -> Any: ...
    @property
    def outer(self) -> Any: ...
    # Similarly at won't be defined for ufuncs that return multiple
    # outputs, so we can't type it very precisely.
    @property
    def at(self) -> Any: ...

absolute: ufunc
add: ufunc
arccos: ufunc
arccosh: ufunc
arcsin: ufunc
arcsinh: ufunc
arctan2: ufunc
arctan: ufunc
arctanh: ufunc
bitwise_and: ufunc
bitwise_or: ufunc
bitwise_xor: ufunc
cbrt: ufunc
ceil: ufunc
conjugate: ufunc
copysign: ufunc
cos: ufunc
cosh: ufunc
deg2rad: ufunc
degrees: ufunc
divmod: ufunc
equal: ufunc
exp2: ufunc
exp: ufunc
expm1: ufunc
fabs: ufunc
float_power: ufunc
floor: ufunc
floor_divide: ufunc
fmax: ufunc
fmin: ufunc
fmod: ufunc
frexp: ufunc
gcd: ufunc
greater: ufunc
greater_equal: ufunc
heaviside: ufunc
hypot: ufunc
invert: ufunc
isfinite: ufunc
isinf: ufunc
isnan: ufunc
isnat: ufunc
lcm: ufunc
ldexp: ufunc
left_shift: ufunc
less: ufunc
less_equal: ufunc
log10: ufunc
log1p: ufunc
log2: ufunc
log: ufunc
logaddexp2: ufunc
logaddexp: ufunc
logical_and: ufunc
logical_not: ufunc
logical_or: ufunc
logical_xor: ufunc
matmul: ufunc
maximum: ufunc
minimum: ufunc
modf: ufunc
multiply: ufunc
negative: ufunc
nextafter: ufunc
not_equal: ufunc
positive: ufunc
power: ufunc
rad2deg: ufunc
radians: ufunc
reciprocal: ufunc
remainder: ufunc
right_shift: ufunc
rint: ufunc
sign: ufunc
signbit: ufunc
sin: ufunc
sinh: ufunc
spacing: ufunc
sqrt: ufunc
square: ufunc
subtract: ufunc
tan: ufunc
tanh: ufunc
true_divide: ufunc
trunc: ufunc

# TODO(shoyer): remove when the full numpy namespace is defined
def __getattr__(name: str) -> Any: ...

# Warnings
class ModuleDeprecationWarning(DeprecationWarning): ...
class VisibleDeprecationWarning(UserWarning): ...
class ComplexWarning(RuntimeWarning): ...
class RankWarning(UserWarning): ...

# Errors
class TooHardError(RuntimeError): ...

class AxisError(ValueError, IndexError):
    def __init__(
        self, axis: int, ndim: Optional[int] = ..., msg_prefix: Optional[str] = ...
    ) -> None: ...

# Functions from np.core.fromnumeric
_Mode = Literal["raise", "wrap", "clip"]
_Order = Literal["C", "F", "A"]
_PartitionKind = Literal["introselect"]
_SortKind = Literal["quicksort", "mergesort", "heapsort", "stable"]
_Side = Literal["left", "right"]

# The actual functions
@overload
def take(
    a: _Generic,
    indices: int,
    axis: Optional[int] = ...,
    out: Optional[ndarray] = ...,
    mode: _Mode = ...,
) -> _Generic: ...
@overload
def take(
    a: _ScalarAny,
    indices: int,
    axis: Optional[int] = ...,
    out: Optional[ndarray] = ...,
    mode: _Mode = ...,
) -> generic: ...
@overload
def take(
    a: _ArrayLike,
    indices: int,
    axis: Optional[int] = ...,
    out: Optional[ndarray] = ...,
    mode: _Mode = ...,
) -> generic: ...
@overload
def take(
    a: _ArrayLike,
    indices: _ArrayLikeInt,
    axis: Optional[int] = ...,
    out: Optional[ndarray] = ...,
    mode: _Mode = ...,
) -> Union[generic, ndarray]: ...
def reshape(a: _ArrayLike, newshape: _ShapeLike, order: _Order = ...) -> ndarray: ...
@overload
def choose(
    a: _Generic,
    choices: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    out: Optional[ndarray] = ...,
    mode: _Mode = ...,
) -> _Generic: ...
@overload
def choose(
    a: _ScalarAny,
    choices: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    out: Optional[ndarray] = ...,
    mode: _Mode = ...,
) -> generic: ...
@overload
def choose(
    a: _ArrayLike,
    choices: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    out: Optional[ndarray] = ...,
    mode: _Mode = ...,
) -> ndarray: ...
def repeat(
    a: _ArrayLike, repeats: _ArrayLikeInt, axis: Optional[int] = ...
) -> ndarray: ...
def put(a: ndarray, ind: _ArrayLikeInt, v: _ArrayLike, mode: _Mode = ...) -> None: ...
def swapaxes(
    a: Union[Sequence[_ArrayLike], _ArrayLikeSeq], axis1: int, axis2: int
) -> ndarray: ...
def transpose(
    a: _ArrayLike, axes: Union[None, Sequence[int], _ArrayLikeSeq] = ...,
) -> ndarray: ...
def partition(
    a: _ArrayLike,
    kth: _ArrayLikeInt,
    axis: Optional[int] = ...,
    kind: _PartitionKind = ...,
    order: Union[None, str, Sequence[str], _ArrayLikeSeq] = ...,
) -> ndarray: ...
def argpartition(
    a: _ArrayLike,
    kth: _ArrayLikeInt,
    axis: Optional[int] = ...,
    kind: _PartitionKind = ...,
    order: Union[None, str, Sequence[str], _ArrayLikeSeq] = ...,
) -> ndarray: ...
def sort(
    a: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    axis: Optional[int] = ...,
    kind: Optional[_SortKind] = ...,
    order: Union[None, str, Sequence[str], _ArrayLikeSeq] = ...,
) -> ndarray: ...
def argsort(
    a: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    axis: Optional[int] = ...,
    kind: Optional[_SortKind] = ...,
    order: Union[None, str, Sequence[str], _ArrayLikeSeq] = ...,
) -> ndarray: ...
@overload
def argmax(
    a: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    axis: None = ...,
    out: Optional[ndarray] = ...,
) -> integer: ...
@overload
def argmax(
    a: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    axis: int = ...,
    out: Optional[ndarray] = ...,
) -> Union[integer, ndarray]: ...
@overload
def argmin(
    a: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    axis: None = ...,
    out: Optional[ndarray] = ...,
) -> integer: ...
@overload
def argmin(
    a: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    axis: int = ...,
    out: Optional[ndarray] = ...,
) -> Union[integer, ndarray]: ...
@overload
def searchsorted(
    a: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    v: _ScalarAny,
    side: _Side = ...,
    sorter: Optional[_ArrayLikeInt] = ...,
) -> integer: ...
@overload
def searchsorted(
    a: Union[Sequence[_ArrayLike], _ArrayLikeSeq],
    v: _ArrayLike,
    side: _Side = ...,
    sorter: Optional[_ArrayLikeInt] = ...,
) -> ndarray: ...
def resize(a: _ArrayLike, new_shape: _ShapeLike) -> ndarray: ...
def squeeze(a: _ArrayLike, axis: Optional[_ShapeLike] = ...) -> ndarray: ...
def diagonal(
    a: Union[
        Sequence[Sequence[_ArrayLike]], _ArrayLikeSeq
    ],  # TODO: requires a >= 2D array
    offset: int = ...,
    axis1: int = ...,
    axis2: int = ...,
) -> ndarray: ...
def trace(
    a: Union[
        Sequence[Sequence[_ArrayLike]], _ArrayLikeSeq
    ],  # TODO: requires a >= 2D array
    offset: int = ...,
    axis1: int = ...,
    axis2: int = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
) -> Union[number, ndarray]: ...
def ravel(a: _ArrayLike, order: _Order = ...) -> ndarray: ...
def nonzero(a: _ArrayLike) -> Tuple[ndarray, ...]: ...
def shape(a: _ArrayLike) -> _Shape: ...
def compress(
    condition: Union[Sequence[_ArrayLikeBool], _ArrayLikeSeq],
    a: _ArrayLike,
    axis: Optional[int] = ...,
    out: Optional[ndarray] = ...,
) -> ndarray: ...
@overload
def clip(
    a: _Number,
    a_min: _ScalarNumeric,
    a_max: _ScalarNumeric,
    out: Optional[ndarray] = ...,
    **kwargs: Any,
) -> _Number: ...
@overload
def clip(
    a: _ScalarNumeric,
    a_min: _ScalarNumeric,
    a_max: _ScalarNumeric,
    out: Optional[ndarray] = ...,
    **kwargs: Any,
) -> number: ...
@overload
def clip(
    a: _ArrayLike,
    a_min: _ArrayLike,
    a_max: _ArrayLike,
    out: Optional[ndarray] = ...,
    **kwargs: Any,
) -> Union[number, ndarray]: ...
@overload
def sum(
    a: _Number,
    axis: Optional[_ShapeLike] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> _Number: ...
@overload
def sum(
    a: _ScalarNumeric,
    axis: Optional[_ShapeLike] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> number: ...
@overload
def sum(
    a: _ArrayLike,
    axis: None = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> number: ...
@overload
def sum(
    a: _ArrayLike,
    axis: _ShapeLike = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> Union[number, ndarray]: ...
@overload
def all(
    a: _ScalarNumeric,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
) -> bool_: ...
@overload
def all(
    a: _ArrayLike,
    axis: None = ...,
    out: Optional[ndarray] = ...,
    keepdims: Literal[False] = ...,
) -> bool_: ...
@overload
def all(
    a: _ArrayLike,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
) -> Union[bool_, ndarray]: ...
@overload
def any(
    a: _ScalarNumeric,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
) -> bool_: ...
@overload
def any(
    a: _ArrayLike,
    axis: None = ...,
    out: Optional[ndarray] = ...,
    keepdims: Literal[False] = ...,
) -> bool_: ...
@overload
def any(
    a: _ArrayLike,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
) -> Union[bool_, ndarray]: ...
def cumsum(
    a: _ArrayLike,
    axis: Optional[int] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
) -> ndarray: ...
@overload
def ptp(
    a: _Number,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
) -> _Number: ...
@overload
def ptp(
    a: _ScalarNumeric,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
) -> number: ...
@overload
def ptp(
    a: _ArrayLike,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
) -> Union[number, ndarray]: ...
@overload
def amax(
    a: _ScalarNumeric,
    axis: Optional[int] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> integer: ...
@overload
def amax(
    a: _ArrayLike,
    axis: None = ...,
    out: Optional[ndarray] = ...,
    keepdims: Literal[False] = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> integer: ...
@overload
def amax(
    a: _ArrayLike,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> Union[integer, ndarray]: ...
@overload
def amin(
    a: _ScalarNumeric,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> integer: ...
@overload
def amin(
    a: _ArrayLike,
    axis: None = ...,
    out: Optional[ndarray] = ...,
    keepdims: Literal[False] = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> integer: ...
@overload
def amin(
    a: _ArrayLike,
    axis: Optional[_ShapeLike] = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> Union[integer, ndarray]: ...
def alen(a: _ArrayLike) -> int: ...
@overload
def prod(
    a: _Number,
    axis: Optional[_ShapeLike] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> _Number: ...
@overload
def prod(
    a: _ScalarNumeric,
    axis: Optional[_ShapeLike] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> number: ...
@overload
def prod(
    a: _ArrayLike,
    axis: None = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: Literal[False] = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> number: ...
@overload
def prod(
    a: _ArrayLike,
    axis: Optional[_ShapeLike] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
    initial: _ScalarNumeric = ...,
    where: _ArrayLikeBool = ...,
) -> Union[number, ndarray]: ...
def cumprod(
    a: _ArrayLike,
    axis: Optional[int] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
) -> ndarray: ...
def ndim(a: _ArrayLike) -> int: ...
def size(a: _ArrayLike, axis: Optional[int] = ...) -> int: ...
@overload
def around(
    a: _Number, decimals: int = ..., out: Optional[ndarray] = ...
) -> _Number: ...
@overload
def around(
    a: _ScalarNumeric, decimals: int = ..., out: Optional[ndarray] = ...
) -> number: ...
@overload
def around(
    a: _ArrayLike, decimals: int = ..., out: Optional[ndarray] = ...
) -> ndarray: ...
@overload
def mean(
    a: _ScalarNumeric,
    axis: None = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: Literal[False] = ...,
) -> number: ...  # TODO: The type of the output is determined by *dtype*
@overload
def mean(
    a: _ArrayLike,
    axis: None = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: Literal[False] = ...,
) -> number: ...
@overload
def mean(
    a: _ArrayLike,
    axis: Optional[_ShapeLike] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    keepdims: bool = ...,
) -> Union[number, ndarray]: ...
@overload
def std(
    a: _ScalarNumeric,
    axis: None = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    ddof: int = ...,
    keepdims: Literal[False] = ...,
) -> number: ...  # TODO: The type of the output is determined by *dtype*
@overload
def std(
    a: _ArrayLike,
    axis: None = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    ddof: int = ...,
    keepdims: Literal[False] = ...,
) -> number: ...
@overload
def std(
    a: _ArrayLike,
    axis: Optional[_ShapeLike] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    ddof: int = ...,
    keepdims: bool = ...,
) -> Union[number, ndarray]: ...
@overload
def var(
    a: _ScalarNumeric,
    axis: None = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    ddof: int = ...,
    keepdims: bool = ...,
) -> number: ...
@overload
def var(
    a: _ArrayLike,
    axis: None = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    ddof: int = ...,
    keepdims: Literal[False] = ...,
) -> number: ...  # TODO: The type of the output is determined by *dtype*
@overload
def var(
    a: _ArrayLike,
    axis: Optional[_ShapeLike] = ...,
    dtype: _DtypeLike = ...,
    out: Optional[ndarray] = ...,
    ddof: int = ...,
    keepdims: bool = ...,
) -> Union[number, ndarray]: ...

round_ = around
product = prod
cumproduct = cumprod
sometrue = any
alltrue = all
