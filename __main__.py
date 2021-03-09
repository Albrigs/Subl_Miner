from modules import *
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('search', help='Search package')
args = parser.parse_args()
print(args)