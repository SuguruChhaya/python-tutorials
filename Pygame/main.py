'''
I have to download the image zip file from tech with tim's tutorial.
Do that on my other account and put it up google drive. I am going to comment it out for now.
'''
'''
Later on, I want to modify this so I can add potions in the game. 
I also want to make it so that as the level increases, the enemy health increases too. 
I also want to add a laser cannon which I have to dodge. 
I want to make different ships that can shoot in a circular motion
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

#*Creating a Ship class to create player ships and enemy ship
class Ship():
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = YELLOW_SPACE_SHIP
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    #*Second argument is the colour
    #*Third argument: 1st: top right x coord, 2nd: top right y coord, 3rd: yoko, 4th: tate
    def draw(self, window):
        WIN.blit(self.ship_image, (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=health)
        self.ship_image = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        #*pygame masks allows you to identify pixel collisions and that stuff.
        self.mask = pygame.mask.from_surface(self.ship_image)
        #*I am creating self.max_health and self.health because self.max_health never changes but self.health will decrease
        
        self.max_health = health

#*In pygame, I have to create a mainloop like tkinter
def main():
    run = True
    #*Higher the fps, the faster the game is going to run
    #*This means that we are checking for collisions, moving characters once every 60 frames per second.
    FPS = 60
    #!I want to create text on the screen mentioning levels and lives. I need to create a font for that.
    #*player veolcity
    player_vel = 5
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    #!Clock is to refresh frames and all that.
    ship = Ship(600, 300, )
    clock = pygame.time.Clock()

    #*I can use the run variable and all that when I have function inside function
    def redraw_window():
        #*We will redraw everything in 60 frames per frame speed
        #blit adds an image to the surface
        #*The coordinate system is the same as tkinter canvas
        WIN.blit(BG, (0, 0))
        #*Don't worry about 2nd argument. Usually always use 1
        #*3rd argument is rgb (red, green, blue) for the colour of the font.
        #?Render means to paint or draw
        #*.render is the equivalent of creating a label in tkinter
        lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))
        level_label = main_font.render(f'Level: {level}', 1, (255, 255, 255))

        #*Blit is the equivalent of .grid in tkinter where it actually comes on the screen.
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))


        ship.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        #*Check if user has quit the game or not. 
        for event in pygame.event.get():
            #print('for loop is ran')
            #print(event)
            #*When I click the close button on top right, that becomes pygame.QUIT. I will then break from the for loop.
            #!I need to add this or it is instantly gonna close
            if event.type == pygame.QUIT:
                run = False
            #*Triggered when key is pressed down


            #*Checking what keys have been pressed 60 times every second
            #*Returns a tuple
        
        #!It is SOOOOO important not to put this bunch of code inside the forloop.
        #*If I uncomment the print(event) in the for loop, I will see that an event DOES NOT occur when I am holding a button down.
        #*It happens when I newly press a key or when I release a key, but not when I hold onto it.
        #*This causes the forloop not to be run: self.x and self.y value doesn't change.
        keys = pygame.key.get_pressed()
        #left
        #*pygame.K_a return the index of the long tuple. The value is 0 when the item doesn't exist.

        #*To check whether the ship is out of the screen, I can add an 'and' statement
        if keys[pygame.K_a] and ship.x - player_vel > 0: 
            ship.x -= player_vel
        #*I also have to cvonsider the width of the rectangle.
        if keys[pygame.K_d] and ship.x + player_vel < WIDTH - 100:
            ship.x += player_vel
        if keys[pygame.K_w] and ship.y - player_vel > 0:
            ship.y -= player_vel
        if keys[pygame.K_s] and ship.y + player_vel < HEIGHT - 200:
            ship.y += player_vel

                

main()
