
#3/18/23
#a Fifteen class with various methods for initializing the game, shuffling the tiles, updating the board, checking for valid moves, and checking if the game is solved. 


import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size=4):
        self.size = size # size of the game
        self.tiles = np.array([i for i in range(1, size**2)] + [0]) # create an array of numbers from 1 to size**2 - 1 and add 0 at the end
        self.board = [i for i in range(1, 16)]
        self.board.append(0)
        #initializes the adj dictionary, which contains the adjacent tiles for each tile.
        self.adj = {
            0: [1, 4],
            1: [0, 2, 5],
            2: [1, 3, 6],
            3: [2, 7],
            4: [0, 5, 8],
            5: [1, 4, 6, 9],
            6: [2, 5, 7, 10],
            7: [3, 6, 11],
            8: [4, 9, 12],
            9: [5, 8, 10, 13],
            10: [6, 9, 11, 14],
            11: [7, 10, 15],
            12: [8, 13],
            13: [9, 12, 14],
            14: [10, 13, 15],
            15: [11, 14]
        }
    
        
    def update(self, move):
        """
        This function updates the position of the tile with the given move, if it's a valid move.
        """
        if self.is_valid_move(move):
            index = np.where(self.tiles == move)[0][0] # get the index of the move in the tiles array
            blank_index = np.where(self.tiles == 0)[0][0] # get the index of the blank tile in the tiles array
            self.tiles[index], self.tiles[blank_index] = self.tiles[blank_index], self.tiles[index] # swap the tiles
    
    def transpose(self, i, j):
        """
        This function transposes the tiles array using the given indices.
        """
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i] # swap the tiles
        
    def shuffle(self, steps=100):
        """
        This function shuffles the tiles array by making random moves for the specified number of steps.
        """
        # get the index of the blank tile
        index = np.where(self.tiles == 0)[0][0]
        
        # define the adjacent tiles for each index
        self.adj = {}
        for i in range(self.size**2):
            adj = []
            if i % self.size > 0: # left
                adj.append(i - 1)
            if i % self.size < self.size - 1: # right
                adj.append(i + 1)
            if i // self.size > 0: # up
                adj.append(i - self.size)
            if i // self.size < self.size - 1: # down
                adj.append(i + self.size)
            self.adj[i] = adj
        
        # make random moves for the specified number of steps
        for i in range(steps):
            move_index = choice(self.adj[index]) # choose a random adjacent tile
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index] # swap the tiles
            index = move_index # update the index of the blank tile
        
    def is_valid_move(self, move):
        """
        This function checks if the given move is a valid move, i.e. if the tile with the given move is adjacent to the blank tile.
        """
        index = np.where(self.tiles == move)[0][0] # get the index of the move in the tiles array
        blank_index = np.where(self.tiles == 0)[0][0] # get the index of the blank tile in the tiles array
        if index in self.adj[blank_index]: # check if the move is adjacent to the blank tile
            return True
        else:
            return False
        
    def is_solved(self): #checks if the given move is a valid move
        #if the tile with the given move is adjacent to the blank tile.
        for i in range(0, len(self.tiles)):
            if i+1 != self.tiles[i] and i != len(self.tiles)-1:
                return False
        return True


        
    def draw(self): #draw the board 
        print("+---+---+---+---+")
        for i in range(0, 16, 4):
            print("|", end="")
            for j in range(i, i+4):
                if self.tiles[j] == 0:
                    print("   ", end="|")
                else:
                    print("{:^3d}".format(self.tiles[j]), end="|")
            print("\n+---+---+---+---+")


    def __str__(self): #returns a string representation of the board.
        res = ''
        for i in range(4):
            res += ' '.join([f'{x:2d}' if x > 0 else '  ' for x in self.tiles[i*4:(i+1)*4]])
            res += ' \n'
        return res


if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
  
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    
    
    
         
    
        
