from generateTower import *

class JengaGame:
    def __init__(self, tower_height):
        self.tower = JengaTower(tower_height)
        # EVERY LAYER VALUE STARTS AT 0

        # when initializing game, populate layers with 1s to indicate presence of pieces
        for layer in self.tower.layers:
            for piece in layer.pieces:
                piece.left = 1
                piece.middle = 1
                piece.right = 1

    def calculateProbability(self, block):
        # Placeholder for probability calculation
        return 0.5

    def checkStability(self):
        # base case: 1. only left or right piece left in layer
        # base case: 2. no piece left in a layer
        self.currentSum = 0
        
        return True

    def addPiece(self, piece):
        
        # Add a piece to the top of the tower
        # Has to check which spots are empty in the top layer before adding a new layer

        self.layers.append(JengaLayer())

    def removePiece(self, layer, piece):
        # Remove a piece from the tower
        
        pass

    def backtracking(self):
        # Undo the last move
        # Returns game_over = True, just in case player wants to backtrack after game over
        # uses a stack or linked list to keep track of moves
        # maybe, can add a limit to undo moves in game loop
        pass

# Game loop
def game_loop():
    game = JengaGame(3)
    game_over = False

    for layer in game.tower.layers:
        print(layer)

    while not game_over:
        # Player makes a move
        move = input("Enter the layer and piece you want to remove (e.g., 2A): ")

        layer, piece = move[:-1], move[-1]

        game.removePiece(layer, piece)

        # Check tower stability
        if not game.checkStability():
            print("Tower falls. Game over!")
            game_over = True

        # Ask the user for the position to add the piece
        position = input("Enter the position to add the piece (A/B/C): ")

        # Add the piece to the tower at the specified position
        game.addPieceToTop(position)

        if not game.checkStability():
            print("Tower falls. Game over!")
            game_over = True

# Start the game
game_loop()

# # Example print:
# height = 10
# tower = JengaTower(height)

# for layer in tower.layers:
#     print(layer)
