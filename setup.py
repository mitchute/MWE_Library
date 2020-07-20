from setuptools import setup

setup(
    name='mwe_lib',
    version=0.6,
    packages=['mwe_lib'],
    url='',
    license='',
    author='edwin',
    author_email='',
    description='MWE Library',
    package_data={
        "mwe_lib": ["core/*", "resources/*", "config.toml", "runner.py"],
    },
)
