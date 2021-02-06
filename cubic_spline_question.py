from methods.cubic_spline import natural_cubic_spline

# question 41

import numpy as np

points = np.array([[-1., 0.8619948], [-0.5, 0.95802009], [0., 1.0986123], [0.5, 1.2943767]])

x = 0.25

print("s({0}) = {1}".format(x, natural_cubic_spline(points)(x)))
