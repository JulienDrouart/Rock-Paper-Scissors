import os
from random import randint
import pygame, sys
import random
import time
import math

from pygame.locals import *
from collections import OrderedDict


def loopFunction():
    pygame.init()

    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('RockPaperScissors')
    color = (255, 255, 255)
    screen.fill(color)
    run = True
    start = gameover = False
    rockImg = pygame.image.load("rock.ico")
    paperImg = pygame.image.load("paper.ico")
    scissorsImg = pygame.image.load("scissors.ico")

    entity = {}

    numberOfEach = 1

    for i in range(numberOfEach):
        cooX = random.randint(0, 400)
        cooY = random.randint(0, 400)
        entity[i] = {'posX': cooX, 'posY': cooY, 'state': "rock"}
        screen.blit(rockImg, (cooX, cooY))
        cooX = random.randint(0, 400)
        cooY = random.randint(0, 400)
        entity[i] = {'posX': cooX, 'posY': cooY, 'state': "paper"}
        screen.blit(paperImg, (cooX, cooY))
        cooX = random.randint(0, 400)
        cooY = random.randint(0, 400)
        entity[i] = {'posX': cooX, 'posY': cooY, 'state': "scissors"}
        screen.blit(scissorsImg, (cooX, cooY))

    while run:
        while gameover:
            font = pygame.font.SysFont(None, 50)
            end = font.render('Press Enter to restart', True, (255, 255, 255))
            screen.blit(end, (350, 500))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        loopFunction()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if start is False:
                        timerEverySeconds = time.time()
                        start = True

            if start is True:
                screen.fill(color)

                for i in range(numberOfEach):

                    #Rock
                    target = "scissors"
                    distanceList, idList = [],[]

                    for j in range(numberOfEach):
                        if entity[j]["state"] == "scissors":
                            distanceList.append(math.hypot(entity[j]["posX"] - entity[j]["posX"], entity[j]["posY"] - entity[j]["posY"]))
                            idList.append(j)
                    nearestTargetId = distanceList.index(max(distanceList))
                    nearestTarget = entity[idList[nearestTargetId]]


                    if nearestTarget["posX"] > entity[i]["posX"]:
                        cooX -= 1
                    if nearestTarget["posX"] < entity[i]["posX"]:
                        cooX += 1
                    if nearestTarget["posY"] > entity[i]["posY"]:
                        cooY -= 1
                    if nearestTarget["posY"] > entity[i]["posY"]:
                        cooY -= 1
                    entity[i] = {'posX': cooX, 'posY': cooY, 'state': "rock"}
                    screen.blit(rockImg, (cooX, cooY))

                    #Paper
                    target = "rock"
                    cooX = random.randint(0, 400)
                    cooY = random.randint(0, 400)
                    entity[i] = {'posX': cooX, 'posY': cooY, 'state': "paper"}
                    screen.blit(paperImg, (cooX, cooY))

                    #Scissors
                    target = "paper"
                    cooX = random.randint(0, 400)
                    cooY = random.randint(0, 400)
                    entity[i] = {'posX': cooX, 'posY': cooY, 'state': "scissors"}
                    screen.blit(scissorsImg, (cooX, cooY))

        pygame.display.flip()


loopFunction()
