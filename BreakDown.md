# 1. Introduction to The Program

My program is a maze generator that uses the Depth-First Search (DFS) algorithm to create a maze. The user is prompted to enter the dimensions of the maze, and the program generates the maze within those dimensions. The maze is displayed in the console using ASCII characters, and the user can choose to generate a new maze after the first one is displayed.

## Key Components of The Program:

- **Input Validation:** Ensures that the user inputs valid dimensions for the maze.
- **Maze Representation:** Uses ASCII characters to visually represent the maze.
- **Maze Generation with DFS:** Uses a recursive DFS algorithm to carve out paths in the maze.
- **Retry Mechanism:** Allows the user to generate another maze if they want to.

---

# 2. Line-by-Line Explanation

## Imports and Initial Setup

```python
import random
import time
import os
```

- random: This module is used to generate random numbers. In the program, it's used to randomly decide the direction in which the maze paths will be carved.
- time: This module provides time-related functions. Although not currently used in the code you provided, time.sleep() could be used to pause the program briefly, creating a delay effect.
- os: This module provides functions to interact with the operating system.

```
print("Please note that larger inputs may cause errors!")
```

- This line prints a warning to the user about potential errors with large maze sizes. It’s good practice to inform users of possible limitations. 

## Input Validation Function

```python
def get_valid_input(prompt, min_value, max_value, ending_digit):
    while True:
        try:
            value = int(input("\033[92m" + prompt + "\033[0m"))
            if min_value <= value <= max_value and str(value)[-1] == str(ending_digit):
                return value
            else:
                print(f"\033[91mPlease enter a value between {min_value} and {max_value} that ends in {ending_digit}.\033[0m")
        except (ValueError, TypeError):
            print("\033[91mInvalid input. Please enter a valid integer.\033[0m")
```

- Function Purpose: This function prompts the user to input a value, validates that the value is within a specified range (min_value to max_value), and checks that the value ends with a specific digit (ending_digit). 

Key Elements: 
- while True: Creates an infinite loop that continues until the user provides valid input. 

