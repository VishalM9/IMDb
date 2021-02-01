#!pip install imdbpy

from imdb import IMDb

ia = IMDb()

#Enter the name of the movie
name=input("Enter the name of the movie")

#Search movie by name
movies = ia.search_movie(name)

for i in range(len(movies)):
    #print(movies[i].movieID)
    #get movie id
    ID=movies[i].movieID
    print('Movie Name : '+str(movies[i]['title']))
    try:
        print('Rating : '+str(ia.get_movie(ID)['rating']))
    except KeyError as e:
        print("Rating not found")