#This function creates and runs 20x2 game 
def table_diceRolls(Pname):

   #Creating and initiallzing variables
   human_moves = 0
   human_black_holes = 0
   computer_moves = 0
   computer_black_holes = 0
   dice_value=0
   computer_dice_value=0
   table= []
   players_location = -1 
   computers_location = -1 
   P_number_of_moves=0
   C_number_of_moves=0
   colum_num=0
   won=0
   new_location=0
   P_new_location=0

   import random
   import time
   #Calling game_summery module as gs
   import game_summery as gs
   #Calling game_session_textfile module as gst
   import game_session_textfile as gst

   #Create game board(game table)
   for i in range(3):
      row = [" "]*21
      table.append(row)
   #Print "O" in specific positions in the table
   table[1][7] = "O"
   table[1][14] = "O"
   table[2][7] = "O"
   table[2][14] = "O"
   #Print "#" in the 1st row 1st block
   table[0][0] = "#"
   #Print "H" in the 2nd row 1st block
   table[1][0]="H"
   #Print "C" in the 3rd row 1st block
   table[2][0]="C"
   #Assign column numbers to the first row of the table
   for colum_num in range(1, 21):
      table[0][colum_num] = str(colum_num)

   print("\t\t\t\t! Let's Roll The Dice & See What Luck Has In Store For You !")

   #Continue playing until one of the players reaches or exceeds the block of 20
   while players_location<20 and computers_location<20:
      #Show the player's location on the table only if they have entered the game
      if players_location>=1: 
          table[1][players_location] = "X"
      #Show the computer's  location on the table only if it has entered the game
      if computers_location>=1: 
          table[2][computers_location ] = "X"
      #Show the game board after each dice roll
      if dice_value>=1:
         time.sleep(2)
         print()
         for row in table:
            print(" ","|", end="")
            for perblock in row:
               print("{:<2}".format(perblock), end="|")
            print()
         print()  
         print("--------------------------------------------------------------------------")
      print()
      time.sleep(1)
      #Player's turn to roll the dice
      print()
      print(">>",Pname,"It's Your Turn..")
      print()
      input("\t<< Press Enter To Roll The Dice >> ")
      print()

      #Generate a random number between 1 and 6 to simulate player's dice roll    
      dice_value = random.randrange(1, 7)
      time.sleep(2)
      print("\t> You Rolled:", dice_value)

      #If the player rolls a 6 before entering the table
      if dice_value == 6 and players_location==-1:
         time.sleep(2)
         print("\t> You Can Start The Game Now..")
         #Move the player's pawn to the 1st block on the table.
         players_location= 0
      #If the player hasn't rolled a 6 to enter the board yet
      elif dice_value != 6 and players_location == -1:
         time.sleep(2)
         print("\t> You Can't Start The Game. Roll The Dice Continuously Until You Get 6..")
      else:
         #Make the player's moving pawn disappear from the previous block it was located in
         table[1][players_location] = " "
         table[1][0]="H"
         #Calculate the number of moves player can make based on the dice roll, rounding down to the nearest integer
         P_number_of_moves = dice_value // 2
         #If the dice value is 1, the player doesn't move
         if P_number_of_moves== 0:
             time.sleep(2)
             print("\t> You Didn't Move..")
         else:
             #Determine player's new location on the table
             P_new_location = players_location + P_number_of_moves 
             #Determine the total number of moves player made 
             human_moves+=1
             #If the player's new location is equal to or greater than the 20th block, the player wins the game
             if P_new_location >=20:
                print()
                print()
                time.sleep(1)
                print("\t\t\t..Congratulations,",Pname,"!", "You Won The Game..")
                #Assign 2 to won variable to use in "game_summery" and "game_session_textfile" modules
                won=1
                break
             #If the player hits on a black hole                
             elif P_new_location==7 or P_new_location==14:
                time.sleep(2)
                print("\t> Oh No! You Hit A Black Hole. Move Back To Block 1.")
                players_location = 1
                #Calculate the player's total black hole hits
                human_black_holes += 1
             #If the player moves on a regular block
             else:
                players_location = P_new_location
                time.sleep(2)
                print("\t> Your Current Location Is:",players_location)
                

      #Generate a random number between 1 and 6 to simulate computers's dice roll 
      computer_dice_value = random.randrange(1, 7)
      print()
      time.sleep(1) 
      print(">> Now Computer's Turn..")
      print()
      time.sleep(2)
      print("\t> Computer Rolled:", computer_dice_value)

      #If the computer rolls a 6 before entering the table
      if computer_dice_value==6 and computers_location==-1:
         time.sleep(2)
         print("\t> Computer Can Start The Game Now..")
         #Move the computer's pawn to the 1st block on the table.
         computers_location=0 
      elif computer_dice_value!= 6 and computers_location==-1:
         time.sleep(2)
         print("\t> Computer Can't Start The Game..")
      else:
        #Make the computer's moving pawn disappear from the previous block it was located in
        table[2][computers_location]= " "
        table[2][0]="C"
        #Calculate the number of moves computer can make based on the dice roll, rounding down to the nearest integer
        C_number_of_moves=computer_dice_value//2
        #If the dice value is 1, the computer doesn't move
        if C_number_of_moves==0:
           time.sleep(2)
           print("\t> Computer Didn't Move..")
        else:
          #Determine computer's new location on the table
          new_location = computers_location + C_number_of_moves
          #Determine the total number of moves computer made
          computer_moves+=1
          #If the computer's new location is equal to or greater than the 20th block, the computer wins the game        
          if new_location>=20:
             time.sleep(1)
             print()
             print()
             print("\t\t\t\t\t Computer Won The Game!!")
             print()
             time.sleep(1)
             print("\t\t Unfortunately, You Didn't Win This Time. Better Luck Next Time",Pname,"!!!")
             #Assign 2 to won variable to use in "game_summery" and "game_session_textfile" modules
             won=2
             break
          #If the computer hits on a black hole          
          elif new_location== 7 or new_location == 14:
             time.sleep(2)
             print("\t> Oh No!The Computer Hit A Black Hole. Move Back To Block 1.")
             computers_location  = 1
             #Calculate the computer's total black hole hits
             computer_black_holes += 1
          #If the player moves on a regular block
          else: 
             computers_location  = new_location
             time.sleep(2)
             print("\t> Computer's Current Location Is:", computers_location)

   print()
   time.sleep(2)

  #Calling "game_summery" function inside "game_summery" module
   gs.game_summery(human_black_holes,computer_black_holes,human_moves,computer_moves,won)

  #Calling "game_session_textfile" function inside "game_session_textfile" module
   gst.game_session_textfile(human_black_holes,computer_black_holes,human_moves,computer_moves,won)

   return

               
