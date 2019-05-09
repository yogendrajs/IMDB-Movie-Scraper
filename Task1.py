## In this task, I have scraped the details of all the 250 movies, according to their position, name, year, rating, and movie url.
## To run this task, uncomment the `scrape_top_list()` function at the bottom.

import requests, pprint
from bs4 import BeautifulSoup
url = "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
page = requests.get(url)
text = page.text
parse = BeautifulSoup(text, "html.parser")

def scrape_top_list():
    lister = parse.find('div', class_ = "lister")
    # print (lister)
    tbody = lister.find('tbody', class_ = "lister-list")
    # print (tbody)
    trs = tbody.find_all('tr')
    # print (trs)
    ############# to find the position of movies:
    position = []
    movies_list = []
    years_of_release = []
    ratings_list = []
    movies_links = []

    for tr in trs:
        # print (tr)
        # print ("-------------------------------------------------------------------------------------------------------------------------------------")
        tds = tr.find('td', class_ = "titleColumn").get_text().strip()
        # print (tds)
        # print ("-------------------------------------------------------------------------------------------------------------------------------------")
        string = ""
        for i in tds:
            if i != ".":
                string = string+i
            else:
                position.append(int(string))
                break
    # print (position)

    all_in_one = []
    for tr in trs:
        main_link = tr.find('td', class_ = "titleColumn")

        # to print the name of every movie
        name = main_link.find('a').get_text()
        movies_list.append(name)

        # to print the year_of_release of every movie
        year = main_link.find('span').text
        years_of_release.append(year)

        # to print the link of every movie
        site_links = tr.find('td', class_ = "titleColumn").a['href']
        link_to_movie = "http://www.imdb.com" + (site_links)
        movies_links.append(link_to_movie)

        # to print the rating of every movie
        ratingtd = tr.find('td', class_ = "ratingColumn imdbRating")
        ratings = ratingtd.find('strong').text
        ratings_list.append(ratings)

    for i in range(len(movies_list)):
        b = {
        'position': position[i],
        'name': movies_list[i],
        'year': years_of_release[i],
        'rating': ratings_list[i],
        'url': movies_links[i],
        }
        all_in_one.append(b)
    mainlist = all_in_one
    return mainlist
    # print (movies_list)
    # print (years_of_release)
    # print (ratings_list)
    # print (movies_links)

# calling the function
# pprint.pprint(scrape_top_list())
