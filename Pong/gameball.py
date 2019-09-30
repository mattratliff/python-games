import pygame
import random
import math
import constants as c

class GameBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.outofbounds = False

        self.image = pygame.Surface([10, 10])
 
        # Color the ball
        self.image.fill(c.WHITE)
 
        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()

        # Get attributes for the height/width of the screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
        # Speed in pixels per cycle
        self.speed = 0
 
        # Floating point representation of where the ball is
        self.x = 0
        self.y = 0
 
        # Height and width of the ball
        self.width = 10
        self.height = 10
 
        self.size = 10
        self.change_x = 0
        self.change_y = 0

        # Set the initial ball speed and position
        self.initialize()

    def initialize(self):
        self.speed = 7
        self.change_x = self.speed
        self.change_y = self.speed

        self.x = random.randrange(50,750)
        self.y = 30

    def update(self):
        if self.y > self.screenheight - self.size or self.y < self.size:
            self.change_y *= -1
        if self.x > self.screenwidth - self.size or self.x < self.size:
            self.change_x *= -1

        self.x += self.change_x
        self.y += self.change_y
 
        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y

        if self.y > self.screenheight - self.size:
            self.outofbounds = True

    def bounce(self):
        self.change_y *= -1