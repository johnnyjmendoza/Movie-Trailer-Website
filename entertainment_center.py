# code created 12.6.2017
# Johnny J Mendoza
# Project: Movie Trailer Website

import media
import fresh_tomatoes

# begin movie list

aliens = media.Movie(
                    "Aliens", "Colonial Marines battle an Alien"
                    "species on a hostile planet.",
                    "https://upload.wikimedia.org/wikipedia"
                    "/en/f/fb/Aliens_poster.jpg",
                    "https://www.youtube.com/watch?v=W857ys3BlRI")

last_of_the_mohicans = media.Movie(
                    "Last of the Mohicans",
                    "The last members of a Native American tribe"
                    "struggle to stay alive.",
                    "http://www.movieposter.com/posters/"
                    "archive/main/62/MPW-31221",
                    "https://www.youtube.com/watch?v=e31_qBk14-w")

tombstone = media.Movie(
                    "Tombstone",
                    "An Arizona Cowboy deals with outlaws in the wild west",
                    "https://upload.wikimedia.org/wikipedia/"
                    "en/7/71/Tombstoneposter.jpeg",
                    "https://www.youtube.com/watch?v=XTWYKf5hXIg")

goodfellas = media.Movie(
                    "Goodfellas",
                    "A story of gangsters in New York in the 1960's.",
                    "https://www.movieposter.com/posters/"
                    "archive/main/36/MPW-18034",
                    "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

groundhog_day = media.Movie(
                    "Groundhog Day",
                    "A news station weatherman relives the same "
                    "day over and over again.",
                    "https://upload.wikimedia.org/wikipedia/"
                    "en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",
                    "https://www.youtube.com/watch?v=tSVeDx9fk60")

being_john_malkovich = media.Movie(
                    "Being John Malkovich",
                    "Going into the mind of actor John Malkovich",
                    "http://img.moviepostershop.com/"
                    "being-john-malkovich-movie-poster-1999-1010696298.jpg",
                    "https://www.youtube.com/watch?v=2UuRFr0GnHM")

# end movie list

movies = [aliens, last_of_the_mohicans, tombstone,
          goodfellas, groundhog_day, being_john_malkovich]
fresh_tomatoes.open_movies_page(movies)
