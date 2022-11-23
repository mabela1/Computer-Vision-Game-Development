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

# Load Images
imgBackground = pygame.image.load("..//Resources/BackgroundBlue.jpeg").convert()
imgBalloonRed = pygame.image.load("..//Resources/BalloonRed.png").convert_alpha()
#imgBalloonRed = pygame.transform.rotate(imgBalloonRed, 90)         #->rotate
#imgBalloonRed = pygame.transform.rotozoom(imgBalloonRed, 90, 0.3)         #->rotozoom
#pygame.transform.flip(imgBalloonRed, True, False)                  #->flip


# main loop
start = True
while start:
    # get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    #imgBalloonRed = pygame.transform.scale(imgBalloonRed, (50, 100))       #->scale
    imgBalloonRed = pygame.transform.smoothscale(imgBalloonRed, (50, 100))


    #window.fill((255,255,255))
    window.blit(imgBackground, (50, 50))
    window.blit(imgBalloonRed, (200, 300))

    # update display
    pygame.display.update()
    # set FPS
    clock.tick(fps)
