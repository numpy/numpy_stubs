import numpy as np

nd = np.array([[1, 2], [3, 4]])

# argmax
# argmin is the same
reveal_type(nd.argmax())  # E: Any

reveal_type(nd.argmax(0))  # E: Any
reveal_type(nd.argmax(axis=0))  # E: Any

reveal_type(nd.argmax(0, np.empty((2, ), dtype=np.int64)))  # E: Any
reveal_type(nd.argmax(0, out=np.empty((2, ), dtype=np.int64)))  # E: Any

# max
# min is the same
reveal_type(nd.max())  # E: Any
reveal_type(nd.max(keepdims=True))  # E: Any

reveal_type(nd.max(0))  # E: Any
reveal_type(nd.max(axis=0))  # E: Any

reveal_type(nd.max(0, np.empty((2, ), dtype=np.int64)))  # E: Any
reveal_type(nd.max(0, out=np.empty((2, ), dtype=np.int64)))  # E: Any

reveal_type(nd.max(0, np.empty((2, ), dtype=np.int64), False))  # E: Any
reveal_type(nd.max(0, np.empty((2, ), dtype=np.int64), keepdims=False))  # E: Any

# ptp
reveal_type(nd.ptp())  # E: Any

reveal_type(nd.ptp(0))  # E: Any
reveal_type(nd.ptp(axis=0))  # E: Any

reveal_type(nd.ptp(0, np.empty((2, ), dtype=np.int64)))  # E: Any
reveal_type(nd.ptp(0, out=np.empty((2, ), dtype=np.int64)))  # E: Any

# clip
reveal_type(nd.clip(2))  # E: numpy.ndarray
reveal_type(nd.clip([1, 2]))  # E: numpy.ndarray

reveal_type(nd.clip(2, 2))  # E: numpy.ndarray
reveal_type(nd.clip(2, None))  # E: numpy.ndarray
reveal_type(nd.clip(2, [1, 2]))  # E: numpy.ndarray

reveal_type(nd.clip(1, np.empty((2, 2), dtype=np.int64)))  # E: numpy.ndarray
reveal_type(nd.clip(1, out=np.empty((2, 2), dtype=np.int64)))  # E: numpy.ndarray

reveal_type(nd.clip(1, 2, np.empty((2, 2), dtype=np.int64)))  # E: numpy.ndarray
reveal_type(nd.clip(1, 2, out=np.empty((2, 2), dtype=np.int64)))  # E: numpy.ndarray

# conj is pretty simple

# round
reveal_type(nd.round())  # E: numpy.ndarray
reveal_type(nd.round(2))  # E: numpy.ndarray
reveal_type(nd.round(decimals=2))  # E: numpy.ndarray

reveal_type(nd.round(2, np.empty((2, 2), dtype=float)))  # E: numpy.ndarray
reveal_type(nd.round(2, out=np.empty((2, 2), dtype=float)))  # E: numpy.ndarray

# trace
reveal_type(nd.trace())  # E: Any
reveal_type(nd.trace(0))  # E: Any
reveal_type(nd.trace(offset=0))  # E: Any

reveal_type(nd.trace(0, 0))  # E: Any
reveal_type(nd.trace(0, axis1=0))  # E: Any

reveal_type(nd.trace(0, 0, 1))  # E: Any
reveal_type(nd.trace(0, 0, axis2=1))  # E: Any

reveal_type(nd.trace(0, 0, 1, int))  # E: Any
reveal_type(nd.trace(0, 0, 1, dtype=int))  # E: Any

reveal_type(nd.trace(0, 0, 1, int, np.empty((2, 2))))  # E: Any
reveal_type(nd.trace(0, 0, 1, int, out=np.empty((2, 2))))  # E: Any

# sum
reveal_type(nd.sum())  # E: Any
reveal_type(nd.sum(None))  # E: Any
reveal_type(nd.sum(1))  # E: Any
reveal_type(nd.sum((0, 1)))  # E: Any

reveal_type(nd.sum(1, int))  # E: Any
reveal_type(nd.sum(1, dtype=int))  # E: Any

reveal_type(nd.sum(1, int, np.empty((2, ), dtype=int)))  # E: Any
reveal_type(nd.sum(1, int, out=np.empty((2, ), dtype=int)))  # E: Any

reveal_type(nd.sum(1, int, np.empty((2, ), dtype=int), False))  # E: Any
reveal_type(nd.sum(1, int, np.empty((2, ), dtype=int), keepdims=False))  # E: Any

# cumsum
reveal_type(nd.cumsum())  # E: numpy.ndarray

reveal_type(nd.cumsum(0))  # E: numpy.ndarray
reveal_type(nd.cumsum(axis=0))  # E: numpy.ndarray

reveal_type(nd.cumsum(0, int))  # E: numpy.ndarray
reveal_type(nd.cumsum(0, dtype=int))  # E: numpy.ndarray

