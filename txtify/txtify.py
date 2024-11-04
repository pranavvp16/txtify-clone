
allow_tags = [
            'p', 'br',
            'code', 'pre', 'h1',
            'h2', 'h3', 'h4', 'h5', 'h6',
]


class Txtify:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.content = None

    def download_content(self):
        import requests

        response = requests.get(self.url)
        response.raise_for_status()
        self.content = response.content

    def parse_html(self, content):
        from bs4 import BeautifulSoup

        self.soup = BeautifulSoup(content, "lxml")

    def extract_content(self, soup):
        main_content = self.soup.find("article")
        if main_content is None:
            main_content = soup.find("div", class_="content")  # Adjust class as needed
        if main_content is None:
            main_content = soup.find("main")
        if main_content is None:
            main_content = soup.body

        if main_content:

            for br in main_content.find_all("br"):
                br.replace_with("\n")

            content = main_content.find_all(allow_tags)
            text_content = "\n".join([i.get_text() for i in content])
            self.content = text_content
        else:
            self.content = "Invalid URL"

        return self.content

    def run(self):
        self.download_content()
        self.parse_html(self.content)

        return self.extract_content(self.soup)


