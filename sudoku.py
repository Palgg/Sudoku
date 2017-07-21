#!usr/bin/env

# imports
from util import *
from  board import *

# globals
new_load_valid = ['new', 'load']
	
# entry
if __name__ == "__main__":
	
	# greet
	print_logo()
	
	# ask whether to start a  new game or not
	newg_or_loadg = parse_input('Start NEW board or LOAD saved board?\n', new_load_valid)
	print('\n')
	
	# if the player wants to start a new game
	if newg_or_loadg.lower() == 'new':
		# fluff display
		print('--------------------------------')
		print('Generating new board...')
		print('--------------------------------\n')
		# create the new board and display
		testboard = new_board()
		print_board(testboard)
	else:
		print('Locating saved boards...\n')
	
	
	
	
	
	