from random import randint
import pygame
import time
from pygame.locals import*
import os

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
        self.image = pygame.image.load('trump.bmp')
        self.rect = self.image.get_rect()
        #self.image = pygame.Surface([width, height])
        #self.image.fill(Trump_Orange)
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
 
allspriteslist = pygame.sprite.Group()
 
# Create an initial snake
snake_segments = []
for x in range(15):
    x = 300 - (width + margin) * x
    y = 40
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
 
 
clock = pygame.time.Clock()
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= (width + margin)
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change += (width + margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change -= (height + margin)
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change += (height + margin)


