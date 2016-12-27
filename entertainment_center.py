"""We are importing fresh_tomatoes module for the front end code of website."""
import fresh_tomatoes  # Supplied by Udacity
import media
# We are importing the media module for storing movies information.

# Below is the backend code. Details of all the movies.
goal = media.Movie("Goal! The Dream Begins",
                   "A story of a boy going after his football dreams",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/GoalPoster.jpg/220px-GoalPoster.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=qGhCJXrqZwE")
interstellar = media.Movie("Interstellar",
                           "A story of the discovery of a new dimention",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

suicide_squade = media.Movie("Suicide Squade",
                             "Story where villains have to be heros",
                             "https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_%28film%29_Poster.png",  # NOQA
                             "https://www.youtube.com/watch?v=CmRih_VtVAs")

harry_potter_1 = media.Movie("Harry Potter and the Philosopher's Stone",
                             "A story of a boy who enters the wizarding world",
                             "http://www.gstatic.com/tv/thumb/movieposters/28630/p28630_p_v8_at.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=VyHV0BRtdxo")

star_wars_rogue_one = media.Movie("Rouge One: A Star Wars Story",
                                  "Story of the lost Jedi",
                                  "http://img.lum.dolimg.com/v1/images/rogueone_onesheeta_1000_309ed8f6.jpeg?region=0%2C0%2C1000%2C1481&width=480",  # NOQA
                                  "https://www.youtube.com/watch?v=frdj1zb9sMY")  # NOQA

shawshank_redumption = media.Movie("The Shawshank Redumption",
                                   "Prison break of a banker",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")  # NOQA

# Below we are making a list of all the movies and their attributes
movies = [goal, interstellar, suicide_squade, harry_potter_1,
          star_wars_rogue_one, shawshank_redumption]

# Below we give movies list as input to open_movies_page method
# in fresh_tomatoes modile
fresh_tomatoes.open_movies_page(movies)
