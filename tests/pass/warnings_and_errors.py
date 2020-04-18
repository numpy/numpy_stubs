import types
from typing import Type

import numpy as np

warnings = np.warnings  # type: types.ModuleType
ModuleDeprecationWarning = np.ModuleDeprecationWarning  # type: Type[DeprecationWarning]
VisibleDeprecationWarning = np.VisibleDeprecationWarning  # type: Type[UserWarning]
ComplexWarning = np.ComplexWarning  # type: Type[RuntimeWarning]
RankWarning = np.RankWarning  # type: Type[UserWarning]

TooHardError = np.TooHardError  # type: Type[RuntimeError]
AxisError1 = np.AxisError  # type: Type[ValueError]
AxisError2 = np.AxisError  # type: Type[IndexError]

np.AxisError(1)
np.AxisError(1, ndim=2)
np.AxisError(1, ndim=2, msg_prefix='error')
