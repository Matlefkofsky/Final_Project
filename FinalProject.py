from pygame.locals import *
from random import randint
import pygame
import time
 
class american:
    x = 0
    y = 0
    step = 47
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Trump:
    x = [0]
    y = [0]
    step = 47
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*47
       self.x[2] = 2*47
 
