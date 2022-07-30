# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Siryon George
# Creation Date: July 29, 2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
        #Place the print statement under the displayIntro of the def function
    print('''You are in a land full of dragons. In front of you,
       you see two caves. In one cave, the dragon is friendly
       and will share his treasure with you. The other dragon
       is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    #A SyntaxError occur here due to inconsistent use of tabs and space indentation. Use the backspace and move the while loop under the cave. 
    while cave != '1' and cave != '2':
            #SyntaxError occur here, move the print statement under the while loop.
	 print('Which cave will you go into? (1 or 2)')
	 cave = input()
    #A Logical error occurs here, the word should be cave, not caves.
    return cave

def checkCave(chosenCave):
     print('You approach the cave...')
	#sleep for 2 seconds
     time.sleep(2)
     print('It is dark and spooky...')
	#sleep for 2 seconds
    # A logical error occurs here, change the (3) to (2)
     time.sleep(3)
     print('A large dragon jumps out in front of you! He opens his jaws and...')
     print()
	#sleep for 2 seconds
     time.sleep(2)
     friendlyCave = random.randint(1, 2)

     if chosenCave == str(friendlyCave):
                #A SyntaxError occur here, move the print statement under the chosenCave of the if loop, place the print under the letter o.
	 print('Gives you his treasure!')
     else:
        #Syntaxerror occur here, place a parentheses around the print statement 
	 print 'Gobbles you down in one bite!'

playAgain = 'yes'
#Logic error occur here, use double == instead of one.
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = choosecave()
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    #Remove the statement here
	if playAgain == "no":
               #Move the print statement under the playAgain for the right indentation
    print("Thanks for planing")

