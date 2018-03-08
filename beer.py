import pygame
from game_colors import *

class Beer:
    def __init__(self,x,y):

        self.rect = pygame.Rect((x,y,20,35))
        self.v_x = 0


    def move(self,time):
        self.rect.x = self.rect.x + self.v_x*time

    def hitBy(self,obj):
        return self.rect.colliderect(obj.getRect())

    def isMoving(self):
        if(self.v_x != 0):
            return True
        else:
            return False

    def getRect(self):
        return self.rect

    def launch(self):
        self.v_x = -40

    def reset(self):
        self.v_x = 0
        self.rect.x = 435
        
    def draw(self,surf):
        pygame.draw.rect(surf,GLASS,self.rect)
        
