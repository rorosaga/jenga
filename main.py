# import pygame
import random
import numpy as np
# import vpython
from jenga import Jenga
from data_structures import Node, Stack, TreeNode

"""
            - Algorithms & Data Structures Group Project - 
        This is a virtual version of the famous game of Jenga
        
    Total data structures used:
        1. Linked List
        2. Stacks
        3. Matrices
    
    
    Total algorithms used:
        1. Algo to generate the probability each cell has of falling, according to its position on the tower
        2. Algo to check if the tower will fall after each move + update values of the probability
        3. Algo to add new elements to the top
        
    Features of our game:
        - Backtracking: you will be able to go back after each move if you don't feel you removed the right piece
        - Probabilistic piece removal: to account for skill in real life, we will be using a probabilistic model to
                                       simulate what pieces would be harder to take out in a real game of jenga
        - Matrix Indexing: after each move, we need to access the top-most index to add the new piece
        
    Explanation: In a Jenga game pieces are placed next to each other in blocks of three and on top of each other
                 at 90° angle forming a grid. In order to simulate this, we will have an empty 3D matrix with the
                 maximum theoretical height of a Jenga tower so that we can populate it after with ease. The 1st, 
                 2nd, and 3rd dimensions will represent the height of our jenga game, each piece in our game, and 
                 each component of every one piece, respectively. Since the pieces are placed on top of others at 
                 right angles, taking out a singular piece will affect the weight distributed of at least 3 other
                 pieces below. To account for this, each piece will be divided into 3 components: left, middle, and 
                 right, that we will use to distribute our weight. 
"""


def welcome_message():
    ...


def still_playing(game_matrix, gameover) -> bool:
    # checks if game conditions are still valid -> the tower is still up 
    
    ...
        

def main():
    welcome_message()
    
    game_matrix = Jenga() # fill the array with standard value - maybe a TreeNode
    
    gameover = False
        
    # variable to keep track of how many pieces you have taken out successfully
    piece_counter = 0
    
    # using nodes for the components can be good to know what values we will change
    # the node can have 3 children -> left, mid, right, component of the row below it
    
    still_playing(game_matrix, gameover) # should be passed every time update_weights is passed
    
    """
    while !gameover: 
        input = wait for input
                
        do action
        
        
        gameover = still_playing(game_matrix, gameover)
    """


"""
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

    if is_tower_empty(jenga_tower):
        print("Tower is empty. Game over!")

"""

