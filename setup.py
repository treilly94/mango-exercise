import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mango-exercise",
    version="0.0.1",
    author="Tom Reilly",
    description="A package for a mango exercise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/treilly94/mango-exercise",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)