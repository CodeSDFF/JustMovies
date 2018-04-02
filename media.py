class Movie():
    """ The Movie Class
    This class will be used to create instances of a movie
    Attributes:
        title (str): Title of the movie.
        art (str): Image of movie poster.
        link (str): Url to the movie trailer on youtube.
        overview (str): Summary of the movie.
        order (int): Order of the movie among other movies.
        id (int): This is the movie id .
        backdrop_path (string): The background image for the movie.
    """

    def __init__(self, title, image, url, overview, order, movie_id, backdrop_path):

        self.title = title
        self.poster_image_url = image
        self.trailer_youtube_url = url
        self.overview = overview
        self.order = order,
        self.movie_id = movie_id,
        self.backdrop_path = backdrop_path

