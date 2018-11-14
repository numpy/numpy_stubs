import numpy as np

nd = np.array([[1, 2], [3, 4]])

# take
reveal_type(nd.take(0))  # E: Any
reveal_type(nd.take(0, 0))  # E: Any
reveal_type(nd.take(0, 1, np.empty(2, dtype=np.int64)))  # E: Any
reveal_type(nd.take(0, 1, np.empty(2, dtype=np.int64), "raise"))  # E: Any

reveal_type(nd.take([0, 1]))  # E: numpy.ndarray
reveal_type(nd.take([0, 1], 1))  # E: numpy.ndarray
reveal_type(nd.take([0, 1], 1, np.empty((2, 2), dtype=np.int64)))  # E: numpy.ndarray
reveal_type(nd.take([0, 1], 1, np.empty((2, 2), dtype=np.int64), "raise"))  # E: numpy.ndarray

# put does not return a value

# repeat
reveal_type(nd.repeat(2))  # E: numpy.ndarray
reveal_type(nd.repeat(2, 0))  # E: numpy.ndarray

reveal_type(nd.repeat([1, 2, 3, 4]))  # E: numpy.ndarray
reveal_type(nd.repeat([1, 2], 0))  # E: numpy.ndarray

# choose
reveal_type(nd.choose([1, 2, 3, 4, 5]))  # E: numpy.ndarray
reveal_type(nd.choose([["a", "b"], ["d", "e"], ["f", "g"], ["h", "i"], ["j", "k"]]))  # E: numpy.ndarray

reveal_type(nd.choose([1, 2, 3, 4, 5], out=np.empty((2, 2), dtype=np.int64)))  # E: numpy.ndarray
reveal_type(nd.choose([1, 2, 3, 4, 5], out=np.empty((2, 2), dtype=np.int64), mode="raise"))  # E: numpy.ndarray

# sort does not return a value

# argsort
reveal_type(nd.argsort())  # E: numpy.ndarray
reveal_type(nd.argsort(0))  # E: numpy.ndarray
reveal_type(nd.argsort(1, "heapsort"))  # E: numpy.ndarray
reveal_type(nd.argsort(1, "heapsort", "f1"))  # E: numpy.ndarray
reveal_type(nd.argsort(1, "heapsort", ["f1", "f2"]))  # E: numpy.ndarray

# partition does not return a value

# argpartition
reveal_type(nd.argpartition(1))  # E: numpy.ndarray
reveal_type(nd.argpartition([0, 1]))  # E: numpy.ndarray
reveal_type(nd.argpartition(1, 0))  # E: numpy.ndarray
reveal_type(nd.argpartition(1, 0, "introselect"))  # E: numpy.ndarray
reveal_type(nd.argpartition(1, 0, "introselect", "f1"))  # E: numpy.ndarray
reveal_type(nd.argpartition(1, 0, "introselect", ["f1", "f2"]))  # E: numpy.ndarray

# searchsorted
reveal_type(nd.searchsorted(5))  # E: Any
reveal_type(nd.searchsorted(5, "right"))  # E: Any
reveal_type(nd.searchsorted(5, "right", [1, 0]))  # E: Any

reveal_type(nd.searchsorted([5, 2]))  # E: numpy.ndarray
reveal_type(nd.searchsorted([5, 2], "right"))  # E: numpy.ndarray
reveal_type(nd.searchsorted([5, 2], "right", [1, 0]))  # E: numpy.ndarray

# nonzero
reveal_type(nd.nonzero())  # E: builtins.tuple[numpy.ndarray]

# compress
reveal_type(nd.compress([0, 1, 1, 0]))  # E: numpy.ndarray
reveal_type(nd.compress([False, True, True, False]))  # E: numpy.ndarray
reveal_type(nd.compress([0, 1], 0))  # E: numpy.ndarray
reveal_type(nd.compress([0, 1], 0, np.empty((1, 2), dtype=np.int64)))  # E: numpy.ndarray

# diagonal is pretty simple
