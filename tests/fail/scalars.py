import numpy as np

# Construction

np.float32(3j)  # E: incompatible type

# Technically the following examples are valid NumPy code. But they
# are not considered a best practice, and people who wish to use the
# stubs should instead do
#
# np.array([1.0, 0.0, 0.0], dtype=np.float32)
# np.array([], dtype=np.complex64)
#
# See e.g. the discussion on the mailing list
#
# https://mail.python.org/pipermail/numpy-discussion/2020-April/080566.html
#
# and the issue
#
# https://github.com/numpy/numpy-stubs/issues/41
#
# for more context.
np.float32([1.0, 0.0, 0.0])  # E: incompatible type
np.complex64([])  # E: incompatible type

np.complex64(1, 2)  # E: Too many arguments
# TODO: protocols (can't check for non-existent protocols w/ __getattr__)

np.datetime64(0)  # E: non-matching overload

dt_64 = np.datetime64(0, 'D')
td_64 = np.timedelta64(1, 'h')

dt_64 + dt_64  # E: Unsupported operand types

td_64 - dt_64  # E: Unsupported operand types
td_64 / dt_64  # E: No overload
td_64 % 1  # E: Unsupported operand types
td_64 % dt_64  # E: Unsupported operand types
