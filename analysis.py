#import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
#import dataset
netflix_df = pd.read_csv('netflix_data.csv')
#print(netflix_df)
#Most frequent movie duration in the 1990s? duration
movies_1990s = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999)]
##plt.hist(movies_1990s['duration'])
##plt.show()
duration = int(movies_1990s['duration'].mode()[0])
print('The most frequent movie duration is ' + str(duration) + ' minutes.')
#Find the number of short action movies in 1990s. Short is defined as < 90-minute movies. short_movie_count 
action_movies = movies_1990s[(movies_1990s['type'] ==  'Movie') & (movies_1990s['genre'] == 'Action')]
short_movie = action_movies[action_movies['duration'] < 90]
short_movie_count = len(short_movie)
print('There are ' + str(short_movie_count) + ' short action movies.')

