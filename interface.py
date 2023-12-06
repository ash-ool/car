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

    # button_G = pygame.Rect(174, 274, 250, 62)
    # button_C = pygame.Rect(174, 440, 250, 62)
    # button_S = pygame.Rect(174, 358, 250, 62)
    # button_Q = pygame.Rect(215, 585, 170, 62)
    # button_settings = pygame.Rect(913, 37, 50, 50)

    button_G = ImgBtn(Vector2(204,274),pygame.image.load("images/button1.png"),"GAME",utils.font32,(255,255,255))
    button_S = ImgBtn(Vector2(204, 274 + 70), pygame.image.load("images/button1.png"), "SETTINGS", utils.font32, (255, 255, 255))
    button_C = ImgBtn(Vector2(204, 274 + 70*2), pygame.image.load("images/button1.png"), "CREDITS", utils.font32,
                      (255, 255, 255))
    button_Q = ImgBtn(Vector2(204 + 27, 274 + 70 * 4), pygame.image.load("images/button2.png"), "QUIT", utils.font32,
                      (255, 255, 255))

    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # press on quit button
            if ev.type == pygame.MOUSEBUTTONUP:
                button_G.onMouseUp()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                button_G.onMouseDown()
                button_S.onMouseDown()
                button_C.onMouseDown()
                button_Q.onMouseDown()
                if button_Q.clicked:
                    pygame.quit()
                    sys.exit()
                if button_G.clicked:
                    game()
                    return
                if button_S.clicked:
                    settings()
                    return
                if button_C.clicked:
                    credits_()
                    return

        screen.blit(interface_image, (0, 0))

        button_G.draw(screen)
        button_S.draw(screen)
        button_C.draw(screen)
        button_Q.draw(screen)

        pygame.display.update()


def settings():
    interface_image = pygame.image.load("Images/settings.png")
    interface_image = pygame.transform.scale(interface_image, (1000, 720))

    # close_btn = pygame.Rect(460, 550, 120, 60)

    musicSlider = Slider(Vector2(1000/2 - 350/2,200),soundManager.getMusicVolume())
    effectSlider = Slider(Vector2(1000 / 2 - 350 / 2, 250), soundManager.getEffectVolume())
    closeBtn = ImgBtn(Vector2(utils.width - 150,  utils.height-50 ), pygame.image.load("images/button2.png"), "CLOSE", utils.font32,
                      (255, 255, 255))

    player1Images = [
        "images/faiscamcqueen.png",
        "images/faiscamcqueen2.png",
        "images/car3.png",
        "images/car4.png",
    ]
    currentPlayer1ImageI = 0
    i = 0
    for img in player1Images:
        if img == utils.player1Img:
            currentPlayer1ImageI = i
        if img == utils.player2Img:
            currentPlayer2ImageI = i
        i += 1


    p1Pos = Vector2(120,400)
    leftBtn = ImgBtn(Vector2(p1Pos.x,p1Pos.y),pygame.image.load("images/leftBtn.png"))
    rightBtn = ImgBtn(Vector2(p1Pos.x + 270, p1Pos.y), pygame.image.load("images/rightBtn.png"))

    p2Pos = Vector2(600, 400)
    leftBtn2 = ImgBtn(Vector2(p2Pos.x, p2Pos.y), pygame.image.load("images/leftBtn.png"))
    rightBtn2 = ImgBtn(Vector2(p2Pos.x + 270, p2Pos.y), pygame.image.load("images/rightBtn.png"))

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
                leftBtn2.onMouseDown()
                rightBtn2.onMouseDown()

                closeBtn.onMouseDown()
                if leftBtn.clicked:
                    currentPlayer1ImageI -= 1
                elif rightBtn.clicked:
                    currentPlayer1ImageI += 1
                if currentPlayer1ImageI < 0:
                    currentPlayer1ImageI = len(player1Images) - 1
                elif currentPlayer1ImageI > len(player1Images)-1:
                    currentPlayer1ImageI = 0

                if leftBtn2.clicked:
                    currentPlayer2ImageI -= 1
                elif rightBtn2.clicked:
                    currentPlayer2ImageI += 1
                if currentPlayer2ImageI < 0:
                    currentPlayer2ImageI = len(player1Images) - 1
                elif currentPlayer2ImageI > len(player1Images)-1:
                    currentPlayer2ImageI = 0

                utils.player1Img = player1Images[currentPlayer1ImageI]
                utils.player2Img = player1Images[currentPlayer2ImageI]

                if closeBtn.clicked:
                    soundManager.play("click")
                    interface()
                    return
            if ev.type == pygame.MOUSEBUTTONUP:
                musicSlider.onMouseUp()
                soundManager.setMusicVolume(musicSlider.getValue())
                effectSlider.onMouseUp()
                soundManager.setEffectVolume(effectSlider.getValue())

                leftBtn.onMouseUp()
                rightBtn.onMouseUp()
                leftBtn2.onMouseUp()
                rightBtn2.onMouseUp()

        screen.blit(interface_image, (0, 0))

        musicSlider.update()
        musicSlider.draw(screen)

        effectSlider.update()
        effectSlider.draw(screen)

        closeBtn.draw(screen)

        utils.drawText(Vector2(250,200),"Music",(233,233,12),utils.font24,screen)
        utils.drawText(Vector2(250, 200 + 50), "Effect", (233, 233, 12), utils.font24, screen)

        settingTextT = utils.font48.render("SETTING", True, (233,213,12))
        utils.drawText(Vector2(utils.width/2 - settingTextT.get_width()/2, 60), "SETTING", (233, 233, 12), utils.font48, screen)

        player = pygame.transform.scale(pygame.image.load(player1Images[currentPlayer1ImageI]),(100,170))
        screen.blit(player,(p1Pos.x + 102,p1Pos.y- 20))
        leftBtn.draw(screen)
        rightBtn.draw(screen)
        utils.drawText(Vector2(p1Pos.x - 20,p1Pos.y - 50), "Player-1: ", (233, 233, 12),
                       utils.font24, screen)

        player2 = pygame.transform.scale(pygame.image.load(player1Images[currentPlayer2ImageI]), (100, 170))
        screen.blit(player2, (p2Pos.x + 102, p2Pos.y - 20))
        leftBtn2.draw(screen)
        rightBtn2.draw(screen)
        utils.drawText(Vector2(p2Pos.x - 20, p2Pos.y - 50), "Player-2: ", (233, 233, 12),
                       utils.font24, screen)

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


