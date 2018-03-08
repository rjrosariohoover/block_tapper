#!/usr/bin/python

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

locx = 473
MIN_Y = 263
MAX_Y = 563

FPS = 30

rand = random.random()

# define game world
def draw_world(surf):
    # surf is a pygame surface
    pygame.display.set_caption('Block Tapper: Serve Beers With the Force')

    # fill in sky/base layer
    surf.fill(BACKGROUND)

    # draw 4 tables
    pygame.draw.rect(surf,TABLE,(0,250,450,50))
    table2 = pygame.draw.rect(surf,TABLE,(0,350,450,50))
    table3 = pygame.draw.rect(surf,TABLE,(0,450,450,50))
    table4 = pygame.draw.rect(surf,TABLE,(0,550,450,50))

    # draw ghost boxes
    ghost_box1 = pygame.draw.rect(surf,BACKGROUND,(450,225,45,75))
    ghost_box2 = pygame.draw.rect(surf,BACKGROUND,(450,325,45,75))
    ghost_box3 = pygame.draw.rect(surf,BACKGROUND,(450,425,45,75))
    ghost_box4 = pygame.draw.rect(surf,BACKGROUND,(450,525,45,75))

    # draw billboard
    pygame.draw.rect(surf,RED,(100,20,400,60))
    Title = pygame.font.Font('freesansbold.ttf',36)
    TitleObj = Title.render('Craig\'s Craft Brews', True, BLUE)
    TitleRectObj = TitleObj.get_rect()
    TitleRectObj.center = (300,50)
    surf.blit(TitleObj, TitleRectObj)
    
def gameOver(str,surf,objs):
    fontObj = pygame.font.Font('freesansbold.ttf',32)
    textSurfaceObj = fontObj.render(str,True,BLUE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIDTH/2,150)
    surf.blit(textSurfaceObj,textRectObj)
    pygame.display.update()
    time.sleep(1)
    for obj in objs:
        obj.reset()
    time.sleep(1)  

def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    surf = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
    s = serial.Serial("/dev/ttyACM0",9600,timeout=0.5)
    # beers on table
    beer1 = beer.Beer(435, TABLE1_Y-17)
    beer2 = beer.Beer(435, TABLE2_Y-17)
    beer3 = beer.Beer(435, TABLE3_Y-17)
    beer4 = beer.Beer(435, TABLE4_Y-17)
    # draw bartender
    craig = bartender.Bartender(locx,MIN_Y)
    # draw customers
    my_customer1 = customer.Customer(0,TABLE1_Y-15)
    my_customer2 = customer.Customer(0,TABLE2_Y-15)
    my_customer3 = customer.Customer(0,TABLE3_Y-15)
    my_customer4 = customer.Customer(0,TABLE4_Y-15)
    objs = [beer1,beer2,beer3,beer4,craig,my_customer1,my_customer2,my_customer3,my_customer4]
    while True:           
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    craig.moveSelf(-100)
                if event.key == K_DOWN:
                    craig.moveSelf(100)
                if event.key == pygame.K_SPACE:
                    if craig.locationy == 263:
                        beer1.launch()
                    if craig.locationy == 363:
                        beer2.launch()
                    if craig.locationy == 463:
                        beer3.launch()
                    if craig.locationy == 563:
                        beer4.launch()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        rgb = read_arduino(s)
        if(rgb is None):
            continue # skip, and try again next time
        if rgb[0] > 150.0:
            craig.moveSelf(-100)
        if rgb[0] < 50.0:
            craig.moveSelf(100)
        if rgb[1] < 25.0:
            if craig.locationy == 263:
                beer1.launch()
            if craig.locationy == 363:
                beer2.launch()
            if craig.locationy == 463:
                beer3.launch()
            if craig.locationy == 563:
                beer4.launch()
        # 2. Do game logic
        my_customer1.arrive()
        my_customer1.move(1.0/FPS)
        my_customer2.arrive()
        my_customer2.move(1.0/FPS)
        my_customer3.arrive()
        my_customer3.move(1.0/FPS)
        my_customer4.arrive()
        beer1.move(1.0/FPS)
        beer2.move(1.0/FPS)
        beer3.move(1.0/FPS)
        beer4.move(1.0/FPS)
        my_customer4.move(1.0/FPS)
        #if moving hit (customer served)
        if beer1.hitBy(my_customer1) and beer1.isMoving():
            my_customer1.reset()
            beer1.reset()
        if beer2.hitBy(my_customer2) and beer2.isMoving():
            my_customer2.reset()
            beer2.reset()
        if beer3.hitBy(my_customer3) and beer3.isMoving():
            my_customer3.reset()
            beer3.reset()
        if beer4.hitBy(my_customer4) and beer4.isMoving():
            my_customer4.reset()
            beer4.reset()
        #if stationary hit (end of table)
        if beer1.hitBy(my_customer1):
            gameOver("Customer 1 is PISSED. You LOSE!",surf,objs)
        if beer2.hitBy(my_customer2):
            gameOver("Customer 2 is PISSED. You LOSE!",surf,objs)
        if beer3.hitBy(my_customer3):
            gameOver("Customer 3 is PISSED. You LOSE!",surf,objs)
        if beer4.hitBy(my_customer4):
            gameOver("Customer 4 is PISSED. You LOSE!",surf,objs)
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

def read_arduino(myserial):
    # ask for data
    myserial.write('p')
    # read the response
    vals = myserial.readline()
    # if arduino doesn't respond
    if(len(vals)==0):
        return None #...ignore
    # convert to an array of numbers
    rgb = [float(x) for x in vals.split(',')]
    return rgb

main()

# customer: __init__, move, draw, collision, reset/move_to 30 wide 40 tall
# beer: __init__, move, draw, reset/move_to -- 45 tall, 35 wide
# bartender: __init__, draw, move -- 40 wide, 75 tall

