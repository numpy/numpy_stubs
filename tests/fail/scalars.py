import numpy as np

# Construction

np.float32(3j)  # E: incompatible type
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
