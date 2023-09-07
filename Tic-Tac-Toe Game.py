#!/usr/bin/env python
# coding: utf-8

# ***TIC-TAC-TOE Game***

# **Step 1:Creating a display board for the Tic-Tac-Toe game**

# In[1]:


from IPython.display import clear_output
clear_output()


# In[2]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-----")
    print(board[7]+'|'+board[8]+'|'+board[9])
    


# In[4]:


from IPython.display import clear_output
clear_output()


# **Step 2: Writing a function that can take in a player input and assign their marker as 'X' or 'O'**

# In[5]:


def player_input():
    Player1_mark =" "
    Player2_mark= " "
    while Player1_mark not in ['X','O']:
        Player1_mark=input('please choose between X or O: ')
        if Player1_mark not in ['X','O']:
            clear_output()
            print("You did not provide a suitable input")
        if Player1_mark in ['X','O']:
            if Player1_mark=='X':
                Player2_mark="O"
                return("X","O")
            else:
                Player2_mark='X'
                return("O","X")
          


# In[6]:


# This function depicts the choice of a position by each player
def position_choice():
    choice=""
    within_range=False
    #When the choice is not a digit and it is not within the range keep asking user the input
    while choice.isdigit()==False or within_range==False:
        choice=input("pick a number between (1-9): ")
        # when it is not a digit provide user a message
        if choice.isdigit()==False:
            print("The number you have typed is not even a digit")
            # when it is a digit and it is within the range break the loop by setting the within_range=True
        if choice.isdigit()==True:
            if int(choice) in range(1,10):
                within_range=True
                # if it is a digit but no withing range keep the within_range value 'False' and start again
            else:
                print('This is not in the range of 1-9..Please Try Again')
                within_range=False
    return int(choice)


# **Step 3: Writing a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board**

# In[8]:


def place_marker(board, marker, position):
#Asking the player to give the marker
#Choose a position where the marker will be given 
# display the board returning marker on the provided location
    board[position]=marker
    return board


# **Step 4: Writing a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.**

# In[10]:


# It includes all the cases in which a person can win

def win_check(board, mark):
    if board[1]==board[2]==board[3]==mark:
        return True
    elif board[4]==board[5]==board[6]==mark:
        return True
    elif board[7]==board[8]==board[9]==mark:
        return True
    elif board[1]==board[5]==board[9]==mark:
        return True
    elif board[2]==board[5]==board[8]==mark:
        return True
    elif board[3]==board[6]==board[9]==mark:
        return True
    elif board[1]==board[4]==board[7]==mark:
        return True
    elif board[3]==board[5]==board[7]==mark:
        return True
    else:
        return False
    


# **Step 5: Writing a function that uses the random module to randomly decide which player goes first**

# In[26]:


# Between player1 and player2 it will choose who will go first
import random
def choose_first():
    toss=random.randint(1,2)
    if toss==1:
        return "Player1"
    else:
        return "Player2"


# In[13]:


choose_first()


# **Step 6: Writing a function that returns a boolean indicating whether a space on the board is freely available**
# 

# In[14]:


def space_check(board, position):
    if board[position]==" ":
        return True
    else:
        return False


# In[15]:


space_check(test_board,2)


# **Step 7: Writing a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[22]:


def full_board_check(board):
    for i in range (1,10):
        if space_check(board, i):
            return False
        
    return True
            
    


# In[23]:


full_board_check(test_board)


# **Step 8: Writing a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[18]:


def player_choice(board):
    position=position_choice()
    space_check(board, position) 
    


# **Step 9: Writing a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[19]:


def replay():
    again=" "
    while again not in ["Y","N"]:
        again=input("would you like to play it again?")
        if again not in ["Y","N"]:
            clear_output()
            print("please make a proper choice on whether or not you want to continue")
        if again=="Y":
            return True
        else:
            return False


# **Step 10: Here comes the hard part! Using while loops and the functions I've made to run the game!**

# In[25]:


# while loop to keep running the game
print('Welcome to the Tic-Tac-Toe game')

while True:
    test_board = [" "]*10
    Player1_mark, Player2_mark = player_input()
    print(f'Player 1 will proceed with {Player1_mark} and Player 2 will proceed with {Player2_mark}')
    
    # Who will go first between two players. We will use 'turn' as an indicator of that
    turn = choose_first()
    print(f'{turn} will go first')
    
    # Start the game if they want to
    start_game = input("Do you want to start? (Y/N): ")
    
    if start_game.upper() == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == "Player1":
            display_board(test_board)
            
            # Choose a position and put the marker
            position = position_choice()
            place_marker(test_board, Player1_mark, position)
           
            if win_check(test_board, Player1_mark):
                display_board(test_board)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("TIE Game")
                    break
                else:
                    turn = 'Player2'
        else:
            if turn == "Player2":
                display_board(test_board)
                
                # Choose a position and put the marker
                position = position_choice()
                place_marker(test_board, Player2_mark, position)
                
                if win_check(test_board, Player2_mark)==True:
                    display_board(test_board)
                    print('Player 2 has won')
                    game_on = False
                else:
                    if full_board_check(test_board):
                        display_board(test_board)
                        print("TIE Game")
                        game_on = False
                    else:
                        turn = 'Player1' 
    if not replay():
        break


# 
