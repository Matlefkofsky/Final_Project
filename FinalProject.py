from pygame.locals import *
from random import randint
import pygame
import time
import random
 
class Trump_Food(pygame.sprite.Sprite):
	x = 0
	y = 0
	multiplier = 4
 
	def __init__(self,x,y):
		self.x = x * self.multiplier
		self.y = y * self.multiplier
 
	def draw(self, surface, image):
		surface.blit(image,(self.x, self.y)) 
 
 
class Trump(pygame.sprite.Sprite):
	x = [0]
	y = [0]
	multiplier = 4
	direction = 0
	length = 3
	NewCountMax = 2
	NewCount = 0
 
	def __init__(self, length):
	   self.length = length
	   for i in range(0,2000):
		   self.x.append(-100)
		   self.y.append(-100)
 
	   # initial positions
	   self.x[1] = 1*4
	   self.x[2] = 2*4
 
	def update(self):
 
		self.NewCount = self.NewCount + 1
		if self.NewCount > self.NewCountMax:
 
			# this is used to update previous positions
			for i in range(self.length-1,0,-1):
				self.x[i] = self.x[i-1]
				self.y[i] = self.y[i-1]
 
			# these lines of code update the position of the head of the snake (the first Donald)
			if self.direction == 0:
				self.x[0] = self.x[0] + self.multiplier
			if self.direction == 1:
				self.x[0] = self.x[0] - self.multiplier
			if self.direction == 2:
				self.y[0] = self.y[0] - self.multiplier
			if self.direction == 3:
				self.y[0] = self.y[0] + self.multiplier
 
			self.NewCount = 0
 
 
	def moveRight(self):
		self.direction = 0
 
	def moveLeft(self):
		self.direction = 1
 
	def moveUp(self):
		self.direction = 2
 
	def moveDown(self):
		self.direction = 3 
 
	def draw(self, surface, image):
		for i in range(0,self.length):
			surface.blit(image,(self.x[i],self.y[i])) 
 
class Game:
	def Colliding(self,x1,y1,x2,y2,bsize):
		if x1 >= x2 and x1 <= x2 + bsize:
			if y1 >= y2 and y1 <= y2 + bsize:
				return True
		return False
 
