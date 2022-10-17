import json
import time
import requests
from models import News
from utils import parse_bbc_source

url = requests.get("https://www.bbc.com/russian/mostread.json")
text = url.text
data = json.loads(text)
news = []
bbc = "https://www.bbc.com"
for record in data["records"]:
    promo = record["promo"]
    source = promo["locators"]["assetUri"]
    content = parse_bbc_source(bbc + source)
    name = promo["headlines"]["shortHeadline"]
    #print(name)
    timestamp = promo["timestamp"]
    story = News(source, name, content, timestamp)
    news.append(story)
    time.sleep(6)
print(news)



# TODO: нужно полученые объекты добавиьть в список и вывести его.
# Создать класс News, прописать параметры и использовать класс для создания объектов.
# Из Json  выбрать необходимые параметры


# анализ текста pymorphy, pymystem
