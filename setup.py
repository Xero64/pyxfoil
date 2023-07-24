from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = '''
    Run XFoil from within Python and work with output results.
    '''

setup(
    name="pyxfoil",
    version="0.0.3",
    author="Xero64",
    author_email="xero64@gmail.com",
    description="Run XFoil from within Python and work with output results.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xero64/pyxfoil",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
