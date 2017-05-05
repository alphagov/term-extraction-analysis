# http://stackoverflow.com/questions/29623171/simple-prediction-using-linear-regression-with-python

from sklearn.linear_model import LinearRegression
import csv

values = []

with open('source.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        values.append((int(row[0]), int(row[1])))

model = LinearRegression()

x, y = zip(*values)

max_x = max(x)
min_x = min(x)
# split the values in train and data.
train_data_X = map(lambda x: [x], list(x[:-20]))
train_data_Y = list(y[:-20])
test_data_X = map(lambda x: [x], list(x[-20:]))
test_data_Y = list(y[-20:])
# feed the linear regression with the train data to obtain a model.
model.fit(train_data_X, train_data_Y)
# check that the coeffients are the expected ones.
m = model.coef_[0]
b = model.intercept_

print(' y = {0} * x + {1}'.format(m, b))

print model.predict([10000])
