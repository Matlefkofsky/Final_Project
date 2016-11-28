#Frames per second manipulation

#required 
from random import randint
import pygame
import time
from pygame.locals import*

# pygame.init();

class food:
	x = 0
	y = 0

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def draw(self, surface, image):
		surface.blit(image,(self.x,self.y))

class snake:

