import os
from typing import Iterator, List
import itertools

from generate.utils import Arg, Func, SELF, STUB_DIR

SIZE = Arg(name="size", ty="_Size", optional=False)
NOSIZE = Arg(name="size", ty="None", optional=True)


def distribution(name: str, return_type: str, *args: Arg) -> Iterator[Func]:
    def func(return_type: str, args: List[Arg], size: bool) -> Func:
        args = [SELF] + list(args)
        if size:
            args.append(SIZE)
        else:
            args.append(NOSIZE)
        return Func(name, return_type, args, overload=True)

    yield func(return_type, args, size=False)
    yield func(
        "ndarray",
        [Arg(arg.name, f"_ScalarOrArray[{arg.ty}]") for arg in args],
        size=True,
    )

    for i in range(len(args)):
        for combo in itertools.combinations(args, i + 1):
            yield func(
                "ndarray",
                [
                    Arg(
                        arg.name,
                        f"_ArrayLike[{arg.ty}]" if arg in combo else arg.ty,
                        optional=False,
                    )
                    for arg in args
                ],
                size=False,
            )


functions = list(
    distribution("beta", "float", Arg("a", "float"), Arg("b", "float"))
)
functions.append(Func("bytes", "builtins.bytes", [SELF, Arg("length", "int")]))
functions += list(
    distribution("binomial", "int", Arg("n", "int"), Arg("p", "float"))
)
functions += list(distribution("chisquared", "float", Arg("df", "int")))


def choice(return_type: str, ty: str, size: bool) -> Func:
    return Func(
        "choice",
        return_type,
        [
            SELF,
            Arg("a", ty),
            SIZE if size else NOSIZE,
            Arg("replace", "bool", True),
            Arg("p", "Optional[_ArrayLike[float]]", True),
        ],
        overload=True,
    )


