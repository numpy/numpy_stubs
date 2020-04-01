"""Simple expression that should fail with mypy."""

import numpy as np

# Array creation routines checks
np.zeros("test")  # E: incompatible type
np.zeros()  # E: All overload variants of "zeros" require at least one argument

np.ones("test")  # E: incompatible type
np.ones()  # E: All overload variants of "ones" require at least one argument
