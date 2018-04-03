// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
	// Remove the src so the player itself gets removed, as this is the only
	// reliable way to ensure the video stops playing in IE
	$("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
	// Show the loading spinner
	$("#trailer-video-container").empty().html('<h1><i class="fa fa-circle-o-notch" aria-hidden="true"></i> Loading ...</h1>');
// Get movie info from to display on modal
	var backdrop_path = $(this).attr('data-backdrop-path');
	var movie_poster = $(this).attr('data-poster');
	var movie_overview = $(this).attr('data-overview');
	var movie_title = $(this).attr('data-movie-title');
	var movie_id = $(this).attr('data-tmdb-id');
	// Set the movie info in HTML elements
	$(".movie-image").css({
		'background-image': 'url(' + backdrop_path + ')'
	});
	$(".movie-overview").text(movie_overview);
	$('.movie-poster').attr("src", movie_poster);
	$(".movie-title").text(movie_title);

// Get the youtube id for the trailer from the Movie Database API
	$.getJSON('https://api.themoviedb.org/3/movie/' + movie_id + '/videos?api_key=697922371b7a841b4a9695d55147f5a3', function (data) {
		// Check to make sure the movie has a trailer
		if (typeof data.results[0] !== 'undefined') {
			var trailerYouTubeId = data.results[0].key;
			var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
			$("#trailer-video-container").empty().append($("<iframe></iframe>", {
				'id': 'trailer-video',
				'type': 'text-html',
				'src': sourceUrl,
				'frameborder': 0
			}));
		} else {
			$("#trailer-video-container").empty().html("Uh oh. The API doesn't have this trailer yet.");
		}
	});
});
// Animate in the movies when the page loads
$(document).ready(function () {
	$('.movie-tile').hide().first().show("medium", function showNext() {
		$(this).next("div").show("medium", showNext);
	});
});