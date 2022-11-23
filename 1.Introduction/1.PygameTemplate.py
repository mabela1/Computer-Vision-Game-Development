"""
Pygame Template

Import
Initialize
Create Window
Initialize Clock for FPS(frames per second)

Loop (events)
    Get events
        if quit
            quit the pygame
    Apply Logic
    Update Display/Window
    Set FPS

"""

# import
import pygame

# initialize
pygame.init()

# create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("My game")

# Initialize clock for FPS
fps = 30
clock = pygame.time.Clock()

# main loop
start = True
while start:
    # get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    window.fill((255,255,255))

    # update display
    pygame.display.update()
    # set FPS
    clock.tick(fps)
