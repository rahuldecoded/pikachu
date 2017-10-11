# https://icanhazdadjoke.com/api
import urllib.request

def joke():
    the_url = "https://icanhazdadjoke.com"
    the_page = urllib.request.urlopen(the_url).read()
    return the_page
