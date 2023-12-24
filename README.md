# Puzzle Fifteen

## Overview
This Python project focuses on representing the Puzzle Fifteen game as a graph and explores various graph implementation methods. The project provides a basic structure for the Puzzle Fifteen game without a graphical user interface (GUI).

## Puzzle Fifteen Game
The Puzzle Fifteen game is modeled as a graph with sixteen vertices, including corner, edge, and central vertices. Each vertex is connected to a specific number of neighbors, creating a graph representation of the game board.

## Modules

### `graph.py`
The `graph.py` module provides the Abstract Data Type (ADT) for the graph with the following classes:
- `Vertex`: Represents a vertex in the graph.
- `Graph`: Represents the graph itself.

To check the correctness of your graph implementation, run the driver code in the template file `graph.py` located under `Files/Programming Assignments/PA5` on Canvas.

### `fifteen.py`
The `fifteen.py` module provides the Abstract Data Type (ADT) for the Puzzle Fifteen game with the class `Fifteen`. It offers the necessary structure for the Puzzle Fifteen game without a GUI.

### `game.py`
The `game.py` module serves as the main program for the Puzzle Fifteen game. Please note that the GUI implementation is not available in this project.

## Usage
1. Explore the graph representation and adjacency list in the `graph.py` module.
2. Understand the Puzzle Fifteen game structure in the `fifteen.py` module.
3. Run the main program in `game.py` (without GUI) to interact with the Puzzle Fifteen game logic.

Feel free to extend and enhance the code as needed. Contributions and improvements are welcome.

## Side Notes 
### Vertex Connections
For example:
- Vertex 1 is connected to vertices 2 and 5.
- Vertex 2 is connected to vertices 1, 3, and 6.
- Vertex 6 is connected to vertices 2, 5, 7, and 10.

## Graph Implementation
The graph can be implemented using various methods, including parallel structures with arrays, lists, or classes such as `Vertex` and `Graph`. Different implementations are explored to represent the adjacency list and structure of the graph.

## Adjacency List
All vertices are represented as a list, and their adjacency list is a nested list indicating the connections between vertices.

