'''
Name: Aalia Anjum
Date: July 30th 2024
'''

#importing  relevant libraries
import tkinter as tk
from tkinter import *

####################################################################################################################################################################
#TITLE SCREEN CODE
####################################################################################################################################################################

# This function is called when "play with friend" is clicked
def start_game_F():
    title_frame.pack_forget()  # Hide the title screen
    gframe.pack(fill="both", expand=True)  # Show the game screen

# This function is called when "play with AI" is clicked
def start_game_AI():
    title_frame.pack_forget()  # Hide the title screen
    AIframe.pack(fill="both", expand=True)  # Show the game screen

# Setting up the main application window
start_win = tk.Tk()
start_win.title('Tick Tac Toe')
start_win.resizable(False, False)
start_win.iconbitmap('xo_image2.ico')

# Defines the color palette for the game
black = "grey25"
grey = "light slate gray"
green = "OliveDrab1"
purple = "maroon1"

# Title screen frame
title_frame = tk.Frame(start_win)
title_frame.pack(fill="both", expand=False)

# Title screen labels
title_label = tk.Label(title_frame, height=2, width = 21,  text="TICK TAC TOE", font=("Consolas", 20), bg=black, foreground='white')
title_label.grid(row=0, column=0, columnspan=3, sticky='we')

title_label2 = tk.Label(title_frame, height=2, text="Choose a game mode to begin", font=("Consolas", 15), bg=black , foreground='white')
title_label2.grid(row=2, column=0, columnspan=3, sticky='we')

title_label3 = tk.Label(title_frame, height=2, text="A Game By Aalia Anjum", font=("Consolas", 15), bg=black, foreground='white')
title_label3.grid(row=6, column=0, columnspan=3, sticky='we')

start_lab_Blank = tk.Label(title_frame, height=4, text=" ",  font=("Arial", 14), bg=black, foreground='white')
start_lab_Blank.grid(row=5, column=0, columnspan=3,sticky='we')

# Start game buttons , respectively;(play with friend, playwith ai(you first), play with ai(ai goes first)
start_button = tk.Button(title_frame, height=4, text="PLAY AGAINST A FREIND",  font=("Arial", 14,'bold'), command=start_game_F, bg=black, foreground=green)
start_button.grid(row=3, column=0, columnspan=3, sticky='we')

start_button_ai = tk.Button(title_frame, height=4, text="PLAY AGAINST AI ",  font=("Arial", 14,'bold'),command=start_game_AI ,bg=black, foreground=purple)
start_button_ai.grid(row=4, column=0, columnspan=3, sticky='we')


####################################################################################################################################################################
#CODE FOR FREIND VS PLAYER GAME
####################################################################################################################################################################


# Defines player X and O
player_x = 'X'
player_o = 'O'
whos_turn = player_x
count = 0
# defines the board as a 3x3 matrix
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
# number of tuns left on the board
turns = 0
game_over = False

# when called changes the respective tile to X or 0 depeding on the turn
def set_tile(row, column):
    global whos_turn

    #checks if the game is over, if it is it exits the func
    if (game_over == True):
        return

    #checks if the square is empty
    if matrix[row][column]['text'] != '' :
        return # exits the function
    
    matrix[row][column]['text'] = whos_turn # marks the boards respective position
    # if its player o's turn, set the turn to player x, else set turn to player o
    if whos_turn == player_o:
        whos_turn = player_x
    else:
        whos_turn = player_o

    game_prompt['text'] = "It is " + whos_turn + "'s turn" # changes the game promt to the respective players 

    # checks the matrix board to see if someone has won , calls func check_win
    check_win()
    


# this erases teh board and starts the game again 
def new_game():
    global turns,game_over
    turns = 0
    game_over = False
    game_prompt.config(text="It is " + whos_turn + "'s turn", foreground = green)
    #makes the tiles blank again
    for row in range(3):
        for column in range(3):
            matrix[row][column].config(text="", foreground = purple , bg = black)
    

