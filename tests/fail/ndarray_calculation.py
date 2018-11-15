import numpy as np

nd = np.array([[1, 2], [3, 4]])

# argmax
# argmin is the same
nd.argmax(out=np.empty((1,)))  # E: No overload

# ptp
nd.ptp(out=np.empty((1,)))  # E: No overload

# clip
nd.clip()  # E: No overload
nd.clip(None)  # should fail but None matches _ArrayLike[Any]
nd.clip(None, None)  # should fail but None matches _ArrayLike[Any]

nd.clip(a_min=2)  # E: No overload
nd.clip(a_max=2)  # E: No overload
