import pygame
pygame.init()
from network import Network

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0



class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)
        self.vel = 3

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel
    
        self.update()

    def update(self):

        self.rect = (self.x, self.y, self.width, self.height)

#!Convert string into tuple
def read_pos(str):
    '''
    Input is something like '45, 67'
    Return as tuple with integer
    '''
    str = str.split(',')
    print(str[0])
    print(str[1])
    return int(str[0]), int(str[1])

#!Convert tuple into string
def make_pos(tup):
    '''
    Input: (45, 67)
    Output: '45, 67'
    '''
    return str(tup[0]) + ',' + str(tup[1])


def redraw(win, p, p2):
    win.fill((255, 255, 255))

    p.draw(window)
    #?Player 1 and 2 are somehow overlapping
    print(f"p1 = {p.x}, {p.y}")
    p2.draw(window)
    print(f"p2 = {p2.x}, {p2.y}")


    pygame.display.update()


def main():
    run = True

    #!Based on which player I am, starting position is going to vary
    n = Network()
    #!Position will initially come in as string, not tuple
    startPos = read_pos(n.get_pos())
    print(f"startPos = {startPos}")
    #*Second player
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0))
    clock = pygame.time.Clock()

    while run:

        #*We are inputting the data for player 1, then receiving data of player 2 and converting it to tuple
        print(f"px, py = {p.x}, {p.y}")
        print(f"make pos = {make_pos((p.x, p.y))}")
        #print(n.send(make_pos((p.x, p.y))))

        #!Send current position
        #*n.send() receives player 2s position
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        

        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        p.move()
        redraw(window, p, p2)

main()
