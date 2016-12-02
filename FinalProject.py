from pygame.locals import *
from random import randint
import pygame
import time
import random
 
Blue = (0, 0, 255)
StrDifficulty = input("* Enter a number 1-3 for difficulty...1 being the slowest and 3 the highest *")
Difficulty = int(StrDifficulty)
class Trump(pygame.sprite.Sprite): #class for snake 
	x = [0]
	y = [0]
	Cell_Size = 45 #allows snake to seperate the board and stay in paths
	direction = 0
	global length #globalize this to print the length later on when you die
	length = 3
	NewCountMax = 2
	NewCount = 0
 
	def __init__(self, length): #intializes the legnth of the snake and appends it to grow 
		self.length = length
		for z in range(0,1000): #set high to avoid issue of eating too much food and bugging out
			self.x.append(-100)
			self.y.append(-100)

	def update(self):
 
		self.NewCount = self.NewCount + Difficulty #speed
		if self.NewCount > self.NewCountMax:
 
			# this is used to update previous positions
			for x in range(self.length-1,0,-1):
				self.x[x] = self.x[x-1] #x-1 makes it so it only takes 1 piece of food/imgage for trump to grow when he eats it
				self.y[x] = self.y[x-1]
 
			# these lines of code update the position of the head of the snake (the first Donald)
			if self.direction == 0:
				self.x[0] = self.x[0] + self.Cell_Size
			if self.direction == 1:
				self.x[0] = self.x[0] - self.Cell_Size
			if self.direction == 2:
				self.y[0] = self.y[0] - self.Cell_Size
			if self.direction == 3:
				self.y[0] = self.y[0] + self.Cell_Size
 
			self.NewCount = 0
 
 #Defines the directions for the snake to go
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
			surface.blit(image,(self.x[i],self.y[i])) #blits the surface for each part of the snake and continuosly updates


class Trump_Food(pygame.sprite.Sprite):
	x = 0
	y = 0
	Cell_Size = 45
 
	def __init__(self,x,y): #intializes the snake food and size/placement of each piece
		self.x = x * self.Cell_Size
		self.y = y * self.Cell_Size
 
	def draw(self, surface, image):
		surface.blit(image,(self.x, self.y)) #draws the image on the surface
 
class Game:
	def Colliding(self,x1,y1,x2,y2): #function recognizes when the snake is colliding with another object
		if x1 >= x2 and x1 <= x2:
			if y1 >= y2 and y1 <= y2:
				return True
		return False

class App(pygame.sprite.Sprite): #class acts as main function initializing the game
 
	Width = 800
	Height = 600
	trump = 0
	Trump_Food = 0
 
	def __init__(self): #initilaizes all the methods of self 
		self._running = True
		self._display_surf = None
		self._image_surf = None
		self._Trump_Food_surf = None
		self.game = Game()
		self.trump = Trump(3) #original length of trump snake
		self.Trump_Food = Trump_Food(1,1)
 
	def Begin(self): 
		pygame.init()
		self._display_surf = pygame.display.set_mode((self.Width,self.Height), pygame.HWSURFACE)
		#initilaizes pygame and the display with the width and height

		pygame.display.set_caption('Trump Game') #sets the caption
		self._running = True
		self._image_surf = pygame.image.load("Media/Trump.bmp").convert() #loads the trump image for the snake

		#this code creates a list of images that it will randomly select one of to be the snake food for trump to eat
		lst_of_pics = ["Media/hillary3.bmp","Media/mexico.bmp", "Media/Obama1.bmp"]
		random_pic = random.choice(lst_of_pics)
		self._Trump_Food_surf = pygame.image.load(random_pic).convert()

		global sound
		sound = pygame.mixer.Sound("Media/Fired.wav") #imports soundtrack of Trump repeating "you're fired!"
 
	def Event(self, event): #function to quit out of game
		if event.type == QUIT:
			self._running = False
 
	def Update(self):
		self.trump.update()
 
		# does snake eat Trump_Food? 
		for i in range(0,self.trump.length):
			if self.game.Colliding(self.Trump_Food.x,self.Trump_Food.y,self.trump.x[i], self.trump.y[i]):
				self.Trump_Food.x = randint(2,9) * 45
				self.Trump_Food.y = randint(2,9) * 45 #If collision then another piece of food is placed
				self.trump.length = self.trump.length + 1 #trump snake gains 1
				# print (self.trump.length)
 
 
		# does snake collide with itself?
		for i in range(2,self.trump.length):
			if self.game.Colliding(self.trump.x[0],self.trump.y[0],self.trump.x[i], self.trump.y[i]): #recognizes collision with self
				self._running = False
				print("Game over. You collided with yourself! Your score was ", (self.trump.length))
				 #exits game and prints the length of the snake as the score of the game
 
		pass
 
	def Create(self): #draws every display mentioned above 
		self._display_surf.fill((0,0,0))
		self.trump.draw(self._display_surf, self._image_surf)
		self.Trump_Food.draw(self._display_surf, self._Trump_Food_surf)
		pygame.display.flip() 
 
	def running(self):
		if self.Begin() == False:
			self._running = False

		while (self._running):
			sound.play() #plays the sound
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN: #when a key is pressed...
					if event.key == pygame.K_LEFT:
						self.trump.goL() #if left arrow then go left
					if event.key == pygame.K_RIGHT:
						self.trump.goR() #if right arrow then go right
					if event.key == pygame.K_UP:
						self.trump.goU() #if up arrow then go up
					if event.key == pygame.K_DOWN:
						self.trump.goD() #if down arrow then go down
					if event.key == pygame.K_ESCAPE:
						self._running = False #if escape button then quit program and print score
						print ("You quit out of the game! Your score was ", self.trump.length)
				if event.type == pygame.QUIT:
					self._running = False
					print ("You quit out of the game! Your score was ", self.trump.length)
						#if red x button then quit program and print score

			self.Update() #calls update and create throughout the course of the game to make sure it runs smoothly
			self.Create()
		pygame.quit()
 
if __name__ == "__main__" : #run the game
	theApp = App()
	theApp.running()