from math import sqrt, log10, atan,pi
from random import randrange
import pygame
from rock import Rock

class ListOfRocks:

    def __init__(self, list = [], score = 0):
      self.list = list
      self.score = score


    def setScore(self, score):
        self.score = score

    # Delta-time is the amount of time that passed since the last frame

    def update(self, deltaTime, score):
        self.spawnNewRock(deltaTime, score)
        self.updateRocks(deltaTime)
        self.deleteRocks()

    def draw(self, screen):
        for Rock in self.list:
            Rock.draw(screen)
    

    def deleteRocks(self):
        rocksToDelete = []
        for i in range(len(self.list)):
            if self.list[i].x > 640:
                rocksToDelete.append(i)

        for i in rocksToDelete:
            self.list.pop(i)

    def updateRocks(self, deltaTime):
        for rock in self.list:
            rock.update(deltaTime)

    def Collision(self,screen,rocket):
        for i in self.list:
            if rocket.x< i.x < rocket.x+40 and rocket.y<i.y<rocket.y+40 :
                if rocket.score > rocket.PB:
                    rocket.PB = rocket.score 
                rocket.score = 0
                rocket.x,rocket.y = rocket.DEFAULT_IMAGE_POSITION


    def spawnNewRock(self, deltaTime, score):

        # The probability of a rock getting created

        spawnProbability =(atan((score-10)/10)*(30/(1.5*pi))+6)*(deltaTime/1000)*70
        if (randrange(0, 100) < spawnProbability):
            self.list.append(Rock(0,randrange(20, 420),(50 + log10(1 + 10 * score))))


        

        
    