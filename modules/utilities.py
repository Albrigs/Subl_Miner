from collections import Counter
from zipfile import ZipFile
from os import remove as delete_file
from os import rename, listdir
from re import sub as subst
from time import sleep
from json import load as load_json
from os.path import expanduser, isfile, abspath, isdir


config_file = expanduser('~') + '/.config/sublime-text-3/Packages/User/Package Control.sublime-settings'
save_file = expanduser('~') + '/subl_pkgs.txt'

def int_installs(txt):
	"""
	Reduce quantity of zeros
	"""
	txt = txt.lower()
	k = Counter(txt)['k']
	quantity = int(subst('[^0-9]','', txt))
	quantity = quantity * pow(1000, k)
	return quantity

def convert_spaces(string):
	"""
	"""
	return string.replace(' ', '%20')

def is_github(url):
	"""
	"""
	return url.startswith('https://github.com/')

def download_link_github(url):
	"""
	Convert a github link into a download from root of master
	"""
	link = f'{url}/archive/master.zip'
	return link

def unzip(path_in, path_out):
	"""
	"""
	old_content=set(listdir(path_out))

	with ZipFile(path_in, 'r') as file:
	    file.extractall(path_out)
	delete_file(path_in)

	new_content=set(listdir(path_out))

	new_folder = list(new_content - old_content)
	new_folder = new_folder[0]
	new_folder = path_out+'/'+new_folder


	rename(new_folder, new_folder.replace('-master',''))


def gen_subl_pckg_list(d_path):
	"""
	"""
	if d_path[-1] != '/':
		d_path = d_path+'/'

	d_path = d_path + 'subl_pkgs.txt'
	installed_packages = []
	with open(config_file, 'r') as file:
		installed_packages = load_json(file)['installed_packages']
		installed_packages.remove('Package Control')
		file.close()

	installed_packages = '\n'.join(installed_packages)


	with open(d_path, 'w') as file:
		file.write(installed_packages)
		file.close()

def read_pckg_save(f_path):
	"""
	"""
	pkgs = []
	if isfile(f_path):
		with open(f_path, 'r') as file:
			pkgs = file.readlines()
			pkgs = [e.replace('\n', '') for e in pkgs]
			file.close()
		return pkgs
	else:
		return f'There is no file subl_pkgs.txt'

def validate_file(f_path):
	f_path = abspath(f_path)
	if isfile(f_path):
		return f_path
	else:
		return 0

def validate_dir(d_path):
	d_path = abspath(d_path)
	if isdir(d_path):
		return d_path
	else:
		return 0