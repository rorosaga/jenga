from generateTower import *

class JengaGame:
    def __init__(self, tower_height):
        self.tower = JengaTower(tower_height)
        # EVERY LAYER VALUE STARTS AT 0

        # when initializing game, populate layers with 1s to indicate presence of pieces
        for layer in self.tower.layers:
            for piece in layer.pieces:
                piece.val = 1

                # piece.left = 1
                # piece.middle = 1
                # piece.right = 1

    def calculateProbability(self, block):
        # Placeholder for probability calculation
        return 0.5

    def checkStability(self):
        # base case: 1. only left or right piece left in layer
        # base case: 2. no piece left in a layer
        self.currentSum = 0
        
        return True

    def addPiece(self, position):
        
        # Add a piece to the top of the tower
        # Has to check which spots are empty in the top layer before adding a new layer
        # Get the last layer
        last_layer = self.tower.layers[-1]

        # Check if the last layer is full
        if all(piece.val == 1 for piece in last_layer.pieces):
            # If the last layer is full, create a new layer with zeros
            new_layer = JengaLayer(orientation="horizontal" if len(self.tower.layers) % 2 == 0 else "vertical")

            # Add the new layer to the tower
            self.tower.layers.append(new_layer)
            last_layer = new_layer

        position = position.upper()
        if position == 'A':
            position_index = 0
        elif position == 'B':
            position_index = 1
        elif position == 'C':
            position_index = 2

        # Check if the specified place has already a piece (val is 1)
        if last_layer.pieces[position_index].val == 1:
            print("Invalid move! There's a piece already in that position. Choose a different place.")
            self.addPiece(input("Enter the position to add the piece you just removed (A/B/C): "))
            return
        
        # Set the value of the position to 1
        last_layer.pieces[position_index].val = 1


    def removePiece(self, move):

        layer, piece = move[:-1], move[-1]

        piece = piece.upper()
        if piece == 'A':
            piece_index = 0
        elif piece == 'B':
            piece_index = 1
        elif piece == 'C':
            piece_index = 2

        # Remove a piece from the tower
        layer_index = int(layer) - 1

        # Check if the specified piece is already removed (val is 0)
        if self.tower.layers[layer_index].pieces[piece_index].val == 0:
            print("Invalid move! The chosen piece has already been removed. Choose a different piece.")
            self.removePiece(input("Enter the layer and piece you want to remove (e.g., 2A): "))
            return
        
        # Set the value of the specified piece to 0
        self.tower.layers[layer_index].pieces[piece_index].val = 0

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

    # Printing of layers is reversed so first layer is at the bottom
    for layer in reversed(game.tower.layers):
        print(layer)

    while not game_over:

        # Player makes a move removing piece
        move = input("Enter the layer and piece you want to remove (e.g., 2A): ")

        game.removePiece(move)

        # Print tower
        for layer in reversed(game.tower.layers):
            print(layer)


        # Check tower stability
        if not game.checkStability():
            print("Tower falls. Game over!")
            game_over = True


        # Ask the user for the position to add the piece
        position = input("Enter the position to add the piece you just removed (A/B/C): ")

        # Add the piece to the tower at the specified position
        game.addPiece(position)

        # Print tower
        for layer in reversed(game.tower.layers):
            print(layer)

        if not game.checkStability():
            print("Tower falls. Game over!")
            game_over = True
    
    # Print Player leaderboard (maybe)

# Start the game
game_loop()