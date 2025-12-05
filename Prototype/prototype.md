# TicTacToe Prototype

This document shows the visual and interaction design of the TicTacToe game before implementation.  
It includes the game board layout, user interaction examples, and a design diagram exported from Miro.  


---

##  Miro Design Diagram

Below is the visual flow/design created in Miro:

![Miro Prototype](images/miro_design.png)



---

## ### Initial Board (Empty Grid)

```
  ------------
 |   |   |   |
  ------------
 |   |   |   |
  ------------
 |   |   |   |
  ------------
```


---

## ### User Interaction Example

```
Player X, enter row and column: 0 2
```


---

## ### Updated Board After Move

```
  ------------
 |   |   | X |
  ------------
 |   |   |   |
  ------------
 |   |   |   |
  ------------
```


---

## ### Another Move Example

```
Player O, enter row and column: 1 1
```

```
  ------------
 |   |   | X |
  ------------
 |   | O |   |
  ------------
 |   |   |   |
  ------------
```


---

## ### Invalid Move Example

```
Player X, enter row and column: 0 2
This position is already taken! Please try again.
```


---

## ### Winning Scenario Example

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


---

## ### Tie Scenario Example

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

---

# End of Prototype
