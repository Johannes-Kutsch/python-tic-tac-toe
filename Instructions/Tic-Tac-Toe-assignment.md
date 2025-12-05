# Tic-Tac-Toe
​

## Introduction
​
Today you're going to be writing a program that does something cool! You're going to write a script that allows two people to play [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe)! This is a much more involved problem than any you've seen in this class so far. In general, you should be thinking about how to break up your solution into smaller parts before you start writing it. In addition, you should try to give all your functions meaningful names when you define them.

This assignment will give suggestions on how to write this program. Remember, though, that there's always more than one solution to any programming problem. So, if you want to do something that's not suggested by the assignment or structure your code differently, by all means give it a try! 

## Some words on debugging 

Within each of these steps, and frequently between them, you will likely need to do some debugging. One way to do this is by trying to play your game as you implement different parts of it. If something isn't working, you'll get an error message telling you why. In addition, Python will tell you where it ran into the error and give you the stack trace leading up to that line getting executed. Try reading these error messages and extracting the important information (in which line did the error occur, what kind of error was raised...) Understanding those messages is a necessary skill for a programmer to have, and one that can only be developed via practice. 

There are far too many programmers who can't debug on this fundamental level: reading an error message and thinking about/reading your code -> figuring out how that error could be produced -> fixing it -> starting over. You're not going to be one of those programmers. Debugging like this is also a great way to get very familiar with any language.
​

## Assignment

Before you start coding, think about the game. Your version of the game can have several degrees of complexity. If you are highly motivated and want to reach for the (tic-tac-toe-)stars, your game can allow two people to play tic-tac-toe, handle all possible exceptions and edge cases that might occur when receiving user input, take into account everything that might go wrong and have a solution for that and on top of that might also have a nice visual interface. But let's be honest. That shouldn't be our claim! It's your first coding challenge, so let's keep it simple:

+ Try to focus on writing a working Python script that allows two people to play tic-tac-toe against each other. 
+ You should be able to start the game by running the script in the command line. 
- Your first version of the game does not have to take into account everything that could go wrong. Like for example handling each possible exception when receiving user input (e.g. getting the input outside a specific range or in the wrong format) is not necessary. 
- The game does not have to look nice! Keep it simple. There is no need for a fancy visual interface :)  

The following suggestions on how to structure your code might help you. And don't forget to write some pseudocode before you start with the "proper" code. 


## Suggestions 

Instead of writing one big function that does everything, we will split the game into several, smaller functions, each for a specific task. This makes it easier to write and debug your code.  

### Step 1: Getting started
Let's start with the main structure, which will start your game when you run the script name in the command line. If you have a look into the [tic_tac_toe.py](tic_tac_toe.py) file you will see that the first line is already there.  Inside this structure you can call all the other functions to perform their tasks. 

Since a game of Tic-tac-toe is basically repeating the same tasks over and over again (like asking the players for input) a `while True` loop can help you to get the game running. You have to make sure, however, that in case of certain events (win, draw,...) the loop will break so that the game will come to an end.  Another challenge to think about is how to allow each player to take turns at making their moves. Here the modulo operator could be helpful...

### Step 2: Display the board 
To play a round of tic-tac-toe, we need a game board. We should start by defining a function that will display the board on the screen when it is called. There are several ways to display a tic-tac-toe board. Choose the implementation that you can work best with as we proceed.

Maybe like this...  
1, 2, 3    
4, 5, 6   
7, 8, 9   

or this...   
(0, 0), (1, 0), (2, 0)   
(0, 1), (1, 1), (2, 1)   
(0, 2), (1, 2), (2, 2)   


### Step 3: Choose a symbol  
Before we can start playing it would be nice if the first player can choose whether to play with "X" or "O"! Player two must then choose the other. 


### Step 4: Ask for player input 
Now you need a function that asks the player (whose turn it is) where he wants to put his marker. The built-in function `input()` will do this task for you. 
If you want, you can directly add a control mechanism that checks if the desired position was already occupied in a previous turn. 

### Step 5: Check for Winner
At the end of each turn, your script will have to determine if the most recent play resulted in a win. If it did, it should break the game loop, the player that just played will be declared the winner, the game will be over, and the script will terminate. If a winner is not found, play will continue. Keep in mind that there are 8 different ways for a player to get three in a row. The function you write to solve this part of the problem will have to implement a lot of logic. Hint: One way to potentially make this part less code-intensive is by using the built-in function `all()`.

### Step 6: Check for Draw
There is a distinct chance that a draw will occur in the game. If this happens, your script should be aware. If all of the squares have been filled in, and there is no winner, it should break the game loop and a draw should be declared. 

## If you want to take it further...

Nice! At this point you should have a running Python script which let's two people play Tic-tac-toe against each other. If you have time and are still motivated, you can take it to the next level. 

No matter how you implemented your game, you never know how users of your script will interact with it. What happens if they enter a square that is off the grid, outside the range of the board? What about if they don't enter properly formatted input? What if they try to play in a square that has already been played in? Can you make your script robust to these possibilities? Try to continually break your solution. It's both fun and can reveal bugs that you hadn't thought of before.

A nice add-on would also be, if you could play the game several times without having to start it from the command line every time. Why not modify the game so that it offers you another round after finishing the first. 

Last but not least, you could work on making what is printed to the screen prettier or you could just relax and play a game of Tic-tac-toe. You've earned it!
