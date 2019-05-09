## In this task, I have categorised all the Genres and counted them all, and then stored in the **totalGenres.json** file.

from Task5 import get_movie_list_details
from Task1 import scrape_top_list
movies_list = scrape_top_list()
top_ten_movie = (movies_list[:250])
import json

def analyse_movies_genre(how_many_movies):
    data = get_movie_list_details(how_many_movies)
    total_genre = []
    for i in data:
        genre = i['Genres']
        for j in genre:
            if j not in total_genre:
                total_genre.append(j)
    empty_dic = {}
    for i in total_genre:
        count = 0
        for j in data:
            genre = j['Genres']
            if i in genre:
                count+=1
        empty_dic[i] = count
    with open("totalGenres.json", "w") as f:
        jsndata = json.dumps(empty_dic, indent=4, sort_keys=True)
        f.write(jsndata)

(analyse_movies_genre(top_ten_movie))
