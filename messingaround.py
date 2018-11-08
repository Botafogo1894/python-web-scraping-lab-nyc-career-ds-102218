import requests
from bs4 import BeautifulSoup

url = 'https://www.azlyrics.com/d/dualipa.html'
r = requests.get(url)
soup = BeautifulSoup(r, 'html.parser')
