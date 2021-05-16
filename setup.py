from setuptools import find_packages, setup

setup(
    name='pypycricbuzz',
    packages=find_packages(),
    version='0.1.0',
    description='Cricbuzz rest api client',
    install_requires=['requests'],
    author='lzzy12',
    license='GPLv3',
)