from player import Player

import pygame
pygame.init()
from network import Network

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")



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

    #*First player
    #!n.getP() return an object that will be assigned to each player
    p1 = n.getP()

    clock = pygame.time.Clock()

    while run:

        #!By calling n.send(), I can receive the player2 object
        p2 = n.send(p1)


        #!Send current position
        #*n.send() receives player 2s position
    
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



        p1.move()
        redraw(window, p1, p2)

main()
