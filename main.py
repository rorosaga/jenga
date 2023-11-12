import pygame
import random
import numpy as np



"""
            Algorithms & Data Structures Group Project! 
        This is a virtual version of the famous game of Jenga
        
    Total data structures used: 
        1. Linked Lists
        2. Matrices
        
    Total algorithms used:
        1. Algo to generate the probability each cell has of falling, according to its position on the tower
        3. Algo to check if the tower will fall after each move
        2. Algo to add new elements to the top
        
    Features of our game:
        - Backtracking: you will be able to go back after each move if you don't feel you removed the right piece
        - Probabilistic piece removal: to account for skill in real life, we will be using a probabilistic model to
                                       simulate what pieces would be harder to take out in a real game of jenga
        - Matrix Indexing: after each move, we need to access the top-most index to add the new piece
"""

TOTAL_PIECES = 54
TOWER_HEIGHT = 18
TOWER_WIDTH = 3
MAX_HEIGHT = 48

# data structure no.1 -> Linked List
# We will be using a linked list to keep track of all the moves the user makes in a game
# This will be used to  be able to backtrack in the game if you feel you didn't like your move
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        

# data structure no.2 -> Matrix
# We will use a 2D matrix to represent our jenga game, each row will represent a possible level in jenga
# We will initialize our array with the theoretical maximum height of a jenga game
# We are doing this so we don't run out of space later on when we use the extra heights

# this line creates an array for our jenga game with the amount of possible moves represented by the 
# max height * 3, and the transforms it into a 2D array with 48 rows and 3 columns
game_matrix = np.zeros(MAX_HEIGHT*3, dtype=int).reshape((MAX_HEIGHT, 3))
print(game_matrix.shape)


def initialize_tower(height):
    tower = []
    for _ in range(height):
        block = "|   |"
        tower.append(block)
    return tower

def print_tower(tower):
    for block in tower:
        print(block)
    print("-" * 25)

def is_tower_empty(tower):
    return len(tower) == 0

def remove_block(tower):
    if not is_tower_empty(tower):
        removed_block = tower.pop()
        print(f"Removed block: {removed_block}")
    else:
        print("Tower is already empty!")

def add_block(tower):
    new_block = "|   |"
    tower.append(new_block)
    print(f"Added block: {new_block}")

def is_jenga(tower):
    return len(set(tower)) == 1

def play_jenga():
    tower_height = int(input("Enter the height of the Jenga tower: "))
    jenga_tower = initialize_tower(tower_height)

    while not is_tower_empty(jenga_tower):
        print_tower(jenga_tower)
        action = input("Do you want to remove a block (r) or add a block (a)? ").lower()

        if action == 'r':
            remove_block(jenga_tower)
        elif action == 'a':
            add_block(jenga_tower)
        else:
            print("Invalid action. Please enter 'r' to remove or 'a' to add.")

        if is_jenga(jenga_tower):
            print("Congratulations! You've successfully built a Jenga tower!")
            break

    if is_tower_empty(jenga_tower):
        print("Tower is empty. Game over!")


if __name__ == "__main__":
    play_jenga()
