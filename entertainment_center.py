import media
import fresh_tomatoes

# Six instances of the class Movie
batman_the_dark_knight = media.Movie(
    "Batman: the dark knight",
    "Batman isn't a comic book anymore. Christopher Nolan's The Dark Knight is a haunted film"
    "that leaps beyond its origins and becomes an engrossing tragedy ",
    "https://avante.biz/wp-content/uploads/The-Dark-Knight-Wallpaper/The-Dark-Knight-Wallpaper-001.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY",   
    "29 august 2012")

blade_runner_2049 = media.Movie(
    "Blade Runner 2049",
    "We now find ourselves in an age where the filmmaking craft is so preoccupied with making money"
    "that it hinders the art form itself and saturates the market with crowd-pleasing dross"
    "Excelent",
    "https://avante.biz/wp-content/uploads/Blade-Runner-2049-wallpapers/Blade-Runner-2049-wallpapers-001.jpg",
    "https://www.youtube.com/watch?v=gCcx85zbxz4",
    "5 october 2017")

inception = media.Movie(
    "inception",
    "he mind-blowing movie event of the summer arrives just in time to hold back the flow "
    "of Hollywood sputum that's been sliming the multiplex. Inception, written and directed "
    "by the visionary Christopher Nolan, will be called many things, starting with James Bond Meets The Matrix",
    "https://www.hdwallpapers.in/walls/joseph_gordon_levitt_in_inception-wide.jpg",
    "https://www.youtube.com/watch?v=YoHD9XEInc0",
    "24 september 2010")

matrix = media.Movie(
    "The Matrix",
    "The Matrix is a visually dazzling cyberadventure, full of kinetic excitement, "
    "but it retreats to formula just when it's getting interesting.",
    "http://www.noisiamofuturo.it/wp-content/uploads/2017/01/Matrix-Background-Wallpaper.png",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8",
    "27 october 2003")

blade_runner = media.Movie(
    "blade runner",
    "blend of science fiction and noir detective fiction, Blade Runner (1982) was a box office and "
    "critical bust upon its initial exhibition, but its unique postmodern production design became "
    "hugely influential within the sci-fi genre",
    "https://georgespigot.files.wordpress.com/2013/07/blade-runner-05.jpg",
    "https://www.youtube.com/watch?v=eogpIG53Cis",
    "14 october 1982")

movies = [batman_the_dark_knight, blade_runner_2049, inception, matrix, blade_runner]

# Create and open the movie website .html file
fresh_tomatoes.open_movies_page(movies)
