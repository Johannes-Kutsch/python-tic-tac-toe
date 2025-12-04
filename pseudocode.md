## Pseudocode for python tic tac toe

#### General ideas:

- Player 1 called "x" plays first and uses x (always) 
- Player 2 called "o" plays first and uses o (always)
- The Board will represented by a list called board.
- The indices of the list will belong to the boardfields as shown below (this is just one way of doing it: we could use a dictionary instead, or nested lists, or many other option)
- In the lest, "" means not played, "x", means an x, "O" means an 0

```
#Game board / indices 
0 | 1 | 2
3 | 4 | 5
6 | 7 | 8
```

For example this board
```
#Example board
   |   | 
   | o | 
 x | o | x
``` 
would be represented as
board=["","","","","o","","x","o","x"]


#### Game logic
----
```
CALL explain_rules()
VAR current_turn="X"
VAR play_more=TRUE

#Loop over several rounds
LOOP (while play_more==TRUE):
    VAR board = CALL create_new_board()
    CALL show_board(board)
    
    #Loop over moves in game
    LOOP (while check_for_game_end()==FALSE):
        OUTPUT "its {current_turn}'s turn"
        VAR next_move = get_next_move()
        UPDATE board = update_board(board,next_move,current_turn)
        CALL show_board(board)
        UPDATE current_turn=next_move(current_turn)
  
    VAR A,B = CALL check_for_game_end(board)
    if B=="X won": 
      OUTPUT (praise player 1)
      elif:B=="O won": 
        OUTPUT (praise player 2)
      elif:B=="Draw": 
        OUTPUT (praise noone)
    
    INPUT (Ask if the players want to continue playing) 
    if input ==yes:
        pass
    else play_more = False

DEF FUNCTION show_board(board):
  OUTPUT board:
      print(board[0],board[1],board[2])
      print(board[3],board[4],board[5])
      print(board[6],board[7],board[8])
      print(" ")

DEF FUNCTION create_new_board():
  VAR board=Empty List of 9
  return board

DEF FUNCTION get_next_move():
  OUTPUT (nice message to aks player for the next move)
  INPUT (next move)
  RETURN move

DEF FUNCTION update_board(board,move,player):
  (check if its a valid move (is field empty? is move between 0..9?))
  If Not valid move: ERROR or repeat
  
  UPDATE board (mark at position move, with player)
  RETURN board

DEF FUNCTION check_for_game_end(board):
  check_for_win()
  check_for_draw()

  return (A: true/false, B: if true: result else empty) 

DEF FUNCTION check_for_win():
  CHECK for the wins (one of 8: 2 diagonals, 3 rows, 3 columns)
  return true/false

DEF FUNCTION check_for_draw():
  IF still empty fields available: 
    RETURN FALSE
  RETURN TRUE

DEF FUNCTION next_move(current_move):
  IF current_move==x
    RETURN o
  IF current_moove==o
    RETURN x
  
DEF FUNCTION explain_rules():
  OUTPUT (hi.... intro... rules... howto play...)
    
```
