#Importing the necessary library for the game module
import random
import os.path
import json
random.seed()

def draw_board(board):
    # develop code to draw the board
    print('-------------')
    print('| ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' |')
    print('-------------')
    print('| ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' |')
    print('-------------')
    print('| ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' |')
    print('-------------')

def welcome(board):
    # prints the welcome message
    print("Welcome to the 'Unbeatable Noughts and Crosses' \n")
    print("The board layout is show below: ")

    
    # display the board by calling draw_board(board)
    draw_board(board)

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    rows = 3
    columns = 3
    
    for row in range(rows):
        for col in range(columns):
            board[row][col] = ' '
    return board

def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter col (1-3): ")) - 1
            if row>2 or col>2 or row<0 or col<0 :
                print("enter 1-3")
                continue   
            else:
            # and return row and col  
                if board[row][col]==" ":  
                    return row, col
                else:
                    print("Invalid position")
        except:
            print("enter 1-3")
            continue

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            break
    # and return row and col
    return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
        
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    initialise_board(board)
    draw_board(board)
    # then in a loop, get the player move, update and draw the board

    # X for player and 0 for computer move
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        if check_for_win(board, 'X'):
            return 1
        if check_for_draw(board):
            return 0
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1
        if check_for_draw(board):
            return 0
       
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    while True:
        choice = input("Enter 1 to play, 2 to save score, 3 to load scores, q to quit: ")
        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print("Invalid Choice")
        

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    try:
        with open("leaderboard.txt", mode = "r") as file:
            players = json.load(file)
            return players
    except FileNotFoundError:
        return {}

def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    name = input("Enter your name: ")
    score_dict = {name: score} # dictionary with name as key and score as value
    
    players = {} #making empty dictionary
    # checks if the file exists and handling using try and except
    if os.path.exists("leaderboard.txt"):
        try:
            with open("leaderboard.txt", mode = "r") as file:
                players = json.load(file)
        except FileNotFoundError as e:
            print(f"Error is {e}")

    # If the name is new, set the initial score to zero
    if name not in players:
        players[name] = 0

    # update the players dictionary with the new score
    players.update(score_dict)

    # save the updated players dictionary to the file
    with open("leaderboard.txt", "w") as file:
        json.dump(players, file)

    
def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print("##### LEADERBOARD #####")
    #items will convert dictionary into tuples
    for player, score in leaders.items():
        print("      "+player + ": " + str(score))
        print("")