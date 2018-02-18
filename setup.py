from setuptools import setup, find_packages

setup(
    name='numpy-stubs',
    maintainer="NumPy Developers",
    maintainer_email="numpy-discussion@python.org",
    description="PEP 561 type stubs for numpy",
    url="http://www.numpy.org",
    license='BSD',
    version="0.0.1",
    packages=find_packages(),

    # PEP 561 requires these
    install_requires=['numpy~=1.14.0'],
    package_data={
        'numpy': 'py.typed'
    },
)
