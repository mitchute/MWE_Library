from setuptools import setup

setup(
    name='mwe_lib',
    version='0.3',
    packages=['mwe_lib'],
    url='',
    license='',
    author='edwin',
    author_email='',
    description='MWE Library',
    package_data={
        "mwe_lib": ["*.txt", "config.toml"],  # add any txt files in the mwe_lib package
    },
)
