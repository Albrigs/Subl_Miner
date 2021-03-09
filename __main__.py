from modules import *
from argparse import ArgumentParser
from pprint import pprint
from os.path import abspath, isfile

parser = ArgumentParser()

parser.add_argument('-s', help='Search package.')
parser.add_argument('-i', help='Install first package of a search.')
parser.add_argument(
	'-r',
	help='Read package config file and install listed files.',
	)
parser.add_argument(
	'-g',
	help='Generate a file with a list of all installed packages.',
	)

args = parser.parse_args()

if args.s:
	res = search_pkg(args.s)
	url = search_ui(res)
	print(url)

if args.i:
	name, res = get_first_pkg(args.i)
	print(f'{name} {res}')

if args.r:
	f_path = validate_file(args.r)
	res = read_pckg_save(f_path)

	res = tuple([get_first_pkg(e) for e in res])
	for name, url in res:
		if url:
			download_from_url(url)
		else:
			print(name)

if args.g:
	d_path = validate_dir(args.g)
	if d_path:
		gen_subl_pckg_list(d_path)