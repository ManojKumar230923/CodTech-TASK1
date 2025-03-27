#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Import neccessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[28]:


# Load the dataset
netflix_data= pd.read_csv(r'C:\Users\WINDOWS\Downloads\netflix_titles_2021.csv\netflix_titles_2021.csv')
netflix_data.head()


# In[29]:


netflix_data.tail()


# In[30]:


# Check the info of the dataset
netflix_data.info()


# In[31]:


netflix_data.shape # Check dataset shape


# In[32]:


# Check for Duplication
netflix_data.duplicated().sum()


# In[33]:


# Missing Values
netflix_data.isnull().sum()


# In[34]:


# The percentage of missing values in each column
(netflix_data.isnull().sum()/(len(netflix_data)))*100


# In[35]:


# Replace null values with "Unknown" in specific columns
columns_to_fill = ['cast', 'country', 'date_added', 'rating',
'duration']
netflix_data[columns_to_fill] = netflix_data[columns_to_fill].fillna('Unknown')
# Now check if all null values are replaced
netflix_data.isnull().sum()


# In[36]:


# Describe the dataset
netflix_data.describe()


# In[37]:


#HIstogram
plt.figure(figsize=(10, 6))
sns.histplot(netflix_data['release_year'], bins=30, kde=True,
color='skyblue')
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()


# In[38]:


#barchart
top_countries = netflix_data['country'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index,
palette='viridis')
plt.title('Top 10 Countries with Most Productions')
plt.xlabel('Number of Productions')
plt.ylabel('Country')
plt.show()


# In[39]:


#Pie chart
content_types = netflix_data['type'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(content_types, labels=content_types.index, autopct='%1.1f%%',
colors=['lightgreen', 'lightcoral'])
plt.title('Proportion of Movies vs TV Shows')
plt.show()


# In[40]:


# Convert 'date_added' to datetime, handling errors gracefully
netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'],
errors='coerce')
# Plotting line plot for date added over time
date_added_counts = netflix_data['date_added'].dt.year.value_counts().sort_index()
plt.figure(figsize=(10, 6))
date_added_counts.plot(kind='line', marker='o', color='orange')
plt.title('Content Added Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Additions')
plt.grid(True)
plt.show()


# In[41]:


#Pairplot
plt.figure(figsize=(12, 6))
sns.pairplot(netflix_data[['release_year', 'duration', 'rating']],
hue='rating', palette='viridis')
plt.suptitle('Pairplot  of         Release Year, Duration, and Rating')
plt.show()


# In[42]:


#fairset
g = sns.FacetGrid(netflix_data, col='rating', col_wrap=4, height=4)
g.map(sns.histplot, 'release_year', bins=20, color='skyblue', kde=True)
g.set_titles('{col_name}')
plt.suptitle('Distribution of Release Years by Rating')
plt.tight_layout()
plt.show()


# In[ ]:




