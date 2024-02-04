# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 10:29:11 2024

@author: Isaac beas
"""

import pandas as pd

import matplotlib.pyplot as plt

# Read the movie dataset from CSV


# Read the movie dataset from CSV
movie_data = pd.read_csv('movie_dataset.csv')

# Check for missing data
print("Number of missing values in each column:")
print(movie_data.isnull().sum())

# Drop rows with missing values
movie_data_clean = movie_data.dropna()

# Verify if missing data is removed
print("Number of missing values in each column after removing them:")
print(movie_data_clean.isnull().sum())

# Explore the dataset and get some basic statistics
movie_data_clean.info() # This will show the number of rows, columns, and data types in the dataset

movie_data_clean.describe() # This will show the summary statistics of the numerical columns, such as mean, median, standard deviation, etc.
movie_data_clean.head() # This will show the first five rows of the dataset

# Group the dataset by the Titles column and find the mean values of each group
movie_data_clean.groupby('Title').mean() # This will group the dataset by the titles column and calculate the mean values of the other columns for each group

# Group the dataset by the titles column and find the mean values of each group
movie_data_clean.groupby('Title').mean() # This will group the dataset by the titles column and calculate the mean values of the other columns for each group

# Access specific columns for analysis
titles = movie_data_clean['Title']

genres = movie_data_clean['Genres']

ratings = movie_data_clean['Rating']

votes = movie_data_clean['Votes']

revenue = movie_data_clean['Revenue (Millions)']

# find the top 5 rates movies 
top_rate_movies = movie_data_clean.nlargest(5, 'Rating')

print("Top 5 highest Rating")

print(top_rate_movies[['Title', 'Rating']])


# Calculate average rating
average_rating = ratings.mean()

print("Average Rating:", average_rating)

# Calculate average revenue (Millions)
average_revenue = revenue.mean()
print("Average Revenue",average_revenue )

# Convert the release_Year column to datetime data type
movie_data_clean['Year'] = pd.to_datetime(movie_data_clean['Year'])

# Filter movies released between 2015 and 2017
filtered_movies = movie_data_clean[(movie_data_clean['Year'].dt.year >= 2015) & 
                             (movie_data_clean['Year'].dt.year <= 2017)]

# Calculate the total revenue
total_revenue = filtered_movies['Revenue (Millions)'].sum()
# Print the total revenue
print("Total Revenue between 2015 and 2017:", total_revenue)


# Convert the release_Year column to datetime data type
movie_data['Year'] = pd.to_datetime(movie_data['Year'])

# Specify the year for which we want to count the movies
year = 2016

# Filter movies released in the specified year
filtered_movies2 = movie_data_clean[movie_data_clean['Year'].dt.year == year]
# Count the number of movies
num_movies = len(filtered_movies2)

# Print the number of movies released in the specified year
print("Number of Movies Released in", year, ":", num_movies)


# Specify the name of the director you want to search for
director_name = 'Christopher Nolan'

# Filter movies directed by the specified director
filtered_movies3 = movie_data_clean[movie_data_clean['Director'].str.contains(director_name)]
# Count the number of movies
num_movies = len(filtered_movies3)
# Print the number of movies directed by the specified director
print("Number of Movies Directed by", director_name, ":", num_movies)



# Specify the minimum rating threshold
min_rating = 8.0

# Filter movies with a rating of at least min_rating
filtered_movies4 = movie_data_clean[movie_data_clean['Rating'] >= min_rating]

# Count the number of movies
num_movies = len(filtered_movies4)

# Print the number of movies with a rating of at least min_rating
print("Number of Movies with a Rating of at least", min_rating, ":", num_movies)


# Specify the name of the director
director_name = 'Christopher Nolan'

# Filter movies directed by Christopher Nolan
filtered_movies = movie_data[movie_data['Director'] == director_name]

# Calculate the median rating
median_rating = filtered_movies['Rating'].median()

# Print the median rating of movies directed by Christopher Nolan
print("Median Rating of Movies Directed by", director_name, ":", median_rating)


# Convert the release_date column to datetime data type
movie_data_clean['Year'] = pd.to_datetime(movie_data_clean['Year'])

# Group the movies by release year and calculate the average rating for each year
average_ratings = movie_data_clean.groupby(movie_data_clean['Year'].dt.year)['Rating'].mean()

# Find the year with the highest average rating
highest_average_rating_year = average_ratings.idxmax

# Filter the movies by year
movies_2006 = movie_data_clean[movie_data_clean["Year"] == 2006]
movies_2016 = movie_data_clean[movie_data_clean["Year"] == 2016]

# Count the number of movies in each year
count_2006 = len(movies_2006)
count_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = (count_2016 - count_2006) / count_2006 * 100

# No 2006 year in the dataset

# Filter the movies by year
movies_2006 = movie_data[movie_data["Year"] == 2006]
movies_2016 = movie_data[movie_data["Year"] == 2016]

# Count the number of movies in each year
count_2006 = len(movies_2006)
count_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = (count_2016 - count_2006) / count_2006 * 100

# Print the result
print(f"The percentage increase in number of movies made between 2006 and 2016 is {percentage_increase:.2f}%")

# Create a series of all the actors by splitting and exploding the actors column
all_actors = movie_data_clean["Actors"].str.split(",").explode()

# Count the frequency of each actor and sort them in descending order
actor_counts = all_actors.value_counts().sort_values(ascending=False)

# Print the name and count of the most common actor
print(f"The most common actor in all the movies is {actor_counts.index[0]} with {actor_counts[0]} movies.")




# Split the genres column by | and explode it to create a series of all genres
all_genres = movie_data["Genre"].str.split("|").explode()

# Count the number of unique genres using nunique method
unique_genres = all_genres.nunique()

# Print the result
print(f"There are {unique_genres} unique genres in the dataset.")

import seaborn as sns

# Calculate the correlation matrix of the numerical features
correlation_matrix = movie_data_clean.iloc[:,1:].corr()

# Plot the correlation matrix as a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="Blues")

