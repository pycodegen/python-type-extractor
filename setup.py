import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py_codegen',
    version='0.0.1',
    author="Dev Doomari",
    author_email="devdoomari@gmail.com",
    description="Generate Code Stubs using Python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "mypy",
        "mypy_extensions",
        "dataclasses",
    ],
)
