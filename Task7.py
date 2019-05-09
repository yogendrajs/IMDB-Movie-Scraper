## In this task, I have counted all the movies that have been released by a particular director.

from Task5 import get_movie_list_details
from Task1 import scrape_top_list
import pprint

movies_list = scrape_top_list()
movies_detail_list = (movies_list[:10])

def analyse_movies_directors(how_many_movies):
    allmovies = get_movie_list_details(how_many_movies)
    director_names = []
    for i in allmovies:
        dir_name = i['Director']
        for j in dir_name:
            if j not in director_names:
                director_names.append(j)
    # print (director_names)
    new_dir_list = {}
    for k in director_names:
        count = 0
        for x in allmovies:
            dirname = x['Director']
            if k in dirname:
                count+=1
        new_dir_list[k] = count
    return new_dir_list
pprint.pprint(analyse_movies_directors(movies_detail_list))
