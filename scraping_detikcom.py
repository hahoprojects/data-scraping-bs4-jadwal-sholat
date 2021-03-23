import requests
from bs4 import BeautifulSoup

url = 'https://news.detik.com/'

html_docs = requests.get(url, params='tag_from=wp_firstnav_detikNews')
soup = BeautifulSoup(html_docs.text, 'html.parser')

berita_utama = soup.find(attrs={'class': 'berita-utama'}).find_all(attrs={'class': 'media__link'})

print(berita_utama)
