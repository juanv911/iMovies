import webbrowser

class Movie():
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url, movie_storyline, movie_genre, movie_year, movie_rating):  
        self.title = movie_title
        self.movie_poster = poster_image_url
        self.movie_trailer = trailer_youtube_url
        self.storyline = movie_storyline
        self.genre = movie_genre
        self.year = movie_year
        self.rating = movie_rating

    def show_trailer(self):
        webbrowser.open(self.movie_trailer)
