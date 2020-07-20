from setuptools import setup

setup(
    name='mwe_lib',
    version='0.1',
    packages=['mwe_lib', ""],
    url='',
    license='',
    author='edwin',
    author_email='',
    description='MWE Library',
    package_data={
        "": ["config.toml"],
        "mwe_lib": ["*.txt"],  # add any txt files in the mwe_lib package
    }
)
