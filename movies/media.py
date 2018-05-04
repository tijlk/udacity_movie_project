class Movie:
    """This is a class to store information about a movie."""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Constructor for the Movie class
        :param movie_title: title of the movie (string)
        :param movie_storyline: storyline of the movie (string)
        :param poster_image: URL of a poster image for the movie (string)
        :param trailer_youtube: URL of a youtube trailer for the movie (string)
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube