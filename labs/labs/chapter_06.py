# labs/chapter_06.py

# 6.1 part 1 =====================================================
x = 10
for row in range(1,10):
    for column in range(row):
        print (x,end=" ")
        x += 1
 
    # Print a blank line
    # to move to the next row
    print()
    
    
# 6.2 part 2 =====================================================
# Step 1: Claculate rows and columns
n = 0
while True:
    n = int(input("Enter n (n > 1): "))
    if n > 1:
        break
    else:
        continue

rows = n
columns = n * 2

# Step 2: Draw the first row
for i in range(columns):
    print("o", end = "")

for i in range (rows - 2):
    print("\n", end = "")
    # Step 3.1: The first character
    print("o", end = "")

    # Step 3.2: The blank spaces
    for j in range (columns - 2):
        print(" ", end = "")
        
    # Step 3.3: The last character
    print("o", end = "")

# Step 4: Draw the last row
print("\n", end = "")
for i in range(columns):
    print("o", end = "")


# 6.3 part 3 =====================================================
# Get user input
n = int(input("Enter number:"))

# Rows in the range of number entered
for row in range(n):
    # Number goes up
    for i in range(0 + row, n):
        print(2*i + 1, end = " ")
    # Spacing in the middle
    for j in range(row):
        print("  ", end = "  ")
    # Reversed the numbers
    for i in reversed(range(0 + row, n)):
        print(2*i + 1, end = " ")

    print()

# Everything goes reversed
for row in reversed(range(n)):
    for i in range(0 + row, n):
        print(2*i + 1, end = " ")
    for j in range(row):
        print("  ", end = "  ")
    for i in range(0 + row, n):
        print(2*i + 1, end = " ")

    print()

    
# 6.4 part 4 =====================================================
# Import a library of functions called 'pygame'
import pygame
 
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


# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Kevin's picture")
 
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
    screen.fill(WHITE)

    # -------------Main drawings here---------
    
    # Draw picture
    square = 0
    rows = 400
    columns = 500

    height = (columns/25)-10
    width = (rows/20)-10
    for i in range (rows):
        for j in range(columns):
            pygame.draw.rect(screen,
                            LIGHT_YELLOW,
                            [0 + (j * (width + 5)), 0 + (i * (height + 5)),
                            width, height])
            

    # Flip the Pygame display
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
