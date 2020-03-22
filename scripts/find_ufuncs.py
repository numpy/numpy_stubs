import numpy as np


def main():
    ufuncs = []
    for obj_name in np.__dir__():
        obj = getattr(np, obj_name)
        if isinstance(obj, np.ufunc):
            ufuncs.append(obj)

    ufunc_stubs = []
    for ufunc in set(ufuncs):
        ufunc_stubs.append(f'{ufunc.__name__}: ufunc')
    ufunc_stubs.sort()

    for stub in ufunc_stubs:
        print(stub)


if __name__ == '__main__':
    main()
