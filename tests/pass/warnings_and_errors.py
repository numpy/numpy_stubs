import types
from typing import Type

import numpy as np

warnings: types.ModuleType = np.warnings
ModuleDeprecationWarning: Type[DeprecationWarning] = np.ModuleDeprecationWarning
VisibleDeprecationWarning: Type[UserWarning] = np.VisibleDeprecationWarning
ComplexWarning: Type[RuntimeWarning] = np.ComplexWarning
RankWarning: Type[UserWarning] = np.RankWarning

TooHardError: Type[RuntimeError] = np.TooHardError
AxisError1: Type[ValueError] = np.AxisError
AxisError2: Type[IndexError] = np.AxisError

np.AxisError(1)
np.AxisError(1, ndim=2)
np.AxisError(1, ndim=2, msg_prefix='error')
