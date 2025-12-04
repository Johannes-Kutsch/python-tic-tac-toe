# Coding Challenge - Tic-Tac-Toe

Today we're going to test and improve our coding skills by creating a simple game of Tic-Tac-Toe in Python. 

## Set up your Environment

Fork this repository, clone it on your machine and create a new environment inside the folder. Don't forget to activate it for the assignment. 

### **`macOS`** type the following commands : 


- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    ```
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    ```

    For `Git-Bash` CLI :
    ```
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    ```

    **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:

    ```Bash
    python.exe -m pip install --upgrade pip
    ```
    

## Task

Write your own Tic-Tac-Toe game. The assignment file contains a description on how the game should work. It may also help you to create a good structure for your code. 

Before you start, have a look at the files [program_design.md](program_design.md) and  [Intro_to_pseudocode.md](Intro_to_pseudocode.md). The techniques described there could be useful for this task. 

## Minimal coding practices to keep in mind!

- Functions should have explicit names.
- Functions should have docstrings explaining how to call them
- Functions should be between 4-10 lines of code long

## Hints

In the ```tic_tac_toe.py``` file you will find the special if-statement ```if __name__ == '__main__':``` if you want to know more about it have a look into the [Example folder](Examples).

