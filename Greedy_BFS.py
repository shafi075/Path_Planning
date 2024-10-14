import pygame
import math
from queue import PriorityQueue

pygame.init()

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Greedy Best-First Search Path Planning")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PALE_YELLOW = (255, 255, 153)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == BLUE

    def is_end(self):
        return self.color == YELLOW

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = BLUE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = YELLOW

    def make_path(self):
        self.color = GREEN

    def make_frontier(self):
        self.color = ORANGE

    def make_checked(self):
        self.color = PALE_YELLOW

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

# Heuristic function
def euclidean_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Greedy Best-First Search Algorithm
def greedy_bfs(draw, grid, start, goal):
    open_list = []
    closed_list = set()
    parents = {}
    h_costs = {}
    shortest_path = []

    start_pos = start.get_pos()
    goal_pos = goal.get_pos()
    start_cost = euclidean_distance(start_pos, goal_pos)
    h_costs[start] = start_cost
    open_list.append([start, start_cost])
    path_found = False

    while open_list:
        # Sort by heuristic cost
        open_list.sort(key=lambda x: x[1])
        current_node = open_list.pop(0)[0]

        # Mark current node as visited
        closed_list.add(current_node)
        current_node.make_checked()

        # If goal is reached, stop
        if current_node == goal:
            path_found = True
            break

        # Update neighbors
        for neighbor in current_node.neighbors:
            if neighbor in closed_list:
                continue

            h_cost = euclidean_distance(neighbor.get_pos(), goal_pos)

            if neighbor not in [n[0] for n in open_list]:
                parents[neighbor] = current_node
                h_costs[neighbor] = h_cost
                open_list.append([neighbor, h_cost])
                neighbor.make_frontier()

        draw()

        if current_node != start:
            current_node.make_closed()

    if not path_found:
        return False

    # Reconstruct path
    node = goal
    while node != start:
        shortest_path.append(node)
        node = parents[node]
        node.make_path()
        draw()

    return True

# Grid functions
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap

    return row, col

def reset_grid(grid, ROWS):
    for row in grid:
        for spot in row:
            spot.reset()
    return None, None 
    
def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    goal = None

    run = True
    while run:
        draw(win, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != goal:
                    start = spot
                    start.make_start()

                elif not goal and spot != start:
                    goal = spot
                    goal.make_end()

                elif spot != goal and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()

                if spot == start:
                    start = None
                elif spot == goal:
                    goal = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and goal:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    greedy_bfs(lambda: draw(win, grid, ROWS, width), grid, start, goal)

                    if event.key == pygame.K_c:
                        start = None
                        end = None
                        grid = make_grid(ROWS, width)

                if event.key == pygame.K_r:  # Reset the grid and start over
                    start, end = reset_grid(grid, ROWS)
                    grid = make_grid(ROWS, width)
    pygame.quit()

main(WIN, WIDTH)
