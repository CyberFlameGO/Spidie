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


def create_files(proj_name, base_url):
    queue = os.path.join(proj_name, 'queue.txt')
    crawled = os.path.join(proj_name, 'crawled.txt')

    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, base_url)


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


def append_file(path, data):
    with open(path, 'a') as file:
        file.write(data)


def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def convert_file_to_set(file_name):
    results = set()

    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file_name):
    with open(file_name, 'w') as file:
        for i in sorted(links):
            file.write(i + '\n')


class Spidie:
    name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, name, base_url, domain_name):
        Spidie.name = name
        Spidie.base_url = base_url
        Spidie.domain_name = domain_name
        Spidie.queue_file = Spidie.name + '/queue.txt'
        Spidie.crawled_file = Spidie.crawled_file + '/crawled.txt'
        # todo load
        # todo crawl


@staticmethod
def load():
    create_directory(Spidie.name)
    create_files(Spidie.name, Spidie.base_url)
    set_to_file(Spidie.queue_file)
    set_to_file(Spidie.crawled_file)