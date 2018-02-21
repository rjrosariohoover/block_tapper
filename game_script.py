#!/usr/bin.python

import pygame, sys
from pygame.locals import *
import serial
import time
import random
import math

from game_colors import *

HEIGHT = 600
WIDTH = 600
FPS = 30
rand = random.random()
s = serial.Serial("/dev/ttyACM0")

# define game world
def draw_world(surf):
    # surf is a pygame surface
    pygame.display.set_caption('Block Tapper: The Customer is Always Right')

    # fill in sky/base layer
    surf.fill(BACKGROUND)

    # draw tables
    table1 = pygame.draw.rect(surf,TABLE,(0,250,450,50))
    table2 = pygame.draw.rect(surf,TABLE,(0,350,450,50))
    table3 = pygame.draw.rect(surf,TABLE,(0,450,450,50))
    table4 = pygame.draw.rect(surf,TABLE,(0,550,450,50))
    
    
# add more functions for logic as necessary

def main():
    while True:
        pygame.init()
        fpsClock = pygame.time.Clock()
        surf = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        draw_world(surf)
        pygame.display.update()
        fpsClock.tick(FPS)
main()

# customer: __init__, move, draw, collision, reset/move_to
# beer: __init__, move, draw, reset/move_to
# bartender: __init__, draw, move

