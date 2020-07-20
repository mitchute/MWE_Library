import subprocess

from setuptools import setup


def get_version():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip().decode("utf-8")


setup(
    name='mwe_lib',
    version=get_version(),
    packages=['mwe_lib', ""],
    url='',
    license='',
    author='edwin',
    author_email='',
    description='MWE Library',
    package_data={
        "": ["config.toml"],
        "mwe_lib": ["*.txt"],  # add any txt files in the mwe_lib package
    },
)
