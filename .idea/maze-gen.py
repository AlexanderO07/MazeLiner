'''
Created and Edited by: Alexander Onyiuke "https://github.com/AlexanderO07"
With Help From: "https://medium.com/geekculture/depth-first-search-dfs-algorithm-with-python-2809866cb358",
"https://gist.github.com/nazwadi/ca00352cd0d20b640efd",
"https://favtutor.com/blogs/depth-first-search-python"
'''

#START

import random
import time
import os

print("Please note that larger inputs may cause errors!")
min_value = 0
max_value = 0
# Function for input validation
def get_valid_input(prompt, min_value, max_value, ending_digit):
    while True:
        try:
            value = int(input("\033[92m" + prompt + "\033[0m"))
            if min_value <= value <= max_value and str(value)[-1] == str(ending_digit):
                return value
            else:
                print(f"\033[91mPlease enter a value between {min_value} and {max_value} that ends in {ending_digit}.\033[0m")
        except (ValueError, TypeError):
            print("\033[91mInvalid input. Please enter a valid integer with no decimals.\033[0m")

# Prompt the user to enter the maze height and width
MAZE_HEIGHT = get_valid_input("\033[92mEnter the maze height: \033[0m", 10, 100, 0)
MAZE_WIDTH = get_valid_input("\033[92mEnter the maze width: \033[0m", 5, 95, 5)

welcome_text = """
         WELCOME TO MAZELINER !
     < __________________________ >
"""

#Maze Generation Symbols (Colored using Bash)
WALL = '|' # Regular Wall
CORNER_L = '\u2572'  # Slanted Left Border
CORNER_R = '\u2571'  # Slanted Right Border
PATH = ' '  # Clear a Path
# PATH_COLOR = "\391847" #Color of path
START = "\033[91m▼\033[0m"  # Red Start Point
END = "\033[92m★\033[0m"  # Green End Point
BORDER = '\033[30m-\033[0m'  # Black Borders

# Seekers (Colored) NOT IMPLEMENTED
SEEKER_VERT =  "\033[92m▮\033[0m"  # Green Seeker Vertical
SEEKER_HORI =  "\033[92m▬\033[0m"  # Green Seeker Horizontal

#extended maze dimensions with borders
EXTENDED_HEIGHT = MAZE_HEIGHT + 4
EXTENDED_WIDTH = MAZE_WIDTH + 4

#initialize the extended maze with borders and walls to contain maze variable defined below
extended_maze = [
    [BORDER if (x == 0 or x == EXTENDED_WIDTH - 1 or y == 0 or y == EXTENDED_HEIGHT - 1) else WALL
     for x in range(EXTENDED_WIDTH)]
        for y in range(EXTENDED_HEIGHT)
]

#initialize the maze inside the extended maze with walls
maze = [
    [WALL for _ in range(MAZE_WIDTH)]
    for _ in range(MAZE_HEIGHT)]


#---- DFS FUNCTION (RECURSIVE)
def dfs(row, col):
    maze[row][col] = PATH

    #shuffle the directions (psuedo-randomness)
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

#---- SETUP FUNCTION
def setup():
    global maze, extended_maze

    # Re-initialize the maze and extended_maze to clear old data from previous responses
    maze = [[WALL for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]
    extended_maze = [
        [BORDER if (x == 0 or x == EXTENDED_WIDTH - 1 or y == 0 or y == EXTENDED_HEIGHT - 1) else WALL
         for x in range(EXTENDED_WIDTH)]
        for y in range(EXTENDED_HEIGHT)
    ]

    #generate start and end points with valid ranges
    start_col = random.randrange(1, MAZE_WIDTH - 2, 2)
    maze[0][start_col] = START
    dfs(1, start_col)

    end_col = random.randrange(1, MAZE_WIDTH - 2, 2)
    maze[MAZE_HEIGHT - 1][end_col] = END

    # Place the maze inside the extended maze
    for row in range(MAZE_HEIGHT):
        for col in range(MAZE_WIDTH):
            extended_maze[row + 2][col + 2] = maze[row][col]

    # Replace the corner walls with slanted variables
    extended_maze[1][1] = CORNER_R
    extended_maze[1][EXTENDED_WIDTH - 2] = CORNER_L
    extended_maze[EXTENDED_HEIGHT - 2][1] = CORNER_L
    extended_maze[EXTENDED_HEIGHT - 2][EXTENDED_WIDTH - 2] = CORNER_R

    # Print the extended maze with borders
    for row in extended_maze:
        print(' '.join(row))

#---- SETUP CALL
setup()

#---- RERUN FUNCTION
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

#---- RERUN CALL
rerun()

#END