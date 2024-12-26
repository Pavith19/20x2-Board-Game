import datetime

#This function will write the game summary to a text file
def game_session_textfile(human_black_holes,computer_black_holes,human_moves,computer_moves,won):

    #Creating and initiallzing variables
    file=None

    #Getting the current date and time
    current=datetime.datetime.now()
    #Formatting the year, month date and time to use as filename
    filename=current.strftime("%Y_%m_%d_%H_%M.txt")
    #Opening the file in write mode with the obtained filename
    file=open(filename,"w")

    #Writing the game summary to the file
    file.write("\t\t<<Summery Of The 20x2 Game Play>>"+"\n")
    file.write(" "+"\n")
    file.write("\tHuman"+"\n")
    file.write(""+"\n")
    file.write("\tTotal moves:"+(str(human_moves))+"\n")
    file.write("\tBlack hole hits:"+(str(human_black_holes))+"\n")
    #Checking if the human player won or lost the game and writing the appropriate message
    if won==1:
       file.write(" "+"\t!Won the game!"+"\n")
    elif won==2:
       file.write(" "+"\t!Lost the game!"+"\n")
    file.write(" "+"\n")
    file.write("\tComputer"+"\n")
    file.write(" "+"\n")
    file.write("\tTotal moves:"+(str(computer_moves))+"\n")
    file.write("\tBlack hole hits:"+(str(computer_black_holes))+"\n")
    #Checking if the computer won or lost the game and writing the appropriate message
    if won==2:
       file.write("  "+"\t!Won the game!"+"\n")
    elif won==1:
       file.write("  "+"\t!Lost the game!"+"\n")
    return 


