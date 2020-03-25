# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:37:14 2020

@author: Biswaraj

Tic-Tac-Toe Game

Completed on Wed Feb 5 2020
"""

player_marker = ''
board_list = ['#','1','2','3','4','5','6','7','8','9']

# For getting the Tic_TAc_Toe Game board.
def getboard(board_list):    
    print(' \t | \t |')
    print('    ' + board_list[1] + ' \t |   ' + board_list[2] + ' \t |    ' + board_list[3])
    print(' \t | \t |')
    print('----------------------------')
    print(' \t | \t |')
    print('    ' + board_list[4] + ' \t |   ' + board_list[5] + ' \t |    ' + board_list[6])
    print(' \t | \t |')
    print('----------------------------')
    print(' \t | \t |')
    print('    ' + board_list[7] + ' \t |   ' + board_list[8] + ' \t |    ' + board_list[9])
    print(' \t | \t |')

# Choose your marker!
def markerchoice():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('\nPlayer 1, Please choose Your Marker (Either X or O ) : ').upper()
        if not (marker == 'X' or marker == 'O'):
            print('\nInvalid Choice!! Choose Again : ')
    if marker == 'X':
        player_marker = ['X', 'O']
    else:
        player_marker = ['O', 'X']
    return player_marker

# Check if the position is already occupied.
def check_position(position):
    if board_list[position] == 'X' or board_list[position] == 'O':
        return True
    else:
        return False

# Take position value to be Marked from the player.
def take_position():
    position = 0
    empty_or_not = ''
    while not ((position in range(1,10)) and (empty_or_not == False)):
        position = int(input('\nEnter The position to Mark : '))
        empty_or_not = check_position(position)
        if empty_or_not == True:
            print('\nThe position is already occupied!! Please choose different position to mark. ')
    
    return position

# To Check if the Board is full or Draw Condition.
def isboardfull(board_list):
    for item in range(1, 10):
        if not (board_list[item] == 'X' or board_list[item] == 'O'):
            check = False
            break
        else:
            check = True
    return check

# To check if the Player Won.
def wincheck():
    if (board_list[1] == board_list[2] == board_list[3]) or \
    (board_list[4] == board_list[5] == board_list[6]) or \
    (board_list[7] == board_list[8] == board_list[9]) or \
    (board_list[1] == board_list[4] == board_list[7]) or \
    (board_list[2] == board_list[5] == board_list[8]) or \
    (board_list[3] == board_list[6] == board_list[9]) or \
    (board_list[1] == board_list[5] == board_list[9]) or \
    (board_list[3] == board_list[5] == board_list[7]):
        return True
    else:
        return False

# To ask user if they want to play again.
def playagain():
    yes_or_no = ''
    while not (yes_or_no == 'YES' or yes_or_no == 'NO' or yes_or_no == 'Y' or yes_or_no == 'N'):
        yes_or_no = input('\nDo you Want to play again ? (Yes or no) : ').upper()
        if not (yes_or_no == 'YES' or yes_or_no == 'NO' or yes_or_no == 'Y' or yes_or_no == 'N'):
            print('\nInvalid Choice!! Choose Again : ')
    if (yes_or_no == 'YES' or yes_or_no == 'Y'):
        update_position()
    else:
        print('\n\tThanks For Playing. \n\tHave a Nice Day!! 😘😘')

# For updating the Game Board and to play the game.
def update_position():
    global board_list # To grab the globaly declared list and update changes to global level.
    board_list = ['#','1','2','3','4','5','6','7','8','9']
    turn = 0
    marker_value = markerchoice()
    
    while True:
        
        if turn%2 == 0:
            print('\nPlayer 1, It\'s Your Turn : ')
            board_index = take_position()
            board_list[board_index] = marker_value[0]
            getboard(board_list)
            if wincheck() == True:
                print('\n\tCongrats!! Player 1 You Won! 🎉😍')
                break
            if isboardfull(board_list) == True:
                print('\n\tGame Draw!!')
                break
        else:
            print('\nPlayer 2, It\'s Your Turn : ')
            board_index = take_position()
            board_list[board_index] = marker_value[1]
            getboard(board_list)
            if wincheck() == True:
                print('\n\tCongrats!! Player 2 You Won! 🎉😍')
                break
            if isboardfull(board_list) == True:
                print('\n\tGame Draw!!')
                break
        
        turn += 1
    playagain()

update_position()


