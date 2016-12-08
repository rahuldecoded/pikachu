# www.timeanddate.com/weather/india/
import urllib2
from bs4 import BeautifulSoup


def weather(city):
    theurl = "https://www.timeanddate.com/weather/india/" + city
    thepage = urllib2.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")
    content = soup.findAll('div', {"class": "three columns"})[0]
    temp = content.find('div', {'class': 'h2'}).text
    cond = content.findAll('p')[0].text
    return temp.split(" ")[0].encode('ascii', 'ignore') + " - " + cond
