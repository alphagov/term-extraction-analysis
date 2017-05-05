# http://www.walkingrandomly.com/?p=5215
# http://stackoverflow.com/questions/10857948/use-of-curve-fit-to-fit-data
# http://kitchingroup.cheme.cmu.edu/blog/2013/02/12/Nonlinear-curve-fitting-with-parameter-confidence-intervals/

import numpy as np
from scipy.optimize import curve_fit
import csv
import math
import scipy as sy


values = []

with open('source.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        values.append((int(row[0]), int(row[1])))

xdata, ydata = zip(*values)

def func(x, a, b):
    return a * x / (b + x)

popt, pcov = curve_fit(func, xdata, ydata, p0 = [1.0, 0.01])

p1 = popt[0]
p2 = popt[1]

for i in range(5000):
    print int(func(i, p1, p2))
