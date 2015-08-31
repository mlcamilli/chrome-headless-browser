from setuptools import setup, find_packages

requires = [
    'PyVirtualDisplay==0.1.5',
    'selenium==2.47.1',
]

__version__ = '0.0.1'


setup(
    name='chrome-headless-browser',
    author="Matt Camilli",
    author_email="mlcamilli@gmail.com",
    version=__version__,
    url="https://github.com/mlcamilli/chrome-headless-browser",
    install_requires=requires,
    packages=find_packages(exclude=['tests']),
)
