import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


filepath = "vgsales.csv"

gameList = pd.read_csv(filepath, low_memory=False)
#gameList.info()
#print(gameList.describe())
# From the data, I am interest to see what is the relationship between genre and rating for new games
# First I want to define what are new shows
# From describe I see that some years show 2020, which is strange for the data
# I want to remove these values so that they do not misappropriate my analysis
gamesSince2010 = gameList[((gameList['Year'] >= 2010) & (gameList['Year'] <= 2017))]

japSales = gamesSince2010['JP_Sales']
naSales = gamesSince2010['NA_Sales']
euSales = gamesSince2010['EU_Sales']
otherSales = gamesSince2010['Other_Sales']
globalSales = gamesSince2010['Global_Sales']
years = gamesSince2010['Year']

# First I want to see what is the frequency of the different genres
countGenre = gamesSince2010['Genre'].value_counts().sort_values(ascending=True)

# I want to display this as a bar chart
#plt.barh(countGenre,japSales)
#plt.show()

# First I want to see what is the frequency of the different genres in Japan
#countJapGenre = japSales['Genre'].value_counts().sort_values(ascending=False)


table_sales = pd.pivot_table(gamesSince2010,values=['NA_Sales'],index=['Year'],columns=['Genre'],aggfunc='mean',margins=False)

plt.figure(figsize=(19,16))
sns.heatmap(table_sales['NA_Sales'],linewidths=.5,annot=True,vmin=0.01,cmap='PuBu')
plt.title('Mean NA and JP sales of games')

#sns.heatmap(table_publisher['Global_Sales'],linewidths=.5,annot=True,vmin=0.01,cmap='PuBu')
#plt.figure(figsize=(19,16))
#plt.title('Max Global_Sales of games')
plt.show()


# I want to display this as a bar chart
#countJapGenre.plot.barh()
#plt.title('Japanese Sales by Genres')
#plt.xlabel('Sales')
#plt.ylabel('Genres')
#plt.show()



# Then I want to put this against ratings
# I define scores
# sales = newestShows["EU_Sales"]
# num_bins = 10
# plt.hist(sales, num_bins, facecolor='green', alpha=0.5)
# plt.xlabel("EU Sales")
# plt.ylabel("Count")
# plt.show()