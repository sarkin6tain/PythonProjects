#Linear and logistic regression
# Used to look at the relationship between the ifferent variables/outcomes
#Linear regeression - allows to predict quantities and outputs
#Logistic regrassions are mainly used for categorical data, but could also give robabilities - additional info

#LINEAR REGRESSION
#y[i] numeric quanity we want to predict
#x[i] the different attributes corresponding to the y[i]
# the aim of the regression is to find a function that would give the most accurate prediction

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold
from sklearn.model_selection import train_test_split


boston = datasets.load_boston()

#tells us the different features of the data
print(boston.keys())

print(boston.data.shape)

print(boston.feature_names)

#Useufulfor built in data that has the description pre-writen
print(boston.DESCR)

#create a data frame, which creates bos from the data in a contrainer
bos = pd.DataFrame(boston.data)

print(bos.head())

#the name of the different columns match the attributes of the data
bos.columns = boston.feature_names

print(bos.head())

x_train, x_test, y_train, y_test = sklearn.cross_validation.train_test_split(bos, boston.target, test_size = 0.25)

lm = LinearRegression()

lm.fit(x_train, y_train)

#these are the weights of the things that get attatched to all of the different attributes that we have
print(lm.coef_)

#gives which are the most significant attributes that we can use to predict the data (e.g. ZN numver of rooms - look for positives)
# which attributes are more important that others
pd.DataFrame(list(zip(bos.columns, lm.coef_)), columns=['Features', 'Coefficients'])

plt.scatter(bos.RM, boston.target)

plt.xlabel('Average number of rooms')

plt.ylabel('House Price')

#shows that generally as the number of rooms goes up, so do prices
plt.show()

predict = lm.predict(x_test)

print(metrics.mean_squared_error(y_test, predict))

#K-cross validation

#creates a ten-fold K-cross validation
kfold = KFold(10)

lm = LinearRegression()

results = sklearn.cross_validation.cross_val_score(lm, bos, boston.target, cv=kfold, scoring='neg_mean_absolute_error')

print(results.mean())

results = sklearn.cross_validation.cross_val_score(lm, bos, boston.target, cv=kfold, scoring='r2')

print(results.mean())