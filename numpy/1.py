import numpy as np

moveie_ratings = np.array([8, 9, 0, 2, 5, 6 ,7, 5, 9, 10])

movie_ratings_3_movies = np.array([[63, 54, 70, 50],
                          [94, 85, 89, 95],
                          [64, 90, 73, 85]])
movie_rating_stars = moveie_ratings/2

# ratings order = a, b, c, d

a_ratings = movie_ratings_3_movies[:, 3]

print(a_ratings)