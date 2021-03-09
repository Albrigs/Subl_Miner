from .web_querys import \
get_url_download,search_pkg, get_first_pkg, \
download_from_url
from .utilities import gen_subl_pkg_list, read_pkg_save, validate_file, validate_dir
from .ui import search_ui

from argparse import ArgumentParser
from pprint import pprint
from os.path import abspath, isfile

def main():
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
		if url:
			download_from_url(url)
			print("Finished")

	if args.i:
		name, res = get_first_pkg(args.i)
		print(f'{name} {res}')

	if args.r:
		f_path = validate_file(args.r)
		res = read_pkg_save(f_path)

		for pkg in res:
			name, url = get_first_pkg(pkg)
			if url:
				download_from_url(url)
				print(f"{name}: ok")
			else:
				print(f"{name}: repository not find")

	if args.g:
		d_path = validate_dir(args.g)
		if d_path:
			gen_subl_pkg_list(d_path)


if __name__ == '__main__':
	main()