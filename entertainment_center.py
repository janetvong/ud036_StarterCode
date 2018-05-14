import fresh_tomatoes  # works only if in the same folder
import media  # media.py file

# This file stores instances of Class media. This file contains the
# characteristics that are unique to each instance.

princess_diaries = media.Movie("Princess Diaries",
                               "A story of a girl who discovers she's a princess\
                               .",
                               "https://upload.wikimedia.org/wikipedia/en/5/58/"
                               "Princess_diaries_ver1.jpg",
                               "https://www.youtube.com/watch?v=2CkcwPi20ms")

star_wars = media.Movie("Star Wars: The Force Awakens",
                        "War continues between the First Order and the new Repub\
                        lic.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_War"
                        "s_The_Force_Awakens_Theatrical_Poster.jpg",
                        "https://www.youtube.com/watch?v=erLk59H86ww")

black_panther = media.Movie("Black Panther",
                            "The story of T'Challa returning to Wakanda to \
                             succeed the throne.",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/"
                            "Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

wonder_woman = media.Movie("Wonder Woman",
                           "A story about the Wonder Woman's past life.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/"
                           "Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

mean_girls = media.Movie("Mean Girls",
                         "Cady moves to a new school and navigates her way \
                         through high school and the Plastics.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/a/ac/"
                         "Mean_Girls_film_poster.png/220px-Mean_Girls_film_poster\
                         .png",
                         "https://www.youtube.com/watch?v=Ezf5vJgTTz0")

avengers = media.Movie("Avengers: Infinity War",
                       "Superheros across the galaxy fight Thanos and try to \
                       protect him from getting all of the inifity stones.",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers"
                       "_Infinity_War_poster.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

white_chicks = media.Movie("White Chicks",
                           "Undercover cops who change their appearance as they \
                           work on a case.",
                           "https://upload.wikimedia.org/wikipedia/en/2/2b/White"
                           "_chicks.jpg",
                           "https://www.youtube.com/watch?v=xebjMIYduxQ")

girls_trip = media.Movie("Girl's Trip",
                         "Old college friends reunite in New Orleans for a crazy\
                          fun weekend.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f4/Girls_"
                         "Trip_film_poster.png",
                         "https://www.youtube.com/watch?v=HnqkPpSn94Y")

ready_player_one = media.Movie("Ready Player One",
                               "Gamer go into the Oasis to find Halloway's\
                                Easter egg.",
                               "https://upload.wikimedia.org/wikipedia/en/7/74/"
                               "Ready_Player_One_%28film%29.png",
                               "https://www.youtube.com/watch?v=cSp1dM2Vj48")

# The line below puts all of the movies into a list.
movies = [princess_diaries, star_wars, black_panther, wonder_woman, mean_girls,
          avengers, white_chicks, girls_trip, ready_player_one]

# The line below opens all of the movies in the html file.
fresh_tomatoes.open_movies_page(movies)

