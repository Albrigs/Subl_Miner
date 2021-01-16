from collections import Counter
from zipfile import ZipFile
from os import remove as delete_file
from os import rename, listdir
from re import sub as subst

def int_installs(txt):
	txt = txt.lower()
	k = Counter(txt)['k']
	quantity = int(subst('[^0-9]','', txt))
	quantity = quantity * pow(1000, k)
	return quantity

def convert_spaces(string): return string.replace(' ', '%20')
def is_github(url): return url.startswith('https://github.com/')

def download_link_github(url):
	link = f'{url}/archive/master.zip'
	return link

def unzip(path_in, path_out):
	old_content=set(listdir())
	
	with ZipFile(path_in, 'r') as file:
	    file.extractall(path_out)
	delete_file(path_in)
	
	new_content=set(listdir())

	new_folder = list(new_content - old_content)[0]

	rename(new_folder, new_folder.replace('-master',''))