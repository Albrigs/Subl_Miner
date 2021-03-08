from collections import Counter
from zipfile import ZipFile
from os import remove as delete_file
from os import rename, listdir
from re import sub as subst
from time import sleep
from json import load as load_json
from os.path import expanduser, isfile


config_file = expanduser('~') + '/.config/sublime-text-3/Packages/User/Package Control.sublime-settings'
save_file = expanduser('~')+'/subl_pkgs.txt'

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
	old_content=set(listdir(path_out))

	with ZipFile(path_in, 'r') as file:
	    file.extractall(path_out)
	delete_file(path_in)

	new_content=set(listdir(path_out))

	new_folder = list(new_content - old_content)
	new_folder = new_folder[0]
	new_folder = path_out+'/'+new_folder


	rename(new_folder, new_folder.replace('-master',''))


def gen_subl_pckg_list():

	installed_packages = []
	with open(config_file, 'r') as file:
		installed_packages = load_json(file)['installed_packages']
		file.close()

	installed_packages = '\n'.join(installed_packages)


	with open(save_file, 'w') as file:
		file.write(installed_packages)
		file.close()

def read_pckg_save():
	pkgs = []
	if isfile(save_file):
		with open(save_file, 'r') as file:
			pkgs = file.readlines()
			pkgs = [e.replace('\n', '') for e in pkgs]
			file.close()
		return pkgs
	else:
		return f'There is no {save_file}'