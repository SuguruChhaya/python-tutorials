'''
I can create a static pygame window using the following code. 
'''

import pygame
pygame.init()

window = pygame.display.set_mode((300, 300))

def update():
    pygame.display.update()
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            else:
                print(pygame.QUIT)

        



main()