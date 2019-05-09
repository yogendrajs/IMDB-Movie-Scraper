## In this task, I am counting which director has worked in how many languages for all the 250 movies and stored all the data in **language_count_of_directors.json** file

from Task5 import get_movie_list_details
from Task1 import scrape_top_list
movies_list = scrape_top_list()
top_ten_movie = movies_list[:250]
# print(top_ten_movie)
import json

def analyse_language_and_directors(how_many_movies):
    data = get_movie_list_details(how_many_movies)
    # print (data)
    # return data
    # mydic = {}
    # firstmydic = {}

    directorlist = []
    languagelist = []
    for i in range(len(data)):
        dic_data = data[i]
        dir_list = (dic_data["Director"])
        lang = dic_data["Language"]
        for i in dir_list:
            if i not in directorlist:
                directorlist.append(i) # list of total directors
        for i in lang:
            if i not in languagelist:
                languagelist.append(i) # list of total movies

    main_dic={}
    for dr in directorlist:
        langdic = {}
        for lg in languagelist:
            count = 0
            for i in data:
                drs = i["Director"]
                newlang = i["Language"]
                if dr in drs:
                    if lg in newlang:
                        count+=1
            if count > 0:
                langdic[lg] = count
        main_dic[dr]=langdic
    jsndata = json.dumps(main_dic, indent=4, sort_keys=True)
    with open("language_count_of_directors.json", "w") as f:
        f.write(jsndata)
# print (main_dic)

analyse_language_and_directors(top_ten_movie)
