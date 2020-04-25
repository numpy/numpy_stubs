"""Tests for :mod:`numpy.core.fromnumeric`."""

import numpy as np

A = np.array(True, ndmin=2, dtype=bool)
A.setflags(write=False)

a = np.bool_(True)

np.take(a, None)  # E: No overload variant of "take" matches argument type
np.take(a, axis=1.0)  # E: No overload variant of "take" matches argument type
np.take(A, out=1)  # E: No overload variant of "take" matches argument type
np.take(A, mode="bob")  # E: No overload variant of "take" matches argument type

np.reshape(a, None)  # E: Argument 2 to "reshape" has incompatible type
np.reshape(A, 1, order="bob")  # E: Argument "order" to "reshape" has incompatible type

np.choose(a, None)  # E: No overload variant of "choose" matches argument type
np.choose(a, out=1.0)  # E: No overload variant of "choose" matches argument type
np.choose(A, mode="bob")  # E: No overload variant of "choose" matches argument type

np.repeat(a, None)  # E: Argument 2 to "repeat" has incompatible type
np.repeat(A, 1, axis=1.0)  # E: Argument "axis" to "repeat" has incompatible type

np.swapaxes(a, 0, 0)  # E: Argument 1 to "swapaxes" has incompatible type
np.swapaxes(A, None, 1)  # E: Argument 2 to "swapaxes" has incompatible type
np.swapaxes(A, 1, [0])  # E: Argument 3 to "swapaxes" has incompatible type

np.transpose(a, axes=1)  # E: Argument "axes" to "transpose" has incompatible type
np.transpose(A, axes=1.0)  # E: Argument "axes" to "transpose" has incompatible type

np.partition(a, None)  # E: Argument 2 to "partition" has incompatible type
np.partition(
    a, 0, axis="bob"  # E: Argument "axis" to "partition" has incompatible type
)
np.partition(
    A, 0, kind="bob"  # E: Argument "kind" to "partition" has incompatible type
)
np.partition(
    A, 0, order=range(5)  # E: Argument "order" to "partition" has incompatible type
)

np.argpartition(  # E: No overload variant of "argpartition" matches argument type
    a, None
)
np.argpartition(  # E: No overload variant of "argpartition" matches argument type
    a, 0, axis="bob"
)
np.argpartition(  # E: No overload variant of "argpartition" matches argument type
    A, 0, kind="bob"
)
np.argpartition(
    A, 0, order=range(5)  # E: Argument "order" to "argpartition" has incompatible type
)

np.sort(a)  # E: Argument 1 to "sort" has incompatible type
np.sort(A, axis="bob")  # E: Argument "axis" to "sort" has incompatible type
np.sort(A, kind="bob")  # E: Argument "kind" to "sort" has incompatible type
np.sort(A, order=range(5))  # E: Argument "order" to "sort" has incompatible type

np.argsort(a)  # E: Argument 1 to "argsort" has incompatible type
np.argsort(A, axis="bob")  # E: Argument "axis" to "argsort" has incompatible type
np.argsort(A, kind="bob")  # E: Argument "kind" to "argsort" has incompatible type
np.argsort(A, order=range(5))  # E: Argument "order" to "argsort" has incompatible type
