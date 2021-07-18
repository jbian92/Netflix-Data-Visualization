# prep the program by importing a few packages
from matplotlib import pyplot as plt
import pandas as pd

# load the data
df = pd.read_csv('netflix_titles.csv')

### QUESTION 1: Who are the best directors? ###
# independent variable is the director, identified by their first and last name
# dependent variable is the value of "goodness," quantified to be the number of movies/shows they've directed that are on Netflix

# remove unnecessary rows where the director is not known
# create a filter called not_null_director, which should return True if a column has a value in the director column and False otherwise
not_null_director = pd.notnull(df['director'])
# filter applied to remove all columns where the director is unknown
q1_df = df[not_null_director] 

# merge rows so each row has a unique director
# also, count the number of movies that each person has directed
q1_df = q1_df.groupby(['director'],as_index=False)['title'].count() # groups by director and counts the number of titles for each director
q1_df = q1_df.rename(columns={'title':"movie/show count"}) # rename the column "title" to "movie/show count"
q1_df = q1_df.nlargest(5,'movie/show count') # look at the top 5 directors in terms of movie/show count

# visualize the data as a bar plot
director = q1_df['director'] # x value
count = q1_df['movie/show count'] # y value
plt.figure(figsize=(9, 3))
plt.bar(director, count)
plt.xlabel("Name of Director")
plt.ylabel("Number of Movies/Shows")

### QUESTION 2: Are shows or movies more popular? ###

# merge rows so there are two rows: movies and shows
q2_df = df.groupby(['type'],as_index=False)['show_id'].count() 
q2_df = q2_df.rename(columns={'show_id':"count"})

# visualize the data as a bar plot
t = q2_df['type']
count = q2_df['count']
plt.figure(figsize=(9, 3))
plt.bar(t, count)
plt.xlabel("Type")
plt.ylabel("Count")

### QUESTION 3: What is the distribution of Netflix TV shows/movies over time by release date? ###

# merge rows by release year 
q3_df = df.groupby(['release_year'],as_index=False)['show_id'].count() 
q3_df = q3_df.rename(columns={'show_id':"count"})

# visualize the data as a line plot
x = q3_df['release_year']
y = q3_df['count']
plt.figure(figsize=(9, 3))
plt.plot(x, y)
plt.xlabel("Release Year")
plt.ylabel("Number of Movies/Shows")

plt.show()