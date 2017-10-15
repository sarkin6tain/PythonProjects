# Logistic Regression
#Trying to predict the probability that something would be in a particular category
# Multinomial logistic regressions could be used to predict across multiple categories
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn.model_selection import train_test_split

dataSet = datasets.load_iris()

lm = LogisticRegression()

X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(dataSet.data, dataSet.target, test_size=0.25)

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

