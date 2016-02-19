import json
import random
import click

def selectRandomWord():
	with open('dictionary.json') as data_file:
		data = json.load(data_file)

	random_index = random.randrange(0,len(data))	
	# print data[random_index]['word']
	# print data[random_index]['meaning']

	return data[random_index]

def main():
	word = selectRandomWord()
	click.echo('~~~~~~~~~~~~~~~~~~~')
	click.secho('word: %s' % word['word'], fg='blue')
	click.secho('\ndef: %s' % word['meaning'], fg='red')
	click.echo('~~~~~~~~~~~~~~~~~~~')



if __name__ == '__main__':
	main()