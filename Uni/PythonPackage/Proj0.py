import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn

from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report

vgsalesraw = pd.read_csv("vgsales.csv", low_memory=False)

#filter my data to include only most recent games by year - this also eliminates the rows where there is no information
vgsales = vgsalesraw[((vgsalesraw['Year'] >= 2010) & (vgsalesraw['Year'] <= 2017))]

#tells us the different features of the data
print(vgsales.keys())

print(vgsales.shape)
vgsales["Genre"] = vgsales["Genre"].codes
vgsales["Platform"] = vgsales["Platform"].codes

vgs = pd.DataFrame(vgsales)

# I use the any method of the dataframe to remove rows where there is even one 0 for sales
# This way I ensure that I am comparing games that have been released across all the interested markets
vgs = vgs[~(vgs == 0).any(axis=1)]
print(pd.crosstab(vgs['Genre'], vgs['Platform'], rownames=["Genre"]))



print(vgs.std())

print(pd.crosstab(vgs['Genre'], vgs['Platform'], rownames=["Genre"]))

#vgs.hist()
#plt.show()

#sb.boxplot(x='Platform', y='Global_Sales', data=vgs, palette='hls')

sb.heatmap(vgs.corr())
plt.show()