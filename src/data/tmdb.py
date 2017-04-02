# -*- coding: utf-8 -*-
import os
import requests 
from ConfigParser import ConfigParser

def get_base_url():
    return "https://api.themoviedb.org/3/"

def get_api_key():
    config = ConfigParser()
    if 'notebooks' in os.getcwd():
        config.read('../config/keys.ini')
    else:
        config.read('../../config/keys.ini')

    return config.get('TMDb', 'key')

def ping_api(url):
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
    else:
        data = "Nada."

    return data    

def get_genres():
    url_add = "genre/movie/list"
    url = "{}{}?api_key={}".format(get_base_url(), url_add,
        get_api_key())

    return ping_api(url)

def find_movie_by_name(query_string):
    url_add = "search/movie"
    url = "{}{}?api_key={}&query={}".format(get_base_url(), url_add,
            get_api_key(), query_string)
    
    return ping_api(url)

def get_popular(page = 1):
    url_add = "movie/popular"
    url = "{}{}?api_key={}&page={}".format(get_base_url(), url_add, get_api_key(), page)
    return ping_api(url)


def main():
    test = find_movie_by_name('Allonsanfan')
    print(test)

if __name__ == '__main__':
    main()