# finction that checks of there is a winner
def check_win():
    global turns, game_over
    turns += 1# adds a turn to the turn counter

    # checking the matrix horaxontally
    for row in range(3):
        if (matrix[row][0]['text'] == matrix[row][1]['text'] == matrix[row][2]['text'] and matrix[row][0]['text'] != '' ):
            #changes the promt box to display winner msg
            game_prompt.config(text=matrix[row][0]['text']+ " is the winner!", foreground = green)
            #changes the colour of the winning grid squares
            for column in range(3):
                matrix[row][column].config(foreground = green, bg = grey)
            game_over = True
            return
        
    # checking the vertically
    for column in range(3):
         if (matrix[0][column]['text'] == matrix[1][column]['text'] == matrix[2][column]['text'] and matrix[0][column]['text'] != '' ):
        #changes the promt box to display winner msg
            game_prompt.config(text=matrix[0][column]['text']+ " is the winner!", foreground = green)
            for row in range(3):
                matrix[row][column].config(foreground = green, bg = grey)
            game_over = True
            return
        
    # checking diagonaly (top left to bottom right)
    if (matrix[0][0]['text'] == matrix[1][1]['text'] == matrix[2][2]['text'] and matrix[0][0]['text'] != '' ):
        #changes the promt box to display winner msg
            game_prompt.config(text=matrix[0][0]['text']+ " is the winner!", foreground = green)
            for i in range(3):
                matrix[i][i].config(foreground = green, bg = grey)
            game_over = True
            return
        
     # checking diagonaly (top right to bottom left)
    if (matrix[0][2]['text'] == matrix[1][1]['text'] == matrix[2][0]['text'] and matrix[0][2]['text'] != '' ):
        #changes the promt box to display winner msg
            game_prompt.config(text=matrix[0][2]['text']+ " is the winner!", foreground = green)
            # individualyy canged the colour of each btn in diagonal
            matrix[0][2].config(foreground = green, bg = grey)
            matrix[1][1].config(foreground = green, bg = grey)
            matrix[2][0].config(foreground = green, bg = grey)
            game_over = True
            return
        
    #checks for tie, (if all squared filled)
    if (turns ==9):
        game_prompt.config(text= "It's a Tie!", foreground = green)
        game_over = True
        return


# this function retuns the player the home screen if home btn is presses on the play with freind game
def go_home():
    gframe.pack_forget()  # Hide the title screen
    title_frame.pack(fill="both", expand=True)  # Show the game screen

####################################################################################################################################################################
#CODE FOR AI VS PLAYER GAME
####################################################################################################################################################################
    
# Defines player X and O
player_xAI = 'X'
player_oAI = 'O'
whos_turnAI = player_oAI
countAI = 0
# defines the board as a 3x3 matrix
matrixAI = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
# number of tuns left on the board
turnsAI = 0
game_overAI = False


# when called places an X or 0 depeding on where the player clicked and where the ai intends to place
def set_tileAI(row, column):
    global whos_turnAI, game_overAI,turnsAI

    #ensures the first turn should always be the human
    if turnsAI == 0:
        whos_turnAI = player_oAI
        
    #checks if the game is over, if it is it exits the func to prevent double tile placement
    if game_overAI:
        whos_turnAI = player_oAI
        return
    
    #checks if the square is empty
    if matrixAI[row][column]['text'] != '':
        return #if empty, it exits the function
    
    # marks the boards respective position
    matrixAI[row][column]['text'] = whos_turnAI 
    
    # checks for the winning conditions
    check_winAI() 

    # if the game is is determined to be over after checking for win, the function exits without switching turns
    if game_overAI:
        return
    
    # Switch turns
    if whos_turnAI == player_oAI and game_over != True:
        whos_turnAI = player_xAI
        ai_move()  # AI plays after the human
    else:
        whos_turnAI = player_oAI
        
    # if the game is not over the function updates the game prompt to show whos turn it is 
    if game_overAI != True: 
        game_promptAI['text'] = "It is " + whos_turnAI + "'s turn" # changes the game promt to the respective players





