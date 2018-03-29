import numpy as np

# Construction

np.float32(3j)  # E: incompatible type
np.complex64([])  # E: incompatible type

np.complex64(1, 2)  # E: Too many arguments
# TODO: protocols (can't check for non-existent protocols w/ __getattr__)
