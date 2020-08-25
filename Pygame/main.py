'''
I have to download the image zip file from tech with tim's tutorial.
Do that on my other account and put it up google drive. I am going to comment it out for now.
'''
import pygame
import os
import time
import random
pygame.font.init()

#*Setup pygame window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

#*Load images
#Look at https://www.geeksforgeeks.org/python-os-path-join-method/ for the os.path.join function.
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
#Alternative
#RED_SPACE_SHIP = pygame.image.load('assets/pixel_ship_red_small_png')
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
#Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#Lasers
RED_LASER = pygame.image.load(os.path.join("assets", 'pixel_laser_red.png'))
GREEN_LASER = pygame.image.load(os.path.join("assets", 'pixel_laser_green.png'))
BLUE_LASER = pygame.image.load(os.path.join("assets", 'pixel_laser_blue.png'))
YELLOW_LASER = pygame.image.load(os.path.join("assets", 'pixel_laser_yellow.png'))

#Background
#?Pygame.transform is to scale the images
#*I can scale the images to the size of the window so it fits perfectly
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", 'background-black.png')), (WIDTH, HEIGHT))


#*In pygame, I have to create a mainloop like tkinter
def main():
    run = True
    #*Higher the fps, the faster the game is going to run
    #*This means that we are checking for collisions, moving characters once every 60 frames per second.
    FPS = 60
    #!I want to create text on the screen mentioning levels and lives. I need to create a font for that.
    level = 1
    lives = 5
    main_font = pygame.font.Sysfont("comicsans", 50)
    #!Clock is to refresh frames and all that.
    clock = pygame.time.Clock()

    #*I can use the run variable and all that when I have function inside function
    def redraw_window():
        #*We will redraw everything in 60 frames per frame speed
        #blit adds an image to the surface
        #*The coordinate system is the same as tkinter canvas
        WIN.blit(BG, (0, 0))
        lives_label = main_font.reder(f'Level')
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        #*Check if user has quit the game or not. 
        for event in pygame.event.get():
            #*When I click the close button on top right, that becomes pygame.QUIT. I will then break from the for loop.
            #!I need to add this or it is instantly gonna close
            if event.type == pygame.QUIT:
                run = False
            #*Triggered when key is pressed down
            '''
            if event.type == pygame.KEYDOWN:
                pass
            '''

main()
