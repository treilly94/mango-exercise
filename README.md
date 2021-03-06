# Mango Exercise

This project contains a notebook that explores NBA freethrow data in the following location:  
./exploration/free_throws_analysis.ipynb

There is also a package that contains both a functional and object orientated approach to creating random datasets that 
fall into either a normal, poisson, or binomial distribution. These can be found in:  
./mango-exercise/

## Installing the Package
The package was created inline with instructions that can be found [here](https://packaging.python.org/tutorials/packaging-projects/)  
The package can be installed using the following command:  
```
pip install --user --index-url https://test.pypi.org/simple/ mango-exercise
```
It must be installed on a python3 environment and it should install numpy as a dependency.

***If there are any issues with numpy being installed as a dependency it may be because it is being installed from the same 
test repository that mango-exercise is hosted in. Pip installing numpy separately should fix any issue.***   

A clean environment can either be created using virtualenv or docker. The below docker command is what I used to create 
a clean test environment:  
```
docker run -i -t --rm python /bin/bash
```
pip and the python3 console should already be available in the container. The container can be exited using 
the escape sequence Ctrl-p + Ctrl-q. Running docker stop against the container will automatically remove it.

## Calling the package
The class and function can then be imported as shown below:  
```python
from mango_exercise.distribution_generator_class import DistributionGenerator
from mango_exercise.distribution_generator_function import distribution_generator
```

The function can be called in the below fashion:  
```python
distribution_generator(3, "normal")
```
The class can be called in the below fashion:
```python
d = DistributionGenerator(16)
d.normal()
d.binomial()
d.poisson()
d.summarise()
```