reveal_type(nd.cumsum(0, int, np.empty((2, 2), dtype=int)))  # E: numpy.ndarray
reveal_type(nd.cumsum(0, int, out=np.empty((2, 2), dtype=int)))  # E: numpy.ndarray

# mean
reveal_type(nd.mean())  # E: Any
reveal_type(nd.mean(None))  # E: Any
reveal_type(nd.mean(1))  # E: Any
reveal_type(nd.mean((0, 1)))  # E: Any

reveal_type(nd.mean(1, int))  # E: Any
reveal_type(nd.mean(1, dtype=int))  # E: Any

reveal_type(nd.mean(1, int, np.empty((2, ), dtype=int)))  # E: Any
reveal_type(nd.mean(1, int, out=np.empty((2, ), dtype=int)))  # E: Any

reveal_type(nd.mean(1, int, np.empty((2, ), dtype=int), False))  # E: Any
reveal_type(nd.mean(1, int, np.empty((2, ), dtype=int), keepdims=False))  # E: Any

# var
reveal_type(nd.var())  # E: Any
reveal_type(nd.var(None))  # E: Any
reveal_type(nd.var(1))  # E: Any
reveal_type(nd.var((0, 1)))  # E: Any

reveal_type(nd.var(1, int))  # E: Any
reveal_type(nd.var(1, dtype=int))  # E: Any

reveal_type(nd.var(1, int, np.empty((2, ), dtype=int)))  # E: Any
reveal_type(nd.var(1, int, out=np.empty((2, ), dtype=int)))  # E: Any

reveal_type(nd.var(1, int, np.empty((2, ), dtype=int), 1))  # E: Any
reveal_type(nd.var(1, int, np.empty((2, ), dtype=int), ddof=1))  # E: Any

reveal_type(nd.var(1, int, np.empty((2, ), dtype=int), 1, False))  # E: Any
reveal_type(nd.var(1, int, np.empty((2, ), dtype=int), 1, keepdims=False))  # E: Any

# std
reveal_type(nd.std())  # E: Any
reveal_type(nd.std(None))  # E: Any
reveal_type(nd.std(1))  # E: Any
reveal_type(nd.std((0, 1)))  # E: Any

reveal_type(nd.std(1, float))  # E: Any
reveal_type(nd.std(1, dtype=float))  # E: Any

reveal_type(nd.std(1, float, np.empty((2, ), dtype=float)))  # E: Any
reveal_type(nd.std(1, float, out=np.empty((2, ), dtype=float)))  # E: Any

reveal_type(nd.std(1, float, np.empty((2, ), dtype=float), 1))  # E: Any
reveal_type(nd.std(1, float, np.empty((2, ), dtype=float), ddof=1))  # E: Any

reveal_type(nd.std(1, float, np.empty((2, ), dtype=float), 1, False))  # E: Any
reveal_type(nd.std(1, float, np.empty((2, ), dtype=float), 1, keepdims=False))  # E: Any

# prod
reveal_type(nd.prod())  # E: Any
reveal_type(nd.prod(None))  # E: Any
reveal_type(nd.prod(1))  # E: Any
reveal_type(nd.prod((0, 1)))  # E: Any

reveal_type(nd.prod(1, int))  # E: Any
reveal_type(nd.prod(1, dtype=int))  # E: Any

reveal_type(nd.prod(1, int, np.empty((2, ), dtype=int)))  # E: Any
reveal_type(nd.prod(1, int, out=np.empty((2, ), dtype=int)))  # E: Any

reveal_type(nd.prod(1, int, np.empty((2, ), dtype=int), False))  # E: Any
reveal_type(nd.prod(1, int, np.empty((2, ), dtype=int), keepdims=False))  # E: Any

# cumprod
reveal_type(nd.cumprod())  # E: numpy.ndarray
reveal_type(nd.cumprod(1))  # E: numpy.ndarray

reveal_type(nd.cumprod(1, int))  # E: numpy.ndarray
reveal_type(nd.cumprod(1, dtype=int))  # E: numpy.ndarray

reveal_type(nd.cumprod(1, int, np.empty((2, 2), dtype=int)))  # E: numpy.ndarray
reveal_type(nd.cumprod(1, int, out=np.empty((2, 2), dtype=int)))  # E: numpy.ndarray

# all
# any is the same
reveal_type(nd.all())  # E: Any
reveal_type(nd.all(None))  # E: Any
reveal_type(nd.all(1))  # E: Any
reveal_type(nd.all((0, 1)))  # E: Any

reveal_type(nd.all(1, np.empty((2, ), dtype=int)))  # E: Any
reveal_type(nd.all(1, out=np.empty((2, ), dtype=int)))  # E: Any

reveal_type(nd.all(1, np.empty((2, ), dtype=int), False))  # E: Any
reveal_type(nd.all(1, np.empty((2, ), dtype=int), keepdims=False))  # E: Any
