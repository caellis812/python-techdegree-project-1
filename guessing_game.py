"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def input_guess():
    while True: 
        try: 
            guess = int(input("\nEnter a number between 1 and 10: "))
            while guess > 10 or guess < 1:
                guess = int(input("\nInvalid entry outside of the range. \n\nEnter a number between 1 and 10: "))
            return guess
        except ValueError:
                print("\nInvalid entry. Please use a numeral.")

                
def start_game(high_score=None):
    if high_score == None:
        print("------------------------------------")
        print("Welcome to the Number Guessing Game!")
        print("------------------------------------")
    
    random_num = random.randrange(1,11)
    print("\nThe computer has generated a random number between 1 and 10. Can you guess it?")
    
    guess_count = 1
    guess = input_guess()
    while guess != random_num:
            if guess > random_num:
                guess_count += 1
                print("\nIt's lower. Try again.")
                guess = input_guess()
            if guess < random_num:
                guess_count += 1
                print("\nIt's higher. Try again.")
                guess = input_guess()
    if high_score == None or high_score > guess_count:
        high_score = guess_count
    
    print("\nGreat job, you've guessed the correct number in {} try/tries!".format(guess_count))
    
    play_again = input("That's the end of the game. Would you like to play again? (Y/N): ")
    if play_again.upper() == "Y":
        print("\nGreat! Try to beat your best score of {}.".format(high_score)) 
        start_game(high_score)
    else:
        print("Thanks for playing!")
     

start_game()