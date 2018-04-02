import urllib
from datetime import datetime, timedelta
import json
import just_movies
import media

API_KEY = "f110442650fb81b1aa9ce95c5a7d2894"


def create_movies(settings):
    """ Creates the movies to pass to the justMovies website.
    This function calls The Movie Database for the best drama's that are between the
    today's date and the date as of 3 years ago. It turns the json results
    into Movie instances and returns an array of the movies created.
    Args:
        settings: An object of settings for TMDB image sizes
    Returns:
        movies: An array of Movie instances.
    """

    new_movies_url = ("https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=" +
                      API_KEY + "&primary_release_date.gte=" +
                      get_three_years_ago_url_param() +
                      "&primary_release_date.lte=" + get_today_url_param())
    jsonurl = urllib.urlopen(new_movies_url)
    api = json.loads(jsonurl.read())

    movies = []
    i = 0
    for item in api['results']:
        # Check for the existence of backdrop_images
        if item['backdrop_path'] is not None:
            backdrop_url = (settings['secure_base_url'] +
                            settings['backdrop_sizes'][1] +
                            item['backdrop_path'])
        else:
            backdrop_url = 'popcorn.jpg'

        if item['poster_path'] is not None:
            image_url = (settings['secure_base_url'] +
                         settings['poster_sizes'][4] +
                         item['poster_path'])
        else:
            image_url = 'poster.jpg'

        movie = media.Movie(item['title'], image_url, "test", item['overview'],
                            i, item['id'], backdrop_url)
        movies.insert(i, movie)
        i = i + 1
    return movies


def create_site(settings):
    """ Creates movies and launches the website.
    Args:
        settings: image settings to pass to the create_movies function
    """

    movies = create_movies(settings)
    just_movies.open_movies_page(movies)


def get_image_settings():
    """ Gets the image settings defined by The Movie Database API.
    Returns:
        An object for various settings for image sizes. For more
        information on why this is necessary, please refer to
    """

    config_url = "https://api.themoviedb.org/3/configuration?api_key="+API_KEY
    results = urllib.urlopen(config_url)
    api = json.loads(results.read())
    return api["images"]


def get_three_years_ago_url_param():
    """ This function gets the date 31 days ago and then formats it so it can
    be used as a URL query string parameter.
    Returns:
        A string in the format "2018-12-31"
    """
    two_weeks_ago = datetime.today() - timedelta(days=720)
    return two_weeks_ago.strftime('%Y-%m-%d')


def get_today_url_param():
    """ This function gets today' width="150px" style="float: left; margin: 10px; width="150px" style="float: left; margin: 10px;s date and then formats it to use as a URL
    query string parameter.
    Returns: width="150px" style="float: left; margin: 10px;
        A string in the format "2018-12-31"
    """
    today = datetime.today()
    return today.strftime('%Y-%m-%d')

IMAGE_SETTINGS = get_image_settings()
create_site(IMAGE_SETTINGS)