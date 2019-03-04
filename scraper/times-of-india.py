"""
This module scrapes content from Times of India.

It provides:
- get_chronological_headlines(url)

# TODO
- get_trending_headlines(url)
"""

import datetime
import requests
from bs4 import BeautifulSoup
from sys import path
import os
path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from sources import KNOWN_NEWS_SOURCES
# from newscrape_common import   \
#     str_is_set, is_string, remove_duplicate_entries


def get_chronological_headlines(url):
	response = requests.get(url)
	if response.status_code == 200:
	    soup = BeautifulSoup(response.text, "html.parser")
	    soup.find("div",id="c_articlelist_widgets_1").decompose()

	    data = []
	    objs = soup.find("div",{"class":"main-content"}).find_all("span", {"class":"w_tle"})

	    for obj in objs:
	    	dt = obj.find_next("span").find("span").get("rodate")
	    	clean_dt = datetime.strptime(dt,"%d %b %Y, %H:%M")

	    	data.append({
	    		"link": "https://timesofindia.indiatimes.com"+obj.find("a").get("href"),
	    		"content": "NA",
	    		"timestamp": clean_dt,
	    		"title": obj.find("a").get("title")
	    	})

	    return data

def get_trending_headlines(url):
	pass
	#TODO

if __name__ == "__main__":
    import json

    SRC = KNOWN_NEWS_SOURCES["Times of India"]

    print(json.dumps(
        get_chronological_headlines(SRC["pages"].format(2)),
        sort_keys=True,
        indent=4
    ))

    print(json.dumps(
        get_trending_headlines(SRC["home"]),
        sort_keys=True,
        indent=4
    ))
