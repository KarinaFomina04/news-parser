import re

import requests
from bs4 import BeautifulSoup


def parse_bbc_source(source):
    response = requests.get(source)
    soup = BeautifulSoup(response.text, "lxml")
    main = soup.find("main")
    info = ""
    for child in main.children:
        info = info + analyze_div(child)
    return info


def is_contain_any_tag(child, tags) -> bool:
    for tag in tags:
        if child.find(tag):
            return True
    return False


def analyze_div(child) -> str:
    if is_contain_any_tag(child, ["h1", "time", "section", "ul"]):
        return ""
    image = child.find("img")
    if image:
        return " " + image["src"] + " "
    if child.find("p"):
        return child.text
    tag = child.find('div', {'data-e2e': re.compile('twitter-embed')})
    if tag:
        return " " + tag["data-e2e"].replace("twitter-embed", "") + " "
    return ""
# TODO read pattern matching
# if div child = figure then find by tag img, and get src
# if div child = p then div.innerText
# if in div element div with attribute data-e2e starts with twitter-embed exists then return twitter url
# #els = soup.find_all(id=re.compile("\w"))
# if div child = figure then find by tag img, and get src
# if div child = h1 then ""
# if div child = time then ""
# if div child = section then ""
# if div child = ul then ""
