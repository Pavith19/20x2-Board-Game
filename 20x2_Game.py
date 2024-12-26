#Creating and initializing variables
start_again=1
play_again=""
Pname=""

import time
#Calling "tableANDdiceroll" module as tdr
import tableANDdiceroll as tdr

print()
#Print welcome message to the player
print("\t\t\t\t\t\t\t... WELCOME TO 20x2 GAME...")
time.sleep(2)
#Adding some space for readability
print()
print()

#This is a while loop that will continue to run until the user enters their name
while not Pname:
   Pname=input("▲ Enter your name >> ")
   #Check if the user has entered a name or left it blank
   if not Pname:
        print()
        print(" ! Please Enter Your Name To Begin The Game !")
        print()
print()
print()
time.sleep(1)
#Print the instructions for playing the game
print("<< Instructions For Playing Game >>")
time.sleep(2)
print()
print()
print("1) The board has 20 blocks numbered 1 to 20 for both players.")
time.sleep(1)
print()
print("2) The other player is the computer.")
time.sleep(1)
print()
print("3) The first row of blocks is for the human player (\"H\"), while the second row is for the computer (\"C\").")
time.sleep(1)
print()
print("4) The game starts when a player rolls a 6 on the dice.")
time.sleep(1)
print()
print("5) Until a player rolls a 6, their pawn cannot enter the board.")
time.sleep(1)
print()
print("6) The player's moving pawn is represented by the letter \"X\".")
time.sleep(1)
print()
print("7) Both players have black holes on the board, located at block numbers \"7\" & \"14\".")
time.sleep(1)
print()
print("8) Black holes are denoted by the letter \"O\".")
time.sleep(1)
print()
print("9) If a player lands on a black hole, they must move back to block 1.")
time.sleep(1)
print()
print("10) If a player passes over a black hole without landing on it, there is no penalty.")
time.sleep(1)
print()
print("11) The number of blocks a player can move is equal to half of the dice value.")
print()
print("""\t*If you roll a 6, you can move 3 blocks.
\t*If you roll a 5, you can move 2 blocks (0.5 is neglected).
\t*If you roll a 1, you don't move at all.""")
time.sleep(1)
print()
print("12) The first player to reach or pass block 20 wins the game.")
time.sleep(1)
print()
print()

#Loop to allow the user to play the game again
while start_again==1:
    time.sleep(2)
    #Calling "table_diceRolls" function inside "tableANDdiceroll" module
    tdr.table_diceRolls(Pname)
    print()
    print()
    #Prompting the player to enter whether they want to play the game again or not
    time.sleep(2)
    print(">> Do you want to play again (Yes/No)?",end=" ")
    play_again=input("")
    print()
    print()
    print()
    #If the user enters "yes" or "Yes", the loop continues by assigning the value 1 to the "start_again" variable  
    if(play_again=="yes" or play_again=="Yes"):
       start_again=1
    #Otherwise, the loop is exited by incrementing the "start_again" variable and using the "break" statement
    else:
        time.sleep(1)
        print("\t\t\tThank you for playing! We hope to see you again soon...")
        print()
        start_again+=1
        break        






