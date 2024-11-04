from .newspaper import Article
import re

class Txtify(Article):
    def __init__(self, url):

        super().__init__(url, language='en')
        self.url = url
        self.soup = None
        self.content = None


    def download_content(self):
        self.download()


    def parse_html(self):
        self.parse()

    def extract_content(self):
        title = self.title
        content = title + "\n" + self.text

        # regex to display text in same format as txtify
        self.content = "\n".join(re.findall(r'.{1,70}(?:\s+|$)', content))

        return self.content

    def run(self):
        self.download_content()
        self.parse_html()
        return self.extract_content()


