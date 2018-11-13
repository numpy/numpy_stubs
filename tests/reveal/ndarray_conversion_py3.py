import numpy as np

nd = np.array([[1, 2], [3, 4]])

# tostring/tobytes
reveal_type(nd.tostring())  # E: bytes
reveal_type(nd.tostring('C'))  # E: bytes
reveal_type(nd.tostring(None))  # E: bytes

reveal_type(nd.tobytes())  # E: bytes
reveal_type(nd.tobytes('C'))  # E: bytes
reveal_type(nd.tobytes(None))  # E: bytes

# dumps
reveal_type(nd.dumps())  # E: bytes