#!/usr/bin/python

import pygame
from pygame.locals import *
import sys
from game_colors import *
import random
import math

class Customer:
  #initialize with these parameters
  def __init__(self,x,y):
    self.locationx = x
    self.locationy = y
    self.vx = 0
    self.rect = pygame.Rect((self.locationx,self.locationy,30,30))
    self.r = (0,0,0,0)

  #make him start moving
  def arrive(self):
    self.vx = random.random()*200

  #give customer velocity
  def move(self,time):
    self.locationx = self.locationx + self.vx*time

  def getRect(self):
    return self.r
    
  #make him reset to original position
  def reset(self):
    self.vx = 0
    self.locationx = 0
    
  #draw him
  def draw(self,surf):
    self.r = pygame.Rect((self.locationx,self.locationy,30,30))
    self.r.center = (self.locationx,self.locationy)
    pygame.draw.rect(surf, CUSTOMER, self.r)
