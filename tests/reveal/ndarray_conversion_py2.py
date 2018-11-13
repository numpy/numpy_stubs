import numpy as np

nd = np.array([[1, 2], [3, 4]])

# tostring/tobytes
reveal_type(nd.tostring())  # E: str
reveal_type(nd.tostring('C'))  # E: str
reveal_type(nd.tostring(None))  # E: str

reveal_type(nd.tobytes())  # E: str
reveal_type(nd.tobytes('C'))  # E: str
reveal_type(nd.tobytes(None))  # E: str

# dumps
reveal_type(nd.dumps())  # E: str