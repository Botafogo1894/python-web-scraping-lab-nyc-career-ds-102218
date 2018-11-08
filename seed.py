from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from venues import *
import requests
from bs4 import BeautifulSoup


Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

artist1 = Artist(name='Shakira')
venue1 = Venue(name="Ballroom")
event1 = Event(name ="First_Event", venue = venue1, artists = [artist1])

session.add_all([artist1, venue1, event1])
session.commit()
# r = requests.get('https://www.residentadvisor.net/events')
# c = r.content
# soup = BeautifulSoup(c, 'html.parser')
#
# deeper = soup.find_all(name = "h1", class_ = "event-title")
# clean = list(map(lambda item: item.text, deeper))
# parti = list(map(lambda item: item.partition(' at '), clean))
#
# list_of_venues = [item[2] for item in parti]
#
# # Make a function which returns the events this week given region and country (this will take two arguments)
# # return the event name, link, and list of artists
# # function returns list of ['event name', 'www.linkaddress.com', ['artist1','artist2','artist3']]
#
# def find_venues(country, region):
#     r = requests.get('https://www.residentadvisor.net/events' + '/' + country + '/' + region)
#     c = r.content
#     soup = BeautifulSoup(c, 'html.parser')
#     deeper = soup.find_all(name = "h1", class_ = "event-title")
#     clean = list(map(lambda item: item.text, deeper))
#     parti = list(map(lambda item: item.partition(' at '), clean))
#     list_of_venues = [item[2] for item in parti]
#     return list_of_venues
#
# def find_events(country, region):
#     r = requests.get('https://www.residentadvisor.net/events' + '/' + country + '/' + region)
#     c = r.content
#     soup = BeautifulSoup(c, 'html.parser')
#     deeper = soup.find_all(name = "h1", class_ = "event-title")
#     empty = []
#     for item in deeper:
#         url = 'https://www.residentadvisor.net/events' + item.find('a')['href']
#         details = item.find('a')['title'].partition(' of ')[2]
#         artists = item.find('a')['title'].partition(' of ')[2].split(' and ')
#         final = {'event': details, 'url': url, 'artists': artists}
#         empty.append(final)
#     return empty
