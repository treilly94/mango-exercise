import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mango_exercise",
    version="0.0.6",
    author="Tom Reilly",
    description="A package for a mango exercise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/treilly94/mango-exercise",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy"
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
