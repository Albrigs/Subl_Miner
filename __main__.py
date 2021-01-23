from modules import *
from pprint import pprint
from PyInquirer import prompt
from math import ceil


result = search_pkg('python')

def print_search_results(result):
	if not result:
		print('Sem resultados')
		return

	result = sorted(result, key=lambda e: e['int_installs'], reverse=True)

	stringfyed_results = [ 
f"""||{e['name']}||
By {e['author']} | Downloads: {e['installs']}
{e['description'][:100]}
-----------------------------------------------""" for e in result
]

	##ADD PAGINATION
	sliced_results = []
	slices_needed = ceil(len(stringfyed_results)/10)
	slice_start = 0
	slice_end = 5

	for i in range(slices_needed):

		#ADD NEXT and previous
		tmp = stringfyed_results[slice_start:slice_end]
		if i != 0: tmp.insert(0, "<< Previous Page")
		
		
		if slice_end < len(stringfyed_results): tmp.append("Next Page >>")
		sliced_results.append(tmp)
		
		slice_start = slice_start + 5
		slice_end = slice_end + 5

	del stringfyed_results


	questions = [
	[{
	'type': 'list',
    'name': 'package',
    'message': f'Select a package. [{i+1}/{len(sliced_results)}]',
    'choices': e
	}] for i, e in enumerate(sliced_results)
	]

	cur_page = 0
	response = ""
	
	while "<<" in response or ">>" in response or not response:
		response = prompt(questions[cur_page])

		if "<<" in response: cur_page -= 1
		if ">>" in response: cur_page += 1


print_search_results(result)

"""
	SublimePythonIDE
	Color​Hints
	File​Icons
	Terminal​View
	SublimeColorSchemeSelector
	SideBarEnhancements
	Sublime-AdvancedNewFile
	Normalize Indentation
"""