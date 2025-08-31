from setuptools import setup, find_packages

setup(
    name="pykosmos",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy~=1.26.4",
        "matplotlib~=3.8.4",
        "astropy~=6.1.0",
        "scipy~=1.16.1",
        "specutils~=2.1.0",
        "ccdproc~=2.5.1",
        "ipywidgets~=7.8.1",
        "pandas~=2.2.2",
        "ipython~=8.25.0",
        "specreduce~=1.6.0",
    ],  # add dependencies if needed
    python_requires=">=3.8",
)