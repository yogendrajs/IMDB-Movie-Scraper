import requests
from bs4 import BeautifulSoup

def scrape_movie_details(user):
    a = requests.get(user)
    b = a.text
    soup = BeautifulSoup(b, "html.parser")
    # to print the main dictionary
    main_dic = {}
    # to print the movie name
    h1 = soup.find('h1').text

    # to print the movie name
    movie_name = ""
    for i in h1:
        if i == " ":
            break
        else:
            movie_name += i
    main_dic['Name'] = (movie_name)

    # to print the director name
    director = soup.find('div', class_ = 'credit_summary_item')
    find_all_a = director.find_all('a')
    dir_list = [dirname.text for dirname in find_all_a]
    main_dic['Director'] = dir_list

    country = soup.find('div', attrs = {'class':'article', 'id': 'titleDetails'})
    divs = country.find_all('div', class_ = "txt-block")
    for i in divs:
        if i.find('h4') in i:
            h4 = i.find('h4').text
            if h4 == 'Country:':
                country_name = i.find('a').text
                main_dic['Country'] = country_name # to print country name
            elif h4 == 'Language:':
                language = i.find_all('a') # to print language in which the film has been released
                total_lang = [b.text for b in language]
                main_dic["Language"] = total_lang
            elif h4 == 'Runtime:':
                runtime = i.find('time').text
                main_dic['Runtime'] = runtime
    # to find the runtime of the movie
    # runtime = soup.find('div', class_ = 'subtext')
    # time = runtime.find('time').text.strip()
    # min = ""
    # for i in range(len(time)):
    #     if time[i] == 'h':
    #         continue
    #     elif i == 0:
    #         hr = int(time[i])*60
    #     elif time[i].isdigit():
    #         min = min + str(time[i])
    # main_dic['Runtime'] = str(hr+int(min))+ ' minutes'

    # to print the link of the image
    poster = soup.find('div', class_= 'poster')
    poster_url = poster.find('a').img['src']
    main_dic['Poster URL'] = poster_url

    #to print the bio of the movie
    bio = soup.find('div', class_ = "summary_text").text.strip()
    main_dic['Bio'] = (bio)

    #to print the genre of the movie
    genre1 = soup.find('div', attrs = {'class':'article', 'id': 'titleStoryLine'})
    genre2 = genre1.find_all('div', class_ = 'see-more inline canwrap')
    for i in genre2:
        h4s = i.find('h4', class_ = 'inline').text
        # print (h4s)
        all_a = i.find_all('a')
        if h4s == 'Genres:':
            value = [k.text for k in all_a]
            main_dic['Genres'] = (value)

    return (main_dic)

#calling the input url
url = input("enter the url: ")
print (scrape_movie_details(url))
