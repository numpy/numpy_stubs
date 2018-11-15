import numpy as np

nd = np.array([[1, 2], [3, 4]])

# argmax
# argmin is the same
nd.argmax()

nd.argmax(0)
nd.argmax(axis=0)

nd.argmax(0, np.empty((2, ), dtype=np.int64))
nd.argmax(0, out=np.empty((2, ), dtype=np.int64))

# max
# min is the same
nd.max()
nd.max(keepdims=True)

nd.max(0)
nd.max(axis=0)

nd.max(0, np.empty((2, ), dtype=np.int64))
nd.max(0, out=np.empty((2, ), dtype=np.int64))

nd.max(0, np.empty((2, ), dtype=np.int64), False)
nd.max(0, np.empty((2, ), dtype=np.int64), keepdims=False)

# ptp
nd.ptp()

nd.ptp(0)
nd.ptp(axis=0)

nd.ptp(0, np.empty((2, ), dtype=np.int64))
nd.ptp(0, out=np.empty((2, ), dtype=np.int64))

# clip
nd.clip(2)
nd.clip([1, 2])

nd.clip(2, 2)
nd.clip(2, None)
nd.clip(2, [1, 2])

nd.clip(1, np.empty((2, 2), dtype=np.int64))
nd.clip(1, out=np.empty((2, 2), dtype=np.int64))

nd.clip(1, 2, np.empty((2, 2), dtype=np.int64))
nd.clip(1, 2, out=np.empty((2, 2), dtype=np.int64))

# conj is pretty simple

# round
nd.round()
nd.round(2)
nd.round(decimals=2)

nd.round(2, np.empty((2, 2), dtype=float))
nd.round(2, out=np.empty((2, 2), dtype=float))

# trace
nd.trace()
nd.trace(0)
nd.trace(offset=0)

nd.trace(0, 0)
nd.trace(0, axis1=0)

nd.trace(0, 0, 1)
nd.trace(0, 0, axis2=1)

nd.trace(0, 0, 1, int)
nd.trace(0, 0, 1, dtype=int)

nd.trace(0, 0, 1, int, np.empty((2, 2)))
nd.trace(0, 0, 1, int, out=np.empty((2, 2)))

# sum
nd.sum()
nd.sum(None)
nd.sum(1)
nd.sum((0, 1))

nd.sum(1, int)
nd.sum(1, dtype=int)

nd.sum(1, int, np.empty((2, ), dtype=int))
nd.sum(1, int, out=np.empty((2, ), dtype=int))

nd.sum(1, int, np.empty((2, ), dtype=int), False)
nd.sum(1, int, np.empty((2, ), dtype=int), keepdims=False)

# cumsum
nd.cumsum()

nd.cumsum(0)
nd.cumsum(axis=0)

nd.cumsum(0, int)
nd.cumsum(0, dtype=int)

nd.cumsum(0, int, np.empty((2, 2), dtype=int))
nd.cumsum(0, int, out=np.empty((2, 2), dtype=int))

# mean
nd.mean()
nd.mean(None)
nd.mean(1)
nd.mean((0, 1))

nd.mean(1, int)
nd.mean(1, dtype=int)

nd.mean(1, int, np.empty((2, ), dtype=int))
nd.mean(1, int, out=np.empty((2, ), dtype=int))

nd.mean(1, int, np.empty((2, ), dtype=int), False)
nd.mean(1, int, np.empty((2, ), dtype=int), keepdims=False)

# var
nd.var()
nd.var(None)
nd.var(1)
nd.var((0, 1))

nd.var(1, int)
nd.var(1, dtype=int)

nd.var(1, int, np.empty((2, ), dtype=int))
nd.var(1, int, out=np.empty((2, ), dtype=int))

nd.var(1, int, np.empty((2, ), dtype=int), 1)
nd.var(1, int, np.empty((2, ), dtype=int), ddof=1)

nd.var(1, int, np.empty((2, ), dtype=int), 1, False)
nd.var(1, int, np.empty((2, ), dtype=int), 1, keepdims=False)

# std
nd.std()
nd.std(None)
nd.std(1)
nd.std((0, 1))

nd.std(1, float)
nd.std(1, dtype=float)

nd.std(1, float, np.empty((2, ), dtype=float))
nd.std(1, float, out=np.empty((2, ), dtype=float))

nd.std(1, float, np.empty((2, ), dtype=float), 1)
nd.std(1, float, np.empty((2, ), dtype=float), ddof=1)

nd.std(1, float, np.empty((2, ), dtype=float), 1, False)
nd.std(1, float, np.empty((2, ), dtype=float), 1, keepdims=False)

# prod
nd.prod()
nd.prod(None)
nd.prod(1)
nd.prod((0, 1))

nd.prod(1, int)
nd.prod(1, dtype=int)

nd.prod(1, int, np.empty((2, ), dtype=int))
nd.prod(1, int, out=np.empty((2, ), dtype=int))

nd.prod(1, int, np.empty((2, ), dtype=int), False)
nd.prod(1, int, np.empty((2, ), dtype=int), keepdims=False)

# cumprod
nd.cumprod()
nd.cumprod(1)

nd.cumprod(1, int)
nd.cumprod(1, dtype=int)

nd.cumprod(1, int, np.empty((2, 2), dtype=int))
nd.cumprod(1, int, out=np.empty((2, 2), dtype=int))

# all
# any is the same
nd.all()
nd.all(None)
nd.all(1)
nd.all((0, 1))

nd.all(1, np.empty((2, ), dtype=int))
nd.all(1, out=np.empty((2, ), dtype=int))

nd.all(1, np.empty((2, ), dtype=int), False)
nd.all(1, np.empty((2, ), dtype=int), keepdims=False)