# this erases teh board and starts the game again 
def new_gameAI():
    global turnsAI ,game_overAI
    turnsAI = 0 # makes num of turns back to 0
    game_overAI = False # makes game over not true
    whos_turnAI = player_oAI # ensures the game always starts with playero
    game_promptAI.config(text="It is " + whos_turnAI + "'s turn", foreground = green) # sets game prompt
    #makes the tiles blank again
    for row in range(3):
        for column in range(3):
            matrixAI[row][column].config(text="", foreground = purple , bg = black)
    

# finction that checks of there is a winner
def check_winAI():
    global turnsAI, game_overAI
    turnsAI += 1# adds a turn to the turn counter

    # checking the matrix horaxontally
    for row in range(3):
        if (matrixAI[row][0]['text'] == matrixAI[row][1]['text'] == matrixAI[row][2]['text'] and matrixAI[row][0]['text'] != '' ):
            #changes the promt box to display winner msg
            game_promptAI.config(text=matrixAI[row][0]['text']+ " is the winner!", foreground = green)
            #changes the colour of the winning grid squares
            for col in range(3):
                matrixAI[row][col].config(foreground = green, bg = grey)
            game_overAI = True
            return
        
    # checking the vertically
    for col in range(3):
         if (matrixAI[0][col]['text'] == matrixAI[1][col]['text'] == matrixAI[2][col]['text'] and matrixAI[0][col]['text'] != '' ):
        #changes the promt box to display winner msg
            game_promptAI.config(text=matrixAI[0][col]['text']+ " is the winner!", foreground = green)
            for row in range(3):
                matrixAI[row][col].config(foreground = green, bg = grey)
            game_overAI = True
            return
        
    # checking diagonaly (top left to bottom right)
    if (matrixAI[0][0]['text'] == matrixAI[1][1]['text'] == matrixAI[2][2]['text'] and matrixAI[0][0]['text'] != '' ):
        #changes the promt box to display winner msg
            game_promptAI.config(text=matrixAI[0][0]['text']+ " is the winner!", foreground = green)
            for i in range(3):
                matrixAI[i][i].config(foreground = green, bg = grey)
            game_overAI = True
            return
        
     # checking diagonaly (top right to bottom left)
    if (matrixAI[0][2]['text'] == matrixAI[1][1]['text'] == matrixAI[2][0]['text'] and matrixAI[0][2]['text'] != '' ):
        #changes the promt box to display winner msg
            game_promptAI.config(text=matrixAI[0][2]['text']+ " is the winner!", foreground = green)
            # individualyy canged the colour of each btn in diagonal
            matrixAI[0][2].config(foreground = green, bg = grey)
            matrixAI[1][1].config(foreground = green, bg = grey)
            matrixAI[2][0].config(foreground = green, bg = grey)
            game_overAI= True
            return
        
    #checks for tie, (if all squared filled)
    if (turnsAI ==9):
        game_promptAI.config(text= "It's a Tie!", foreground = green)
        game_overAI = True
        return



#checks what possible moves are left on the board
def get_available_moves():
    moves = [] # blank matrix to store quardinates of free tiles 
    #loops through all cols and rows in matrixAI, if empty saves row and column as tuple in matrixAI
    for row in range(3):
        for col in range(3):
            if matrixAI[row][col]['text'] == '':
                moves.append((row, col))
    return moves



# this function retuns the player the home screen if home btn is presses on the play with ai game
def go_homeAI():
    AIframe.pack_forget()  # Hide the title screen
    title_frame.pack(fill="both", expand=True)  # Show the game screen


