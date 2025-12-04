# TicTacToe Prototype
### Initial Board (Empty TicTocToe Gird)


```
Initial Board (Empty Grid)

  ------------
 |   |   |   |
  ------------
 |   |   |   |
  ------------
 |   |   |   |
  ------------

```
###  Tic-Tac-Toe Grid Layout (How positions map)

```
Grid Positions (row, column)

  -------------------
 | (0,0) (0,1) (0,2) |
  -------------------
 | (1,0) (1,1) (1,2) |
  -------------------
 | (2,0) (2,1) (2,2) |
  -------------------

```


## User Interaction Example

```
Player X, enter row and column: 0 2

```

###  Board After Move

```
Board after Player X moves to (0,2)

  ------------
 |   |   | X |
  ------------
 |   |   |   |
  ------------
 |   |   |   |
  ------------
  
```
###  Another Move Example

```
  ------------
 |   |   | X |
  ------------
 |   | O |   |
  ------------
 |   |   |   |
  ------------

```

###  Invalid Move Example

```
Player X, enter row and column: 0 2
This position is already taken! Please try again.

```

###  Winning Scenario Example

```
  ------------
 | X | X | X |
  ------------
 | O |   | O |
  ------------
 |   |   |   |
  ------------

Player X wins!

```
###  Tie Scenario Example

```
  ------------
 | X | O | X |
  ------------
 | X | O | O |
  ------------
 | O | X | X |
  ------------

It's a tie!
```