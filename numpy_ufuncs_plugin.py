from mypy.nodes import ARG_POS
from mypy.plugin import Plugin
from mypy.types import CallableType


def ufunc_call_hook(ctx):
    ufunc_name = ctx.context.callee.name

    type_info = ctx.type.serialize()
    nin_arg, nout_arg = type_info['args']
    if nin_arg['.class'] != 'LiteralType':
        return ctx.default_signature
    if nout_arg['.class'] != 'LiteralType':
        return ctx.default_signature

    nin = nin_arg['value']
    nout = nout_arg['value']

    # Strip off the *args and replace it with the correct number of
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
    return ctx.default_signature.copy_modified(
        arg_kinds=arg_kinds,
        arg_names=arg_names,
        arg_types=arg_types,
    )


class UFuncPlugin(Plugin):
    def get_method_signature_hook(self, method):
        if method == 'numpy.ufunc.__call__':
            return ufunc_call_hook


def plugin(version):
    return UFuncPlugin
