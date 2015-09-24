# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:44:27 2015

@author: Doug
"""
'''
1.Read  yelp.csv  into a DataFrame. 
Bonus: Ignore the yelp.csv file, and construct this DataFrame yourself from yelp json. 
This involves reading the data into Python, decoding the JSON, converting it to a DataFrame, 
and adding individual columns for each of the vote types.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression 
from sklearn.cross_validation import train_test_split
from sklearn import metrics 
import numpy as np 



yelp = pd.read_csv('~\Desktop\DAT8\data\yelp.csv')
yelp.head()

'''
2.Explore the relationship between each of the vote types (cool/useful/funny) 
and the number of stars.
'''
yelp.isnull()
yelp.groupby('stars').describe()

yelp.plot(kind='scatter', x='stars', y='cool', alpha=0.2)
sns.lmplot(x='stars', y='cool', data=yelp, aspect=1.5, scatter_kws={'alpha':0.2})
yelp.boxplot(by='stars')
pd.scatter_matrix(yelp)
yelp.stars.value_counts().plot(kind='bar')



'''
Based on the scatter matrix, it looks like a positive relationship betwen the number of stars and the votes
There also seems to be a positive relationship between the votes
'''

'''
3.Define cool/useful/funny as the features, and stars as the response.
'''

x = yelp[['cool', 'useful', 'funny']]
x.shape

y = yelp.stars 
y.shape

'''
4.Fit a linear regression model and interpret the coefficients. 
Do the coefficients make intuitive sense to you? 
Explore the Yelp website to see if you detect similar trends.
'''
linreg = LinearRegression() 
linreg.fit(x, y) 

print linreg.intercept_ 
print linreg.coef_ 

linreg.predict([1,1,1])
'''
Given the coefficients, it seems like people generally vote between 3 & 4 stars, 
with a high tendancy toward 4 as indicated by the intercept.  From there, the votes
for cool affect the predicted score positively, while usefule and funny affect it negatively.
As a Yelp user myself, this makes sense. Cool is generally a positive term and it doesn't
sound right to say, "cool, this establishment sucks".  Reviews tend to be funny when they're 
trash talking an establishment.  And you usually think a review is useful if it is telling
you to stay away from an establishment, but perhaps the off chance of suggesting a dish.
'''

'''
5.Evaluate the model by splitting it into training and testing sets and computing the RMSE. 
Does the RMSE make intuitive sense to you?
'''

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=36)
linreg = LinearRegression() 
linreg.fit(x_train, y_train) 
y_pred = linreg.predict(x_test) 
np.sqrt(metrics.mean_squared_error(y_test, y_pred)) 

#The error given the random state of 36 results in an error of roughly 1.2

'''
6.Try removing some of the features and see if the RMSE improves.
'''
#I will be removing the features useful and funny
x = yelp[['cool']]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=36)
linreg = LinearRegression() 
linreg.fit(x_train, y_train) 
y_pred = linreg.predict(x_test) 
np.sqrt(metrics.mean_squared_error(y_test, y_pred)) 

#The RMSE gets worse
'''
7.Bonus: Think of some new features you could create from the existing data that might be 
predictive of the response. Figure out how to create those features in Pandas, add them to 
your model, and see if the RMSE improves.
'''
yelp['textlen'] = yelp.text.str.len()

x = yelp[['cool', 'useful', 'textlen']]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=36)
linreg = LinearRegression() 
linreg.fit(x_train, y_train) 
y_pred = linreg.predict(x_test) 
np.sqrt(metrics.mean_squared_error(y_test, y_pred)) 

#this comination seems to do better
'''
8.Bonus: Compare your best RMSE on the testing set with the RMSE for the "null model", 
which is the model that ignores all features and simply predicts the mean response value 
in the testing set.
'''

'''
9.Bonus: Instead of treating this as a regression problem, treat it as a classification 
problem and see what testing accuracy you can achieve with KNN.
'''

'''
10.Bonus: Figure out how to use linear regression for classification, and compare its 
classification accuracy with KNN's accuracy.
'''