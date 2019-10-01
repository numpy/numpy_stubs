import numpy as np

nd = np.array([[1, 2], [3, 4]])

reveal_type(nd.all())  # E: numpy.bool_
reveal_type(nd.all(1))  # E: numpy.ndarray
reveal_type(nd.all(axis=1))  # E: numpy.ndarray

reveal_type(nd.any())  # E: numpy.bool_
reveal_type(nd.any(axis=1))  # E: numpy.ndarray

reveal_type(nd.argmax())  # E: numpy.integer
reveal_type(nd.argmax(axis=1))  # E: numpy.ndarray

reveal_type(nd.argmin())  # E: numpy.integer
reveal_type(nd.argmin(axis=1))  # E: numpy.ndarray

reveal_type(nd.argpartition())  # E: numpy.ndarray
reveal_type(nd.argsort())  # E: numpy.ndarray

reveal_type(nd.cumprod())  # E: numpy.ndarray
reveal_type(nd.cumsum())  # E: numpy.ndarray

reveal_type(nd.diagonal())  # E: numpy.ndarray
