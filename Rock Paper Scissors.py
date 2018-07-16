"""This program prompts the user to select Rock, Paper, or Scissors while the computer randomly selects Rock, Paper, or Scissors.
It then compares the user's choice to determine a winner.
~The Zymurgist~ October 2017"""

from random import randint
from time import sleep

OPTIONS = ["R", "P", "S"]
LOSS_MSG = "You lost!"
WIN_MSG = "You won!"
TIE_MSG = "It's a tie! Would you like to try again? "

#compares user choice and computer choice and determines a winner
def decide_winner(user_choice, computer_choice):
	
	#declare the user and computer choices
	print "User chooses %s" % user_choice
	print "Computer selecting..."
	sleep(1)
	print "Computer chooses %s" % computer_choice
	
	#find the index of the choices
	user_choice_index = OPTIONS.index(user_choice)
	computer_choice_index = OPTIONS.index(computer_choice)
	
	#compare the indices
	#tie scenario; option to start a new game
	if user_choice_index == computer_choice_index:
		print TIE_MSG
		try_again = raw_input("Y/N?").upper()
		if try_again == "Y":
			play_RPS()
		elif try_again == "N":
			print "No judgment here, but a tie is as good as a loss in my book... \n Exiting..."
		else:
			"Sorry, I don't understand, but I'll take that as a no. \nExiting..."
			return
			
	#win scenarios
	elif user_choice_index == 0 and computer_choice_index == 2:
		print WIN_MSG
	elif user_choice_index == 1 and computer_choice_index == 0:
		print WIN_MSG
	elif user_choice_index == 2 and computer_choice_index == 1:
		print WIN_MSG
		
	#check for garbage
	elif user_choice_index > 2:
		print "Not sure what you did here, but that's not going to work >_<."
		play_RPS()
	
	#loss scenarios (aka all other scenarios)
	else:
		print LOSS_MSG
		
def play_RPS():
	print "Welcome to Rock, Paper, Scissors!"
	
	#get user choice
	user_choice = "X"
	while user_choice not in OPTIONS:
		user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ").upper()
	sleep(1)
	
	#get computer choice
	computer_choice = OPTIONS[randint(0, len(OPTIONS) - 1)]
	
	#decide winner
	decide_winner(user_choice, computer_choice)
	
play_RPS()