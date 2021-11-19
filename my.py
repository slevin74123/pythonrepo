import cloudscraper
from requests import get
from bs4 import BeautifulSoup as bs
scraper = cloudscraper.create_scraper() 
 
html = scraper.get("https://lotopolonia.eu")
soup = bs(html.text)