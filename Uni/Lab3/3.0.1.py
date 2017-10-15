from sklearn import datasets

from sklearn import metrics

import pandas as pd

from sklearn.neighbors import KNeighborsClassifier

dataset = datasets.load_iris()

model = KNeighborsClassifier()

# data's attribute we use to train and target is what we want t obtain = input, output
model.fit(dataset.data, dataset.target)

expected = dataset.target

predicted = model.predict(dataset.data)

print(metrics.classification_report(expected, predicted))

print(metrics.confusion_matrix(expected, predicted))
