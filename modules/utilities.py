from collections import Counter
from zipfile import ZipFile

def int_installs(txt):
	txt = txt.lower()
	k = Counter(txt)['k']
	quantity = int(re.sub('[^0-9]','', txt))
	quantity = quantity * pow(1000, k)
	return quantity

def convert_spaces(string): return string.replace(' ', '%20')
def is_github(url): return url.startswith('https://github.com/')

def download_link_github(url):
	link = f'{url}/archive/master.zip'
	return link

def unzip(path_in, path_out):
	with ZipFile(path_in, 'r') as file:
	    file.extractall(path_out)