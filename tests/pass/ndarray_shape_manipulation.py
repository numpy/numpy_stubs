import numpy as np

nd = np.array([[1, 2], [3, 4]])

# reshape
nd.reshape()
nd.reshape(4)
nd.reshape(2, 2)
nd.reshape((2, 2))

nd.reshape((2, 2), order="C")
nd.reshape(4, order="C")

# resize
nd.resize()
nd.resize(4)
nd.resize(2, 2)
nd.resize((2, 2))

nd.resize((2, 2), refcheck=True)
nd.resize(4, refcheck=True)

# transpose
nd.transpose()
nd.transpose(1, 0)
nd.transpose((1, 0))

# swapaxes
nd.swapaxes(0, 1)

# flatten
nd.flatten()
nd.flatten("C")

# ravel
nd.ravel()
nd.ravel("C")

# squeeze
nd.squeeze()
nd.squeeze(0)
nd.squeeze((0, 2))
