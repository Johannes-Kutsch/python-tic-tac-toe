def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.

    Parameters:
        board (list): A 2D list representing the Tic Tac Toe board.

    Returns:
        None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """
    Checks if a player has won the game.

    Parameters:
        board (list): A 2D list representing the Tic Tac Toe board.
        player (str): The player's marker ('X' or 'O') to check for a win.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check rows for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns for a win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """
    Checks if the Tic Tac Toe board is full.

    Parameters:
        board (list): A 2D list representing the Tic Tac Toe board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    # Check if any cell is empty
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def get_move(player_name):
    """
    Gets the player's move from the user.

    Parameters:
        player_name (str): The name of the current player.

    Returns:
        tuple: A tuple (row, column) representing the player's move.
    """
    while True:
        move = input(f"{player_name}, enter your move (row[1-3] col[1-3]): ")
        try:
            row, col = map(int, move.split())
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1
            else:
                print("Invalid input. Row and column must be between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter row and column as numbers.")

def play_game():
    """
    Main function to play the Tic Tac Toe game.

    Parameters:
        None

    Returns:
        None
    """
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Get player names and markers
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")

    player1_marker = input(f"{player1_name}, choose your marker (X or O): ").upper()
    while player1_marker not in ["X", "O"]:
        player1_marker = input("Invalid marker. Please choose X or O: ").upper()

    player2_marker = "X" if player1_marker == "O" else "O"

    players = {player1_marker: player1_name, player2_marker: player2_name}
    player_index = 0

    while True:
        print_board(board)
        current_player_marker = list(players.keys())[player_index]
        current_player_name = players[current_player_marker]

        print(f"{current_player_name}'s turn. Marker: {current_player_marker}")
        row, col = get_move(current_player_name)

        if board[row][col] == " ":
            board[row][col] = current_player_marker

            # Check if the current player wins
            if check_winner(board, current_player_marker):
                print_board(board)
                print(f"{current_player_name} wins!")
                break

            # Check if the board is full (draw)
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            player_index = 1 - player_index  # Switch to the other player for the next turn
        else:
            print("That spot is already taken. Try again.")

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    play_game()
