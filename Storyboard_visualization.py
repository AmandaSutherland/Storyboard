#!/usr/bin/env python

#Software Design - Fall 2015
#This script will import a Project Gutenberg book and do ____
from pattern.web import*
# import nltk
# from nltk import*
import re
import pprint

def get_book():
# this function downloads the book
	#Peter_Pan_full_text = URL('http://www.gutenberg.org/cache/epub/16/pg16.txt').download()
	textfile = open("Peter_Pan_direct_text.txt")
	Peter_Pan_full_text = textfile.read()
	print'got book!'
	return Peter_Pan_full_text
	
def delete_introduction(Peter_Pan_full_text):
# this function deletes extranious text from Peter_Pan_full_text
	from gutenberg.cleanup import strip_headers
	text = strip_headers(Peter_Pan_full_text).strip()
	print'headers are gone'
	return Peter_Pan_full_text

def find_chapter(Peter_Pan_full_text):
#finds the chapter titles in the book 
	indices = [m.start() for m in re.finditer('Chapter', Peter_Pan_full_text)]
	for i in range(17):
		m = Peter_Pan_full_text[indices[i]:indices[i]+len("Chapter xxx")]
		print m 

#def chapter_split():
#divides the book by chapters so we know where we are
	
# def parts_of_speech(Peter_Pan_full_text):
# #tags all words (probably bad!) with their parts of speech 
# #comes from nltk
# 	full_text_parts_speech = word_tokenize(Peter_Pan_full_text)
# 	nltk.pos_tag(full_text_parts_speech)
# 	print'text tagged!'
# 	return full_text_parts_speech


#def find_common_nouns():
# finds the most common nouns in the book




Peter_Pan_full_text = get_book()  
delete_introduction(Peter_Pan_full_text)
# parts_of_speech(Peter_Pan_full_text)
find_chapter(Peter_Pan_full_text)
