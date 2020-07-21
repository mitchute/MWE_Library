from setuptools import setup


def read_lines(filename):
    with open(filename) as f_in:
        return f_in.readlines()


setup(
    name="mwe_lib",
    version=0.12,
    url="",
    license="",
    author="edwin",
    author_email="",
    description="MWE Library",
    packages=["mwe_lib"],
    include_package_data=True,
    install_requires=read_lines("requirements.txt"),
)
