import fresh_tomatoes
import media

# This Python file contains the movies and series data
# The movies and series subclasses are separated by its category nomination

moonlight = media.Movie_Drama(
    "Moonlight",
    """A chronicle of the childhood, adolescence and burgeoning adulthood of a
                        young black man growing up in a rough neighborhood of Miami.""",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQxNTIyODAxMV5BMl5BanBnXkFtZTgwNzQyMDA3OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=9NJj12tJzqc",
    "7,6",
    "97%",
    "Berry Jenkins")


hacksaw_ridge = media.Movie_Drama(
    "Hacksaw Ridge",
    """WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa,
                        refuses to kill people, and becomes the first man in American history to receive the
                        Medal of Honor without firing a shot.""",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ1NjM3MTUxNV5BMl5BanBnXkFtZTgwMDc5MTY5OTE@._V1_SY1000_CR0,0,647,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=sslCRVx7nPQ",
    "8,2",
    "87%",
    "Mel Gibson")

deadpool = media.Movie_Comedy(
    "Deadpool",
    """A fast-talking mercenary with a morbid sense of humor is subjected
                        to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.""",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SY1000_SX686_AL_.jpg",
    "https://www.youtube.com/watch?v=gtTfd6tISfw",
    "8,1",
    "84%",
    "Tim Miller")


sing_street = media.Movie_Comedy(
    "Sing Street",
    """A boy growing up in Dublin during the 1980s escapes his strained
                        family life by starting a band to impress the mysterious girl he likes.""",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEzODA3MDcxMl5BMl5BanBnXkFtZTgwODgxNDk3NzE@._V1_SY1000_SX675_AL_.jpg",
    "https://www.youtube.com/watch?v=C_YqJ_aimkM",
    "8,0",
    "96%",
    "John Carney")

# Serie class contains an extra item for the season to test inheritance
# between the classes

crown = media.Serie_Drama(
    "The Crown",
    "The early reign of Queen Elizabeth II of the United Kingdom is portrayed.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNjU2NzA5MzgyM15BMl5BanBnXkFtZTgwNDAwOTUxMDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=JWtnJjn6ng0",
    "8,8",
    "91%",
    "Peter Morgan",
    "1")

game_of_thrones = media.Serie_Drama(
    "Game of Thrones",
    """Nine noble families fight for control over the mythical lands of Westeros;
                        A forgotten race returns after being dormant for thousands of years.""",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE3NTQ1NDg1Ml5BMl5BanBnXkFtZTgwNzY2NDA0MjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=yu8eRaq1FUM",
    "9,5",
    "95%",
    "David Benioff & D.B. Weiss",
    "6")

stranger_things = media.Serie_Drama(
    "Stranger Things",
    """When a young boy disappears, his mother, a police chief,
                        and his friends must confront terrifying forces in order to get him back.""",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEzMDAxOTUyMV5BMl5BanBnXkFtZTgwNzAxMzYzOTE@._V1_.jpg",
    "https://www.youtube.com/watch?v=XWxyRG_tckY",
    "9,0",
    "91%",
    "Matt Duffer & Ross Duffer",
    "1")

american_crime_story = media.Serie_Limited(
    "American Crime Story",
    """An anthology series centered around some of history's
                        most famous criminals, including O.J Simpson.""",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc4Mzg0MzMwMF5BMl5BanBnXkFtZTgwNzQ3NTY3NzE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=ZT0m9MBCMDo",
    "8,4",
    "97%",
    "Scott Alexander & Larry Karaszewski",
    "1")

# All the classes are in the same list

movies = [
    moonlight,
    hacksaw_ridge,
    deadpool,
    sing_street,
    crown,
    game_of_thrones,
    stranger_things,
    american_crime_story]
fresh_tomatoes.open_movies_page(movies)
