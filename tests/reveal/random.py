import numpy as np

np.random.beta(3, 4.0)  # E: float
np.random.beta(3.0, 4.0, size=[3, 4])  # E: ndarray
