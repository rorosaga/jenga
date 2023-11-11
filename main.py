import pygame
import random

TOWER_HEIGHT = 20
TOWER_WIDTH = 3



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
