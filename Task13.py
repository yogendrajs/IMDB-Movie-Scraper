## In this file, I have stored the whole data like languages, directors, runtime etc. alongwith casts data in the **Total_movie_list_with_casts.json** file for all the 250 movies. 

import requests, pprint, json
from bs4 import BeautifulSoup
from Task1 import scrape_top_list
from Task5 import scrape_movie_details
from Task12 import casting

total_data_list = []
def first():
    data = scrape_top_list()
    for i in data:
        movie_url = i['url']
        cast_link = movie_url + 'fullcredits#cast'
        linked_Data = link_movie(movie_url, cast_link)
        total_data_list.append(linked_Data)
    js = json.dumps(total_data_list, indent=4, sort_keys=True)
    with open("Total_movie_list_with_casts.json", "w") as q: # Total movies List of 250 movies
        q.write(js)

def link_movie(movie_link, cast_link):
    cast_dic = casting(cast_link)
    task5 = scrape_movie_details(movie_link)
    task5['casts'] = cast_dic
    return task5
    # pprint.pprint (task5)
    # print('\n\n')

first()
