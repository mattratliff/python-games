import pygame
import constants as c

class Paddle(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, y_pos):
        # Call the parent's constructor
        super().__init__()
 
        self.width=75
        self.height=15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(c.WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
        self.rect.x = 30
        self.rect.y = y_pos
 
    # Update the player
    def update(self, speed):
        self.rect.x = self.rect.x + speed * 15

        # Make sure we don't push the player paddle off the right side of the screen
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.width
