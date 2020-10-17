import numpy
import pandas
import matplotlib.pyplot as plt
import scipy.stats


data = numpy.array([0.1, 0.01, 0.02])

a = 10.0
b = a*(1.0 - data)

x = numpy.linspace(0.0, 1.0, 10)

print(x)
kde = scipy.stats.beta(x, a, b)

print(kde)
    




