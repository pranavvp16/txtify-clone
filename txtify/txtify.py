from newspaper import Article, languages

allow_tags = [
            'p', 'br', 'a',
            'em', 'i', 'tt', 'code', 'pre', 'blockquote', 'h1',
            'h2', 'h3', 'h4', 'h5', 'h6',
            'ul', 'ol', 'li', 'dl', 'dt', 'dd'
]


class Txtify(Article):
    def __init__(self, url):

        super().__init__(url, language='en')
        self.url = url
        self.soup = None
        self.content = None


    def download_content(self):
        self.download()
        print(self.html)


    def parse_html(self):
        self.parse()

    def extract_content(self):
        import regex as re
        title = self.title
        content = title + "\n" + self.text

        # regex to display text in same format as txtify
        self.content = "\n".join(re.findall(r'.{1,70}(?:\s+|$)', content))

        return self.content

    def run(self):
        self.download_content()
        self.parse_html()

        return self.extract_content()


