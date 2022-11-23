'''
Rect
    can detect collisions
    can access x and y points

    two ways of creating a rect
        1. pygame.Rect(x, y, width, height)
        2. surface.get_rect() #create rect arounf a surface/image



'''


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
rectBallon = imgBalloonRed.get_rect()

# Rect
rectNew = pygame.Rect(500, 0, 200, 200) #x,y,width,height

# main loop
start = True
while start:
    # get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    print(rectBallon.colliderect(rectNew)) #when it hits

    rectBallon.x += 5 #move
    rectNew.y += 5

    #window.fill((255,255,255))
    window.blit(imgBackground, (50, 50))
    #pygame.draw.rect(window, (0, 255, 255), rectBallon)
    #pygame.draw.rect(window, (0, 255, 255), rectNew)   #when its comment,it is invisible
    window.blit(imgBalloonRed, rectBallon)


    # update display
    pygame.display.update()
    # set FPS
    clock.tick(fps)
