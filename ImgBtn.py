import pygame
from pygame import Vector2

from utils import utils


class ImgBtn:
    def __init__(self,pos,img):
        self.pos = pos
        self.img = img
        self.clicked = False

    def onMouseDown(self):
        mousePos = pygame.mouse.get_pos()
        if utils.pointInRect(Vector2(mousePos[0],mousePos[1]),self.getRect()):
            self.clicked = True


    def onMouseUp(self):
        if self.clicked:
            self.clicked = False

    def getRect(self):
        return pygame.rect.Rect(self.pos.x, self.pos.y, self.img.get_rect().width, self.img.get_rect().h)

    def draw(self,screen):
        screen.blit(self.img,(self.pos.x,self.pos.y))