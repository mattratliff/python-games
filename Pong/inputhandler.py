import pygame
import constants as c

class InputHandler():

    def __init__(self):
        # Call the parent's constructor
        super().__init__()

    def getinput(self):
        keys = pygame.key.get_pressed()  #checking pressed keys
        x_speed = 0
        if keys[pygame.K_LEFT]:
            x_speed = -2
        elif keys[pygame.K_RIGHT]:
            x_speed = 2
        return x_speed

