## In this task, I have scraped all the Casts for all the 250 movies, and then, stored the whole data in the **Casts** Folder according to their ID name followed by cast.json.


import requests, os, json, pprint
from os import path
from bs4 import BeautifulSoup
from Task1 import scrape_top_list

def funfirst():
    data1 = scrape_top_list()
    for i in data1:
        castLink = i['url'] + 'fullcredits#cast'
        casting(castLink)

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
            # print (linkdata)
            index = linkdata.index('name')
            newind = index+5
            string = ""
            for i in range(newind, len(linkdata)):
                if linkdata[i] == "/":
                    name_dic['imdb_id'] = string
                    break
                else:
                    string = string + linkdata[i]
            # print (string)
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
    new_url_link = os.path.join("/home/yogi/Documents/IMDB-Movie-Scraper/Casts", url_link)
    exists = path.exists(new_url_link)
    if exists:
        with open(new_url_link, "r+") as f:
            loading = json.load(f)
            return (loading)
    else:
        data = scrape_movie_cast(user)
        data_json = json.dumps(data, indent=4, sort_keys=True)
        with open(new_url_link, "w") as f:
            f.write(data_json)
        return data

# for Task12 only
# funfirst()
