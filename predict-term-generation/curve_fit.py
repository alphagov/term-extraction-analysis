# http://www.walkingrandomly.com/?p=5215
# http://stackoverflow.com/questions/10857948/use-of-curve-fit-to-fit-data
# http://kitchingroup.cheme.cmu.edu/blog/2013/02/12/Nonlinear-curve-fitting-with-parameter-confidence-intervals/

import numpy as np
from scipy.optimize import curve_fit
import csv
import math
import scipy as sy

values = []

i = 0

with open('data/education.txt', 'rb') as source_file:
    reader = source_file.readlines()
    for row in reader:
        i = i + 1
        values.append((int(i), int(row)))
        if i >= 100:
            break

xdata, ydata = zip(*values)

# exponential approach - http://physics.info/curve-fitting/
# http://stackoverflow.com/questions/18442116/fitting-an-exponential-approach-asymptotic-power-law-in-r-python
def func(x, a, b, c):
    return a * (-100 ** (-b * x)) - c

popt, pcov = curve_fit(func, xdata, ydata, p0 = [1., 1., 1.], maxfev = 50000)

a = popt[0]
b = popt[1]
c = popt[2]

for i in range(5000):
    print int(func(i, a, b, c))

print " a: " + str(a)
print " b: " + str(b)
print " c: " + str(c)
