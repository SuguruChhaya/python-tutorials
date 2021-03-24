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

    #!Uses a graph kind of thought method?
    def update_neighbors(self, grid):
        #*Determine all of the neighbors that aren't barriers. Save time. 
        #Check up down and left right. 
        self.neighbors = []
        #*total_rows is length_based while row is index based. 
        #*Down a row
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col])

        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_barrier():
            self.neighbors.append(grid[self.row][self.col+1])

        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbors.append(grid[self.row][self.col-1])

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

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end):
    #!Calls the draw function
    draw()

    count = 0
    #*First argument is f score: 0. 
    #*Second is count: 0 (when inserted in queue)
    #?Prevent looking at same f-score and look at inserted first?
    open_set = PriorityQueue()
    #*Start is the actual node. 
    open_set.put((0, count, start))
    #!Each dictionary keeps track of x-scores for every node. 
    came_from = {}
    g_score = {}
    for row in grid:
        for spot in row:
            g_score[spot] = float("inf")

    g_score[start] = 0

    
    f_score = {}
    for row in grid:
        for spot in row:
            f_score[spot] = float("inf")
    
    #Since g_score for start node is 0, f score (which is h score aka heuristic) just equals the h score. 
    f_score[start] = h(start.get_pos(), end.get_pos())

    #Creating a set
    open_set_hash = {start}
    #Priority queue cannot check whether specific node is in queue so need set to do that. 

    #When set is empty, we have considered every path
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        #[2] just tells that we are interested in checking the node (which is stored in index 2)
        #*.get() will return a single item from the queue (deque)
        #!Here is where a priority queue becomes useful. 
        #*Gets element with the minimum f-score (based on the first element.)
        current = open_set.get()[2]
        open_set_hash.remove(current)




        if current == end:
            #Found path
            reconstruct_path(came_from, end, draw)
            start.make_start()
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            #!Any neighbor will be 1 away from the start node compared to the current node. 
            temp_g_score = g_score[current]+1

            if temp_g_score < g_score[neighbor]:
                #*Have found a better way to reach this neighbor than what had previously been used. 
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = g_score[neighbor] + h(end.get_pos(), neighbor.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count,neighbor))
                    open_set_hash.add(neighbor)
                    #*For visualization to show that we are going to consider this neighbor. 
                    neighbor.make_open()
        draw()

        if current != start:
            #*Has already been considered. 
            current.make_closed()

    return False


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
def draw_grid(win, rows, width):
    #Draw lines. 
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i*gap))

    #?Tim puts all of this in a nested for-loop but I am not really sure which one is correct...
    for j in range(rows):
        pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    #Spots are drawn first. 
    draw_grid(win, rows, width)
    pygame.display.update()

#*Manages mouse methods. 
#Find based on mouse position. 

def get_clicked_pos(pos, rows, width):
    gap = width //rows
    #?Why y x though?
    #!Official docs also says return is (x, y)
    #*But when I correspond grid x, it will help determine column
    #?
    x, y = pos

    row = x // gap
    col = y // gap

    return row, col

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #*When the algorithm is running, we don't want the user to click anything and game to respond so continue. 
            if started:
                continue

            #Check mouse position
            #*If the left mouse button was pressed
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                #*Set start or end. 
                if not start and spot != end:
                    #*Need to assign to change the value from None. 
                    start = spot
                    start.make_start()

                #!I shouldn't be able to press the start and end positions right on top of eachother. 
                elif not end and spot !=start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    #Barrier. 
                    spot.make_barrier()
                


            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and started == False:
                #Start algo
                #*Update negithbors. 
                for row in grid:
                    for spot in row:
                        spot.update_neighbors(grid)

                #*Passing the draw function as an argument for the algorithm?
                #!This may be useful when we don't want to congregate a method with so much info (like win, grid) and stuff.
                #*lambda saves these stuff and allows to call function without having these values right there. 
                algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                started = True

    pygame.quit()

main(WIN, WIDTH)