# function checks if the board is at terminal states (win, draw, loss)
def evaluate():
    # Check for win conditions as in check_winAI but return a score instead of setting game_overAI

    #checking horizontally
    for row in range(3):
        if matrixAI[row][0]['text'] == matrixAI[row][1]['text'] == matrixAI[row][2]['text']:
            if matrixAI[row][0]['text'] == player_xAI: # if the row has all x's in it, returns max score of 10
                return 10
            elif matrixAI[row][0]['text'] == player_oAI:# if the row has all o's in it, returns min score of -10
                return -10
            
    #checking vertically
    for col in range(3):
        if matrixAI[0][col]['text'] == matrixAI[1][col]['text'] == matrixAI[2][col]['text']:
            if matrixAI[0][col]['text'] == player_xAI: # if the col has all x's in it, returns max score of 10
                return 10
            elif matrixAI[0][col]['text'] == player_oAI:# if the col has all o's in it, returns min score of -10
                return -10
            
    # checks for vertical win from top left to bottom right
    if matrixAI[0][0]['text'] == matrixAI[1][1]['text'] == matrixAI[2][2]['text']:
        if matrixAI[0][0]['text'] == player_xAI:# if the vertical has all x's in it, returns max score of 10
            return 10
        elif matrixAI[0][0]['text'] == player_oAI:# if the vertical has all o's in it, returns min score of -10
            return -10
        
    # checks for vertical win from top right to bottom left
    if matrixAI[0][2]['text'] == matrixAI[1][1]['text'] == matrixAI[2][0]['text']:
        if matrixAI[0][2]['text'] == player_xAI:# if the vertical has all x's in it, returns max score of 10
            return 10
        elif matrixAI[0][2]['text'] == player_oAI:# if the vertical has all o's in it, returns min score of -10
            return -10

    # if no 3 matiching consecutive symbols, score 0 (draw state), no winner
    return 0  


#minimax function, by looking at the board, edits the score and returns it
def minimax(depth, is_maximizing): # depth is the current depth of the recursion, represents how many movies ahead the ai considers, is_miximizing is a bool that indicates wether the current turn is the minimizing player (o) or the maximizing ai player (x)
    score = evaluate() # calls function that checks and gets score if terminal states have been reached (o won, x won , or draw)

    # If the game is over, return the score
    if score == 10 or score == -10:
        return score

    # checks if no more moves left  and if there is no winner. if so, then its a tie, returns a score of 0
    if len(get_available_moves()) == 0:
        return 0

    # Maximizing player (AI)
    if is_maximizing:
        best_score = -float('inf') # innitalizes  the best score to -inf (the ai will try to bring this value up and compare to -inf)

        # loops through all available moves
        for move in get_available_moves():
            row, col = move # unpacks the move quardinates from the tupel and stores as row and col
            matrixAI[row][col]['text'] = player_xAI# make the move by placing the ai's mark (x) on board

            # Recursively call minimax for the next depth level with the minimizing player's turn
            best_score = max(best_score, minimax(depth + 1, False))
            # Undo the move to restore the board state
            matrixAI[row][col]['text'] = ''  # Undo the move to restore the matrix board state
        return best_score # Return the best score found for maximizing player (AI)

    # Minimizing player (Human)
    else:
        best_score = float('inf') # innitalizes  the best score to inf (the ai will try to bring this value down and compare to inf)
        # Loop through all available move
        for move in get_available_moves():
            row, col = move  # unpacks the move quardinates from the tupel and stores as row and col
            matrixAI[row][col]['text'] = player_oAI # make the move by placing the human's mark (o) on board
             # Recursively call minimax for the next depth level with the maximizing player's turn
            best_score = min(best_score, minimax(depth + 1, True))

            matrixAI[row][col]['text'] = ''  # Undo the move to restore the matrix board state
        return best_score# Return the best score found for minimizing player (Human)

