#!/usr/bin/env python

#Software Design - Fall 2015
#This script will import a Project Gutenberg book and do ____
from pattern.web import*
from pattern.en import parse
import nltk
from nltk import tokenize
from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize
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
	# print Peter_Pan_full_text
	return Peter_Pan_full_text

def find_chapter(Peter_Pan_full_text):
#finds the chapter titles in the book 
	indices = [m.start() for m in re.finditer('Chapter', Peter_Pan_full_text)]
	for i in range(17):
		m = Peter_Pan_full_text[indices[i]:indices[i]+len("Chapter xx")] 
		# print m 

# def find_chapter_fullname(Peter_Pan_full_text):
# #finds the full chapter names
# 	indices = [m.start() for m in re.finditer('Chapter', Peter_Pan_full_text)]
# 	for i in range(17):
# 		#it would be good if this next line could do it based on the length of the line
# 		while True:
# 			n = Peter_Pan_full_text[indices[i]]
# 	    	if "\n" in n: 
# 		    	break
# 		print n
	
def chapter_split(Peter_Pan_full_text):
# divides the book by chapters so we know where we are
	for i in range(17):
		chapter[i] = Peter_Pan_full_text.split('Chapter')
	print'split into chapters!'
	print chapter[1]
	# return chapter[i]

	
def parts_of_speech(Peter_Pan_full_text):
#tags all words (probably bad!) with their parts of speech 
#comes from nltk
	full_text_parts_speech = word_tokenize(Peter_Pan_full_text)
	Peter_Pan_parsed_nltk = nltk.pos_tag(full_text_parts_speech)
	print'text tagged!'
	# print Peter_Pan_parsed_nltk
	return Peter_Pan_parsed_nltk

# def parts_of_speech(Peter_Pan_full_text):
# 	Peter_Pan_parsed = parse(Peter_Pan_full_text, relations=True, lemmata=True)
# 	print Peter_Pan_parsed
# 	return Peter_Pan_parsed

def find_common_nouns(parsed_text):
# finds the 5 most common nouns in the book and gives them in order of frequency
#most common of three types: NNS, NN, NNP

	cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in parsed_text
	                                  if tag.startswith('NN'))
	common_nouns = dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())
	
	print common_nouns
	print 'found common nouns'
	return common_nouns

Peter_Pan_full_text = get_book()
delete_introduction(Peter_Pan_full_text)
POS = parts_of_speech(Peter_Pan_full_text)
find_chapter(Peter_Pan_full_text)
# find_chapter_fullname(Peter_Pan_full_text)
chapter_split(Peter_Pan_full_text)
find_common_nouns(POS)