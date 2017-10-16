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

data = pd.read_csv("flights.csv", low_memory=False)

flights = pd.DataFrame(data)
flights.dropna(axis=1, how='any')

columns_of_interest = flights['YEAR', 'DAY', 'FLIGHT_NUMBER', 'TAIL_NUMBER', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'DEPARTURE_TIME', 'DEPARTURE_DELAY', 'TAXI_OUT', 'WHEELS_OFF', 'SCHEDULED_TIME',
                             'ELAPSED_TIME', 'AIR_TIME', 'WHEELS_ON', 'TAXI_IN', 'SCHEDULED_ARRIVAL',
                             'ARRIVAL_TIME', 'DIVERTED', 'AIR_SYSTEM_DELAY',	'SECURITY_DELAY',
                            'AIRLINE_DELAY','LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY']

flights.drop(columns_of_interest, axis=1, inplace=True)


#y0 = flights['AIRLINE'] == 'AS'
#y1 = flights['AIRLINE'] == 'NK'

#print(y0, y1)


print(flights.keys())
print(flights.describe())

#print(pd.crosstab(flights['CANCELLED'], flights['CANCELLATION_REASON'], rownames=["count"]))

#flights.hist()
#plt.show()

#count = flights['CANCELLED'].count()
#print("{} flights got cancelled in 2015.".format(count))

#sb.boxplot(x='CANCELLED' == 1, y='CANCELLATION_REASON', data=flights, palette='hls')
#plt.show()


#sb.heatmap(input_raw.corr())