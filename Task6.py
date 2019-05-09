## In this task, I have counted all the movies that have been released in Hindi, English and Malayalam languages.

from Task5 import get_movie_list_details
from Task1 import scrape_top_list
movies_list = scrape_top_list()
top_ten_movie = movies_list[:250]

def analyse_movies_language(how_many_movies):
    allmovies = get_movie_list_details(how_many_movies)
    hindi = 0
    english = 0
    malayalam = 0
    for each_movie in allmovies:
        # print (allmovies)
        lang_list = each_movie['Language']
        for i in lang_list:
            if i == "Hindi":
                hindi += 1
            elif i == "English":
                english += 1
            elif i == "Malayalam":
                malayalam+=1
    lang_dic = {'Hindi': hindi, 'English': english, 'Malayalam': malayalam}
    return (lang_dic)
print (analyse_movies_language(top_ten_movie))
