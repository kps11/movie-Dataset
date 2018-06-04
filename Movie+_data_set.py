
# coding: utf-8

#  coding: utf-8
# # Investigte a movie Data set
# # Let's analyse the question with the following data set
# # Which genres are most popular from year to year? 
# # What kinds of properties are associated with movies that have high revenues?

# In[3]:

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# In[4]:

movies= pd.read_csv('C:/Users/khiro/Desktop/udacity/tmdb-movies.csv')


# In[8]:

movies.shape


# # Let's begin with the 1st question 
# Which genres are most popular from year to year?

# > so first we have to is there any null avalue in the genres secstion if availabe then we have to remove them 
# 

# In[12]:

remove_null_geners_movie= movies.dropna(subset=['genres'],axis=0)


# In[141]:

remove_null_geners_movie.isnull().sum()


# In[68]:

remove_null_geners_movie.head()


# In[217]:

piv = remove_null_geners_movie.pivot_table(index='release_year', columns='genres', values='popularity')


# In[219]:

piv.idxmax(axis=1)


# In[232]:

type(deduplicated)


# In[221]:

df = pd.read_csv('C:/Users/khiro/Desktop/udacity/tmdb-movies.csv')
sorted_df = df.sort_values(by=['popularity'],ascending=False)
deduplicated = sorted_df.drop_duplicates(subset=['release_year'],keep='first')
deduplicated.loc[:,['release_year','genres','popularity']].sort_values(by=['release_year'])


# In[222]:

ax=sns.barplot(data=deduplicated,x='release_year',y='popularity')
ax.set(ylabel='popularity')

ax.set_title('Survival Rate based on age group')


# # Let's move to the 2nd question

# >What kinds of properties are associated with movies that have high revenues?

# In[223]:

movies.head()


# >>Sort the dataset according to revenue

# In[224]:

movies_df= movies.sort_values(by=['revenue'],ascending=False)


# In[230]:

movies_df.head()


# >remove duplicates from release_year

# In[233]:

movies_year=movies_df.drop_duplicates(subset=['release_year'],keep='first')


# In[238]:

movies_year


# In[239]:

movies_year.loc[:,['release_year','cast','director']].sort_values(by=['release_year'])



# >plot the graph

# In[268]:

ax=sns.barplot(data=movies_year,x='director',y='revenue')
ax.set(ylabel='revenue')

ax.set_title('Survival Rate based on age group')


# # From the above analysis we know that some directors are manage to generate more revenue 
