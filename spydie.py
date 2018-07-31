from bs4 import BeautifulSoup
import urllib3
import json
import sys
import re

http = urllib3.PoolManager()


def json_update(title, description, keywords, url):
    if title == "":
        title = description
        if description == "":
            title = keywords
    jsonData = {"Title": title, "Description": description, "Keywords": keywords, "URL": url}

    with open("data.json", "r") as file:
        data = json.load(file)
        file.close()
    strData = str(data)

    if not strData.find(str(jsonData)) >= 0:
        data.append(jsonData)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4, separators=(',', ':'))
            file.close()
# TODO CRAWL