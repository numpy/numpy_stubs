from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name='numpy-stubs',
    maintainer="NumPy Developers",
    maintainer_email="numpy-discussion@python.org",
    description="PEP 561 type stubs for numpy",
    url="http://www.numpy.org",
    license='BSD',
    version="0.0.1",
    packages=['numpy-stubs'],
    # PEP 561 requires these
    install_requires=['numpy>=1.14.0'],
    package_data=find_stubs('numpy-stubs'),
)
