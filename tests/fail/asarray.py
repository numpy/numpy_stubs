from datetime import datetime

import numpy as np


float_value = 1.23
int_list = [1, 2, 3]
float_tuple = (1., 2., 3.)
bool_array = np.array([True, False, True], dtype=np.bool_)
list_of_tup = [(1, 2.), (3, 4.)]


# A few unsupported types
np.asarray(dict(a=1))  # E: Argument 1 to "asarray" has incompatible type "Dict[str, int]"
np.asarray(datetime(1970, 1, 1))  # E: Argument 1 to "asarray" has incompatible type


# Unsupported flags
np.asarray([1], dtype=datetime(1970, 1, 1))  # E:  Argument "dtype" to "asarray" has incompatible type "datetime"
np.asarray([1], dtype=True)  # E:  Argument "dtype" to "asarray" has incompatible type "bool"
np.asarray([1], order=[2])  # E:  Argument "order" to "asarray" has incompatible type "List[int]"
