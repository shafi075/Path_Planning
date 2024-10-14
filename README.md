# Path Planning Algorithms: A*, Dijkstra, and Greedy Best-First Search (BFS)

This project implements three classic path planning algorithms — A*, Dijkstra, and Greedy Best-First Search (BFS) — in a simulated environment. These algorithms enable a robot to find the shortest path from a start point to a goal while navigating around obstacles.

## Algorithms Implemented

### 1. **A* Algorithm**
A* (A-Star) is a popular search algorithm that is used for pathfinding and graph traversal. It aims to find the shortest path between two points by minimizing the total cost of a path (sum of the path cost and a heuristic estimate of the remaining cost to the goal). It balances between breadth-first and depth-first strategies by incorporating both the distance already traveled (g-cost) and the estimated remaining distance (h-cost) to the goal.

### 2. **Dijkstra's Algorithm**
Dijkstra’s Algorithm is a well-known pathfinding algorithm that finds the shortest path between nodes in a graph. It does not use a heuristic function, and instead, it searches the entire graph systematically by visiting all nodes in increasing order of distance from the starting node, ensuring that the shortest path to any node is found.

### 3. **Greedy Best-First Search (BFS)**
Greedy Best-First Search focuses on expanding the node that appears to be closest to the goal, using only a heuristic function. This approach may not always find the shortest path but is efficient in certain cases. It is faster than A* but may lead to suboptimal paths since it does not account for the cost already traveled.

## Features

- **Path planning** using A*, Dijkstra, and Greedy BFS algorithms.
- **Visualized pathfinding** on a 2D grid or map.
- **Simulated environment** to test the effectiveness of each algorithm.
- **Obstacle avoidance**, ensuring the robot or agent navigates around barriers.

## Project Structure

- **astar.py**: Implementation of the A* algorithm.
- **dijkstra.py**: Implementation of Dijkstra's algorithm.
- **greedy_bfs.py**: Implementation of Greedy Best-First Search algorithm.
- **main.py**: Main script that runs the selected path planning algorithm in the simulation.
- **utils.py**: Utility functions such as grid creation, obstacle placement, and path visualization.

## Getting Started

### Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- `matplotlib` for visualization
- `numpy` for matrix operations

You can install the required packages using:

```bash
pip install matplotlib numpy