- try-except Block: Used to handle potential errors (like if the user inputs something that can't be converted to an integer). 

### Input Validation: 

- value = int(input(...)): Prompts the user for input and tries to convert it to an integer. 
- if min_value <= value <= max_value and str(value)[-1] == str(ending_digit):: Checks that the input value is within the specified range and ends with the specified digit. 
- return value: If the input is valid, the function returns the value. 
- Error Handling: If the input isn't valid (either it's not an integer, or it's out of range), an error message is printed, and the loop continues. 

## Prompting User for Maze Dimensions 
```python
MAZE_HEIGHT = get_valid_input("\033[92mEnter the maze height: \033[0m", 10, 100, 0) 
MAZE_WIDTH = get_valid_input("\033[92mEnter the maze width: \033[0m", 5, 95, 5)
```
- These lines prompt the user to enter the height and width of the maze. The height must be between 10 and 100 and must end in 0, while the width must be between 5 and 95 and must end in 5. 
- Escape Sequences (\033[92m, \033[0m): Used to change text color in the console. \033[92m sets the text to green, and \033[0m resets it back to the default color. 

## Welcome Text (Commented Out) 
```python
welcome_text = """ 
         WELCOME TO MAZELINER ! 
     < __________________________ > 
""" 
# print("\n\n", welcome_text,"\n\n") 
```
- This block contains a welcome message for the user. It’s currently commented out, but when enabled, it will print a stylized welcome message in the console.

## Maze Symbols and Colors 
```python
WALL = '|' # Regular Wall 
CORNER_L = '\u2572'  # Slanted Left Border 
CORNER_R = '\u2571'  # Slanted Right Border 
PATH = ' '  # Clear a Path 
START = "\033[91m▼\033[0m"  # Red Start Point 
END = "\033[92m★\033[0m"  # Green End Point 
BORDER = '\033[30m-\033[0m'  # Black Borders 
 
# Seekers (Colored) 
SEEKER_VERT =  "\033[92m▮\033[0m"  # Green Seeker Vertical 
SEEKER_HORI =  "\033[92m▬\033[0m"  # Green Seeker Horizontal 
 ```
ASCII Characters: The program uses various ASCII characters to represent different elements of the maze: 

- WALL: Represents walls inside the maze. 

- CORNER_L and CORNER_R: Represent slanted borders at the maze corners. 

- PATH: Represents an open path in the maze. 

- START and END: Represent the start and end points of the maze, respectively, with specific colors. 

- BORDER: Represents the borders around the maze. 

- SEEKER_VERT and SEEKER_HORI: Represent potential seeker characters (user-controlled or otherwise) in the maze. 

## Extended Maze Dimensions with Borders 
```python
EXTENDED_HEIGHT = MAZE_HEIGHT + 4 
EXTENDED_WIDTH = MAZE_WIDTH + 4 
```
- These lines define the dimensions of the extended maze, which includes an additional border around the actual maze. The height and width are increased by 4 to account for the top, bottom, left, and right borders. 

## Initializing the Extended Maze with Borders and Walls 
```python
extended_maze = [ 
    [BORDER if (x == 0 or x == EXTENDED_WIDTH - 1 or y == 0 or y == EXTENDED_HEIGHT - 1) else WALL 
     for x in range(EXTENDED_WIDTH)] 
        for y in range(EXTENDED_HEIGHT) 
] 
```
- extended_maze: A 2D list representing the maze with borders. 

- List Comprehension: 
The maze is initialized as a grid of characters. 
If a cell is on the border of the extended maze (first or last row/column), it is set to BORDER. 
Otherwise, the cell is set to WALL. 

## Initializing the Internal Maze 
```python
maze = [ 
    [WALL for _ in range(MAZE_WIDTH)] 
    for _ in range(MAZE_HEIGHT) 
] 
```
- Generates a 2D list representing the maze (without borders) originally filled with walls.

 ## Depth-First Search Algorithm (DFS) Implementation 
```python
def dfs(row, col): 
    maze[row][col] = PATH 
 
    # Randomly shuffle the directions 
    directions = ["up", "down", "left", "right"] 
    random.shuffle(directions) 
 
    for direction in directions: 
        if direction == "up" and row > 1 and maze[row - 2][col] == WALL: 
            maze[row - 1][col] = PATH 
            dfs(row - 2, col) 
        elif direction == "down" and row < MAZE_HEIGHT - 2 and maze[row + 2][col] == WALL: 
            maze[row + 1][col] = PATH 
            dfs(row + 2, col) 
        elif direction == "left" and col > 1 and maze[row][col - 2] == WALL: 
            maze[row][col - 1] = PATH 
            dfs(row, col - 2) 
        elif direction == "right" and col < MAZE_WIDTH - 2 and maze[row][col + 2] == WALL: 
            maze[row][col + 1] = PATH 
            dfs(row, col + 2) 
 ```
- This function is responsible for generating the maze by recursively carving out paths. 
- Base Case: 
maze[row][col] = PATH: The current cell is marked as a path (i.e., it is no longer a wall). 
Randomizing Directions: 
directions = ["up", "down", "left", "right"]: A list of possible directions in which to move. 
random.shuffle(directions): Shuffles the list to ensure that the maze is randomized. 
- Recursive Case: 
Directional Movement: 
For each direction (up, down, left, right), the algorithm checks if the move is valid (i.e., it doesn't go out of bounds, and the target cell is still a wall). 
If the move is valid, it carves out a path (sets the intermediate cell to PATH) and then recursively calls dfs() on the new cell. 
- Recursive Carving: This process continues, with the DFS algorithm exploring each direction until it can't move further. When all directions from a cell are exhausted, the recursion unwinds back to the previous cell, continuing to explore any remaining directions from there. 

## Carving the Initial Path 
```python
start_col = random.randrange(1, MAZE_WIDTH - 2, 2) 
maze[0][start_col] = START 
dfs(1, start_col) 
```
- start_col: Chooses a random column in the top row to start the maze. The randrange() function is used to pick a random odd number between 1 and MAZE_WIDTH - 2. 

- maze[0][start_col] = START: Sets the starting point of the maze at the top row in the selected column. 

- dfs(1, start_col): Begins the DFS maze generation from the cell below the starting point.

## Finding the Maze Endpoint 
```python
end_col = random.randrange(1, MAZE_WIDTH - 2, 2) 
maze[MAZE_HEIGHT - 1][end_col] = END 
```
- end_col: Chooses a random column in the bottom row for the maze endpoint. 

- maze[MAZE_HEIGHT - 1][end_col] = END: Sets the endpoint of the maze at the bottom row in the selected column.

## Placing the Maze Inside the Extended Maze 
```python
for row in range(MAZE_HEIGHT): 
    for col in range(MAZE_WIDTH): 
        extended_maze[row + 2][col + 2] = maze[row][col] 
```
## Replacing Corner Walls with Slanted Borders 
```python
extended_maze[1][1] = CORNER_R 
extended_maze[1][EXTENDED_WIDTH - 2] = CORNER_L 
extended_maze[EXTENDED_HEIGHT - 2][1] = CORNER_L 
extended_maze[EXTENDED_HEIGHT - 2][EXTENDED_WIDTH - 2] = CORNER_R 
```
## Printing the Extended Maze 
```python
for row in extended_maze: 
    print(' '.join(row)) 
```
- Displaying the Maze: This loop iterates through each row of the extended_maze and prints it. The join() method is used to concatenate the characters in each row into a single string, with spaces in between for better readability.

# Rerun Function
```python
def rerun():
    global MAZE_WIDTH, MAZE_HEIGHT

    while True:
        retry = input("Again?: { YES } | { NO } ").strip().capitalize()
        if retry == "Yes":
            # Get new maze dimensions
            MAZE_HEIGHT = get_valid_input("\033[92mEnter the maze height: \033[0m", 10, 100, 0)
            MAZE_WIDTH = get_valid_input("\033[92mEnter the maze width: \033[0m", 5, 95, 5)

            # Update the extended maze dimensions
            global EXTENDED_HEIGHT, EXTENDED_WIDTH
            EXTENDED_HEIGHT = MAZE_HEIGHT + 4
            EXTENDED_WIDTH = MAZE_WIDTH + 4

            # Rerun setup with new values
            setup()
        elif retry == "No":
            exitText = """
                THANK YOU FOR PLAYING MAZELINER !
                > __________________________ <
            """
            print(f"\n{exitText}\n")
            break #ends retry and program.
        else:
            print("\033[91mINVALID INPUT. \033[0m  PLEASE ENTER { YES } OR { NO }")

rerun()
```
- Purpose: This function allows the user to decide whether they want to generate another maze or exit the program. 
- while True Loop: Keeps the prompt going until the user provides a valid input (Yes or No). 
- Handling "Yes": 
If the user chooses "Yes", the program prompts for new maze dimensions and regenerates the maze. 
-generate_maze(): You would need a separate function like generate_maze() that wraps the maze generation logic. This would involve initializing the maze, running DFS, and embedding it in the extended maze (as done earlier). 
-Handling "No": 
If the user chooses "No", the program prints a goodbye message and exits the loop, effectively ending the program. 
-Error Handling: 
If the user inputs anything other than "Yes" or "No", the program prints an error message and prompts the user again.

# What is a Depth-First-Search Algorithm?
- Depth-First Search (DFS) is an algorithm used for traversing or searching tree or graph data structures. The algorithm starts at the root node (or an arbitrary node in the case of a graph) and explores as far as possible along each branch before backtracking.
## How DFS is Applied in The Maze Generator 
- Starting Point: 
DFS starts at the initial position (in this case, the start point of the maze). 
- Path Carving: 
DFS explores each possible direction (up, down, left, right) randomly. 
For each direction, DFS checks if the move is valid (i.e., it stays within bounds and moves to a wall). 
If the move is valid, DFS carves a path in that direction and recursively calls itself on the new position. 
-Backtracking: 
When DFS reaches a dead-end (i.e., no more valid moves like reaching the maze wall limit set by the user), it backtracks to the previous position and continues exploring any remaining directions. 
-Completion: 
DFS continues this process until all cells are visited, resulting in a complete maze. 
