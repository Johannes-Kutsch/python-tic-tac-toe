# Program Design
In programming, we want to go from an idea (an informal thought) to code (a precise formal language). Conducting this process is what programming really is about, writing the commands is only the last bit.
For a small program, writing code might be sufficient. In a large one, we need tools that support us. Here, we will call them __artifacts__.
We can distinguish three types of artifacts:
+ __Idea__ - tools that help us to write down the idea and communicate it with non-programmers and programmers
+ __Design__ - formalize the idea but keep it independent of the technology (e.g. languages or libraries)
+ __Coding Strategies__ – things that directly result in code


### Class Diagram

Diagram focusing on Data Structure. Shows all classes, their attributes, methods and relations. Might also include modules in Python. Agnostic of behavior and programming language. In databases, the Entity-Relationship-diagram fulfills a similar purpose.

### Data Flow Diagram

Like a flow chart but more focusing on where the data goes. Useful to describe a pipeline-like architecture


### Flowchart

Drawing containing fine-grained sequence of steps including branches and loops. Helps to discuss algorithms and processes but is agnostic of program structure, data structure and programming language.

### Prototype

Quick & dirty implementation that is done as a proof of concept before a more costly real implementation. Used to prove a design and hereby reduce risk.
Example questions a prototype could answer include (1 or 2 per prototype):

### Pseudocode

Semi-formal description of an alogrithm or process that helps to guide the implementation. More detailed than many other design tools, because it may mention variables and what happens to them. Focus on behavior but agnostic of program structure and programming language. For more information read the file [Intro_to_pseudocode.md](Intro_to_pseudocode.md)
Example Pseudocode:

1. Ask the player to make a move
2. If the square is already occupied go to step 1
3. If win end the game
4. If draw end the game
5. Switch player
6. Repeat to step 1

###  Requirements Document

Detailed description of what the users need (User Requirements), what is to be done technically (System Requirements), and what constraints need to be taken into account (Nonfunctional Requirements, e.g. programming language, speed, OS).
Requirements are often developed before the design. In a large project, developing Requirements may take months and result in hundreds of written pages. From a Requirements Doc GitHub issues can be generated.
Example Requirements for Tic-Tac-Toe
1. __User Requirement__
  + 1.1 As a user, I want a clear  game interface that visually represents the Tic-Tac-Toe grid.
  + 1.2 I should be able to make moves by selecting a row and column on the grid.
  + 1.3 I should receive immediate feedback on the success or failure of my move.
  + 1.4 I should be notified when I win the game.
  + 1.5 I should be notified when the game ends in a tie.
2. __System Requirements__
  + 2.1 The Tic-Tac-Toe grid should be implemented as a nested list
  + 2.2 A player  should be implemented with X or O

3. __Nonfunctional Requirements__
  + 3.1 Implementation is to be done in Python
  + 3.2 The program should run on a machine with at least 2 GB
  + 3.3 The program should run on all OS


### Skeleton Code

Writing a program with classes and functions, but leaving all the function bodies empty:

```python
def print_board():
  pass

def check_win():
  pass

...

```
Skeleton code helps to assess the initial program structure and find out whether it is feasible, ignoring details of the implementation. Ideally, skeleton code can already be executed

### User Story

Short description of a feature from a users point of view. User Stories are very common in Agile processes. A User Story needs to fit on an A6 card:

_As a player, I want to be able to enjoy a game of Tic-Tac-Toe against another player. I want the game to be easy to understand and provide clear instructions for making moves. After each move, I expect to see the updated game board, and I would like to be notified if I win, lose, or if the game ends in a tie._
