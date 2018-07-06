import numpy as np

np.random.RandomState(b"hello")  # E: incompatible type
np.random.RandomState("")  # E: incompatible type

np.random.beta(3)  # E: No overload variant
np.random.beta(3, "hello")  # E: incompatible type
np.random.beta(3, 4, "hello")  # E: incompatible type
