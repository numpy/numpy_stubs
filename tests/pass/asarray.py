import numpy as np

float_value = 1.23
int_list = [1, 2, 3]
float_tuple = (1., 2., 3.)
bool_array = np.array([True, False, True], dtype=np.bool_)
list_of_tup = [(1, 2.), (3, 4.)]


# Different supported types
np.asarray(float_value)
np.asarray(int_list)
np.asarray(float_tuple)
np.asarray(bool_array)
np.asarray(list_of_tup)

# # Different flags
np.asarray(list_of_tup, dtype=None)
np.asarray(list_of_tup, dtype=np.int32)
np.asarray(list_of_tup, dtype='i4,f4')
np.asarray(list_of_tup, order=None)
np.asarray(list_of_tup, order='C')
