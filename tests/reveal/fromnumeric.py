"""Tests for :mod:`numpy.core.fromnumeric`."""

import numpy as np

A = np.array(True, ndmin=2, dtype=bool)
B = np.array(1.0, ndmin=2, dtype=np.float32)
A.setflags(write=False)
B.setflags(write=False)

a = np.bool_(True)
b = np.float32(1.0)
c = 1.0

reveal_type(np.take(a, 0))  # E: numpy.bool_
reveal_type(np.take(b, 0))  # E: numpy.float32
reveal_type(
    np.take(c, 0)  # E: Union[numpy.generic, datetime.datetime, datetime.timedelta]
)
reveal_type(
    np.take(A, 0)  # E: Union[numpy.generic, datetime.datetime, datetime.timedelta]
)
reveal_type(
    np.take(B, 0)  # E: Union[numpy.generic, datetime.datetime, datetime.timedelta]
)
reveal_type(
    np.take(  # E: Union[numpy.generic, datetime.datetime, datetime.timedelta, numpy.ndarray]
        A, [0]
    )
)
reveal_type(
    np.take(  # E: Union[numpy.generic, datetime.datetime, datetime.timedelta, numpy.ndarray]
        B, [0]
    )
)

reveal_type(np.reshape(a, 1))  # E: numpy.ndarray
reveal_type(np.reshape(b, 1))  # E: numpy.ndarray
reveal_type(np.reshape(c, 1))  # E: numpy.ndarray
reveal_type(np.reshape(A, 1))  # E: numpy.ndarray
reveal_type(np.reshape(B, 1))  # E: numpy.ndarray

reveal_type(np.choose(a, [True]))  # E: numpy.bool_
reveal_type(np.choose(b, [1.0]))  # E: numpy.float32
reveal_type(
    np.choose(  # E: Union[numpy.generic, datetime.datetime, datetime.timedelta]
        c, [1.0]
    )
)
reveal_type(np.choose(A, [True]))  # E: numpy.ndarray
reveal_type(np.choose(B, [1.0]))  # E: numpy.ndarray

reveal_type(np.repeat(a, 1))  # E: numpy.ndarray
reveal_type(np.repeat(b, 1))  # E: numpy.ndarray
reveal_type(np.repeat(c, 1))  # E: numpy.ndarray
reveal_type(np.repeat(A, 1))  # E: numpy.ndarray
reveal_type(np.repeat(B, 1))  # E: numpy.ndarray

# TODO: Add tests for np.put()

reveal_type(np.swapaxes(A, 0, 0))  # E: numpy.ndarray
reveal_type(np.swapaxes(B, 0, 0))  # E: numpy.ndarray

reveal_type(np.transpose(a))  # E: numpy.ndarray
reveal_type(np.transpose(b))  # E: numpy.ndarray
reveal_type(np.transpose(c))  # E: numpy.ndarray
reveal_type(np.transpose(A))  # E: numpy.ndarray
reveal_type(np.transpose(B))  # E: numpy.ndarray

reveal_type(np.partition(a, 0))  # E: numpy.ndarray
reveal_type(np.partition(b, 0))  # E: numpy.ndarray
reveal_type(np.partition(c, 0))  # E: numpy.ndarray
reveal_type(np.partition(A, 0))  # E: numpy.ndarray
reveal_type(np.partition(B, 0))  # E: numpy.ndarray

reveal_type(np.argpartition(a, 0))  # E: numpy.ndarray
reveal_type(np.argpartition(b, 0))  # E: numpy.ndarray
reveal_type(np.argpartition(c, 0))  # E: numpy.ndarray
reveal_type(np.argpartition(A, 0))  # E: numpy.ndarray
reveal_type(np.argpartition(B, 0))  # E: numpy.ndarray

reveal_type(np.sort(A, 0))  # E: numpy.ndarray
reveal_type(np.sort(B, 0))  # E: numpy.ndarray

reveal_type(np.argsort(A, 0))  # E: numpy.ndarray
reveal_type(np.argsort(B, 0))  # E: numpy.ndarray
