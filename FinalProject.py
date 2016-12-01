from pygame.locals import *
from random import randint
import pygame
import time
import random

"""A:  Create a variation of PacMan, Breakout, Asteroids.    You can create a game of your choice, but it must include movement, collision detection, scoring and/or time, and animation. All games should include sound. Base score is 100/150 pts for a working game.

B: Show at least two consistent weeks of commits (at least 10 different days, more than 5 hours apart) 10pts

C: Demonstrate a unique implementation of Class Inheritance 10pts

D: Final 30 points are on a curved scale.  The class will rank the best games in the class."""
 
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
	global length
	length = 3
	NewCountMax = 2
	NewCount = 0
 
	def __init__(self, length):
	    self.length = length
	    for x in range(0,5000):
		    self.x.append(-100)
		    self.y.append(-100)
 
	   # initial positions
	    self.x[1] = 1*47
	    self.x[2] = 2*47
 
	def update(self):
 
		self.NewCount = self.NewCount + 1
		if self.NewCount > self.NewCountMax:
 
			# this is used to update previous positions
			for x in range(self.length-1,0,-1):
				self.x[x] = self.x[x-1]
				self.y[x] = self.y[x-1]
 
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
 
 
	def goR(self):
		self.direction = 0
 
	def goL(self):
		self.direction = 1
 
	def goU(self):
		self.direction = 2
 
	def goD(self):
		self.direction = 3 
 
	def draw(self, surface, image):
		for i in range(0,self.length):
			surface.blit(image,(self.x[i],self.y[i])) 
 
class Game:
	def Colliding(self,x1,y1,x2,y2):
		if x1 >= x2 and x1 <= x2:
			if y1 >= y2 and y1 <= y2:
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

		global sound
		sound = pygame.mixer.Sound("Best_of_Donald.wav")
 
	def Event(self, event):
		if event.type == QUIT:
			self._running = False
 
	def Update(self):
		self.trump.update()
 
		# does snake eat Trump_Food?
		for i in range(0,self.trump.length):
			if self.game.Colliding(self.Trump_Food.x,self.Trump_Food.y,self.trump.x[i], self.trump.y[i]):
				self.Trump_Food.x = randint(2,9) * 47
				self.Trump_Food.y = randint(2,9) * 47
				self.trump.length = self.trump.length + 1
				# print (self.trump.length)
 
 
		# does snake collide with itself?
		for i in range(2,self.trump.length):
			if self.game.Colliding(self.trump.x[0],self.trump.y[0],self.trump.x[i], self.trump.y[i]):
				print("Game over. You collided with yourself! Your score was ", (self.trump.length))
				exit(0)
 
		pass
 
	def Create(self):
		self._display_surf.fill((0,0,0))
		self.trump.draw(self._display_surf, self._image_surf)
		self.Trump_Food.draw(self._display_surf, self._Trump_Food_surf)
		pygame.display.flip()
 
	def quit(self):
		pygame.quit()
 
	def running(self):
		if self.Begin() == False:
			self._running = False

		while (self._running):
			sound.play()
			pygame.event.pump()
			keys = pygame.key.get_pressed() 
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.trump.goL()
					if event.key == pygame.K_RIGHT:
						self.trump.goR()
					if event.key == pygame.K_UP:
						self.trump.goU()
					if event.key == pygame.K_DOWN:
						self.trump.goD()
					if event.key == pygame.K_ESCAPE:
						self._running = False
						print ("You quit out of the game! Your score was ", self.trump.length)
				if event.type == pygame.QUIT:
					self._running = False
					print ("You quit out of the game! Your score was ", self.trump.length)
 
			self.Update()
			self.Create()
 
			time.sleep (50.0 / 1000.0);
		self.quit()
 
if __name__ == "__main__" :
	theApp = App()
	theApp.running()