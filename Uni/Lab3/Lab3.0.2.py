from sklearn import datasets

from sklearn import metrics

import pandas as pd

from sklearn.naive_bayes import GaussianNB

dataset = datasets.load_iris()

model = GaussianNB()

model.fit(dataset.data, dataset.target)

expected = dataset.target

predicted = model.predict(dataset.data)

print(metrics.classification_report(expected, predicted))

# easy and fast to calculate predictions as it generates frequency tables
# works well for categorical values when we try to label things
print(metrics.confusion_matrix(expected, predicted))