# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (102, 204, 0)
RED = (255, 0, 0)
DARK_RED = (154, 32, 32)
LIGHT_YELLOW = (255, 255, 102)
SKY_BLUE = (204,255,255)

# Defining PI
PI = 3.141592653
 
# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Kevin's picture")

# Create an empty array
snow_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])
 
# Loop until user click quit
done = False

# Manage how fast the screen updates
clock = pygame.time.Clock()
 
# Loop as long as done == False
while done == False:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # Clear the screen and set the screen background
    screen.fill(BLACK)

    # -------------Main drawings here---------


    # Draw picture

    pygame.draw.rect(screen, BLACK, [0, 0, 400, 400] )
    pygame.draw.rect(screen, GREEN, [0, 400, 400, 100] )
    #pygame.draw.rect(screen, LIGHT_YELLOW, [20, 250, 250, 230] )
    pygame.draw.rect(screen, WHITE, [50, 300, 100, 70] )
    pygame.draw.polygon(screen, DARK_RED, [[88,170], [0,269], [180,269]])
    pygame.draw.polygon(screen, DARK_RED, [[300,170], [200,270], [400,270]])

    house = 0
    while house < 400:
        pygame.draw.rect(screen,LIGHT_YELLOW,[0+house,270,180+house,200])
        house = house + 200

    pygame.draw.rect(screen, WHITE, [50, 300, 100, 70] )
    pygame.draw.rect(screen, WHITE, [290, 300, 100, 70] )

        # Process each snow flake in the list
    for i in range(len(snow_list)):
 
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
 
        # Move the snow flake down one pixel
        snow_list[i][1] += 1
 
        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 400:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x


    # Flip the Pygame display
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
