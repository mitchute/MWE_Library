from setuptools import setup


def read_lines(filename):
    with open(filename) as f_in:
        return f_in.readlines()


setup(
    name="mwe_lib",
    version=0.8,
    packages=["mwe_lib"],
    url="",
    license="",
    author="edwin",
    author_email="",
    description="MWE Library",
    package_dir={"mwe_lib": "mwe_lib"},
    package_data={"": ["config2.toml"]},
    include_package_data=True,
    install_requires=read_lines("requirements.txt"),
)
