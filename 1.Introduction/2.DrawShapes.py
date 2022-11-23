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
    window.fill((255,255,255)) #rgb
    red, green, blue = (255,0,0), (0,255,0), (0,0,255)
    pygame.draw.polygon(window, red, ((491, 100), (788, 100), (937, 357), (788, 614), (491, 614), (342, 357)))
    pygame.draw.circle(window, green, (641,360), 200)
    pygame.draw.line(window, blue, (468, 392), (812, 392), 10)
    pygame.draw.rect(window, blue, (468, 307, 345, 70), border_radius=20)

    # update display
    pygame.display.update()
    # set FPS
    clock.tick(fps)
