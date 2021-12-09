# Big Data
## MovieLens Dataset
Project made as my final for the Big Data class, attended during A.A. 2020/2021.
> Mattia Zorzan

## Queries
The following is a list of all the queries:

### Exploratory Analysis
* Number of ratings for each movie (and its distribution).
* Number of ratings for each user (and its distribution).
* Average score received by each movie.
* Average score given by each user.
* Top K movies (e.g., K = 10) with at least R ratings (e.g., R>20), i.e., the K movies with the highest average rating that have at least R reviews.

### Advanced Queries:
* Find if there is a correlation between the standard deviation of the ratings a movie has received, and the number of ratings.
* Find the evolution over time (with a granularity of N months) of the number of ratings and the average rating: do high rated movies maintain their ratings? Are low rated movies “abandoned” after a while?
* Find how the average rating of each movie changes as we progressively remove the ratings from users that rated more and more movies. For instance, we can identify different groups of users (who rated less than 10 movies, who rated between 11 and 30 movies, ...) and we can compute the average rating considering all the groups, then only the groups of users with at least 11 ratings, and so forth.
* Is it possible to identify groups of similar movies based on the ratings they received from the users? For instance, if movies m1 and m2 have both obtained 5 stars from users u1 and u2, they may be considered similar.

## Required packages
A list of all required packages can be found in the [requirements.txt](requirements.txt) file.<br>
To install them simply run `pip install -r requirements.txt` in the project root.