import requests


def get_html_status(url):
    response = requests.get(url)

    if response.status_code != 200:
        html = None

    html =

