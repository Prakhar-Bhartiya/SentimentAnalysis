"""
DATA DESCRIPTION

sentiment140 dataset. It contains 1,600,000 tweets extracted using the twitter api . The tweets have been annotated (0 = negative, 4 = positive) and they can be used to detect sentiment .

It contains the following 6 fields:

target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
ids: The id of the tweet ( 2087)
date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)
flag: The query (lyx). If there is no query, then this value is NO_QUERY.
user: the user that tweeted (robotickilldozr)
text: the text of the tweet (Lyx is cool)

"""

#import libraries
import pandas as pd

data = pd.read_csv('training.1600000.processed.noemoticon.csv',encoding = 'latin', header=None, nrows=25)

#Adding header to data
data = data.rename(columns={0: 'target', 1: 'id', 2: 'TimeStamp', 3: 'query', 4: 'username', 5: 'content'})

#Dropping unncessary columns
data.drop(['id','TimeStamp','query'], axis=1, inplace=True)


print(data.to_string())
