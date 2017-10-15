from sklearn import datasets

from sklearn import metrics

import pandas as pd

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split

from sklearn import tree

data = pd.read_csv("vgsalespredict.csv", low_memory=False)


data.shape
data.head()
x = data.values[:, 1:5]
y = data.values[:,0]
x_train, x_test, y_train, y_test =train_test_split( x, y, test_size = 0.25)

model = DecisionTreeClassifier(max_depth=4, min_samples_leaf=6, splitter="best")

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

y_pred

print(metrics.accuracy_score(y_test,y_pred))

print(metrics.classification_report(y_test,y_pred))

print(metrics.confusion_matrix(y_test,y_pred))
