# Guess the number mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    global counter
    global secret_number
 
    if num_range == 100:
        range100()
    else:
        range1000()
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    global counter
    counter = 7
    global secret_number
    secret_number = random.randrange(0,num_range)
    print ""
    print "New game.  Range is from 0 to 100"
    print "Number of remaining guesses is", counter
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game    
    global num_range
    num_range = 1000
    global counter
    counter = 10
    global secret_number
    secret_number = random.randrange(0,num_range)
    print ""
    print "New game.  Range is from 0 to 1000"
    print "Number of remaining guesses is", counter
    return num_range
    
def input_guess(guess):
    # main game logic going here
    guessnumber = int(guess)
    global secret_number
    global counter
    counter = counter - 1
    if counter == 0:
        print ""
        print "Guess was", guess
        print "Number of remaining guesses is", counter
        if guessnumber == secret_number:
            print "Correct!"
            new_game()
        else:         
            print "You ran out of guesses.  The number was", secret_number
            new_game()
    else:
        print ""
        print "Guess was", guess
        print "Number of remaining guesses is", counter
        if guessnumber == secret_number:
            print "Correct!"
            new_game()
        elif guessnumber < secret_number:
            print "Higher!"
        else:
            print "Lower!"       

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
f.add_button("Range is (0, 100)", range100, 200)
f.add_button("Range is (0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

