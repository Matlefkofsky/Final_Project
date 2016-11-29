from pygame.locals import *
from random import randint
import pygame
import time
 
class Food:
    x = 0
    y = 0
    step = 47
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
 
class Player:
    x = [0]
    y = [0]
    step = 47
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
 