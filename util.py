#!usr/bin/env

# imports

"""
util functions to be utilized by the main game
"""

# greet the user and print logo
def print_logo():
	# get the logo file and print
	with open('logo.txt') as logo:
		# make a list of files lines
		logo_lines = logo.readlines()
	# for each line
	for line in logo_lines:
		# strip the white space at the end of each line and print
		print(line.rstrip())
	print('------------------------------------')
	
# parse input, returns True if fine and False if not
def parse_input(prompt, valid):
	while 1:
		inp = input(prompt + '\n')
		if inp.lower() in valid:
			return inp