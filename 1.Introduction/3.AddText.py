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
    font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 100)
    font2 = pygame.font.Font(None, 100)
    text = font.render("My Game", True, (50, 50, 50))
    text2 = font2.render("My Game", True, (50, 50, 50))
    window.blit(text, (350, 200))
    window.blit(text2, (350, 400))


    # update display
    pygame.display.update()
    # set FPS
    clock.tick(fps)
