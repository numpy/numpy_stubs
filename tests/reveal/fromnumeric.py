import numpy as np

A = np.array([True])
A.setflags(write=False)

reveal_type(np.all(A))  # E: numpy.bool_
reveal_type(np.all(A, keepdims=True))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.all(A, keepdims=False))  # E: numpy.bool_
reveal_type(np.all(A, axis=0, keepdims=True))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.all(A, axis=0, keepdims=False))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.all(A, keepdims=True, axis=0))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.all(A, keepdims=False, axis=0))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.all(A, axis=0))  # E: Union[numpy.bool_, numpy.ndarray]

reveal_type(np.any(A))  # E: numpy.bool_
reveal_type(np.any(A, keepdims=True))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.any(A, keepdims=False))  # E: numpy.bool_
reveal_type(np.any(A, axis=0, keepdims=True))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.any(A, axis=0, keepdims=False))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.any(A, keepdims=True, axis=0))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.any(A, keepdims=False, axis=0))  # E: Union[numpy.bool_, numpy.ndarray]
reveal_type(np.any(A, axis=0))  # E: Union[numpy.bool_, numpy.ndarray]
