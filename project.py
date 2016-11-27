#Frames per second manipulation

#required 
from random import randint
import pygame
import time
from pygame.locals import*

pygame.init();

Trump = pygame.image.load('Media/trump.png').convert()

#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
Trump_Orange = (255, 165, 0)	

#position vars
x = 0
y = 0
x_delta = 0
y_delta = 0
clock = pygame.time.Clock()

hungryX = randint(20,750)
hungryY = randint(20,550)
#print (hungryX,hungryY)

#create a surface
gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

#lets add a title, aka "caption"
pygame.display.set_caption("Donald Trump Snake")
pygame.display.update()		#only updates portion specified


gameExit = False
while not gameExit:
	gameDisplay.fill(black)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	if event.type == pygame.KEYDOWN:
		x_delta=0;
		y_delta=0;
		if event.key == pygame.K_LEFT:
			x_delta -= 1
		if event.key == pygame.K_RIGHT:
			x_delta += 1
		if event.key == pygame.K_UP:
			y_delta -= 1
		if event.key == pygame.K_DOWN:
			y_delta += 1

	if x == hungryX: #When the X values are EXACTLY lined up this pushes the blue dot back to zero... can easily randomize a new HungryX
		#gameDisplay.Surface.blit(Trump,(100,100))
		hungryX = randint(20,750)
		hungryY = randint(20,550) #HOW CAN WE GET THIS TO A RANGE THO SO IT DOESNT HAVE TO BE EXACT?


	x +=x_delta
	y +=y_delta
	gameDisplay.fill(Trump_Orange, rect=[x,y, 20,20]) #place orange dot and control size
	gameDisplay.fill(blue, rect = [hungryX,hungryY,20,20]) #randomly place blue dot and controls size
	pygame.display.update()		
	clock.tick(30)



#required
pygame.quit()
quit()				#exits python