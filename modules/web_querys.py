from bs4 import BeautifulSoup
from requests import get
from .utilities import int_installs, convert_spaces, is_github, download_link_github, unzip
from os.path import abspath
from os import getenv


__URL_BASE = 'https://packagecontrol.io/'
__URL_SEARCH = f'{__URL_BASE}search/'
__URL_PACKAGES = f'{__URL_BASE}packages/'
__PKGS_FOLDER = abspath(getenv('HOME')+"/.config/sublime-text-3/Packages/")
#TODO detect this thing



def __get_one_soup(url):
	"""
	Get one HTML content warped in a soup
	url: targeted URL
	"""
	html = get(url).text
	return BeautifulSoup(html, 'lxml')

def __get_soups(url):
	"""
	Return soups from paginated search result
	url: url of search
	"""
	soup = [__get_one_soup(url)]

	#Verify if search has a pagination
	pagination = soup[0].find('nav', attrs={'class': 'pagination'})
	if pagination:
		#Find all result pages
		pagination = pagination.find_all('a')
		pagination = len(pagination)+1
		soup = []

		for page in range(1, pagination):
			tmp = __get_one_soup(f"{url}?page={page}")
			soup.append(tmp)

	return soup

def __page_exists(url):
	"""
	Return if a page exists or not
	url: targeted url
	"""
	req = get(url)
	return req.status_code == 200

def get_first_pkg(search_term):
	"""
	Return the first pckg of a search
	search_term: self explain
	"""
	soup = __get_one_soup(f'{__URL_SEARCH}{search_term}')
	soup = soup.find("li", attrs={"class": "package"})
	name = soup.text.split('by')[0].strip()
	res = __URL_PACKAGES+convert_spaces(name)
	res = get_url_download(res)

	return name, res

def search_pkg(search_term):
	"""
	Initial search interface return a map
	search_term: self explained
	"""

	soups = [ e.find_all("li", attrs={"class": "package"}) for e in __get_soups(f'{__URL_SEARCH}{search_term}')]
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
				'url': __URL_PACKAGES+convert_spaces(name)

				})
	return res

def get_url_download(url):
	"""
	Return a github download page from a page
	url: targeted page
	"""
	page_soup = __get_one_soup(url)
	list_item = page_soup.find('li', attrs={'class':'homepage'})

	home_link = ''
	if list_item:
		home_link =	list_item.find('a')['href']

	issues_link = ''
	list_item = page_soup.find('li', attrs={'class':'issues'})
	if list_item:
		issues_link = list_item.find('a')['href']

	res = 0
	if is_github(home_link):
		res = download_link_github(home_link)
	if is_github(issues_link):
		res = download_link_github(
			issues_link.replace('/issues','')
			)

	if res:
		if not __page_exists(res):
			res = 0

	return res



def download_from_url(url, chunk_size=128):
	"""
	Download a file from a url
	"""
	req = get(url, stream=True)
	tmp_zip = __PKGS_FOLDER+'tmp.zip'
	with open( tmp_zip, 'wb') as file:
		for chunk in req.iter_content(chunk_size=chunk_size):
			file.write(chunk)
	unzip(tmp_zip, __PKGS_FOLDER)
