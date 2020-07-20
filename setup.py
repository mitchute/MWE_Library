from setuptools import setup


def read_lines(filename):
    with open(filename) as f_in:
        return f_in.readlines()


setup(
    name='mwe_lib',
    version=0.7,
    packages=['mwe_lib'],
    url='',
    license='',
    author='edwin',
    author_email='',
    description='MWE Library',
    package_data={
        "mwe_lib": ["core/*", "resources/*", "config.toml", "runner.py"],
    },
    install_requires=read_lines("requirements.txt"),
)
