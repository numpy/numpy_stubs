import numpy as np

A = np.array([True])
A.setflags(write=False)

reveal_type(np.all(A))  # E: builtins.bool
reveal_type(np.all(A, keepdims=True))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.all(A, keepdims=False))  # E: builtins.bool
reveal_type(np.all(A, axis=0, keepdims=True))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.all(A, axis=0, keepdims=False))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.all(A, keepdims=True, axis=0))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.all(A, keepdims=False, axis=0))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.all(A, axis=0))  # E: Union[builtins.bool, numpy.ndarray]

reveal_type(np.any(A))  # E: builtins.bool
reveal_type(np.any(A, keepdims=True))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.any(A, keepdims=False))  # E: builtins.bool
reveal_type(np.any(A, axis=0, keepdims=True))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.any(A, axis=0, keepdims=False))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.any(A, keepdims=True, axis=0))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.any(A, keepdims=False, axis=0))  # E: Union[builtins.bool, numpy.ndarray]
reveal_type(np.any(A, axis=0))  # E: Union[builtins.bool, numpy.ndarray]
