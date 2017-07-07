# www.timeanddate.com/weather/india/
import urllib.request
from bs4 import BeautifulSoup


def weather(city):
    theurl = "https://www.timeanddate.com/weather/india/" + city
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")
    content = soup.findAll('div', {"class": "three columns"})[0]
    temp = content.find('div', {'class': 'h2'}).text
    cond = str(content.findAll('p')[0].text)
    degree = temp.split(" ")[0].encode('ascii', 'ignore').decode()
    print(cond)
    print(degree)
    return degree.encode() + " - ".encode() + cond.encode()


place = input("Enter city")
print(weather(place))
