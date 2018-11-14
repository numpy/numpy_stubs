import numpy as np

nd = np.array([[1, 2], [3, 4]])

# take
nd.take(0, out=np.empty(1))  # E: No overload
nd.take(0, out=np.empty(1), mode="raise")  # E: No overload

# choose
nd.choose([1, 2, 3, 4, 5], np.empty((2, 2), dtype=np.int64))  # E: Too many positional arguments
