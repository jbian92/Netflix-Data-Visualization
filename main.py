# prep program by importing a few packages
from matplotlib import pyplot as plt
import pandas as pd

# load the data
df = pd.read_csv('netflix_titles.csv')

### QUESTION 1: who are the best directors? ###
# directors are better if they have directed more shows on Netflix
# independent variable is the director, identified by their first and last name; categorical variable
# dependent variable is the value of "goodness", quantified to be the number of movies/shows they've directed that are on Netflix; numerical variable

# remove unnecessary rows where the director is not known
not_null_director = pd.notnull(df['director']) # creating a filter called not_null_director which should return True if a column has a value in the director column and False otherwise
q1_df = df[not_null_director] # filter applied to remove all columns where the director is unknown

q1_df.head() # to see the first couple of rows in dataframe

# merge rows with the same rows so the each row has a unique director
# count the number of movies that each person has directed
q1_df = q1_df.groupby(['director'],as_index=False)['title'].count() # groups by director and counts the number of titles for each director
q1_df = q1_df.rename(columns={'title':"movie/show count"})
q1_df = q1_df.nlargest(5,'movie/show count') # look at the top 5 directors in terms of movie/show count

# visualize the data as a bar plot
director = q1_df['director'] # x value
count = q1_df['movie/show count'] # y value
plt.figure(figsize=(9, 3))
plt.bar(director, count)
# plt.show()

### QUESTION 2: are shows or movies more popular? ###
# define popularity to be based on count

# merge rows so there are two rows: movies and shows
q2_df = df.groupby(['type'],as_index=False)['show_id'].count() 
q2_df = q2_df.rename(columns={'show_id':"count"})

# visualize the data as a bar plot
t = q2_df['type']
count = q2_df['count']
plt.figure(figsize=(9, 3))
plt.bar(t, count)
# plt.show()

### QUESTION 3: what is the distribution of Netflix TV shows/movies over time by release date? ###

# merge rows by release year 
q3_df = df.groupby(['release_year'],as_index=False)['show_id'].count() 
q3_df = q3_df.rename(columns={'show_id':"count"})

# visualize the data as a line plot
x = q3_df['release_year']
y = q3_df['count']
plt.figure(figsize=(9, 3))
plt.plot(x, y)
plt.show()