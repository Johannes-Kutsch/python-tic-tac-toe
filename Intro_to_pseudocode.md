# Brief Introduction to Pseudocode

Imagine you have to write a program for a really complex task. How would you start?

Sitting down and starting to code might sound appealing, but in the end you will realize how easy it is to get lost in the process or get stuck in a dead end. There is less that is more frustrating than sitting in front of a pile of buggy code that just won't run. 

A helpful technique to avoid getting stuck in this trap, is writing **pseudocode**. Pseudocode, in computer science, is an informal high-level description of the single steps an algorithm has to carrie out to solve a specific task. Its structure resembles that of real code in that sense that it also uses structural conventions like indentation or keywords and mathematical operators you would also use when writing real code. Its main purpose, however, is to be easy readable and understandable for humans. Breaking a complex program down into smaller pieces and writing the single steps necessary to perform the tasks down in an easy to understand and also easy to write language, simplifies writing real code immensely. 

There is no strict set of standard notations for writing pseudocode and everyone will probably develop their own style of writing it. But there are some notations, which are widely recognized:

* **INPUT**: indicates a user will be inputting something
* **OUTPUT**: indicates that an output will appear on the screen
* **WHILE**: a loop (iteration that has a condition at the beginning)
* **FOR**: a counting loop (iteration)
* **REPEAT – UNTIL**: a loop (iteration) that has a condition at the end
* **IF – THEN – ELSE**: a decision (selection) in which a choice is made
* any instructions that occur inside a selection or iteration are usually indented


### Example 1

Goal: This program will allow the user to check whether the number is even or odd.

```
INPUT user inputs number
STORE user input in number variable

IF number is even THEN
	OUTPUT "I am even"

ELSE
    OUTPUT "I am odd"

```


### Example 2

Goal: This program will ask the user for the best subject they take. If it's "Computer Science" it will print "Of course it is!" otherwise "Try again!".

```
REPEAT
	OUTPUT 'What is the best subject you take?'
	INPUT user inputs the best subject they take
	STORE the user's input in the answer variable
	IF answer = 'Computer Science' THEN
		OUTPUT 'Of course it is!'
	ELSE
		OUTPUT 'Try again!'
UNTIL answer = 'Computer Science'
```




You will find a nice beginners guide on how to write proper pseudocode [here](https://blog.usejournal.com/how-to-write-pseudocode-a-beginners-guide-29956242698).