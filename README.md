# Path Planning Algorithms: A*, Dijkstra, and Greedy Best-First Search (BFS)

## Project Overview

This project implements three classical path planning algorithms—A*, Dijkstra, and Greedy Best-First Search (BFS)—used in robot navigation and AI for finding the shortest path between two points in a grid-based environment. Each of these algorithms has its own strengths and weaknesses in terms of efficiency, optimality, and real-world application.

The project includes Python implementations of these algorithms, simulations of their performance, and visualizations of their pathfinding process. You can experiment with each algorithm to understand their differences and use them in real-world robotic applications.

## Table of Contents

- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [A* Algorithm](#1-a-algorithm)
  - [Dijkstra's Algorithm](#2-dijkstras-algorithm)
  - [Greedy Best-First Search](#3-greedy-best-first-search)
- [Installation](#installation)
- [Usage](#usage)
- [Simulations](#simulations)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In the context of robotics and AI, path planning refers to the process of finding a viable route from a start position to a goal position, avoiding obstacles along the way. This project showcases three fundamental path planning algorithms—A*, Dijkstra, and Greedy BFS—each with different approaches to searching for optimal or near-optimal paths.

- **A***: Widely used due to its balance of optimality and efficiency.
- **Dijkstra**: Guarantees the shortest path but may take longer due to exploring all possible nodes.
- **Greedy BFS**: Focuses on speed, often finding suboptimal solutions quickly.

## Algorithms

### 1. A* Algorithm

The A* algorithm is a search algorithm that finds the shortest path between two points using a heuristic. It combines the advantages of Dijkstra's algorithm and Greedy BFS by considering both the actual cost to reach a node and an estimate of the remaining distance to the goal. This combination makes A* one of the most efficient pathfinding algorithms, providing optimal paths while avoiding unnecessary exploration.

- **Heuristic Function (h)**: Typically the Euclidean distance or Manhattan distance between the current node and the goal.
- **Cost Function (g)**: The actual cost to reach a node from the start.
- **Total Cost (f)**: The sum of both g and h (i.e., f(n) = g(n) + h(n)).

A* guarantees the shortest path as long as the heuristic is admissible (it never overestimates the distance to the goal).

**Time Complexity**: O(b^d), where b is the branching factor and d is the depth of the shortest path.

### 2. Dijkstra's Algorithm

Dijkstra's Algorithm is one of the most famous algorithms for finding the shortest path in a graph. It works by expanding nodes in all directions, giving priority to the nodes with the lowest accumulated cost. Unlike A*, Dijkstra’s algorithm doesn’t use a heuristic function, which means it explores a larger portion of the graph compared to A*, especially in cases where the goal is far from the starting point.

- **Cost Function (g)**: Dijkstra relies solely on the cost to reach a node from the start, ensuring it explores every node at least once with the least possible cost.

Since Dijkstra explores all possible paths, it guarantees finding the shortest path but is not very efficient in large search spaces where heuristic guidance could narrow down the search.

**Time Complexity**: O(V^2) for an unoptimized version, where V is the number of vertices (can be reduced to O(V + E log V) using a priority queue).

### 3. Greedy Best-First Search (BFS)

The Greedy Best-First Search algorithm is a faster but less optimal alternative to A*. It focuses entirely on minimizing the estimated distance to the goal, without considering the cost to reach the current node. This greedy approach makes it faster but can often lead to non-optimal paths, especially in complex environments with many obstacles.

- **Heuristic Function (h)**: Similar to A*, this algorithm uses the Euclidean or Manhattan distance to estimate the distance to the goal, but it doesn’t account for the actual cost g(n) of reaching a node.
- **Total Cost (f)**: Only the heuristic is considered (i.e., f(n) = h(n)).

This makes Greedy BFS much faster than Dijkstra and A*, but it does not guarantee the shortest path.

**Time Complexity**: O(b^m), where b is the branching factor and m is the maximum depth of the search space.

## Algorithm Comparison

| Algorithm         | Time Complexity       | Optimality                  | Heuristic | Description                                 |
|-------------------|-----------------------|-----------------------------|-----------|---------------------------------------------|
| A*                | O(b^d)                | Optimal (with admissible heuristic) | Yes       | Balances exploration and goal-reaching      |
| Dijkstra          | O(V^2) or O(V + E log V) | Optimal                    | No        | Explores all paths to guarantee shortest path |
| Greedy Best-First | O(b^m)                | Suboptimal                  | Yes       | Quick but not necessarily optimal           |

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/path-planning-algorithms.git
cd path-planning-algorithms
