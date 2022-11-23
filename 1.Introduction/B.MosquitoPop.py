# import
import random

import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time


# initialize
pygame.init()

# create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mosquito Pop")

# Initialize clock for FPS
fps = 30
clock = pygame.time.Clock()

#Webcam
cap =cv2.VideoCapture(0)
cap.set(3, 1280) #width
cap.set(4, 720)  #height

# Images
imgMosquito = pygame.image.load('..//Resources/mosquito.png').convert_alpha()
imgMosquito = pygame.transform.scale(imgMosquito, (80, 80))
rectMosquito = imgMosquito.get_rect()
rectMosquito.x, rectMosquito.y = 500, 300

#Variables
speed = 15
score = 0
startTime = time.time()
totalTime = 5

#Detector
detector = HandDetector(detectionCon = 0.8, maxHands=1)

def resetMosquito():
    rectMosquito.x = random.randint(100, img.shape[1]-100)
    rectMosquito.y = img.shape[0]+50


# main loop
start = True
while start:
    # get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    timeRemain = int(totalTime-(time.time()-startTime))
    if timeRemain < 0:
        window.fill((255, 255, 255))

        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
        textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time UP', True, (50, 50, 255))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))


    else:
        # OpenCV
        success, img = cap.read()
        img = cv2.flip(img, 1) #1->horizontal;0->vertical
        hands, img = detector.findHands(img, flipType=False)

        rectMosquito.y -= speed #move the mosquito up

        #check if mosquito has reached the top without pop
        if rectMosquito.y < 0:
            resetMosquito()
            speed += 1

        if hands:
            hand = hands[0]
            x, y = hand['lmList'][8]
            if rectMosquito.collidepoint(x, y):
                resetMosquito()
                score += 10
                speed += 1


        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))
        window.blit(imgMosquito, rectMosquito)

        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
        textScore = font.render(f'Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000,35))
    # update display
    pygame.display.update()
    # set FPS
    clock.tick(fps)