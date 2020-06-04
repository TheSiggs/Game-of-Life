# ID: 16059692
# 159172
import pygame

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# This sets the width and height of each grid location
width = 10
height = 10

# This sets the margin between each cell
margin = 2

# Create row 2 dimensional array. A two dimensional
# array in our implementation is simply row list of lists.
grid = []
for row in range(30):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(30):
        grid[row].append(0)  # Append row cell

# Set row 0, c ell 0 to one. (Remember rows and
# column numbers start at zero.)
grid[0][0] = 1

# Initialize pygame
pygame.init()

# Set the height and width of the screen
size = [362, 362]
screen = pygame.display.set_mode(size)

# Set title of screen
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create row list of live cells, initially empty
alive = [] 
# alive = [(9, 9), (9, 10), (9, 11), (9, 15), (9, 16), (9, 17), (11, 7), (11, 12), (11, 14), (11, 19), (12, 7), (12, 12), (12, 14), (12, 19), (13, 7), (13, 12), (13, 14), (13, 19), (14, 9), (14, 10), (14, 11), (14, 15), (14, 16), (14, 17), (16, 9), (16, 10), (16, 11), (16, 15), (16, 16), (16, 17), (17, 7), (17, 12), (17, 14), (17, 19), (18, 7), (18, 12), (18, 14), (18, 19), (19, 7), (19, 12), (19, 14), (19, 19), (21, 9), (21, 10), (21, 11), (21, 15), (21, 16), (21, 17)]
# alive = [(6, 13), (7, 12), (7, 13), (7, 14), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (16, 12), (16, 13), (16, 14), (17, 13)]

# Change to play mode when user clicks start position
started = False

######################################
# This is code section which you need to implement
def find_neighbours(gen):
    new_gen = []
    newBorn = []
    for cell in gen:
        neighbours = []
        for row in range(-1, 2):
            for col in range(-1, 2):
                if (cell[0] + row, cell[1] + col) in gen:
                    neighbours.append((cell[0] + row, cell[1] + col))

                newBorn.append((cell[0] + row, cell[1] + col))
        newBorn.remove(cell)
        neighbours.remove(cell)
        if len(neighbours) == 2 or len(neighbours) == 3:
            new_gen.append(cell)

    for born in newBorn:
        if newBorn.count(born) == 3 and born not in new_gen:
            new_gen.append(born)
    return new_gen


def nextgen(gen):
    gen = find_neighbours(gen)
    return gen


########################################
def remove_dupes(gen):
    return list(set(gen))

# -------- Main Program Loop -----------
while done is False:
    if not (started):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                # Set that location to one
                grid[row][column] = 1
                # If user clicks start position
                if row == 0 and column == 0:
                    started = True
                    grid[row][column] = 0
                    # Set up live cell list
                    for row in range(30):
                        for column in range(30):
                            if grid[row][column] == 1:
                                alive.append((row, column))

    if started:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                # If user clicks stop position
                if row == 0 and column == 0:
                    started = False
                    alive = []
        # Clear the grid
        for row in range(30):
            for column in range(30):
                grid[row][column] = 0
        # Set live cells
        for (row, column) in alive:
            grid[row][column] = 1
        # Set up next generation
        # print(alive)
        # done = True
        alive = nextgen(alive)

    # Set the screen background
    screen.fill(black)

    # Draw the grid
    grid[0][0] = 1
    for row in range(30):
        for column in range(30):
            color = white
            if grid[row][column] == 1:
                if started:
                    color = green
                else:
                    color = red
            pygame.draw.rect(screen, color, [
                             (margin + width) * column + margin, (margin + height) * row + margin, width, height])

    # Limit to 20 frames per second
    clock.tick(10)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

# If you forget this line, the program will 'hang' on exit.
pygame.quit()