import webbrowser

# Movie is a parent class which stores title, storyline, cover image, youtube trailer url
# IMDB and Rotten Tomatoes ratings and direction/production for Movies and
# Series child classes


class Movie():
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_rating,
            rotten_tomatoes,
            movie_director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb = imdb_rating
        self.tomatoes = rotten_tomatoes
        self.director = movie_director

# All the other classes inherited Movie properties


class Movie_Drama(Movie):
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_rating,
            rotten_tomatoes,
            movie_director):
        Movie.__init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_rating,
            rotten_tomatoes,
            movie_director)


class Movie_Comedy(Movie):
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_rating,
            rotten_tomatoes,
            movie_director):
        Movie.__init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_rating,
            rotten_tomatoes,
            movie_director)

# To the Serie_Drama and Serie_Limited classes the property "season" is added


class Serie_Drama(Movie):
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_rating,
            rotten_tomatoes,
            movie_director,
            serie_season):
        Movie.__init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_rating,
            rotten_tomatoes,
            movie_director)
        self.season = serie_season


class Serie_Limited(Movie):
    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_rating,
            rotten_tomatoes,
            movie_director,
            serie_season):
        Movie.__init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube,
            imdb_rating,
            rotten_tomatoes,
            movie_director)
        self.season = serie_season
