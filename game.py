# Python Text RPG
# Harshad Sontakke

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

####### PLayer Setup ########
class player:
	def __init__(self):
		self.name = ''
		self.hp = 0
		self.mp = 0
		self.location = 'start'
		self.status_effects = []

myPlayer = player()

####### Title Screen ########
def title_screen_selections():
	option = input('> ')
	if option.lower() == ('play'):
		start_game() #placeholder for now
	elif option.lower() == ('help'):
		help_menu()
	elif option.lower() == ('quit'):
		sys.exit()
	while option.lower() not in ['play', 'help', 'quit']:
		print("Please enter a valid command.")
		option = input('> ')
		if option.lower() == ('play'):
			start_game() #placeholder for now
		elif option.lower() == ('help'):
			help_menu()
		elif option.lower() == ('quit'):
			sys.exit()

def title_screen():
	os.system('clear')
	print('###########################')
	print('# Welcome to the Text RPG #')
	print('###########################')
	print('        -Play-             ')
	print('        -Help-             ')
	print('        -Quit-             ')
	print('     Copyright 2025        ')
	title_screen_selections()

def help_menu():
	print('#####################################')
	print('#       Welcome to the Text RPG     #')
	print('#####################################')
	print('- Use up, down, right, left to move -')
	print('-      Type Commands to do them     -')
	print('-   Use look to inspect something   -')
	print('-       Good Luck and have fun      -')
	title_screen_selections()