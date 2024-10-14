# Path Planning Algorithms

This project implements three path planning algorithms: **A\* (A-star)**, **Dijkstra**, and **Greedy Best-First Search (BFS)**, using **Pygame** for visualizing the algorithms. Each algorithm finds the shortest path from a start node to a goal node in a grid-based environment.

## Table of Contents
- [Introduction](#introduction)
- [A\* Algorithm](#a-algorithm)
  - [Explanation](#explanation-1)
  - [Time Complexity](#time-complexity)
  - [Formula](#formula)
- [Dijkstra's Algorithm](#dijkstras-algorithm)
  - [Explanation](#explanation-2)
  - [Time Complexity](#time-complexity-1)
  - [Formula](#formula-1)
- [Greedy Best-First Search](#greedy-best-first-search)
  - [Explanation](#explanation-3)
  - [Time Complexity](#time-complexity-2)
  - [Formula](#formula-2)
- [Installation and Running the Program](#installation-and-running-the-program)

## Introduction
Path planning algorithms are fundamental for navigating agents through complex environments. These algorithms aim to compute the shortest path between a start point and a goal point, avoiding obstacles. Here, we explore three different algorithms, each with its unique approach to finding the path.

## A* Algorithm

### Explanation
The **A\*** algorithm is one of the most efficient and widely used pathfinding algorithms. It combines the benefits of Dijkstra's algorithm and Greedy BFS by considering both the cost to reach a node and the estimated cost to the goal.

A\* uses a **heuristic function** to estimate the remaining distance from the current node to the goal. This heuristic helps prioritize exploring nodes that are likely to lead to the goal, making it more efficient than Dijkstra's algorithm, which explores all nodes equally.

A\* works by maintaining two key values for each node:
- **\( g(n) \)**: the actual cost to reach node \( n \) from the start.
- **\( h(n) \)**: the estimated cost to reach the goal from node \( n \) (heuristic).

The algorithm uses a priority queue to always explore the node with the lowest **\( f(n) \)** value, where:

\[
f(n) = g(n) + h(n)
\]

### Time Complexity
The time complexity of A\* depends on the heuristic function:
- In the worst case (when the heuristic is not very effective or too optimistic), the time complexity is **\( O(b^d) \)**, where \( b \) is the branching factor and \( d \) is the depth of the solution.
- In the best case (with an optimal heuristic), the time complexity can be reduced to **\( O(d) \)**.

### Formula
For A\*, the total cost function **\( f(n) \)** is calculated as:

\[
f(n) = g(n) + h(n)
\]

- **\( g(n) \)**: The cost to reach the node \( n \) from the start node.
- **\( h(n) \)**: The heuristic function that estimates the remaining distance from node \( n \) to the goal (commonly using Manhattan or Euclidean distance).

## Dijkstra's Algorithm

### Explanation
Dijkstra's algorithm is a classic shortest-path algorithm. It explores every possible path and guarantees finding the shortest path in a graph with non-negative edge weights.

Dijkstra's algorithm is similar to A\* but without the heuristic. It only considers the actual cost to reach a node, meaning it explores every possible node until it finds the goal. This makes it less efficient than A\*, especially in large search spaces.

The algorithm maintains a cost value for each node and iteratively selects the node with the lowest cost (smallest distance from the start) to expand.

### Time Complexity
Dijkstra's algorithm has a time complexity of **\( O(V + E \log V) \)**, where:
- \( V \) is the number of vertices (nodes).
- \( E \) is the number of edges in the graph.

### Formula
For Dijkstra's algorithm, the cost function **\( g(n) \)** is:

\[
g(n) = \text{distance from start to } n
\]

There is no heuristic function, so it evaluates each node based solely on the cost to reach it.

## Greedy Best-First Search

### Explanation
**Greedy Best-First Search** is a heuristic-based algorithm that always selects the node closest to the goal according to the heuristic function, without considering the actual cost to reach the node (i.e., it ignores the \( g(n) \) value used in A\*).

This algorithm can be faster than A\* or Dijkstra's because it prioritizes nodes based solely on their estimated distance to the goal. However, it does not guarantee finding the shortest path because it doesn't account for the cost already incurred to reach a node.

Greedy BFS uses only the **\( h(n) \)** value to select the next node to explore, where **\( h(n) \)** is the heuristic estimate of the cost from the current node to the goal.

### Time Complexity
The time complexity of Greedy BFS is **\( O(b^d) \)**, where:
- \( b \) is the branching factor (the number of nodes expanded at each step).
- \( d \) is the depth of the solution.

Because it doesn't necessarily explore all nodes in a balanced way, Greedy BFS can run faster than A\* but may result in a non-optimal path.

### Formula
For Greedy BFS, the evaluation function **\( h(n) \)** is used:

\[
h(n) = \text{heuristic estimate from } n \text{ to the goal}
\]

The heuristic can be chosen based on the environment:
- **Manhattan Distance** for grid-based environments:
  
\[
h(n) = |x_1 - x_2| + |y_1 - y_2|
\]

- **Euclidean Distance** for continuous environments:

\[
h(n) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
\]

## Installation and Running the Program
To run the path planning algorithms, follow these steps:

1. **Install Pygame**:
   Open your Bash terminal and run the following command to install Pygame:

   ```bash
   sudo apt install pygame

2. **Clone the GitHub Repository: Download the repository containing the code:**
   ```bash 
   git clone <repository_url>
   cd <repository_directory>

3. **Run the Code: Navigate to the directory containing the Python files and run your desired algorithm using:**
   ```bash
   python3 <name_of_the_file>.py

