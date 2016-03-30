#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
import requests
from bs4 import BeautifulSoup

def getJokes():
	page = requests.get("http://www.qiushibaike.com")
	page = page.content
	soup = BeautifulSoup(page)
	jokes = []
	contents = soup.find_all("div", attrs = {"class":"article block untagged mb15"})
	for item in contents:
		if len(item.find_all("div", attrs = {"class":"thumb"}))!=0:
			continue
		else:
			jokes += [i.text.encode('utf-8') for i in item.find_all("div", attrs = {"class":"content"})]
	items = {"jokes":jokes} 
	json_string = json.dumps(items, ensure_ascii=False)
	headers = {'Content-type': 'application/json'}
	r = requests.post("http://httpbin.org/post", data=json_string, headers = headers)
	print r.text.encode("utf-8")

if __name__=="__main__":
	getJokes()
