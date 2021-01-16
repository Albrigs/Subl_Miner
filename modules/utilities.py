from collections import Counter


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

