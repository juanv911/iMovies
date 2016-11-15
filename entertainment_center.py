import fresh_tomatoes
import media

# Doctor Strange movie instance
doctor_strange = media.Movie(
    "Doctor Strange", "img/placeholder.png",
    "https://www.youtube.com/watch?v=HSzx-zryEgM",
    "A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.",
    "Action, Adventure, Fantasy",
    2017,
    8.0)

# Star Trek Into Darkness movie instance
star_trek = media.Movie(
    "Star Trek Into Darkness",
    "img/placeholder.png",
    "https://www.youtube.com/watch?v=sJNyGFqgyag",
    "A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.",
    "Action, Adventure, Fantasy",
    2013,
    7.8)

# Transcendence movie instance
transcendence = media.Movie(
    "Transcendence",
    "img/placeholder.png",
    "https://www.youtube.com/watch?v=VCTen3-B8GU",
    "A scientist's drive for artificial intelligence, takes on dangerous implications when his consciousness is uploaded into one such program.",
    "Drama, Mystery, Romance",
    2014,
    6.3)

# The Dark Knight Rises movie instance
dark_knight = media.Movie(
    "The Dark Knight Rises",
    "img/placeholder.png",
    "https://www.youtube.com/watch?v=g8evyE9TuYk",
    "Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Catwoman, is forced from his imposed exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.",
    "Action, Thriller",
    2012,
    8.5)

# Skyfall movie instance
skyfall = media.Movie(
    "Skyfall",
    "img/placeholder.png",
    "https://www.youtube.com/watch?v=6kw1UVovByw",
    "Bond's loyalty to M is tested when her past comes back to haunt her. Whilst MI6 comes under attack, 007 must track down and destroy the threat, no matter how personal the cost.",
    "Action, Adventure, Thriller",
    2012,
    7.8)

# Django Unchained movie instance
django = media.Movie(
    "Django Unchained",
    "img/placeholder.png",
    "https://www.youtube.com/watch?v=eUdM9vrCbow",
    "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.",
    "Drama, Western",
    2012,
    8.5)

# Inglourious Basterds movie instance
inglourious_bastards = media.Movie(
    "Inglourious Bastards",
    "img/placeholder.png",
    "https://www.youtube.com/watch?v=KnrRy6kSFF0",
    "In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner's vengeful plans for the same",
    "Adventure, War, Drama",
    2009,
    8.3)

# The Dictator " movie instance
dictator = media.Movie(
    "The Dictator",
    "img/placeholder.png",
    "https://www.youtube.com/watch?v=cYplvwBvGA4",
    "The heroic story of a dictator who risked his life to ensure that democracy would never come to the country he so lovingly oppressed.",
    "Comedy, Romance",
    2012,
    6.4)

# Create array to hold instances of all movies
movies = [doctor_strange, star_trek, transcendence, dark_knight, skyfall, django, inglourious_bastards, dictator]

# Include movies array into the open_movies_page method from the fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)
