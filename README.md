# Multivariable Riemann Sums

This file provides a python function to estimate the definite integral of a continuous bounded function.

## Dependencies

While the code requires no packages to run, NumPy or SymPy are useful to define complex functions. The 'typing' module is imported to provide typing hints not supported in older versions of python.

## Examples

```python
import numpy as np #used for examples
>>> def f(vector): #Function to integrate
	x, y = vector
	return np.sin(x) * np.cos(y)
>>> reg = [(0, np.pi), (np.pi, 0)] #Region of integration
    
>>> est_integral(reg, f, .1)
>>> -0.28235318442224444

```
