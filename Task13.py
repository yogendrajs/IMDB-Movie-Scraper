import requests
from bs4 import BeautifulSoup
from Task5 import scrape_movie_details
from Task12 import casting

def link_movie(user):
    task5=scrape_movie_details(user)
    task12=casting(user)
    task5["cast"]=task12
    return (task5)

# user = input("Enter a link: ")
# print (link_movie(user))
