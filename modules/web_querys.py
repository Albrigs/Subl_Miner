from bs4 import BeautifulSoup
from requests import get
import re
from .utilities import int_installs, convert_spaces, is_github, download_link_github


URL_BASE = 'https://packagecontrol.io/'
URL_SEARCH = f'{URL_BASE}search/'
URL_PACKAGES = f'{URL_BASE}packages/'


def get_one_soup(url):
	html = get(url).text
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
	return res

def get_home_page(url):
	list_item = get_one_soup(url).find('li', attrs={'class':'homepage'})
	link = list_item.find('a')['href']
	return link

def page_exists(url):
	req = get(url)
	return req.status_code == 200
