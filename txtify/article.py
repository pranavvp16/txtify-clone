import requests
from bs4 import BeautifulSoup

class Article:
    def __init__(self, url):
        self.url = url
        self.html = None
        self.content = None
        self.title = None
        self._is_downloaded = False


    def download(self, input_html=None):

        if input_html:
            self.html = input_html
        else:
            response = requests.get(self.url)
            response.raise_for_status()
            self.html = response.content
        self._is_downloaded = True

    def parse(self):
        if not self._is_downloaded:
            self.download()

        soup = BeautifulSoup(self.html, "lxml")




