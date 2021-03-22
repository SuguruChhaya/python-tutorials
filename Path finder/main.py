import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
#Based on color, we can tell whether they are starting point, ending point, obstacle etc. 

#Visualization tool
class Spot:
    #*Represent the visualization of each block. 
    
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        #*Probably because it is a square so height=width
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        #*Tells whether we have already considered this spot or no. 
        #*probably to divide tasks accordingly (since this class only deals with visuals)
        # claffication is just based on color. 
        return self.color == RED

    def is_open(self):
        #*Asking whether the Spot is in the open set or no. 
        return self.color == GREEN                          

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    #*While all the above methods check whether a certain color, need methods to actually change to certain colors. 

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE          
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    #What happens when I compare 2 spots? Kind of confusing. 
    def __lt__(self, other):
        return False

#*Heuristic formula 
def h(p1, p2):
    #*Manhattan distance is whatever the quickest L is (not diagonal and stuff)
    #Used to give estimate. 
    x1, y1 = p1
    #A tuple or something will be passed.
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

#List holds all sports. 

def make_grid(rows, width):
    grid = []
    #*Width is the width of the entire grid. 
    gap = width // rows
    #*Because square so same number of rows as columns
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            #*Or could make temp list and append at the end. 
            grid[i].append(spot)

    return grid

#*Need to draw the grid lines. 