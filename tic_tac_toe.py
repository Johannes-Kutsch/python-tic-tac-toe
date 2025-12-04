# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
def blabla():
    pass

def draw_board(board_data):
    """
    Draws a 3x3 Tic-Tac-Toe board
    """
    print("\n Current Board\n")
    

    for row in board_data:
        print(" " + "-" * 11)  # Top border
        print(f'| {row[0]} | {row[1]} | {row[2]} |')  
    print(" " + "-" * 11)


def get_value(inp_string):
    if inp_string == 'o':
        return -1
    elif inp_string == 'x':
        return 1
    elif inp_string == ' ':
        return 0
    else:
        print("f'Invalid user input'")




def is_win(board_data):

    rows = range(3)
    cols = range(3)

    # Check rows
    for row in rows:
        rowscore = 0
        for col in cols:
            rowscore += get_value(board_data[row][col])
        
        #Check for 3 in row
        if abs(rowscore) == 3:
            print(f"Full row {row}")
            return True
        
    # check cols
    for col in cols:
        colscore = 0
        for row in rows:
            colscore += get_value(board_data[row][col])
        
        #Check for 3 in col
        if abs(colscore) == 3:
            print(f"Full column {col}")
            return True
    
    # check diagonals
    diag1_sum = get_value(board_data[0][0]) + get_value(board_data[1][1]) + get_value(board_data[2][2])
    diag2_sum = get_value(board_data[2][0]) + get_value(board_data[1][1]) + get_value(board_data[0][2])

    print(f'diga1 = {diag1_sum}')
    print(f'diga2 = {diag2_sum}')
    if abs(diag1_sum) == 3 or abs(diag2_sum) == 3 :
        print(f"Full diagonal")
        return True
            



# Tic-tac-toe game
if __name__ == "__main__":


    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")

    board_data = [
    ['o', 'o', 'o'], 
    ['o', 'o', 'o'], 
    ['o', ' ', 'x']]

    draw_board(board_data)
    print(is_win(board_data))







