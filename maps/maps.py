from typing import Union
from functools import reduce

class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        movies_with_rating = filter(lambda movie: movie["rating_kinopoisk"], list_of_movies)
        filtered_movies = filter(
            lambda movie: float(movie["rating_kinopoisk"]) > 0
            and len(movie["country"].split(",")) > 1,
            movies_with_rating,
        )
        ratings = list(map(lambda movie: float(movie["rating_kinopoisk"]), filtered_movies))
        average_rating = sum(ratings) / len(ratings)
        return average_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        movies_with_rating = filter(lambda movie: movie["rating_kinopoisk"], list_of_movies)
        filtered_movies = filter(
            lambda movie: float(movie["rating_kinopoisk"]) >= rating,
            movies_with_rating,
        )
        list_of_movie_names = list(map(lambda movie: movie['name'], filtered_movies))
        count = reduce(lambda acc, name: acc + name.count('и'), list_of_movie_names, 0)
        return count
