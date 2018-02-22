#!/usr/bin.python

import pygame, sys
from pygame.locals import *
import serial
import time
import random
import math

import customer
import bartender
import beer
from game_colors import *

HEIGHT = 600
WIDTH = 600

TABLE_X = 450
TABLE1_Y = 250
TABLE2_Y = 350
TABLE3_Y = 450
TABLE4_Y = 550

FPS = 30

rand = random.random()

#s = serial.Serial("/dev/ttyACM0")

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

    # draw ghost boxes
    ghost_box1 = pygame.draw.rect(surf,BACKGROUND,(450,225,45,75))
    ghost_box2 = pygame.draw.rect(surf,BACKGROUND,(450,325,45,75))
    ghost_box3 = pygame.draw.rect(surf,BACKGROUND,(450,425,45,75))
    ghost_box4 = pygame.draw.rect(surf,BACKGROUND,(450,525,45,75))
    
    
# add more functions for logic as necessary

def main():
    while True:
        pygame.init()
        fpsClock = pygame.time.Clock()
        surf = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
        # beers on table
        beer1 = beer.Beer(435, TABLE1_Y-17)
        beer2 = beer.Beer(435, TABLE2_Y-17)
        beer3 = beer.Beer(435, TABLE3_Y-17)
        beer4 = beer.Beer(435, TABLE4_Y-17)
        # draw bartender
        craig = bartender.Bartender(TABLE_X+23,TABLE1_Y+13)
        # draw customers
        my_customer = customer.Customer(0,TABLE1_Y-15)
        objs = [beer1,beer2,beer3,beer4,craig,my_customer]
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    craig.moveSelf(1)
                if event.key == pygame.K_DOWN:
                    craig.moveSelf(0)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 2. Do game logic
        my_customer.arrive()
        my_customer.move(1.0/FPS)
        #my_customer.hitBy(beer1)

        # 3. Draw Everything
        draw_world(surf)
        for obj in objs:
            obj.draw(surf)
        box1 = pygame.draw.rect(surf,BLACK,(0,200,50,50))
        box2 = pygame.draw.rect(surf,BLACK,(0,300,50,50))
        box3 = pygame.draw.rect(surf,BLACK,(0,400,50,50))
        box4 = pygame.draw.rect(surf,BLACK,(0,500,50,50))
        pygame.display.update()
        fpsClock.tick(FPS)
main()

# customer: __init__, move, draw, collision, reset/move_to 30 wide 40 tall
# beer: __init__, move, draw, reset/move_to -- 45 tall, 35 wide
# bartender: __init__, draw, move -- 40 wide, 75 tall

