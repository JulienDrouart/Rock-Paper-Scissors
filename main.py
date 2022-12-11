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
    entitySpeed = 0.01

    entities = []

    numberOfEach = 5

    for i in range(numberOfEach):
        cooX = random.randint(0, 400)
        cooY = random.randint(0, 400)
        entities.append({'posX': cooX, 'posY': cooY, 'state': "rock"})
        screen.blit(rockImg, (cooX, cooY))
        cooX = random.randint(0, 400)
        cooY = random.randint(0, 400)
        entities.append({'posX': cooX, 'posY': cooY, 'state': "paper"})
        screen.blit(paperImg, (cooX, cooY))
        cooX = random.randint(0, 400)
        cooY = random.randint(0, 400)
        entities.append({'posX': cooX, 'posY': cooY, 'state': "scissors"})
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
                for entity in entities:
                    nearestTarget = ""
                    if entity["state"] == "rock":
                        # Rock
                        target = "scissors"
                        distanceList, entitiesList = [], []

                        for j in entities:
                            if j["state"] == target:
                                distanceList.append(math.hypot(entity["posX"] - j["posX"],
                                                               entity["posY"] - j["posY"]))
                                entitiesList.append(j)
                        nearestTargetId = distanceList.index(min(distanceList))
                        nearestTarget = entitiesList[nearestTargetId]
                        entityToUpdateId = entities.index(entity)
                        cooX = entity["posX"]
                        cooY = entity["posY"]

                        if nearestTarget["posX"] > entity["posX"]:
                            cooX += entitySpeed
                        if nearestTarget["posX"] < entity["posX"]:
                            cooX -= entitySpeed
                        if nearestTarget["posY"] > entity["posY"]:
                            cooY += entitySpeed
                        if nearestTarget["posY"] < entity["posY"]:
                            cooY -= entitySpeed
                        entity = {'posX': cooX, 'posY': cooY, 'state': "rock"}
                        screen.blit(rockImg, (cooX, cooY))
                        entities[entityToUpdateId] = entity
                    if entity["state"] == "paper":
                        # Paper
                        target = "rock"
                        distanceList, entitiesList = [], []

                        for j in entities:
                            if j["state"] == target:
                                distanceList.append(math.hypot(entity["posX"] - j["posX"],
                                                               entity["posY"] - j["posY"]))
                                entitiesList.append(j)
                        nearestTargetId = distanceList.index(min(distanceList))
                        nearestTarget = entitiesList[nearestTargetId]
                        entityToUpdateId = entities.index(entity)
                        cooX = entity["posX"]
                        cooY = entity["posY"]

                        if nearestTarget["posX"] > entity["posX"]:
                            cooX += entitySpeed
                        if nearestTarget["posX"] < entity["posX"]:
                            cooX -= entitySpeed
                        if nearestTarget["posY"] > entity["posY"]:
                            cooY += entitySpeed
                        if nearestTarget["posY"] < entity["posY"]:
                            cooY -= entitySpeed

                        entity = {'posX': cooX, 'posY': cooY, 'state': "paper"}
                        screen.blit(paperImg, (cooX, cooY))
                        entities[entityToUpdateId] = entity
                    if entity["state"] == "scissors":
                        # Scissors
                        target = "paper"
                        distanceList, entitiesList = [], []

                        for j in entities:
                            if j["state"] == target:
                                distanceList.append(math.hypot(entity["posX"] - j["posX"],
                                                               entity["posY"] - j["posY"]))
                                entitiesList.append(j)
                        nearestTargetId = distanceList.index(min(distanceList))
                        nearestTarget = entitiesList[nearestTargetId]
                        entityToUpdateId = entities.index(entity)
                        cooX = entity["posX"]
                        cooY = entity["posY"]

                        if nearestTarget["posX"] > entity["posX"]:
                            cooX += entitySpeed
                        if nearestTarget["posX"] < entity["posX"]:
                            cooX -= entitySpeed
                        if nearestTarget["posY"] > entity["posY"]:
                            cooY += entitySpeed
                        if nearestTarget["posY"] < entity["posY"]:
                            cooY -= entitySpeed
                        entity = {'posX': cooX, 'posY': cooY, 'state': "scissors"}
                        screen.blit(scissorsImg, (cooX, cooY))
                        entities[entityToUpdateId] = entity

        pygame.display.flip()


loopFunction()
