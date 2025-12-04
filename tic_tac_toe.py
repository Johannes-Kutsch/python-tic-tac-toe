# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def blabla():
    pass


# Function for... (choosing a player?)
def draw_board(board_data):
    """
    Draws a 3x3 Tic-Tac-Toe board
    """
    print("\n Current Board\n")
    

    for row in board_data:
        print(" " + "-" * 11)  # Top border
        print(f'| {row[0]} | {row[1]} | {row[2]} |')  
    print(" " + "-" * 11)  # Top border



def is_win(board_data):

    rows = range(3)
    cols = range(3)

    # Check rows
    for row in rows:
        rowscore = 0
        for col in cols:
            if board_data[row][col] == 'x':
                rowscore +=1
            elif board_data[row][col]== 'o':
                rowscore -=1
        if rowscore == abs(3):
            print(f"Full row {row}")
            return True
        
    # check cols
    for col in cols:
        colscore = 0
        for row in rows:
            if board_data[row][col] == 'x':
                colscore +=1
            elif board_data[row][col]== 'o':
                colscore -=1
        if colscore == abs(3):
            print(f"Full column {col}")
            return True
    
    # check diagonals
    #diag1_sum = board_data[0][0] + board_data[1][1] + board_data[2][2]
    #diag2_sum = board_data[2][0] + board_data[1][1] + board_data[2][2]
            



# Tic-tac-toe game
if __name__ == "__main__":


    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")

    board_data = [
    ['x', ' ', 'x'], 
    [' ', 'x', 'x'], 
    ['x', ' ', 'x']]

    draw_board(board_data)
    print(is_win(board_data))







