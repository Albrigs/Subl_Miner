from modules import *
from argparse import ArgumentParser
from pprint import pprint

parser = ArgumentParser()

parser.add_argument('-s', help='Search package.')
parser.add_argument('-i', help='Install first package of a search.')
parser.add_argument(
	'-r',
	help='Read package config file and install listed files.',
	action="store_true"
	)
parser.add_argument(
	'-g',
	help='Generate a file with a list of all installed packages.',
	action="store_true"
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
	res = read_pckg_save()
	print(res)

if args.g:
	gen_subl_pckg_list()