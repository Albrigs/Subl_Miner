from modules import *
from argparse import ArgumentParser
from pprint import pprint

parser = ArgumentParser()

parser.add_argument('-s', help='Search package')
args = parser.parse_args()

if args.s:
	results = search_pkg(args.s)
	pprint(results)