"""Tests for :mod:`numpy.core.fromnumeric`."""

import numpy as np

A = np.array(True, ndmin=2, dtype=bool)
B = np.array(1.0, ndmin=2, dtype=np.float32)
A.setflags(write=False)
B.setflags(write=False)

a = np.bool_(True)
b = np.float32(1.0)
c = 1.0

np.take(a, 0)
np.take(b, 0)
np.take(c, 0)
np.take(A, 0)
np.take(B, 0)
np.take(A, [0])
np.take(B, [0])

np.reshape(a, 1)
np.reshape(b, 1)
np.reshape(c, 1)
np.reshape(A, 1)
np.reshape(B, 1)

np.choose(a, [True])
np.choose(b, [1.0])
np.choose(c, [1.0])
np.choose(A, [True])
np.choose(B, [1.0])

np.repeat(a, 1)
np.repeat(b, 1)
np.repeat(c, 1)
np.repeat(A, 1)
np.repeat(B, 1)

np.swapaxes(A, 0, 0)
np.swapaxes(B, 0, 0)

np.transpose(a)
np.transpose(b)
np.transpose(c)
np.transpose(A)
np.transpose(B)

np.partition(a, 0)
np.partition(b, 0)
np.partition(c, 0)
np.partition(A, 0)
np.partition(B, 0)

np.argpartition(a, 0)
np.argpartition(b, 0)
np.argpartition(c, 0)
np.argpartition(A, 0)
np.argpartition(B, 0)

np.sort(A, 0)
np.sort(B, 0)

np.argsort(A, 0)
np.argsort(B, 0)
