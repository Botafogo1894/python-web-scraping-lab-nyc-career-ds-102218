import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.residentadvisor.net/events')
c = r.content
soup = BeautifulSoup(c, 'html.parser')

deeper = soup.find_all(name = "h1", class_ = "event-title")
clean = list(map(lambda item: item.text, deeper))
parti = list(map(lambda item: item.partition(' at '), clean))

list_of_venues = [item[2] for item in parti]


# Make a function which returns the events this week given region and country (this will take two arguments)
# return the event name, link, and list of artists
# function returns list of ['event name', 'www.linkaddress.com', ['artist1','artist2','artist3']]


def find_venues(country, region):
    r = requests.get('https://www.residentadvisor.net/events' + '/' + country + '/' + region)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    deeper = soup.find_all(name = "h1", class_ = "event-title")
    clean = list(map(lambda item: item.text, deeper))
    parti = list(map(lambda item: item.partition(' at '), clean))
    list_of_venues = [item[2] for item in parti]
    return list_of_venues

def find_events(country, region):
    r = requests.get('https://www.residentadvisor.net/events' + '/' + country + '/' + region)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    deeper = soup.find_all(name = "h1", class_ = "event-title")
    empty = []
    for item in deeper:
        url = 'https://www.residentadvisor.net/events' + item.find('a')['href']
        details = item.find('a')['title'].partition(' of ')[2]
        artists = item.find('a')['title'].partition(' of ')[2].split(' and ')
        final = {'event': details, 'url': url, 'artists': artists}
        empty.append(final)
    return empty



# <div class="grey event-lineup">Good Room presents, Love Games with, Lauren Murada and Finn Jones</div>


# <article class="event-item  clearfix " itemscope="" itemtype="http://data-vocabulary.org/Event"><span style="display:none;"><time itemprop="startDate" datetime="2018-11-07T00:00">2018-11-07T00:00</time></span><a href="/events/1171717"><img src="/images/events/flyer/2018/11/us-1107-1171717-list.jpg" width="152" height="76"></a><div class="bbox"><h1 class="event-title" itemprop="summary"><a href="/events/1171717" itemprop="url" title="Event details of Love Games with Lauren Murada and Finn Jones">Love Games with Lauren Murada and Finn Jones</a> <span>at <a href="/club.aspx?id=97606">Good Room</a></span></h1><div class="grey event-lineup">Good Room presents, Love Games with, Lauren Murada and Finn Jones</div><p class="attending"><span>8</span> Attending</p></div></article>
