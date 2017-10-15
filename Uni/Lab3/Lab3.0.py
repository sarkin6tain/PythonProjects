from sklearn import datasets

from sklearn import metrics

import pandas as pd

from sklearn.tree import DecisionTreeClassifier

from sklearn import tree

dataset = datasets.load_iris()

# creates blank decision tree
model = DecisionTreeClassifier()

# fit model to this data and target set
model.fit(dataset.data, dataset.target)

expected = dataset.target

# this model would not segment the data into test and training data, so we expect to o really well
predicted = model.predict(dataset.data)

print(metrics.classification_report(expected, predicted))

# can also generate confusion matrix
# in this data set the first variable would be very easy to predict
print(metrics.confusion_matrix(expected, predicted))

tree.export_graphviz(model)
