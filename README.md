# Mango Exercise

This project contains a notebook that explores NBA freethrow data in the following directory:  
./exploration/free_throws_analysis.ipynb

There is also a package that contains both a functional and object orientated approach to creating random datasets that 
fall into either a normal, poisson, or binomial distribution. These can be found in:  
./mango-exercise/

## Installing the Package
The package can be installed using the following command:  
```
pip install --index-url https://test.pypi.org/simple/ mango-exercise
```

The class and function can then be imported as shown below:  
```python
from mango_exercise.distribution_generator_class import DistributionGenerator
from mango_exercise.distribution_generator_function import distribution_generator
```