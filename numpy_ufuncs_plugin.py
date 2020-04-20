from mypy.nodes import ARG_POS
from mypy.plugin import Plugin
import mypy.types
from mypy.types import CallableType, LiteralType, TupleType, UnionType


def ufunc_call_hook(ctx):
    nin_arg, nout_arg = ctx.type.args
    if not isinstance(nin_arg, LiteralType):
        # Not a literal; we can't make the signature any more precise.
        return ctx.default_signature
    if not isinstance(nout_arg, LiteralType):
        return ctx.default_signature
    nin, nout = nin_arg.value, nout_arg.value

    # Strip off *args and replace it with the correct number of
    # positional arguments.
    arg_kinds = [ARG_POS] * nin + ctx.default_signature.arg_kinds[1:]
    arg_names = (
        [f'x{i}' for i in range(nin)] +
        ctx.default_signature.arg_names[1:]
    )
    arg_types = (
        [ctx.default_signature.arg_types[0]] * nin +
        ctx.default_signature.arg_types[1:]
    )
    ndarray_type, generic_type, _ = ctx.default_signature.ret_type.items
    scalar_or_ndarray = UnionType([ndarray_type, generic_type])
    if nout == 1:
        ret_type = scalar_or_ndarray
    else:
        ret_type = TupleType([scalar_or_ndarray] * nout)

    return ctx.default_signature.copy_modified(
        arg_kinds=arg_kinds,
        arg_names=arg_names,
        arg_types=arg_types,
        ret_type=ret_type,
    )


class UFuncPlugin(Plugin):
    def get_method_signature_hook(self, method):
        if method == 'numpy.ufunc.__call__':
            return ufunc_call_hook


def plugin(version):
    return UFuncPlugin
