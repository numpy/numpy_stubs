import numpy as np

nd = np.array([[1, 2], [3, 4]])

# item
nd.item()  # `nd` should be one-element in runtime
nd.item(1)
nd.item(0, 1)
nd.item((0, 1))

# tolist is pretty simple

# itemset
nd.itemset(3)  # `nd` should be one-element in runtime
nd.itemset(3, 0)
nd.itemset((0, 0), 3)

# tostring/tobytes
nd.tostring()
nd.tostring("C")
nd.tostring(None)

nd.tobytes()
nd.tobytes("C")
nd.tobytes(None)

# tofile
nd.tofile("a.txt")
nd.tofile(open("a.txt", mode="bw"))

nd.tofile("a.txt", "")
nd.tofile("a.txt", sep="")

nd.tofile("a.txt", "", "%s")
nd.tofile("a.txt", format="%s")

# dump is pretty simple
# dumps is pretty simple

# astype
nd.astype("float")
nd.astype(float)

nd.astype(float, "K")
nd.astype(float, order="K")

nd.astype(float, "K", "unsafe")
nd.astype(float, casting="unsafe")

nd.astype(float, "K", "unsafe", True)
nd.astype(float, subok=True)

nd.astype(float, "K", "unsafe", True, True)
nd.astype(float, copy=True)

# byteswap
nd.byteswap()
nd.byteswap(True)

# copy
nd.copy()
nd.copy("C")

# view
nd.view()
nd.view(np.int64)
nd.view(dtype=np.int64)
nd.view(np.int64, np.matrix)
nd.view(type=np.matrix)

# getfield
nd.getfield("float")
nd.getfield(float)

nd.getfield("float", 8)
nd.getfield(float, offset=8)

# setflags
nd.setflags()

nd.setflags(True)
nd.setflags(write=True)

nd.setflags(True, True)
nd.setflags(write=True, align=True)

nd.setflags(True, True, False)
nd.setflags(write=True, align=True, uic=False)

# fill is pretty simple
