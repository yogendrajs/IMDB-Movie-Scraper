import requests
import os
import json
from os import path
from bs4 import BeautifulSoup

def scrape_movie_cast(url):
    link = requests.get(url)
    text = link.text
    parse = BeautifulSoup(text, "html.parser")
    maindiv = parse.find('div', attrs = {'class':'header', 'id': 'fullcredits_content'})
    table = maindiv.find('table', class_ = "cast_list")
    tbody = table.find_all('tr')

    final_list = []
    for tr in tbody:
        name_dic = {}
        tds = tr.find_all('td', class_ = None)
        for anchor in tds:
            linkdata = anchor.a['href']
            index = linkdata.index('name')
            newind = index+5
            string = ""
            for i in range(newind, len(linkdata)):
                if linkdata[i] == "/":
                    name_dic['imdb_id'] = string
                    break
                else:
                    string = string + linkdata[i]
            name = anchor.text.strip()
            name_dic['name'] = name
        if name_dic != {}:
            final_list.append(name_dic)
    return (final_list)

def casting(user):
    main_index = user.index('title')
    newmainindex = main_index + 6
    start = newmainindex
    strout = ""
    for i in range(start, len(user)):
        if user[i] == "/":
            break
        else:
            strout+=user[i]
    url_link = strout + "_cast.json"
    new_url_link = os.path.join("/home/yogendra/Desktop/Scraping/Casts", url_link)
    exists = path.exists(new_url_link)
    if exists:
        with open(new_url_link, "r+") as f:
            loading = json.load(f)
            return (loading)
    else:
        data = scrape_movie_cast(user)
        data_json = json.dumps(data)
        with open(new_url_link, "w") as f:
            f.write(data_json)
        return data

# for Task12 only
# user = input("Enter your cast url: ")
# print (casting(user))
