import pygame
import paddle as p
import gameball as b
import constants as c
import inputhandler as d

score1 = 0
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Pong')
 
# Enable this to make the mouse disappear when over our window
pygame.mouse.set_visible(0)
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())
 
# Create the ball
ball = b.GameBall()
# Create a group of 1 ball (used in checking collisions)
# balls = pygame.sprite.Group()
# balls.add(ball)
 
# Create the player paddle object
player = p.Paddle(580)
 
movingsprites = pygame.sprite.Group()
movingsprites.add(player)
movingsprites.add(ball)
 
handler = d.InputHandler()

clock = pygame.time.Clock()
done = False
exit_program = False

while not exit_program:

    screen.fill(c.BLACK)

    speed = handler.getinput()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True

    if not done:
        # Update the player and ball positions
        player.update(speed)
        ball.update()

    # Draw Everything
    movingsprites.draw(screen)
 
    # Update the screen
    pygame.display.flip()
     
    clock.tick(30)
 
pygame.quit()