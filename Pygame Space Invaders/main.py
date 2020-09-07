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
    #*Cooldown time is half a second cuz 50 fps per second
    COOLDOWN = 30
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
        window.blit(self.ship_image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def get_width(self):
        #*This returns the width of the ship
        return self.ship_image.get_width()

    def get_height(self):
        return self.ship_image.get_height()

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            #*Start cooldown counting 
            self.cool_down_counter = 1
        
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def move_lasers(self, vel, obj):
        #*Every time I move the laser, the cooldown method will be called
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=100)
        self.ship_image = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        #*pygame masks allows you to identify pixel collisions and that stuff.
        #!What is interesting is that pygame recognizes where the actual pixels are in the image.
        #*This means it recognizes the actual image and the outside frame. 
        self.mask = pygame.mask.from_surface(self.ship_image)
        #*I am creating self.max_health and self.health because self.max_health never changes but self.health will decrease
        self.max_health = health

    def move_lasers(self, vel, objs):
        #*Every time I move the laser, the cooldown method will be called
        #*objs will be a list of the enemy
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def health_bar(self, window):
        #*First draw red rectange. Then draw a green triangle over it with the length corresponding to health. 
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_image.get_height() + 10, self.ship_image.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_image.get_height() + 10, self.ship_image.get_width() *  (self.health / self.max_health), 10))

    def draw(self, window):
        #*The draw method for the player is special because we have to draw the health bar
        super().draw(window)
        self.health_bar(window)

class Enemy(Ship):
    #*To map the colour with the corresponding space ship and laser colour
    COLOR_MAP = {
        'red': (RED_SPACE_SHIP, RED_LASER),
        'green': (GREEN_SPACE_SHIP, GREEN_LASER),
        'blue': (BLUE_SPACE_SHIP, BLUE_LASER)
    }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health=100)
        #*Enemy ship will have different colour
        self.ship_image, self.laser_img = Enemy.COLOR_MAP[color][0], Enemy.COLOR_MAP[color][1]
        self.mask = pygame.mask.from_surface(self.ship_image)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 13, self.y, self.laser_img)
            self.lasers.append(laser)
            #*Start cooldown counting 
            self.cool_down_counter = 1

class Laser():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    
    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        #!returns true if off screen and false when on screen
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

def collide(obj1, obj2):
    #*To use the mask thingy, I need to use the distance between the top right corners of two objects.
    #!I had issues with this part. I need to learn more about masks if I want to do more pygame collisions.
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

#*In pygame, I have to create a mainloop like tkinter
def main():
    run = True
    #*Higher the fps, the faster the game is going to run
    #*This means that we are checking for collisions, moving characters once every 60 frames per second.
    FPS = 60
    #!I want to create text on the screen mentioning levels and lives. I need to create a font for that.
    #*player veolcity
    player_vel = 5
    level = 0
    lives = 5
    lost = False
    lost_counter = 0
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60, bold=False, italic=False)
    #!Clock is to refresh frames and all that.
    player = Player(300, 600)
    laser_vel = 10

    #*wavelength is the number of enemies in one level. Starts with 5. 
    enemies = []
    wave_length = 0
    enemy_vel = 1

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

        #*Enemy is drawn first so that the player comes on top of the enemy
        for enemy in enemies:
            enemy.draw(WIN)
            
        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!! ", 1, (255, 255, 255))
            WIN.blit(lost_label, (int(WIDTH / 2 - lost_label.get_width() /2), 350))

        pygame.display.update()

    while run:
        print('hello world')

        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_counter += 1

            #*Lost message shows for 5 seconds
            if lost_counter > FPS * 3:
                run = False
            
            else:
                #!continue means that all the stuff written after this else statement will not be executed. 
                #*This means the player cannot move, the enemies cannot spawn or move etc
                continue


        #*Check if there are more enemies. If not, level up by 1
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            #*Need to spawn them at same time but should look like they are comming down at different times. 
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(['red', 'blue', 'green']))
                enemies.append(enemy)
                
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
        if keys[pygame.K_a] and player.x - player_vel > 0: 
            player.x -= player_vel
        #*I also have to cvonsider the width of the rectangle.
        if keys[pygame.K_d] and player.x + player_vel < WIDTH - player.get_width():
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        #*Make sure health bar shows
        if keys[pygame.K_s] and player.y + player_vel < HEIGHT - player.get_height() - 20:
            player.y += player_vel

        #*Shooting
        if keys[pygame.K_SPACE]:
            player.shoot()

        #*The [:] in the forloop is 
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            #*This checks whether the enemy laser had hit the player
            enemy.move_lasers(laser_vel, player)


            #*I need to make up a probability that the enemy will shoot. 
            #!For eandom.randrange(0, 2), 2 is not included. 
            #*Since this is 60 frames per second, multiple by 60
            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()
            
            #*Player and enemy collide
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)


            #*If enemy moves out of the screen, we lose health. We then have to remove the enemies from the list. 
            if enemy.y + enemy_vel > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

def main_menu():
    title_font = pygame.font.SysFont('comicsans',70)
    run = True
    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render("Press the mouse to begin", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH/ 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()     
    pygame.quit()
    
main_menu()
    
