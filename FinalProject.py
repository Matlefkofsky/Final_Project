from pygame.locals import *
from random import randint
import pygame
import time
import random
 
class Trump_Food(pygame.sprite.Sprite):
	x = 0
	y = 0
	multiplier = 47
 
	def __init__(self,x,y):
		self.x = x * self.multiplier
		self.y = y * self.multiplier
 
	def draw(self, surface, image):
		surface.blit(image,(self.x, self.y)) 
 
 
class Trump(pygame.sprite.Sprite):
	x = [0]
	y = [0]
	multiplier = 47
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
	   self.x[1] = 1*47
	   self.x[2] = 2*47
 
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
 
class App(pygame.sprite.Sprite):
 
	Width = 800
	Height = 600
	trump = 0
	Trump_Food = 0
 
	def __init__(self):
		self._running = True
		self._display_surf = None
		self._image_surf = None
		self._Trump_Food_surf = None
		self.game = Game()
		self.trump = Trump(3) 
		self.Trump_Food = Trump_Food(5,5)
 
	def Begin(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode((self.Width,self.Height), pygame.HWSURFACE)
 
		pygame.display.set_caption('Trump Game')
		self._running = True
		self._image_surf = pygame.image.load("trump.bmp").convert()

		lst_of_pics = ["hillary3.bmp","mexico.bmp"]
		random_pic = random.choice(lst_of_pics)
		self._Trump_Food_surf = pygame.image.load(random_pic).convert()
		# for i in range(0,self.trump.length):
		# 	if self.game.Colliding(self.Trump_Food.x,self.Trump_Food.y,self.trump.x[i], self.trump.y[i],40):
		# 		self._Trump_Food_surf = pygame.image.load(random_pic).convert()
		# 		self.flip()   ###doesnt work!!!!!!

 
	def Event(self, event):
		if event.type == QUIT:
			self._running = False
 
	def Update(self):
		self.trump.update()
 
		# does snake eat Trump_Food?
		for i in range(0,self.trump.length):
			if self.game.Colliding(self.Trump_Food.x,self.Trump_Food.y,self.trump.x[i], self.trump.y[i],40):
				self.Trump_Food.x = randint(2,9) * 47
				self.Trump_Food.y = randint(2,9) * 47
				self.trump.length = self.trump.length + 1
 
 
		# does snake collide with itself?
		for i in range(2,self.trump.length):
			if self.game.Colliding(self.trump.x[0],self.trump.y[0],self.trump.x[i], self.trump.y[i],40):
				print("Game over. You collided with yourself!: ")
				exit(0)
 
		pass
 
