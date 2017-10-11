from bs4 import BeautifulSoup
import requests, re

def get_urls(search_string):
    temp        = []
    url         = 'http://www.google.com/search'
    payload     = { 'q' : search_string }
    my_headers  = { 'User-agent' : 'Mozilla/11.0' }
    r           = requests.get( url, params = payload, headers = my_headers )
    soup        = BeautifulSoup( r.text, 'html.parser' )
    h3tags      = soup.find_all( 'h3', class_='r' )
    for h3 in h3tags:
        try:
            temp.append( re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1) )
        except Exception:
            return "Something went wrong with your search query."
    temp = temp[:3]
    return ', '.join(temp)
