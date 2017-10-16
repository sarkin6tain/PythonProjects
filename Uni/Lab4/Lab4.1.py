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


vgsalesraw = pd.read_csv("vgsales.csv", low_memory=False)

#filter my data to include only most recent games by year - this also eliminates the rows where there is no information
vgsales = vgsalesraw[((vgsalesraw['Year'] >= 2010) & (vgsalesraw['Year'] <= 2017))]

#tells us the different features of the data
print(vgsales.keys())

print(vgsales.shape)

vgs = pd.DataFrame(vgsales)

# I use the any method of the dataframe to remove rows where there is even one 0 for sales
# This way I ensure that I am comparing games that have been released across all the interested markets
vgs = vgs[~(vgs == 0).any(axis=1)]
#print(vgs == 0)

#first replace 0 values with nan

print(vgs.head())

x = vgs.values[:, 2, 3, 5]
y = vgs.values[:,10]
x_train, x_test, y_train, y_test =train_test_split( x, y, test_size = 0.25)

lm = LinearRegression()

lm.fit(x_train, y_train)

#these are the weights of the things that get attatched to all of the different attributes that we have
print(lm.coef_)

