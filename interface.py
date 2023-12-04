import pygame
import sys

from pygame import Vector2

from ImgBtn import ImgBtn
from Slider import Slider
from game import car_racing
from multiplayer import multi_player
from soundManager import soundManager
from utils import utils

# initiating pygames
pygame.init()
# creating the screen 720x720 pixels
res = (1000, 720)
screen = pygame.display.set_mode(res)


# Creating a function that creates the GUI

def interface():
    soundManager.playMusic()
    interface_image = pygame.image.load("Images/M_menu.png")
    interface_image = pygame.transform.scale(interface_image, (1000, 720))

    button_G = pygame.Rect(174, 274, 250, 62)
    button_C = pygame.Rect(174, 440, 250, 62)
    button_S = pygame.Rect(174, 358, 250, 62)
    button_Q = pygame.Rect(215, 585, 170, 62)
    # button_settings = pygame.Rect(913, 37, 50, 50)

    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if button_Q.collidepoint((mx, my)):
                    soundManager.play("click")
                    pygame.quit()
                    sys.exit()

                if button_G.collidepoint((mx, my)):
                    soundManager.play("click")
                    game()

                if button_S.collidepoint((mx, my)):
                    soundManager.play("click")
                    settings()

                if button_C.collidepoint((mx, my)):
                    soundManager.play("click")
                    credits_()

        screen.blit(interface_image, (0, 0))
        pygame.display.update()


def settings():
    interface_image = pygame.image.load("Images/settings.png")
    interface_image = pygame.transform.scale(interface_image, (1000, 720))

    close_btn = pygame.Rect(460, 550, 120, 60)

    musicSlider = Slider(Vector2(1000/2 - 350/2,200),soundManager.getMusicVolume())
    effectSlider = Slider(Vector2(1000 / 2 - 350 / 2, 250), soundManager.getEffectVolume())

    player1Images = [
        "images/faiscamcqueen.png",
        "images/faiscamcqueen2.png",
        "images/car3.png",
        "images/car4.png",
    ]
    currentPlayerImageI = 0
    i = 0
    for img in player1Images:
        if img == utils.playerImg:
            currentPlayerImageI = i
        i += 1

    leftBtn = ImgBtn(Vector2(350,400),pygame.image.load("images/leftBtn.png"))
    rightBtn = ImgBtn(Vector2(620, 400), pygame.image.load("images/rightBtn.png"))


    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                musicSlider.onMouseDown()
                effectSlider.onMouseDown()

                leftBtn.onMouseDown()
                rightBtn.onMouseDown()
                if leftBtn.clicked:
                    currentPlayerImageI -= 1
                elif rightBtn.clicked:
                    currentPlayerImageI += 1
                if currentPlayerImageI < 0:
                    currentPlayerImageI = len(player1Images) - 1
                elif currentPlayerImageI > len(player1Images)-1:
                    currentPlayerImageI = 0
                utils.playerImg = player1Images[currentPlayerImageI]

                if close_btn.collidepoint((mx, my)):
                    soundManager.play("click")
                    interface()
            if ev.type == pygame.MOUSEBUTTONUP:
                musicSlider.onMouseUp()
                soundManager.setMusicVolume(musicSlider.getValue())
                effectSlider.onMouseUp()
                soundManager.setEffectVolume(effectSlider.getValue())

                leftBtn.onMouseUp()
                rightBtn.onMouseUp()

        screen.blit(interface_image, (0, 0))

        musicSlider.update()
        musicSlider.draw(screen)

        effectSlider.update()
        effectSlider.draw(screen)

        utils.drawText(Vector2(250,200),"Music",(233,233,12),utils.font24,screen)
        utils.drawText(Vector2(250, 200 + 50), "Effect", (233, 233, 12), utils.font24, screen)

        player = pygame.transform.scale(pygame.image.load(player1Images[currentPlayerImageI]),(100,170))
        screen.blit(player,(utils.width/2 - player.get_rect().width/2,320))
        leftBtn.draw(screen)
        rightBtn.draw(screen)

        pygame.display.update()


def credits_():
    interface_image = pygame.image.load("Images/C_menu.png")
    interface_image = pygame.transform.scale(interface_image, (1000, 720))

    button_B = pygame.Rect(15, 15, 50, 50)
    button_I = pygame.Rect(936, 15, 50, 50)

    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if button_B.collidepoint((mx, my)):
                    interface()

        screen.blit(interface_image, (0, 0))

        pygame.display.update()


def how_to_play(flag):
    interface_image = pygame.image.load("Images/H_menu.png")
    interface_image = pygame.transform.scale(interface_image, (1000, 720))

    button_B = pygame.Rect(15, 15, 50, 50)
    button_I = pygame.Rect(830, 550, 100, 100)

    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if button_I.collidepoint((mx, my)):
                    if flag == 1:
                        car_racing()
                    elif flag == 2:
                        multi_player()

        screen.blit(interface_image, (0, 0))

        pygame.display.update()


def info():
    interface_image = pygame.image.load("Images/C_menu_01.png")
    interface_image = pygame.transform.scale(interface_image, (1000, 720))

    button_B = pygame.Rect(15, 15, 50, 50)

    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if button_B.collidepoint((mx, my)):
                    interface()

        screen.blit(interface_image, (0, 0))
        pygame.display.update()


def game():
    interface_image = pygame.image.load("Images/G_menu_01.png")
    interface_image = pygame.transform.scale(interface_image, (1000, 720))

    button_S = pygame.Rect(267, 282, 466, 91)
    button_M = pygame.Rect(267, 413, 466, 91)

    button_B = pygame.Rect(15, 15, 50, 50)
    button_I = pygame.Rect(936, 15, 50, 50)

    # interface loop
    while True:
        # getting the input of the user

        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if button_M.collidepoint((mx, my)):
                    # multi_player()
                    how_to_play(2)

                if button_S.collidepoint((mx, my)):
                    # car_racing()
                    how_to_play(1)

                if button_I.collidepoint((mx, my)):
                    info()

                if button_B.collidepoint((mx, my)):
                    interface()

        screen.blit(interface_image, (0, 0))

        pygame.display.update()


