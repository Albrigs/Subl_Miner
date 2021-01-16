from bs4 import BeautifulSoup
import requests
from pprint import pprint
from collections import Counter
import re

def convert_spaces(string): return string.replace(' ', '%20')

URL_BASE = 'https://packagecontrol.io/'
URL_SEARCH = f'{URL_BASE}search/'
URL_PACKAGES = f'{URL_BASE}packages/'

def get_one_soup(url):
	html = requests.get(url).text
	return BeautifulSoup(html, 'lxml')

def get_soups(url):
	soup = [get_one_soup(url)]

	pagination = soup[0].find('nav', attrs={'class': 'pagination'})
	if pagination:
		
		pagination = pagination.find_all('a')
		pagination = len(pagination)+1
		soup = []

		for page in range(1, pagination):
			tmp = get_one_soup(f"{url}?page={page}")
			soup.append(tmp)

	return soup

def int_installs(txt):
	txt = txt.lower()
	k = Counter(txt)['k']
	quantity = int(re.sub('[^0-9]','', txt))
	quantity = quantity * pow(1000, k)
	return quantity


def get_packages_info(search_term):

	soups = [ e.find_all("li", attrs={"class": "package"}) for e in get_soups(f'{URL_SEARCH}{search_term}')]
	res = []
	for soup in soups: 
		for s in soup:
			installs = s.find('span', attrs = {'class':"installs"}).text.split()[0]
			name = s.text.split('by')[0].strip()
			res.append({
				'name': name,
				'author': s.find('span', attrs = {'class':"author"}).text.replace('by ', ''),
				'installs': installs,
				'int_installs': int_installs(installs),
				'description': s.find('div', attrs={'class':'description'}).text,
				'url': URL_PACKAGES+convert_spaces(name)

				})
	pprint(res)
	return res

get_packages_info('python')