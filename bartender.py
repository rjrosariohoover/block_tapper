#!/usr/bin/python

import pygame
from pygame.locals import *
import sys
from game_colors import *

MAX_Y = 563
MIN_Y = 263

class Bartender:
  #initialize with these parameters
  def __init__(self,x,y):
    self.locationx = x
    self.locationy = y 
    self.r = (0,0,0,0)

  def moveSelf(self,delta):
    #if direction == 1: #if going up
     #   if self.position == 1: #if at top and going up, send to position 4
      #      self.locationy = loc4y #top left at position 4
       #     self.position = 4 #track position by setting to position 4
        #else: #if going up in any other position
         #   self.position = self.locationy - 100 #move up by 100
          #  self.position = self.position -1 #move up one position
    #else: #used if going down
     #   if self.position == 4: #if at position 4 while going down
      #      self.locationy = loc1y #set to top position y coordinate
       #     self.position = 1 #track position by setting to position 1
        #else: #if going down from other position
         #   self.locationy = self.locationy + 100 #push down screen by 100
          #  self.position = self.position + 1 #track position by adding 1
    self.locationy += delta
    if(self.locationy >= MAX_Y):
      self.locationy = MAX_Y
    if(self.locationy <= MIN_Y):
      self.locationy = MIN_Y
    
    
  def draw(self,surf):
    self.r = pygame.Rect((0,0,45,75))
    self.r.center = (self.locationx,self.locationy)
    pygame.draw.rect(surf, BARTENDER, self.r)
