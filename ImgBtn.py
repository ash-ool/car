import pygame
from pygame import Vector2

from soundManager import soundManager
from utils import utils


class ImgBtn:
    def __init__(self,pos,img,text = "",font = utils.font16,textColor = (255,211,12)):
        self.pos = pos
        self.img = img
        self.clicked = False
        self.text = text
        self.font = font
        self.textColor = textColor

    def onMouseDown(self):
        mousePos = pygame.mouse.get_pos()
        if utils.pointInRect(Vector2(mousePos[0],mousePos[1]),self.getRect()):
            soundManager.play("click")
            self.clicked = True


    def onMouseUp(self):
        if self.clicked:
            self.clicked = False

    def getRect(self):
        return pygame.rect.Rect(self.pos.x, self.pos.y, self.img.get_rect().width, self.img.get_rect().h)

    def draw(self,screen):
        screen.blit(self.img,(self.pos.x,self.pos.y))
        if self.text != "":
            textT = self.font.render(self.text, True, self.textColor)
            text_rect = textT.get_rect(center=(self.pos.x + self.img.get_width() / 2, self.pos.y + self.img.get_height() - textT.get_height()/2 ))
            text_rect.y -= 4
            # if self.clicked:
            #     text_rect.y += 4
            screen.blit(textT, text_rect)