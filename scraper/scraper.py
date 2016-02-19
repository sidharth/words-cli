from bs4 import BeautifulSoup
import json

class Word:
	def __init__(self, word, meaning):
		self.word = word
		self.meaning = meaning

raw_html = open("webpage.html").read()

soup = BeautifulSoup(raw_html,"html.parser")
divs_set = soup.findAll("div",{"class":"text"})

dict_word_list = []


for div in divs_set:
	word = str(div.find("span",{"class":"qWord"}).contents[0])
	meaning = str(div.find("span",{"class":"qDef"}).contents[0])
	word_object = vars(Word(word,meaning))
	dict_word_list.append(word_object)

# print dict_word_list
with open('dictionary.json','w') as outfile:
	json.dump(dict_word_list,outfile)
