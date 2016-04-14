#Helper function to convert name to number
def name_to_number(name):
    if name == "rock": 
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "You have entered invalid choice"
    
######################################################

#Helper function to convert number to name
def number_to_name(number):
    if number == 0: 
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Number is invalid"
    
########################################################   

#Main Function - rpsls()
import random

def rpsls(player_choice):
    print ""
    
    #1st part - Get the Player's choice
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    

    #2nd part - Generate the computer's choice
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
  

    #Calculate the winner  
    diff = (player_number - comp_number) % 5
    if diff == 1 or diff == 2:
        print "Player wins!"
    elif diff == 3 or diff == 4:
        print "Computer wins!"
    elif diff == 0:
        print "Player and computer tie!"
    else:
        print "Invalid game"
    
#########################################################   

#Calling rpsls with various player's choice
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



