#This fuction prints out a summary of the game play including total moves made, black hole hits, and whether the player won or lost
def game_summery(human_black_holes,computer_black_holes,human_moves,computer_moves,won):
    print()
    print("\t\t-------------------------------------------------------------")
    print()
    print("\t\t\t\t**Summery Of The Game Play**")
    print()
    #Printing the summary of the human player's performance
    print("\t\t\t\tYOU")
    print()
    print("\t\t\t\tTotal moves:",human_moves)
    print("\t\t\t\tBlack hole hits:",human_black_holes)
    #Checking if the human player's won or lost the game and printing the appropriate message
    if won==1:
       print("\t\t\t\t!Won the game!")
    elif won==2:
       print("\t\t\t\t!Lost the game!")
    print()
    print()
    #Printing the summary of the computer's performance
    print("\t\t\t\tCOMPUTER")
    print()
    print("\t\t\t\tTotal moves:",computer_moves)
    print("\t\t\t\tBlack hole hits:",computer_black_holes)
    #Checking if the computer won or lost the game and printing the appropriate message
    if won==2:
       print("\t\t\t\t!Won the game!")
       print()
       print("\t\t-------------------------------------------------------------")
    elif won==1:
       print("\t\t\t\t!Lost the game!")
       print()
       print("\t\t-------------------------------------------------------------")

    return
    
    
    
  
     
