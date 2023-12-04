import pygame.image
from pygame import Vector2

from utils import utils


class Slider:
    def __init__(self,pos,value = -1):
        self.pos = pos
        self.min = self.pos.x + 50
        self.max = self.pos.x + 310
        self.knobPos = Vector2(self.max,pos.y + 11)
        if value != -1:
            self.knobPos.x = utils.lerp(self.min,self.max,value)
        self.sliderImg = pygame.image.load("images/slider.png")
        self.dragging = False

    def onMouseDown(self):
        mousePos = pygame.mouse.get_pos()
        if utils.pointInRect(Vector2(mousePos[0],mousePos[1]),self.getRect()):
            self.dragging = True


    def onMouseUp(self):
        if self.dragging:
            self.dragging = False

    def update(self):
        if not self.dragging:
            return
        mousePos = pygame.mouse.get_pos()
        self.knobPos.x = mousePos[0]
        if self.knobPos.x < self.min:
            self.knobPos.x = self.min
        if self.knobPos.x > self.max:
            self.knobPos.x = self.max

    def  getRect(self):
        return pygame.rect.Rect(self.pos.x,self.pos.y,self.sliderImg.get_rect().width,self.sliderImg.get_rect().h)

    def getValue(self):
        return utils.lerp(0,1,utils.lerpInv(self.knobPos.x,self.min,self.max))

    def draw(self, surface):
        surface.blit(self.sliderImg,(self.pos.x,self.pos.y))
        pygame.draw.circle(surface,(23,255,23),(self.knobPos.x,self.knobPos.y),12)