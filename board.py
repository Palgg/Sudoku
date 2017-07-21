#!usr/bin/env

# imports

"""
	file responsible for generating a board
"""

# blank board template
board_template = [['--', '--', '--', '==', '--', '--', '--', '==', '--', '--', '--'],
				  ['--', '--', '--', '==', '--', '--', '--', '==', '--', '--', '--'],
				  ['--', '--', '--', '==', '--', '--', '--', '==', '--', '--', '--'],
				  ['==', '==', '==', '==', '==', '==', '==', '==', '==', '==', '=='],
				  ['--', '--', '--', '==', '--', '--', '--', '==', '--', '--', '--'],
				  ['--', '--', '--', '==', '--', '--', '--', '==', '--', '--', '--'],
				  ['--', '--', '--', '==', '--', '--', '--', '==', '--', '--', '--'],
				  ['==', '==', '==', '==', '==', '==', '==', '==', '==', '==', '=='],
				  ['--', '--', '--', '==', '--', '--', '--', '==', '--', '--', '--'],
				  ['--', '--', '--', '==', '--', '--', '--', '==', '--', '--', '--'],
				  ['--', '--', '--', '==', '--', '--', '--', '==', '--', '--', '--']]

# class for board object
class Board:
	# constructor, initialize with empty seed and board
	def __init__(self):
		self.seed =[['-', '-', '-'],
					['-', '-', '-'],
					['-', '-', '-']]
		self.board = board_template

# generate and return a new board
def gen_board():
	return Board()

# print a given board
def print_board(board):
	# for each row
	for row in board:
		# reset the print_str
		print_str = ""
		# for each col
		for col in row:
			print_str = print_str + col + " "
		print(print_str)