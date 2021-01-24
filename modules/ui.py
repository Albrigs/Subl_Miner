from PyInquirer import prompt
from math import ceil
from os import system as terminal


def __clear_console():
	terminal('clear')

def search_ui(result):
	if not result:
		print('Sem resultados')
		return

	result = sorted(result, key=lambda e: e['int_installs'], reverse=True)

	stringfyed_results = [ 
f"""-----------------------------------------------
||{e['name']}||
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
		__clear_console()
		response = prompt(questions[cur_page])['package']

		if "<<" in response: cur_page -= 1
		if ">>" in response: cur_page += 1

	response = response.split('||')[1]
	for e in result:
		if response in e['name']:
			response = get_url_download(e['url'])
			break

	return response