import requests
from bs4 import BeautifulSoup

class Crawler():

    def __init__(self, url):
        self.url = url
        self.soup = None

    def getHtml(self):
        response = requests.get(self.url)
        
        if response.status_code == 200:
            html = response.text
            self.soup = BeautifulSoup(html, 'html.parser')
            return self.soup