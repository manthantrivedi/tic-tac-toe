'''
    File: Tic-Tac-Toe Milestone Project for Udemy Python Course
    Author: Manthan Trivedi
    Description: A simple two player Tic-Tac-Toe game made within a Jupyter Notebook
    '''

from IPython.display import clear_output

#Note: We are ignoring index 0.
board = [' '] * 10  #empty list of 10 elements long.
game_state = True
announce = ''


def reset_board():
    '''This function resets the board to initial blank state.'''
    global board, game_state
    board = [' '] * 10
    game_state = True


def display_board():
    '''This function displays the whole board with each index corresponding to a normal Keyboard's Number pad's arranged numbers'''
    clear_output() # clears Jupyter Notebook output in cell
    print ("  " + board[7] + " |  " + board[8] + " |  " + board[9] + "  ")
    print ("--------------")
    print ("  " + board[4] + " |  " + board[5] + " |  " + board[6] + "  ")
    print ("--------------")
    print ("  " + board[1] + " |  " + board[2] + " |  " + board[3] + "  ")

def check_win(board, symbol):
    '''This function checks if a player has won by checking the board's horizontal, vertical, and diagonal alignments for the same symbol'''
    if(board[1] == board[2] == board[3] == symbol) or \
      (board[4] == board[5] == board[6] == symbol) or \
      (board[7] == board[8] == board[9] == symbol) or \
      (board[1] == board[4] == board[7] == symbol) or \
      (board[2] == board[5] == board[8] == symbol) or \
      (board[3] == board[6] == board[9] == symbol) or \
      (board[1] == board[5] == board[9] == symbol) or \
      (board[3] == board[5] == board[7] == symbol):
        return True
    else:
        return False

def check_empty(board):
    '''This function checks if there are remaining spaces unfilled in the board'''
    if " " in board[1:10]: #if the board is empty
        return False
    else:  #if the board is filled
        return True

def ask_location(symbol):
    '''This function asks the player's where to place their X or O symbol on the board and checks if it's valid'''
    global board
    x = 'Choose from 1-9 on where to place your ' + symbol + '  --->  '
    while True:
        try:
            pick = int(input(x))
        except ValueError:
            print("Please input a number between 1-9")
            continue
        
        if board[pick] == " ":
            board[pick] = symbol
            break
        else:
            print ('That space is not empty. Please choose another space.')
            continue


def player_choice(symbol):
    '''This function determines the new game's state after the player makes a choice'''
    global board, game_state, announce
    announce = ''
    symbol = str(symbol)
    ask_location(symbol)
    if check_win(board,symbol):
        clear_output() #clears output of Jupyter notebook cell
        display_board()
        announce = symbol + " wins! Congratulations!"
        game_state = False
    
    clear_output()
    display_board()
    if check_empty(board):
        announce = "Game tied! End of game."
        game_state = False
    return game_state, announce



def lets_play():
    reset_board()
    global announce
    
    X = 'X'
    O = 'O'
    while True:
        clear_output()
        display_board()
        
        game_state, announce = player_choice(X)
        print (announce)
        if game_state == False:
            break
        
        game_state, announce = player_choice(O)
        print (announce)
        if game_state == False:
            break

    rematch = input('Would you like to play again? y or n')
    if rematch == 'y':
        play()
    else:
        print ("Okay. Have a nice day!")

lets_play()