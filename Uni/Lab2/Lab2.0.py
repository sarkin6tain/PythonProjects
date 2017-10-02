import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# list of salaries for employees of San Francisco
# can already see that there are some missing values. e.g. Notes
filepath = "Salaries.csv"

salaries = pd.read_csv(filepath, low_memory=False)

# print(salaries.head())
# first 5 lines

# print(salaries.describe())
# gives summary stats for the data
# e.g. see that minimum pay is with a minus

latest_salaries = salaries[salaries['Year'] == 2014]
# using similar syntax to lists can drill down. Specifies the range of data to use

# print(latest_salaries.describe())

# print("\n Result: ${:,.02f}".format(latest_salaries['TotalPay'].mean()))
# histograms
# pay_data = latest_salaries['TotalPay']
# num_bin = 5

# plt.hist(pay_data, num_bin, facecolor='green', alpha=0.5)
# alpha is for transparency

# plt.show()

# plt.xlabel('Total Pay')

# plt.ylabel('Count')

# density plots
# pay_data.plot.density()

# pay_data.plot.density().set_yscale('log')
# plt.show()

# bar chart

# status = ('Divorced', 'Single', 'Married', 'Widowed')
# y_pos = np.arange(len(status))
# numbers = [400, 556, 778, 90]
# plt.bar(y_pos, numbers, align='center', alpha=0.5)
# plt.xticks(y_pos, status)
# plt.ylabel('Count')
# plt.title('Marital Status')
# plt.show()


# Different example
# CountJob = latest_salaries['JobTitle'].value_counts().nlargest(30).sort_values(ascending=True)
# count how many times each job title occurs, but show 30 most common ones, and sort them ascending
# CountJob.plot.barh()
# plt.show()

# TWO VARIABLES

# Line graphs
# x = np.arange(10)
# fig = plt.figure()
# ax = plt.subplot(111)
# on the same plot, subplots allow to give more figures
# for i in range(5):
  #  ax.plot(x, i*x, label='$y = %i$' %i)
    # first is x position and second is y position

# ax.legend()

# plt.show()

#Scatter plot
# x = np.arange(10)
# fig = plt.figure()
# ax = plt.subplot(111)
# fig.ax = plt.subplot()
# ax.scatter(np.linspace(-10, 10, 500), np.random.randn(500))

# plt.show()

# -------------------
#colourful scatter plot
# n=100
# x = np.random.rand(n)
# y = np.random.rand(n)
# colours = np.random.rand(n)
# area = np.pi*(20 * np.random.rand(n))**2
# plt.scatter(x, y, s=area, c = colours, alpha = 0.5)

# plt.show()

# -------------
# n = 500
# x = np.random.rand(n)
# y = x * np.random.rand(n)
# fog.ax = plt.subplot()
# fog?!?!?!?
# fit = np.polyfit(x, y, deg=1)
# ax.plot(x, fit[0]*x + fit[1], color='g')
# ax.scatter(x,y)
# plt.show()

#-----------
# BAR CHARTS FOR TWO VARS
# a = [67, 10, 30, 20, 23]
# b = [3, 42, 11, 17, 5]
# x = np.arange(5)
# width = 0.25
# plt.bar(x, a, width, color='r')
# plt.bar(x, b, width, color='y', bottom=a)
# plt.xticks(x, ('1','2','3','4','5'))
# plt.show()

# put them side by side
width=0.25
a = [67, 10, 30, 20, 25]
b = [30, 42, 11, 17, 5]
X = np.arange(5)
fig, ax = plt.subplots()
ax.bar(X, a, width, color='blue')
ax.bar(X+width, b, width, color='y')
ax.set_xticks(X + width / 2)
ax.set_xticklabels(('Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5'))
plt.show()

# ----------------
# HOW TO DEAL WITH MISSING VALUES
latest_
# shows in a lot of missing values in notesalaries.head()
latest_salaries.isnull().any()
latest_salaries.isnull().any().any()
# nesting any goes up
latest_salaries.isnull().sum()s
latest_salaries = latest_salaries.drop('Notes', axis=1)
latest_salaries.isnull().sum()
# axis to say it is a column
latest_salaries = latest_salaries.dropna()
# drop any column where there are any null values