#function to allow ai to move
def ai_move():
    best_score = -float('inf')  # Initialize the best score to negative infinity; AI aims to maximize this score
    best_move = None  # Initialize best_move to None; this will store the best move found

    # Iterate through all available moves on the board
    for move in get_available_moves():
        row, col = move  # Unpack the move into row and column coordinates
        matrixAI[row][col]['text'] = player_xAI  # Simulate the AI's move by placing its mark (X) on the board

        # Call the minimax function to evaluate the potential outcome of this move
        move_score = minimax(0, False)

        matrixAI[row][col]['text'] = ''  # Undo the move to restore the board state

        # If the score of the current move is better than the best score found so far, update best_score and best_move
        if move_score > best_score:
            best_score = move_score  # Update best_score with the higher score
            best_move = (row, col)  # Update best_move with the current move's coordinates

    # If a best move was found, make that move on the board
    if best_move:
        set_tileAI(best_move[0], best_move[1])  # Place the AI's mark on the board at the best_move coordinates

####################################################################################################################################################################
#creates the game board for human vs human
####################################################################################################################################################################

# Creating the game screen frame (initially hidden)
gframe = tk.Frame(start_win)

# Game title
game_title = tk.Label(gframe, height=2, text="TIC TAC TOE", font=("Consolas", 20), bg=black, foreground='white')
game_title.grid(row=0, column=0, columnspan=3, sticky='we')

# Prompt for whose turn it is
game_prompt = tk.Label(gframe, height=1, width=20, text=(whos_turn + "'s turn"), font=("Consolas", 15), bg=black)
game_prompt.grid(row=1, column=0, columnspan=3, sticky='we')

# Initializing the 9 buttons relative to the matrix
for row in range(3):
    for column in range(3):
        matrix[row][column] = tk.Button(gframe, text='', height=4, width=9, font=('Consolas', 15, "bold"), bg=black, foreground=purple, command=lambda row=row, column=column: set_tile(row, column))
        matrix[row][column].grid(row=row+2, column=column)

# Creating the reset game button
reset_btn = tk.Button(gframe, text='Reset Game',  height =2,font=("Consolas", 15), bg=black, foreground='white', command=lambda: new_game())
reset_btn.grid(row=5, column=0, columnspan=2, sticky='we')

# Creating the home button
home_btn = tk.Button(gframe, text='Home',  height =2,font=("Consolas", 15), bg=black, foreground='white', command=lambda: go_home())
home_btn.grid(row=5, column=2, sticky='we')

####################################################################################################################################################################
#creates the game board for human vs ai
####################################################################################################################################################################

# Creating the game screen frame (initially hidden)
AIframe = tk.Frame(start_win)

# Game title
game_titleAI= tk.Label(AIframe, height=2, text="TIC TAC TOE - AI", font=("Consolas", 20), bg=black, foreground='white')
game_titleAI.grid(row=0, column=0, columnspan=3, sticky='we')

# Prompt for whose turn it is
game_promptAI = tk.Label(AIframe, height=1, width=20, text=(whos_turnAI + "'s turn"), font=("Consolas", 15), bg=black)
game_promptAI.grid(row=1, column=0, columnspan=3, sticky='we')

# Initializing the 9 buttons relative to the matrix
for row in range(3):
    for column in range(3):
        matrixAI[row][column] = tk.Button(AIframe, text='', height=4, width=9, font=('Consolas', 15, "bold"), bg=black, foreground=purple, command=lambda row=row, column=column: set_tileAI(row, column))
        matrixAI[row][column].grid(row=row+2, column=column)

# Creating the reset game button
reset_btnAI = tk.Button(AIframe, height =2, text='Reset Game', font=("Consolas", 15), bg=black, foreground='white', command=lambda: new_gameAI())
reset_btnAI.grid(row=5, column=0, columnspan=2, sticky='we')

# Creating the home button
home_btnAI = tk.Button(AIframe, text='Home',  height =2,font=("Consolas", 15), bg=black, foreground='white', command=lambda: go_homeAI())
home_btnAI.grid(row=5, column=2, sticky='we')


####################################################################################################################################################################
#positions the game screen in the middle of the screen when it opens
####################################################################################################################################################################
start_win.update()
window_width = start_win.winfo_width()
window_height = start_win.winfo_height()
screen_width = start_win.winfo_screenwidth()
screen_height = start_win.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
start_win.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Shows the window until the user closes it
start_win.mainloop()





