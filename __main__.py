from modules import *
from os import listdir
from os.path import expanduser

def generate_package_save():
	pkgs = listdir(PKGS_FOLDER)
	pkgs.remove('User')
	pkgs = '\n'.join(pkgs)

	file_path = expanduser("~")+'/sublime_pkgs.txt'


	file = open(file_path, 'w')
	file.write(pkgs)
	file.close()

	print(f'Your save file is in {file_path}')

def read_package_save(target=0):

	target = expanduser("~")+'/sublime_pkgs.txt'

	file = open(target)
	content = file.read().split('\n')
	file.close()

	return content

read_package_save()