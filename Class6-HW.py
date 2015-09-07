# -*- coding: utf-8 -*-
"""
Created on Sun Sep 06 18:21:46 2015

@author: Doug
"""

''' 
Pandas Homework with IMDb data 
''' 

 
''' 
BASIC LEVEL 
''' 

 
import pandas as pd 
import matplotlib.pyplot as plt 
 
 
# read in 'imdb_1000.csv' and store it in a DataFrame named movies 

imdb = pd.read_csv('imdb_1000.csv')
imdb.head()
 

# check the data type of each column 
imdb.dtypes
 
# calculate the average movie duration 
imdb.duration.mean()
 
# sort the DataFrame by duration to find the shortest and longest movies 
imdb.sort('duration').drop(['star_rating', 'content_rating', 'genre', 'actors_list'], axis=1)
 
# create a histogram of duration, choosing an "appropriate" number of bins 
imdb.duration.plot(kind='hist', bins=20)
 
# use a box plot to display that same data 
imdb.duration.plot(kind='box')
 
''' 
INTERMEDIATE LEVEL 
''' 

# count how many movies have each of the content ratings 
imdb.genre.value_counts()
 
# use a visualization to display that same data, including a title and x and y labels 
imdb.genre.value_counts().plot(kind='bar', title='Counts by Genre')
plt.xlabel('Genre')
plt.ylabel('Count')
 
# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP 
imdb.content_rating.replace(to_replace=['NOT RATED', 'APPROVED', 'PASSED', 'GP'], value='UNRATED', inplace=True)
imdb.content_rating.value_counts()
 
# convert the following content ratings to "NC-17": X, TV-MA 
imdb.content_rating.replace(to_replace=['X', 'TV-MA'], value='NC-17', inplace=True)
imdb.content_rating.value_counts()
 
# count the number of missing values in each column 
imdb.isnull().sum() 
 
# if there are missing values: examine them, then fill them in with "reasonable" values 
imdb.content_rating.fillna(value='UNRATED', inplace=True)
 
# calculate the average star rating for movies 2 hours or longer, 
imdb[imdb.duration >= 120].star_rating.mean()

# and compare that with the average star rating for movies shorter than 2 hours 
imdb[imdb.duration < 120].star_rating.mean()
 
# use a visualization to detect whether there is a relationship between duration and star rating 
imdb.plot(kind='scatter', x='duration', y='star_rating', alpha = 0.2)

# calculate the average duration for each genre 
imdb.groupby('genre').agg('mean')
 
''' 
ADVANCED LEVEL 
''' 

# visualize the relationship between content rating and duration 
imdb['content_num'] = imdb.content_rating.map({'R':1, 'PG-13':2, 'UNRATED':3, 'PG':4, 'G':5, 'NC-17':6})
imdb.plot(kind='scatter', x='duration', y='content_num', alpha = 0.2)
imdb.drop('content_num', axis=1, inplace =True)

imdb.hist(column='duration', by='content_rating', sharex=True)

# determine the top rated movie (by star rating) for each genre 

imdb.drop(['content_rating', 'duration', 'actors_list'], axis=1).groupby('genre').max()

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates 
imdb.duplicated('title')].sum()
imdb.title.value_counts()
imdb[imdb.duplicated()]
 
# calculate the average star rating for each genre, but only include genres with at least 10 movies 

imdb.groupby('genre').star_rating.agg('mean')[imdb.genre.value_counts() >= 10]
 
''' 
BONUS 
''' 
 
# Figure out something "interesting" using the actors data! 
imdb[imdb.actors_list.str.contains('Morgan Freeman')]

#These are the movies that Morgan Freeman acting in