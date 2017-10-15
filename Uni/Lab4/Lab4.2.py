# Logistic regressin with my data
import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

from pandas import Series, DataFrame
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

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
#vgs.info()

X = vgs.ix[:,(6,7,8,9,10)].values
Y = vgs.ix[:,4].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)

lm = LogisticRegression()
lm.fit(X_train, Y_train)

#for each model it predicts the probability of the test data
#it shows for each row the probability of it being in a different category
lm.predict_proba(X_test)

predicted = lm.predict(X_test)

#shows how well we are at predictiong the different categories
# for the 1st categry we have good precision, this changes for the second and so on
print(metrics.classification_report(Y_test, predicted))

#helps us to see where we made errors, in the second and third category
print(metrics.confusion_matrix(Y_test, predicted))