functions += [
    choice("int", "int", False),
    choice("_T", "Sequence[_T]", False),
    choice("Any", "ndarray", False),
    choice("ndarray", "Union[int, ndarray]", True),
]
functions.append(
    Func(
        "dirichlet",
        "ndarray",
        [
            SELF,
            Arg("alpha", "_ArrayLike[float]"),
            Arg("size", "Optional[_Size]", True),
        ],
    )
)
functions += list(
    distribution("exponential", "float", Arg("scale", "float", True))
)
functions += list(
    distribution("f", "float", Arg("dfnum", "float"), Arg("dfden", "float"))
)
functions += list(
    distribution(
        "gamma", "float", Arg("shape", "float"), Arg("scale", "float", True)
    )
)
functions += list(distribution("geometric", "float", Arg("p", "float")))
functions.append(
    Func("get_state", "Tuple[str, ndarray, int, int, float]", [SELF])
)
functions += list(
    distribution(
        "gumbel",
        "float",
        Arg("loc", "float", True),
        Arg("scale", "float", True),
    )
)
functions += list(
    distribution(
        "hypergeometric",
        "int",
        Arg("ngood", "int"),
        Arg("nbad", "int"),
        Arg("nsample", "int"),
    )
)
functions += list(
    distribution(
        "laplace",
        "float",
        Arg("loc", "float", True),
        Arg("scale", "float", True),
    )
)
functions += list(
    distribution(
        "logistic",
        "float",
        Arg("loc", "float", True),
        Arg("scale", "float", True),
    )
)
functions += list(
    distribution(
        "lognormal",
        "float",
        Arg("mean", "float", True),
        Arg("sigma", "float", True),
    )
)
functions += list(distribution("logseries", "int", Arg("p", "float")))
functions.append(
    Func(
        "multinomial",
        "ndarray",
        [SELF, Arg("n", "int"), Arg("size", "Optional[_Size]", True)],
    )
)
functions.append(
    Func(
        "multivariate_normal",
        "ndarray",
        [
            SELF,
            Arg("mean", "ndarray"),
            Arg("cov", "ndarray"),
            Arg("size", "Optional[_Size]", True),
            Arg("check_valid", "str", True),
            Arg("tol", "float", True),
        ],
    )
)
functions += list(
    distribution(
        "negative_binomial", "int", Arg("n", "int"), Arg("p", "float")
    )
)
functions += list(
    distribution(
        "noncentral_chisquare",
        "float",
        Arg("df", "float"),
        Arg("nonc", "float"),
    )
)
functions += list(
    distribution(
        "noncentral_f",
        "float",
        Arg("dfnum", "float"),
        Arg("dfden", "float"),
        Arg("nonc", "float"),
    )
)
functions += list(
    distribution(
        "normal",
        "float",
        Arg("loc", "float", True),
        Arg("scale", "float", True),
    )
)
functions += list(distribution("pareto", "float", Arg("a", "float")))
functions.append(
    Func("permutation", "ndarray", [SELF, Arg("x", "Union[int, ndarray]")])
)
functions += list(distribution("poisson", "float", Arg("lam", "float", True)))
functions += list(distribution("power", "float", Arg("a", "float")))
functions += [
    Func("rand", "float", [SELF], overload=True),
    Func(
        "rand",
        "ndarray",
        [SELF, Arg("d0", "int"), Arg("*dn", "int")],
        overload=True,
    ),
]
# TODO(alan): dtype parameter
functions += list(
    distribution("randint", "int", Arg("low", "int"), Arg("high", "int", True))
)
functions += [
    Func("randn", "float", [SELF], overload=True),
    Func(
        "randn",
        "ndarray",
        [SELF, Arg("d0", "int"), Arg("*dn", "int")],
        overload=True,
    ),
]
functions += list(
    distribution(
        "random_integers", "int", Arg("low", "int"), Arg("high", "int", True)
    )
)
functions += list(distribution("random_sample", "int"))
functions += list(distribution("rayleigh", "float", Arg("scale", "float")))
functions += [
    Func(
        "seed",
        "None",
        [SELF, Arg("seed", "Union[None, int, Tuple[int], List[int]]", True)],
    ),
    Func(
        "set_state",
        "None",
        [SELF, Arg("state", "Tuple[str, ndarray, int, int, float]")],
    ),
    Func("shuffle", "None", [SELF, Arg("x", "_ArrayLike[Any]")]),
]
functions += list(distribution("standard_cauchy", "float"))
functions += list(distribution("standard_exponential", "float"))
functions += list(distribution("standard_gamma", "float"))
functions += list(distribution("standard_normal", "float"))
functions += list(distribution("standard_t", "float", Arg("t", "int")))
functions += list(distribution("tomaxint", "int", Arg("t", "int")))
functions += list(
    distribution(
        "triangular",
        "float",
        Arg("left", "float"),
        Arg("mode", "float"),
        Arg("right", "float"),
    )
)
functions += list(
    distribution(
        "uniform",
        "float",
        Arg("low", "float", True),
        Arg("high", "float", True),
    )
)
functions += list(
    distribution(
        "vonmises", "float", Arg("mu", "float"), Arg("kappa", "float")
    )
)
functions += list(
    distribution("wald", "float", Arg("mean", "float"), Arg("scale", "float"))
)
functions += list(distribution("weibull", "float", Arg("a", "float")))
functions += list(distribution("zipf", "int", Arg("a", "float")))


imports = """\
import builtins
from typing import (
    Any, List, overload, Optional, Sequence, Tuple, TypeVar, Union
)
from numpy import ndarray
"""

typevars = """\
_Size = Union[int, Sequence[int]]
_T = TypeVar("_T")
_ArrayLike = Union[Sequence[_T], ndarray]
_ScalarOrArray = Union[_T, Sequence[_T], ndarray]
"""

with open(os.path.join(STUB_DIR, "random", "mtrand.pyi"), "w") as fout:
    fout.write(imports)
    fout.write(typevars)
    fout.write(
        """
class RandomState:
    def __init__(
        self, state: Union[None, int, List[int], Tuple[int]] = ...
    ) -> None: ...
"""
    )
    prev = None
    for func in functions:
        if func.name != prev:
            fout.write("\n")
        prev = func.name
        fout.write(func.render(indent=4))

with open(os.path.join(STUB_DIR, "random", "__init__.pyi"), "w") as fout:
    fout.write(imports)
    fout.write("from . import mtrand\n")
    fout.write(typevars)
    fout.write(
        """\
RandomState = mtrand.RandomState
"""
    )

    prev = None
    for func in functions:
        if func.name != prev:
            fout.write("\n")
        prev = func.name

        # Leave out first argument (SELF)
        assert func.args[0] == SELF
        func = Func(func.name, func.return_type, func.args[1:], func.overload)
        fout.write(func.render())
