#!/usr/bin/python

import pygame
from pygame.locals import *
import sys
from game_colors import *

class Bartender:
  #initialize with these parameters
  def __init__(self,x,y):
    self.locationx = x
    self.locationy = y
    self.position = 1
    self.r = (0,0,0,0)

  def moveSelf(self,direction):
    if direction == 1: #if going up
        if self.position == 1: #if at top and going up, send to position 4
            self.locationy = 525 #top left at position 4
            self.position = 4 #track position by setting to position 4
        else: #if going up in any other position
            self.position = self.locationy - 100 #move up by 100
            self.position = self.position -1 #move up one position
    else: #used if going down
        if self.position == 4: #if at position 4 while going down
            self.locationy = 225 #set to top position y coordinate
            self.position = 1 #track position by setting to position 1
        else: #if going down from other position
            self.locationy = self.locationy + 100 #push down screen by 100
            self.position = self.position + 1 #track position by adding 1
           
  def draw(self,surf):
    self.r = pygame.Rect((0,0,45,75))
    self.r.center = (self.locationx,self.locationy)
    pygame.draw.rect(surf, BARTENDER, self.r)
