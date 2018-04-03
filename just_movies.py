import webbrowser
import os

# Styles and scripting for the page
MAIN_PAGE_HEAD = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>justMovies</title>
    <link href="https://fonts.googleapis.com/css?family=Fredoka+One|Prompt:400,600,700" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Fredoka+One|Prompt" rel="stylesheet">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <!-- Bootstrap 4 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/css/bootstrap.min.css" integrity="sha384-AysaV+vQoT3kOAXZkl02PThvDr8HYKPZhNT5h/CXfBThSRXQ6jW5DO2ekP5ViFdi" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha384-3ceskX3iaEnIogmQchP8opvBy3Mi7Ce34nWjpBIwVTHfGYWQS9jwHDVRnpKKHJg7" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.3.7/js/tether.min.js" integrity="sha384-XTs3FgkjiBgo8qjEjBk0tGmf3wPrWtA6coPfQDfFEY8AnYJwjalXCiosYRBIBZX8" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="css/style.css">
    <script type="text/javascript" src="js/main.js"> </script>
</head>
'''

# The main page layout and title bar
MAIN_PAGE_CONTENT = '''

  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="close" data-dismiss="modal" aria-hidden="true">
            <img src="images/close.png"/>
          </a>
          <div class="scale-media" id="trailer-video-container"></div>
          <div class="modalImage">
            <div class="movie-image"></div>
            <div class="container">
                <img src="" class="movie-poster">
                <h2 class="movie-title"></h2>
                <p class="movie-overview"></p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Navbar -->
    <nav class="navbar navbar-fixed-top navbar-dark bg-primary">
        <div class="container ">
            <a class="navbar-brand logoTitle" href="#">
                <img src="images/justMovies.png" class="logo"  class="d-inline-block align-top" alt="Site logo">
                &nbsp; justMovies <span class="hidden-sm-down">best dramas of the past 3 years</span>
            </a>
            
        </div>
    </nav>
    </br>
    <div class="container">
      {movie_tiles}
    </div>
    <footer>
        <div class="content">
            <div class="rights">copyright &copy; 2018 <a href = "http://irinaserova.com/">Irina Serova</a></div>
        </div>  
    </footer>
    
    
 
  </body>
</html>
'''

# A single movie entry html template
MOVIE_TILE_CONTENT = '''
<div class="col-md-6 col-lg-4 movie-tile text-center cardBorder" data-tmdb-id="{movie_id}" data-movie-title="{movie_title}" data-backdrop-path="{backdrop_path}" data-poster="{poster_image_url}" data-overview="{overview}" data-toggle="modal" data-target="#trailer">
    <div class="card">
        <img src="{backdrop_path}" width="100%" alt="Image">
        <div class="title">
            <h4 class="card-title">{movie_title}</h4>
            <p class="watchTrailer" class="card-text">{overview}</p> 
            <a href="#" class="btn btn-primary">Trailer</a> 
        </div>
    </div>
</div>
'''


def create_movie_tiles_content (movies):
    """ Creates each movie tile for the justMovies website. """
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += MOVIE_TILE_CONTENT.format (
            movie_title=movie.title.encode ("ascii", "ignore"),
            poster_image_url=movie.poster_image_url,
            overview=movie.overview.encode ('utf-8').strip (),
            movie_id=movie.movie_id[0],
            backdrop_path=movie.backdrop_path,
            order=movie.order
        )
    return content


def open_movies_page (movies):
    """ Renders the justMovies HTML file and opens it in a web browser."""
    # Create or overwrite the output file
    output_file = open ('just_movies.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = MAIN_PAGE_CONTENT.format (movie_tiles=create_movie_tiles_content (movies))

    # Output the file
    output_file.write (MAIN_PAGE_HEAD + rendered_content)
    output_file.close ()

    # open the output file in the browser
    url = os.path.abspath (output_file.name)
    webbrowser.open ('file://' + url, new=2)  # open in a new tab, if possible