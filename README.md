# CODTECH-TASK-1
# Exploratory Data Analysis (EDA) on Netflix Dataset
## Table of Contents
- [Overview](#overview)
- [Key Activities](#key-activities)
- [Technologies](#technologies)
- [Observations / Insights](#observations--insights)
## Overview
**Name:** MANOJ KUMAR

**Company:** CODTECH IT SOLUTIONS

**Domain:** Data Scientist

**ID:** CT8DS698

**Mentor:** Muzammil Ahmed

**Duration:** June, 2024 - August, 2024

### Project
**Project:** Exploratory Data Analysis (EDA) on Netflix Dataset
**Objective:**
Perform a comprehensive EDA on the Netflix dataset to uncover insights related to content
diversity, audience targeting, and genre preferences.
## Technologies
- Python
- Jupyter Notebook
- pandas
- numpy
- seaborn
- matplotlib
## Key Activities
### 1. Imported Libraries
The first step in any data analysis project is importing the necessary libraries. For this
project, the following libraries are used:
- **pandas:** Used for data manipulation and analysis. It provides data structures and
functions needed to manipulate structured data seamlessly.
- **numpy:** A fundamental package for scientific computing with Python. It provides support
for arrays and matrices, along with a collection of mathematical functions to operate on
these data structures.
- **seaborn:** A statistical data visualization library based on matplotlib. It provides a
high-level interface for drawing attractive and informative statistical graphics.
- **matplotlib:** A comprehensive library for creating static, animated, and interactive
visualizations in Python.
### 2. Loaded the Netflix Data
Loading the dataset is a crucial step. The dataset is loaded into a pandas DataFrame, which
provides various functionalities to explore and manipulate the data. This step typically
involves reading a CSV file or other data formats:
```python
import pandas as pd
netflix_data = pd.read_csv('path_to_netflix_dataset.csv')
```
### 3. Analyzed the Data
Once the data is loaded, the next step is to get an understanding of its structure and
contents. This involves several basic exploration commands:
- **head() and tail():** These functions are used to view the first few and last few rows of the
dataset, respectively, giving a quick glimpse into the data.
```python
print(netflix_data.head())
print(netflix_data.tail())
```
- **info():** This function provides a concise summary of the DataFrame, including the
number of non-null entries and the data types of each column.
```python
print(netflix_data.info())
```
- **shape:** This attribute returns the dimensions of the DataFrame, showing the number of
rows and columns.
```python
print(netflix_data.shape)
```
### 4. Preprocessing
Data preprocessing is an essential step to clean and prepare the data for analysis. This
involves:
- **Finding Duplicates:** Identifying and handling duplicate entries to ensure the dataset's
integrity.
```python
duplicates = netflix_data.duplicated()
print(duplicates.sum())
```
- **Handling Missing Values:** Checking for missing values and deciding on a strategy to
handle them, such as removing rows/columns or imputing values.
```python
missing_values = netflix_data.isnull().sum()
print(missing_values)
```
- **Replacing Missing Values:** Depending on the analysis requirements, missing values can
be replaced with appropriate values, like the mean, median, or mode.
```python
netflix_data.fillna(method='ffill', inplace=True)
```
### 5. Data Visualization
Data visualization is a crucial part of EDA, providing insights that are not immediately
obvious from the raw data. Different types of plots are used to explore various aspects of the
data:
- **Histogram:** Shows the distribution of a single numeric variable.
```python
netflix_data['column_name'].hist()
```
- **Bar Chart:** Used to compare different categories of data.
```python
netflix_data['column_name'].value_counts().plot(kind='bar')
```
- **Pie Chart:** Displays the proportion of categories in a dataset.
```python
netflix_data['column_name'].value_counts().plot(kind='pie')
```

- **Line Plot:** Useful for showing trends over time.
```python
netflix_data.plot(x='date_column', y='numeric_column', kind='line')
```

- **Pair Plot:** Plots pairwise relationships in a dataset.
```python
sns.pairplot(netflix_data)
```
- **FacetGrid:** Used for plotting conditional relationships.
```python
g = sns.FacetGrid(netflix_data, col="column_name")
g.map(plt.hist, "another_column")
```
## OutComes

![Untitled design (2)](https://github.com/user-attachments/assets/83359ff5-8cbd-4f7f-9851-9ecc9af756db)
## 6. Observations / Insights
#### Global Content Diversity
The dataset represents content from a diverse range of countries, including prominent
contributions from the United States, South Africa, and India. This diversity reflects a global
approach to content acquisition and audience targeting.
#### Shift Towards Streaming TV Shows
There is a noticeable trend towards streaming TV shows, as indicated by the prevalence of
multiple seasons listed in the dataset. This suggests a strategic focus on episodic content to
cater to binge-watching habits.
#### Audience Targeting by Rating
The predominant rating category in the dataset is 'TV-MA', indicating a focus on mature
audiences. This strategic choice likely aligns with viewer demographics and content
preferences on the platform.
#### Recent Content Emphasis
A significant portion of the content was added or released in recent years, particularly
around 2020 and 2021. This reflects a strategy of acquiring and showcasing recent
productions to maintain viewer engagement with up-to-date content.
#### Genre Preferences and Diversity
The dataset covers a wide array of genres, including documentaries, international TV shows,
dramas, and crime series. This genre diversity caters to varied viewer interests and ensures
a broad appeal across different demographics and preferences
