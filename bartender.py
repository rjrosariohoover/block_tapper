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
    self.locationy += delta
    if(self.locationy >= MAX_Y):
      self.locationy = MAX_Y
    if(self.locationy <= MIN_Y):
      self.locationy = MIN_Y
    
  def draw(self,surf):
    self.r = pygame.Rect((0,0,45,75))
    self.r.center = (self.locationx,self.locationy)
    pygame.draw.rect(surf, BARTENDER, self.r)

  def reset(self):
    self.locationx = 473
    self.locationy = 263
