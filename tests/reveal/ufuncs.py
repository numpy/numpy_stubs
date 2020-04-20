import numpy as np

reveal_type(np.sin(1))  # E: Union[numpy.ndarray, numpy.generic]
reveal_type(np.sin([1, 2, 3]))  # E: Union[numpy.ndarray, numpy.generic]
reveal_type(np.sin.nin)  # E: Literal[1]
reveal_type(np.sin.nout)  # E: Literal[1]
