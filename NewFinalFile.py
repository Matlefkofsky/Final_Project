from random import randint
import pygame
import time
from pygame.locals import*
import os


def load_png(name): #this was taken from pygame website on loading pngs
	fullname = os.path.join('Media', name)
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error as message:
		print ('Cannot load image:' + fullname)
		raise SystemExit
	return image, image.get_rect() 

# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Trump_Orange = (255, 165, 0)	
blue = (0, 0, 255)

 
# Set the width and height of each snake segment
width = 18
height = 18
# Margin between each segment
margin = 2
 
# Set initial speed
x_change = width + margin
y_change = 0
 
 
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([width, height])
        self.image.fill(Trump_Orange)
        #self.image.fill(load_png('trump.png'))
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Trump Game')
 
