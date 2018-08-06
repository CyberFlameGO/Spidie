from urllib.parse import urlparse
from urllib import parse
from html.parser import HTMLParser
import os


def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


class LinkFinder(HTMLParser):

    def __init__(self, baseURL, pageURL):
        super().__init__()
        self.baseURL = baseURL
        self.pageURL = pageURL
        self.links = set()

        def handle_star_tag(self, tag, attr):
            if tag == 'a':
                for attribute, value in attr:
                    if attribute == 'href':
                        url = parse.urljoin(self.baseURL, value)
                        self.links.add(url)

        def page_links(self):
            return self.links


def create_directory(dir):
    if not os.path.exists(dir):
        print('[+] Creating new directory ' + dir)
        os.makedirs(dir)
