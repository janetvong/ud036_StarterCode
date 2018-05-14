import webbrowser


class Movie():
    """ This is the documentation. class variables, outside of init function,
    google likes to keep contants as all caps. """

    valid_ratings = ["G", "PG", "PG-13", "R"]

    # intializes title, storyline, poster image, and trailer.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline,
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)  # Open trailer in webbrowser
