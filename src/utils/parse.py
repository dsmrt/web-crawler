import re

from bs4 import BeautifulSoup


def parse_html(html_text: str):
    soup = BeautifulSoup(html_text, 'html.parser')
    attrs = {
        # fetch absolute urls only
        # also, we probably only want to follow html files?
        'href': re.compile(r'^http(s)?://')
    }

    # Use BeautifulSoup to find all of the anchor tags
    return soup.find_all('a', attrs=attrs,)
