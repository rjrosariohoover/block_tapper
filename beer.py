import pygame
from game_colors import *

class Beer:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #self.rect = pygame.Rect((self.x,self.y,20.35))
        self.v_x = 0.0
        self.r = (0,0,0,0)

    def move(self,time):
        self.x = self.x + self.v_x*time

    def getRect(self):
        return self.rect
        
    def draw(self,surf):
        self.r = pygame.Rect((0,0,20,35))
        self.r.center = (self.x, self.y)
        pygame.draw.rect(surf,GLASS,self.r)
        
