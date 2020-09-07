'''
This tutorial is from the tech with tim networking and socketing pygame tutorial series. 
'''
import pygame
pygame.init()
WIDTH = 500
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Client')

clinet_number = 0

#*The class is for the Player
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.rect = (self.x, self.y, self.width, self.height)

        #*Speed of object movement
        self.vel = 3

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        #*Check which key was pressed
 
        keys = pygame.key.get_pressed()

        
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


def redraw_window(player):
    window.fill((255, 255, 255))
    player.draw(window)
    pygame.display.update()

def main():
    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))

    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

        p.move()
        redraw_window(p)

main()