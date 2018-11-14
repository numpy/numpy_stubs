import numpy as np

nd = np.array([[1, 2], [3, 4]])

# take
nd.take(0)
nd.take(0, mode="clip")

nd.take(0, 0)
nd.take(0, axis=1)

nd.take(0, 1, np.empty(2, dtype=np.int64))
nd.take(0, 1, out=np.empty(2, dtype=np.int64))

nd.take(0, 1, np.empty(2, dtype=np.int64), "raise")
nd.take(0, 1, np.empty(2, dtype=np.int64), mode="raise")

nd.take([0, 1])

nd.take([0, 1], 1)
nd.take([0, 1], axis=1)

nd.take([0, 1], 1, np.empty((2, 2), dtype=np.int64))
nd.take([0, 1], 1, out=np.empty((2, 2), dtype=np.int64))

nd.take([0, 1], 1, np.empty((2, 2), dtype=np.int64), "raise")
nd.take([0, 1], 1, np.empty((2, 2), dtype=np.int64), mode="raise")

# put
nd.put(0, 5)
nd.put(0, [1, 5])
nd.put([0, 1], 5)
nd.put([0, 1], [5, 6])

nd.put(0, 5, "raise")
nd.put(0, 5, mode="raise")

# repeat
nd.repeat(2)
nd.repeat(2, 0)
nd.repeat(2, axis=0)

nd.repeat([1, 2, 3, 4])
nd.repeat([1, 2], 0)
nd.repeat([1, 2], axis=0)

# choose
nd.choose([1, 2, 3, 4, 5])
nd.choose([["a", "b"], ["d", "e"], ["f", "g"], ["h", "i"], ["j", "k"]])

nd.choose([1, 2, 3, 4, 5], out=np.empty((2, 2), dtype=np.int64))
nd.choose([1, 2, 3, 4, 5], out=np.empty((2, 2), dtype=np.int64), mode="raise")

# sort
nd.sort()

nd.sort(0)
nd.sort(axis=0)

nd.sort(1, "heapsort")
nd.sort(1, kind="heapsort")

nd.sort(1, "heapsort", "f1")
nd.sort(1, "heapsort", order="f1")

nd.sort(1, "heapsort", ["f1", "f2"])
nd.sort(1, "heapsort", order=["f1", "f2"])

# argsort
nd.argsort()

nd.argsort(0)
nd.argsort(None)
nd.argsort(axis=0)

nd.argsort(1, "heapsort")
nd.argsort(1, kind="heapsort")

nd.argsort(1, "heapsort", "f1")
nd.argsort(1, "heapsort", order="f1")

nd.argsort(1, "heapsort", ["f1", "f2"])
nd.argsort(1, "heapsort", order=["f1", "f2"])

# partition
nd.partition(1)
nd.partition([0, 1])

nd.partition(1, 0)
nd.partition(1, axis=0)

nd.partition(1, 0, "introselect")
nd.partition(1, 0, kind="introselect")

nd.partition(1, 0, "introselect", "f1")
nd.partition(1, 0, "introselect", order="f1")

nd.partition(1, 0, "introselect", ["f1", "f2"])
nd.partition(1, 0, "introselect", order=["f1", "f2"])

# argpartition
nd.argpartition(1)
nd.argpartition([0, 1])

nd.argpartition(1, 0)
nd.argpartition(1, None)
nd.argpartition(1, axis=0)

nd.argpartition(1, 0, "introselect")
nd.argpartition(1, 0, kind="introselect")

nd.argpartition(1, 0, "introselect", "f1")
nd.argpartition(1, 0, "introselect", order="f1")

nd.argpartition(1, 0, "introselect", ["f1", "f2"])
nd.argpartition(1, 0, "introselect", order=["f1", "f2"])

# searchsorted
nd.searchsorted(5)
nd.searchsorted([5, 2])

nd.searchsorted(5, "right")
nd.searchsorted(5, side="right")

nd.searchsorted(5, "right", [1, 0])
nd.searchsorted(5, "right", sorter=[1, 0])

# nonzero is pretty simple

# compress
nd.compress([0, 1, 1, 0])
nd.compress([False, True, True, False])

nd.compress([0, 1], 0)
nd.compress([0, 1], axis=0)

nd.compress([0, 1], 0, np.empty((1, 2), dtype=np.int64))
nd.compress([0, 1], 0, out=np.empty((1, 2), dtype=np.int64))

# diagonal is pretty simple
