#Tic Tac Toe

import pygame
import time
import random

# Screen Parameters
pygame.init()
X = 420
Y = 490

screen = pygame.display.set_mode((X, Y), pygame.NOFRAME)

# Things to do
# Title screen

# Colours
purple = (78, 24, 171)
orange = (252, 148, 3)
black = (0, 0, 0)
white = (255, 255, 255)
background = (20, 189, 168)
green = (53, 252, 3)
screen.fill(background)


def title():
    global game
    tap = 1
    game = 0
    screen.fill(background)
    pygame.display.update()
    title_font = pygame.font.Font('freesansbold.ttf', 36)
    title = title_font.render('tic-tac-toe'.upper(), True, black)
    title_rect = title.get_rect(center=(X / 2, Y / 4))
    screen.blit(title, title_rect)

    text_font = pygame.font.Font('freesansbold.ttf', 18)
    text1 = text_font.render('Tic-Tac-Toe'.upper(), True, black)
    text1_rect = text1.get_rect(center=(135, 225))
    screen.blit(text1, text1_rect)

    text2 = text_font.render('3 player'.upper(), True, black)
    text2_rect = text2.get_rect(center=(275, 225))
    screen.blit(text2, text2_rect)

    text3 = text_font.render('Speed'.upper(), True, black)
    text3_rect = text3.get_rect(center=(135, 300))
    screen.blit(text3, text3_rect)

    text4 = text_font.render('Invisible'.upper(), True, black)
    text4_rect = text4.get_rect(center=(275, 300))
    screen.blit(text4, text4_rect)

    text5 = text_font.render('reverse'.upper(), True, black)
    text5_rect = text5.get_rect(center=(135, 375))
    screen.blit(text5, text5_rect)

    text6 = text_font.render('random'.upper(), True, black)
    text6_rect = text6.get_rect(center=(275, 375))
    screen.blit(text6, text6_rect)

    original = pygame.draw.rect(screen, black, pygame.Rect(70, 200, 130, 50), 3)
    three_play = pygame.draw.rect(screen, black, pygame.Rect(210, 200, 130, 50), 3)
    speedy = pygame.draw.rect(screen, black, pygame.Rect(70, 275, 130, 50), 3)
    invis = pygame.draw.rect(screen, black, pygame.Rect(210, 275, 130, 50), 3)
    rewind = pygame.draw.rect(screen, black, pygame.Rect(70, 350, 130, 50), 3)
    rando = pygame.draw.rect(screen, black, pygame.Rect(210, 350, 130, 50), 3)

    creds = pygame.image.load("info.png")
    creds = pygame.transform.scale(creds, (40, 40))
    credsRect = creds.get_rect()
    credsRect = credsRect.move((360, 20))
    screen.blit(creds, credsRect)

    mouse = pygame.image.load("mouse.png")
    mouse = pygame.transform.scale(mouse, (40, 40))
    mouseRect = mouse.get_rect()
    mouseRect = mouseRect.move((360, 430))
    screen.blit(mouse, mouseRect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if original.collidepoint(event.pos):
                    screen.fill(background)
                    tictactoe()
                elif three_play.collidepoint(event.pos):
                    screen.fill(background)
                    three_player()
                elif speedy.collidepoint(event.pos):
                    screen.fill(background)
                    speed()
                elif invis.collidepoint(event.pos):
                    screen.fill(background)
                    invisible()
                elif rewind.collidepoint(event.pos):
                    screen.fill(background)
                    reverse()
                elif rando.collidepoint(event.pos):
                    screen.fill(background)
                    randomgame()
                elif credsRect.collidepoint(event.pos):
                    screen.fill(background)
                    credits()
                elif mouseRect.collidepoint(event.pos):
                    tap += 1
                    if tap % 2 == 0:
                        tappy = False
                    else:
                        tappy = True
                    pygame.mouse.set_visible(tappy)


def tictactoe():
    global game
    # Variables
    ## x's
    up_left_x = False
    left_x = False
    down_left_x = False
    up_x = False
    mid_x = False
    down_x = False
    up_right_x = False
    right_x = False
    down_right_x = False

    ## y's
    up_left_o = False
    left_o = False
    down_left_o = False
    up_o = False
    mid_o = False
    down_o = False
    up_right_o = False
    right_o = False
    down_right_o = False
    if game == 0:
        game = 1
    turn = 0
    tiles = 0
    colour_x = black
    colour_o = background
    # Font
    font = pygame.font.Font('freesansbold.ttf', 160)
    win_font = pygame.font.Font('freesansbold.ttf', 320)
    indicator_font = pygame.font.Font('freesansbold.ttf', 40)
    x_letter = font.render('x', True, purple)
    o_letter = font.render('o', True, orange)
    win_x = win_font.render('x', True, black)
    win_xRect = win_x.get_rect(center=(X / 2, Y / 2))
    win_o = win_font.render('o', True, black)
    win_oRect = win_o.get_rect(center=(X / 2, Y / 2))
    tie = win_font.render('xo', True, black)
    tieRect = tie.get_rect(center=(X / 2, Y / 2))
    while True:
        indicator_x = indicator_font.render('x turn', True, colour_x)
        indicator_xRect = indicator_x.get_rect(center=(X / 2, 455))
        indicator_o = indicator_font.render('o turn', True, colour_o)
        indicator_oRect = indicator_o.get_rect(center=(X / 2, 455))
        # Points To Click For X's And O's
        left = pygame.draw.rect(screen, background, pygame.Rect(0, 140, X / 3, 140))
        bottom_left = pygame.draw.rect(screen, background, pygame.Rect(0, 280, X / 3, 140))
        top_left = pygame.draw.rect(screen, background, pygame.Rect(0, 0, X / 3, 140))
        mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 140, X / 3, 140))
        top_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 0, X / 3, 140))
        bottom_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 280, X / 3, 140))
        right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 140, X / 3, 140))
        top_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 0, X / 3, 140))
        bottom_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 280, X / 3, 140))
        if turn % 2 == 1:
            screen.blit(indicator_x, indicator_xRect)
            screen.blit(indicator_o, indicator_oRect)
        else:
            screen.blit(indicator_o, indicator_oRect)
            screen.blit(indicator_x, indicator_xRect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if left_o:
                            turn -= 1
                            tiles -= 1
                        elif left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            left_x = True
                    else:
                        if left_x:
                            turn -= 1
                            tiles -= 1
                        elif left_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            left_o = True
                if bottom_left.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if down_left_o:
                            turn -= 1
                            tiles -= 1
                        elif down_left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_left_x = True
                    else:
                        if down_left_x:
                            turn -= 1
                            tiles -= 1
                        elif down_left_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_left_o = True
                if top_left.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if up_left_o:
                            turn -= 1
                            tiles -= 1
                        elif up_left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_left_x = True
                    else:
                        if up_left_x:
                            turn -= 1
                            tiles -= 1
                        elif up_left_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_left_o = True
                if mid.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if mid_o:
                            turn -= 1
                            tiles -= 1
                        elif mid_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            mid_x = True
                    else:
                        if mid_x:
                            turn -= 1
                            tiles -= 1
                        elif mid_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            mid_o = True
                if top_mid.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if up_o:
                            turn -= 1
                            tiles -= 1
                        elif up_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_x = True
                    else:
                        if up_x:
                            turn -= 1
                            tiles -= 1
                        elif up_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_o = True
                if bottom_mid.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if down_o:
                            turn -= 1
                            tiles -= 1
                        elif down_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_x = True
                    else:
                        if down_x:
                            turn -= 1
                            tiles -= 1
                        elif down_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_o = True
                if right.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if right_o:
                            turn -= 1
                            tiles -= 1
                        elif right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            right_x = True
                    else:
                        if right_x:
                            turn -= 1
                            tiles -= 1
                        elif right_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            right_o = True
                if top_right.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if up_right_o:
                            turn -= 1
                            tiles -= 1
                        elif up_right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_right_x = True
                    else:
                        if up_right_x:
                            turn -= 1
                            tiles -= 1
                        elif up_right_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_right_o = True
                if bottom_right.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if down_right_o:
                            turn -= 1
                            tiles -= 1
                        elif down_right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_right_x = True
                    else:
                        if down_right_x:
                            turn -= 1
                            tiles -= 1
                        elif down_right_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_right_o = True
        pygame.draw.rect(screen, black, pygame.Rect(X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(2 * X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(0, 140, X, 5))
        pygame.draw.rect(screen, black, pygame.Rect(0, 280, X, 5))
        if turn % 2 == 1:
            colour_o = black
            colour_x = background
        else:
            colour_x = black
            colour_o = background
        # x's
        if up_left_x:
            xRect = x_letter.get_rect(center=(70, 70))
            screen.blit(x_letter, xRect)
        if left_x:
            xRect = x_letter.get_rect(center=(70, 210))
            screen.blit(x_letter, xRect)
        if down_left_x:
            xRect = x_letter.get_rect(center=(70, 350))
            screen.blit(x_letter, xRect)
        if up_x:
            xRect = x_letter.get_rect(center=(210, 70))
            screen.blit(x_letter, xRect)
        if mid_x:
            xRect = x_letter.get_rect(center=(210, 210))
            screen.blit(x_letter, xRect)
        if down_x:
            xRect = x_letter.get_rect(center=(210, 350))
            screen.blit(x_letter, xRect)
        if up_right_x:
            xRect = x_letter.get_rect(center=(350, 70))
            screen.blit(x_letter, xRect)
        if right_x:
            xRect = x_letter.get_rect(center=(350, 210))
            screen.blit(x_letter, xRect)
        if down_right_x:
            xRect = x_letter.get_rect(center=(350, 350))
            screen.blit(x_letter, xRect)

        # o's
        if up_left_o:
            oRect = o_letter.get_rect(center=(70, 70))
            screen.blit(o_letter, oRect)
        if left_o:
            oRect = o_letter.get_rect(center=(70, 210))
            screen.blit(o_letter, oRect)
        if down_left_o:
            oRect = o_letter.get_rect(center=(70, 350))
            screen.blit(o_letter, oRect)
        if up_o:
            oRect = o_letter.get_rect(center=(210, 70))
            screen.blit(o_letter, oRect)
        if mid_o:
            oRect = o_letter.get_rect(center=(210, 210))
            screen.blit(o_letter, oRect)
        if down_o:
            oRect = o_letter.get_rect(center=(210, 350))
            screen.blit(o_letter, oRect)
        if up_right_o:
            oRect = o_letter.get_rect(center=(350, 70))
            screen.blit(o_letter, oRect)
        if right_o:
            oRect = o_letter.get_rect(center=(350, 210))
            screen.blit(o_letter, oRect)
        if down_right_o:
            oRect = o_letter.get_rect(center=(350, 350))
            screen.blit(o_letter, oRect)
        pygame.display.update()
        if up_left_x and down_left_x and left_x or up_x and down_x and mid_x or up_right_x and down_right_x and right_x or up_left_x and up_x and up_right_x or left_x and mid_x and right_x or down_left_x and down_x and down_right_x or up_left_x and mid_x and down_right_x or up_right_x and mid_x and down_left_x:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_x, win_xRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif up_left_o and down_left_o and left_o or up_o and down_o and mid_o or up_right_o and down_right_o and right_o or up_left_o and up_o and up_right_o or left_o and mid_o and right_o or down_left_o and down_o and down_right_o or up_left_o and mid_o and down_right_o or up_right_o and mid_o and down_left_o:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_o, win_oRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif tiles == 9:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(tie, tieRect)
            pygame.display.update()
            time.sleep(1)
            play_again()


def invisible():
    global game
    # Variables
    ## x's
    up_left_x = False
    left_x = False
    down_left_x = False
    up_x = False
    mid_x = False
    down_x = False
    up_right_x = False
    right_x = False
    down_right_x = False

    ## y's
    up_left_o = False
    left_o = False
    down_left_o = False
    up_o = False
    mid_o = False
    down_o = False
    up_right_o = False
    right_o = False
    down_right_o = False
    if game == 0:
        game = 2
    turn = 0
    tiles = 0
    colour_x = black
    colour_o = background
    # Font
    font = pygame.font.Font('freesansbold.ttf', 160)
    win_font = pygame.font.Font('freesansbold.ttf', 320)
    indicator_font = pygame.font.Font('freesansbold.ttf', 40)

    x_letter = font.render('x', True, purple)
    o_letter = font.render('o', True, orange)
    win_x = win_font.render('x', True, black)
    win_xRect = win_x.get_rect(center=(X / 2, Y / 2))
    win_o = win_font.render('o', True, black)
    win_oRect = win_o.get_rect(center=(X / 2, Y / 2))
    tie = win_font.render('xo', True, black)
    tieRect = tie.get_rect(center=(X / 2, Y / 2))
    while True:
        indicator_x = indicator_font.render('x turn', True, colour_x)
        indicator_xRect = indicator_x.get_rect(center=(X / 2, 455))
        indicator_o = indicator_font.render('o turn', True, colour_o)
        indicator_oRect = indicator_o.get_rect(center=(X / 2, 455))
        # Points To Click For X's And O's
        left = pygame.draw.rect(screen, background, pygame.Rect(0, Y / 3, X / 3, 140))
        bottom_left = pygame.draw.rect(screen, background, pygame.Rect(0, 2 * 140, X / 3, 140))
        top_left = pygame.draw.rect(screen, background, pygame.Rect(0, 0, X / 3, 140))
        mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, Y / 3, X / 3, 140))
        top_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 0, X / 3, 140))
        bottom_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 2 * Y / 3, X / 3, 140))
        right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, Y / 3, X / 3, 140))
        top_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 0, X / 3, 140))
        bottom_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 2 * Y / 3, X / 3, 140))
        if turn % 2 == 1:
            screen.blit(indicator_x, indicator_xRect)
            screen.blit(indicator_o, indicator_oRect)
        else:
            screen.blit(indicator_o, indicator_oRect)
            screen.blit(indicator_x, indicator_xRect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if left_o:
                            turn -= 1
                            tiles -= 1
                        elif left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            left_x = True
                    else:
                        if left_x:
                            turn -= 1
                            tiles -= 1
                        elif left_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            left_o = True
                if bottom_left.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if down_left_o:
                            turn -= 1
                            tiles -= 1
                        elif down_left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_left_x = True
                    else:
                        if down_left_x:
                            turn -= 1
                            tiles -= 1
                        elif down_left_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_left_o = True
                if top_left.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if up_left_o:
                            turn -= 1
                            tiles -= 1
                        elif up_left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_left_x = True
                    else:
                        if up_left_x:
                            turn -= 1
                            tiles -= 1
                        elif up_left_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_left_o = True
                if mid.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if mid_o:
                            turn -= 1
                            tiles -= 1
                        elif mid_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            mid_x = True
                    else:
                        if mid_x:
                            turn -= 1
                            tiles -= 1
                        elif mid_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            mid_o = True
                if top_mid.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if up_o:
                            turn -= 1
                            tiles -= 1
                        elif up_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_x = True
                    else:
                        if up_x:
                            turn -= 1
                            tiles -= 1
                        elif up_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_o = True
                if bottom_mid.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if down_o:
                            turn -= 1
                            tiles -= 1
                        elif down_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_x = True
                    else:
                        print('o')
                        if down_x:
                            turn -= 1
                            tiles -= 1
                        elif down_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_o = True
                if right.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if right_o:
                            turn -= 1
                            tiles -= 1
                        elif right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            right_x = True
                    else:
                        if right_x:
                            turn -= 1
                            tiles -= 1
                        elif right_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            right_o = True
                if top_right.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if up_right_o:
                            turn -= 1
                            tiles -= 1
                        elif up_right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_right_x = True
                    else:
                        if up_right_x:
                            turn -= 1
                            tiles -= 1
                        elif up_right_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_right_o = True
                if bottom_right.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if down_right_o:
                            turn -= 1
                            tiles -= 1
                        elif down_right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_right_x = True
                    else:
                        if down_right_x:
                            turn -= 1
                            tiles -= 1
                        elif down_right_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_right_o = True
        pygame.draw.rect(screen, black, pygame.Rect(X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(2 * X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(0, 140, X, 5))
        pygame.draw.rect(screen, black, pygame.Rect(0, 2 * 140, X, 5))

        pygame.display.update()
        if turn % 2 == 1:
            colour_o = black
            colour_x = background
        else:
            colour_x = black
            colour_o = background
        if up_left_x and down_left_x and left_x or up_x and down_x and mid_x or up_right_x and down_right_x and right_x or up_left_x and up_x and up_right_x or left_x and mid_x and right_x or down_left_x and down_x and down_right_x or up_left_x and mid_x and down_right_x or up_right_x and mid_x and down_left_x:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_x, win_xRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif up_left_o and down_left_o and left_o or up_o and down_o and mid_o or up_right_o and down_right_o and right_o or up_left_o and up_o and up_right_o or left_o and mid_o and right_o or down_left_o and down_o and down_right_o or up_left_o and mid_o and down_right_o or up_right_o and mid_o and down_left_o:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_o, win_oRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif tiles == 9:
            print('tie')
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(tie, tieRect)
            pygame.display.update()
            time.sleep(1)
            play_again()


def reverse():
    global game
    # Variables
    ## x's
    up_left_x = False
    left_x = False
    down_left_x = False
    up_x = False
    mid_x = False
    down_x = False
    up_right_x = False
    right_x = False
    down_right_x = False

    ## y's
    up_left_o = False
    left_o = False
    down_left_o = False
    up_o = False
    mid_o = False
    down_o = False
    up_right_o = False
    right_o = False
    down_right_o = False
    if game == 0:
        game = 3
    turn = 0
    tiles = 0
    colour_x = black
    colour_o = background
    # Font
    font = pygame.font.Font('freesansbold.ttf', 160)
    win_font = pygame.font.Font('freesansbold.ttf', 320)
    indicator_font = pygame.font.Font('freesansbold.ttf', 40)
    x_letter = font.render('x', True, purple)
    o_letter = font.render('o', True, orange)
    win_x = win_font.render('x', True, black)
    win_xRect = win_x.get_rect(center=(X / 2, Y / 2))
    win_o = win_font.render('o', True, black)
    win_oRect = win_o.get_rect(center=(X / 2, Y / 2))
    tie = win_font.render('xo', True, black)
    tieRect = tie.get_rect(center=(X / 2, Y / 2))
    while True:
        indicator_x = indicator_font.render('x turn', True, colour_x)
        indicator_xRect = indicator_x.get_rect(center=(X / 2, 455))
        indicator_o = indicator_font.render('o turn', True, colour_o)
        indicator_oRect = indicator_o.get_rect(center=(X / 2, 455))
        # Points To Click For X's And O's
        left = pygame.draw.rect(screen, background, pygame.Rect(0, 140, X / 3, 140))
        bottom_left = pygame.draw.rect(screen, background, pygame.Rect(0, 280, X / 3, 140))
        top_left = pygame.draw.rect(screen, background, pygame.Rect(0, 0, X / 3, 140))
        mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 140, X / 3, 140))
        top_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 0, X / 3, 140))
        bottom_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 280, X / 3, 140))
        right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 140, X / 3, 140))
        top_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 0, X / 3, 140))
        bottom_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 280, X / 3, 140))
        if turn % 2 == 1:
            screen.blit(indicator_x, indicator_xRect)
            screen.blit(indicator_o, indicator_oRect)
        else:
            screen.blit(indicator_o, indicator_oRect)
            screen.blit(indicator_x, indicator_xRect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if left_o:
                            turn -= 1
                            tiles -= 1
                        elif left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            left_x = True
                    else:
                        print('o')
                        if left_x:
                            turn -= 1
                            tiles -= 1
                        elif left_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            left_o = True
                if bottom_left.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if down_left_o:
                            turn -= 1
                            tiles -= 1
                        elif down_left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_left_x = True
                    else:
                        print('o')
                        if down_left_x:
                            turn -= 1
                            tiles -= 1
                        elif down_left_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_left_o = True
                if top_left.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if up_left_o:
                            turn -= 1
                            tiles -= 1
                        elif up_left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_left_x = True
                    else:
                        if up_left_x:
                            turn -= 1
                            tiles -= 1
                        elif up_left_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_left_o = True
                if mid.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if mid_o:
                            turn -= 1
                            tiles -= 1
                        elif mid_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            mid_x = True
                    else:
                        if mid_x:
                            turn -= 1
                            tiles -= 1
                        elif mid_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            mid_o = True
                if top_mid.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if up_o:
                            turn -= 1
                            tiles -= 1
                        elif up_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_x = True
                    else:
                        if up_x:
                            turn -= 1
                            tiles -= 1
                        elif up_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_o = True
                if bottom_mid.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if down_o:
                            turn -= 1
                            tiles -= 1
                        elif down_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_x = True
                    else:
                        if down_x:
                            turn -= 1
                            tiles -= 1
                        elif down_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_o = True
                if right.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        if right_o:
                            turn -= 1
                            tiles -= 1
                        elif right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            right_x = True
                    else:
                        if right_x:
                            turn -= 1
                            tiles -= 1
                        elif right_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            right_o = True
                if top_right.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if up_right_o:
                            turn -= 1
                            tiles -= 1
                        elif up_right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_right_x = True
                    else:
                        if up_right_x:
                            turn -= 1
                            tiles -= 1
                        elif up_right_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_right_o = True
                if bottom_right.collidepoint(event.pos):
                    turn += 1
                    tiles += 1
                    if turn % 2 == 1:
                        print('x')
                        if down_right_o:
                            turn -= 1
                            tiles -= 1
                        elif down_right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_right_x = True
                    else:
                        if down_right_x:
                            turn -= 1
                            tiles -= 1
                        elif down_right_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_right_o = True
        pygame.draw.rect(screen, black, pygame.Rect(X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(2 * X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(0, 140, X, 5))
        pygame.draw.rect(screen, black, pygame.Rect(0, 280, X, 5))
        if turn % 2 == 1:
            colour_o = black
            colour_x = background
        else:
            colour_x = black
            colour_o = background
        # x's
        if up_left_x:
            xRect = x_letter.get_rect(center=(70, 70))
            screen.blit(x_letter, xRect)
        if left_x:
            xRect = x_letter.get_rect(center=(70, 210))
            screen.blit(x_letter, xRect)
        if down_left_x:
            xRect = x_letter.get_rect(center=(70, 350))
            screen.blit(x_letter, xRect)
        if up_x:
            xRect = x_letter.get_rect(center=(210, 70))
            screen.blit(x_letter, xRect)
        if mid_x:
            xRect = x_letter.get_rect(center=(210, 210))
            screen.blit(x_letter, xRect)
        if down_x:
            xRect = x_letter.get_rect(center=(210, 350))
            screen.blit(x_letter, xRect)
        if up_right_x:
            xRect = x_letter.get_rect(center=(350, 70))
            screen.blit(x_letter, xRect)
        if right_x:
            xRect = x_letter.get_rect(center=(350, 210))
            screen.blit(x_letter, xRect)
        if down_right_x:
            xRect = x_letter.get_rect(center=(350, 350))
            screen.blit(x_letter, xRect)

        # o's
        if up_left_o:
            oRect = o_letter.get_rect(center=(70, 70))
            screen.blit(o_letter, oRect)
        if left_o:
            oRect = o_letter.get_rect(center=(70, 210))
            screen.blit(o_letter, oRect)
        if down_left_o:
            oRect = o_letter.get_rect(center=(70, 350))
            screen.blit(o_letter, oRect)
        if up_o:
            oRect = o_letter.get_rect(center=(210, 70))
            screen.blit(o_letter, oRect)
        if mid_o:
            oRect = o_letter.get_rect(center=(210, 210))
            screen.blit(o_letter, oRect)
        if down_o:
            oRect = o_letter.get_rect(center=(210, 350))
            screen.blit(o_letter, oRect)
        if up_right_o:
            oRect = o_letter.get_rect(center=(350, 70))
            screen.blit(o_letter, oRect)
        if right_o:
            oRect = o_letter.get_rect(center=(350, 210))
            screen.blit(o_letter, oRect)
        if down_right_o:
            oRect = o_letter.get_rect(center=(350, 350))
            screen.blit(o_letter, oRect)
        pygame.display.update()
        if up_left_x and down_left_x and left_x or up_x and down_x and mid_x or up_right_x and down_right_x and right_x or up_left_x and up_x and up_right_x or left_x and mid_x and right_x or down_left_x and down_x and down_right_x or up_left_x and mid_x and down_right_x or up_right_x and mid_x and down_left_x:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_o, win_oRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif up_left_o and down_left_o and left_o or up_o and down_o and mid_o or up_right_o and down_right_o and right_o or up_left_o and up_o and up_right_o or left_o and mid_o and right_o or down_left_o and down_o and down_right_o or up_left_o and mid_o and down_right_o or up_right_o and mid_o and down_left_o:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_x, win_xRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif tiles == 9:
            print('tie')
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(tie, tieRect)
            pygame.display.update()
            time.sleep(1)
            play_again()


def speed():
    global game
    # Variables
    ## x's
    up_left_x = False
    left_x = False
    down_left_x = False
    up_x = False
    mid_x = False
    down_x = False
    up_right_x = False
    right_x = False
    down_right_x = False

    ## y's
    up_left_o = False
    left_o = False
    down_left_o = False
    up_o = False
    mid_o = False
    down_o = False
    up_right_o = False
    right_o = False
    down_right_o = False
    if game == 0:
        game = 4
    turn = 0
    tiles = 0
    colour_x = black
    colour_o = background
    start = time.time()
    # Font
    font = pygame.font.Font('freesansbold.ttf', 160)
    win_font = pygame.font.Font('freesansbold.ttf', 320)
    indicator_font = pygame.font.Font('freesansbold.ttf', 40)
    timer_font = pygame.font.Font('freesansbold.ttf', 20)
    x_letter = font.render('x', True, purple)
    o_letter = font.render('o', True, orange)
    win_x = win_font.render('x', True, black)
    win_xRect = win_x.get_rect(center=(X / 2, Y / 2))
    win_o = win_font.render('o', True, black)
    win_oRect = win_o.get_rect(center=(X / 2, Y / 2))
    tie = win_font.render('xo', True, black)
    tieRect = tie.get_rect(center=(X / 2, Y / 2))
    while True:
        indicator_x = indicator_font.render('x turn', True, colour_x)
        indicator_xRect = indicator_x.get_rect(center=(X / 2, 455))
        indicator_o = indicator_font.render('o turn', True, colour_o)
        indicator_oRect = indicator_o.get_rect(center=(X / 2, 455))
        # Points To Click For X's And O's
        left = pygame.draw.rect(screen, background, pygame.Rect(0, 140, X / 3, 140))
        bottom_left = pygame.draw.rect(screen, background, pygame.Rect(0, 280, X / 3, 140))
        top_left = pygame.draw.rect(screen, background, pygame.Rect(0, 0, X / 3, 140))
        mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 140, X / 3, 140))
        top_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 0, X / 3, 140))
        bottom_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 280, X / 3, 140))
        right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 140, X / 3, 140))
        top_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 0, X / 3, 140))
        bottom_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 280, X / 3, 140))
        bottom = pygame.draw.rect(screen, background, pygame.Rect(0, 420, X, 70))
        if turn % 2 == 1:
            screen.blit(indicator_x, indicator_xRect)
            screen.blit(indicator_o, indicator_oRect)

        else:
            screen.blit(indicator_o, indicator_oRect)
            screen.blit(indicator_x, indicator_xRect)
        if time.time() - start < 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if left.collidepoint(event.pos):
                        turn += 1
                        tiles += 1
                        if turn % 2 == 1:
                            if left_o:
                                turn -= 1
                                tiles -= 1
                            elif left_x:
                                turn -= 1
                                tiles -= 1
                            else:
                                left_x = True
                                start = time.time()
                        else:
                            if left_x:
                                turn -= 1
                                tiles -= 1
                            elif left_o:
                                turn -= 1
                                tiles -= 1
                            else:
                                left_o = True
                                start = time.time()
                    if bottom_left.collidepoint(event.pos):
                        turn += 1
                        tiles += 1
                        if turn % 2 == 1:
                            if down_left_o:
                                turn -= 1
                                tiles -= 1
                            elif down_left_x:
                                turn -= 1
                                tiles -= 1
                            else:
                                down_left_x = True
                                start = time.time()
                        else:
                            if down_left_x:
                                turn -= 1
                                tiles -= 1
                            elif down_left_o:
                                turn -= 1
                                tiles -= 1
                            else:
                                down_left_o = True
                                start = time.time()
                    if top_left.collidepoint(event.pos):
                        turn += 1
                        tiles += 1
                        if turn % 2 == 1:
                            if up_left_o:
                                turn -= 1
                                tiles -= 1
                            elif up_left_x:
                                turn -= 1
                                tiles -= 1
                            else:
                                up_left_x = True
                                start = time.time()
                        else:
                            if up_left_x:
                                turn -= 1
                                tiles -= 1
                            elif up_left_o:
                                turn -= 1
                                tiles -= 1
                            else:
                                up_left_o = True
                                start = time.time()
                    if mid.collidepoint(event.pos):
                        print('Mid')
                        turn += 1
                        tiles += 1
                        if turn % 2 == 1:
                            print('x')
                            if mid_o:
                                turn -= 1
                                tiles -= 1
                            elif mid_x:
                                turn -= 1
                                tiles -= 1
                            else:
                                mid_x = True
                                start = time.time()
                        else:
                            print('o')
                            if mid_x:
                                turn -= 1
                                tiles -= 1
                            elif mid_o:
                                turn -= 1
                                tiles -= 1
                            else:
                                mid_o = True
                                start = time.time()
                    if top_mid.collidepoint(event.pos):
                        print('Top_Mid')
                        turn += 1
                        tiles += 1
                        if turn % 2 == 1:
                            print('x')
                            if up_o:
                                turn -= 1
                                tiles -= 1
                            elif up_x:
                                turn -= 1
                                tiles -= 1
                            else:
                                up_x = True
                                start = time.time()
                        else:
                            print('o')
                            if up_x:
                                turn -= 1
                                tiles -= 1
                            elif up_o:
                                turn -= 1
                                tiles -= 1
                            else:
                                up_o = True
                                start = time.time()
                    if bottom_mid.collidepoint(event.pos):
                        print('Bottom_Mid')
                        turn += 1
                        tiles += 1
                        if turn % 2 == 1:
                            print('x')
                            if down_o:
                                turn -= 1
                                tiles -= 1
                            elif down_x:
                                turn -= 1
                                tiles -= 1
                            else:
                                down_x = True
                                start = time.time()
                        else:
                            print('o')
                            if down_x:
                                turn -= 1
                                tiles -= 1
                            elif down_o:
                                turn -= 1
                                tiles -= 1
                            else:
                                down_o = True
                                start = time.time()
                    if right.collidepoint(event.pos):
                        print('Mid_Right')
                        turn += 1
                        tiles += 1
                        if turn % 2 == 1:
                            print('x')
                            if right_o:
                                turn -= 1
                                tiles -= 1
                            elif right_x:
                                turn -= 1
                                tiles -= 1
                            else:
                                right_x = True
                                start = time.time()
                        else:
                            print('o')
                            if right_x:
                                turn -= 1
                                tiles -= 1
                            elif right_o:
                                turn -= 1
                                tiles -= 1
                            else:
                                right_o = True
                                start = time.time()
                    if top_right.collidepoint(event.pos):
                        print('Top_Right')
                        turn += 1
                        tiles += 1
                        if turn % 2 == 1:
                            print('x')
                            if up_right_o:
                                turn -= 1
                                tiles -= 1
                            elif up_right_x:
                                turn -= 1
                                tiles -= 1
                            else:
                                up_right_x = True
                                start = time.time()
                        else:
                            print('o')
                            if up_right_x:
                                turn -= 1
                                tiles -= 1
                            elif up_right_o:
                                turn -= 1
                                tiles -= 1
                            else:
                                up_right_o = True
                                start = time.time()
                    if bottom_right.collidepoint(event.pos):
                        print('Bottom_Right')
                        turn += 1
                        tiles += 1
                        if turn % 2 == 1:
                            print('x')
                            if down_right_o:
                                turn -= 1
                                tiles -= 1
                            elif down_right_x:
                                turn -= 1
                                tiles -= 1
                            else:
                                down_right_x = True
                                start = time.time()
                        else:
                            print('o')
                            if down_right_x:
                                turn -= 1
                                tiles -= 1
                            elif down_right_o:
                                turn -= 1
                                tiles -= 1
                            else:
                                down_right_o = True
                                start = time.time()
        else:
            turn += 1
            start = time.time()
        pygame.draw.rect(screen, black, pygame.Rect(X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(2 * X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(0, 140, X, 5))
        pygame.draw.rect(screen, black, pygame.Rect(0, 280, X, 5))
        timer = str(round(time.time() - start, 2))
        screen.blit(timer_font.render(timer, True, white), (200, 470))
        if turn % 2 == 1:
            colour_o = black
            colour_x = background
        else:
            colour_x = black
            colour_o = background
        # x's
        if up_left_x:
            xRect = x_letter.get_rect(center=(70, 70))
            screen.blit(x_letter, xRect)
        if left_x:
            xRect = x_letter.get_rect(center=(70, 210))
            screen.blit(x_letter, xRect)
        if down_left_x:
            xRect = x_letter.get_rect(center=(70, 350))
            screen.blit(x_letter, xRect)
        if up_x:
            xRect = x_letter.get_rect(center=(210, 70))
            screen.blit(x_letter, xRect)
        if mid_x:
            xRect = x_letter.get_rect(center=(210, 210))
            screen.blit(x_letter, xRect)
        if down_x:
            xRect = x_letter.get_rect(center=(210, 350))
            screen.blit(x_letter, xRect)
        if up_right_x:
            xRect = x_letter.get_rect(center=(350, 70))
            screen.blit(x_letter, xRect)
        if right_x:
            xRect = x_letter.get_rect(center=(350, 210))
            screen.blit(x_letter, xRect)
        if down_right_x:
            xRect = x_letter.get_rect(center=(350, 350))
            screen.blit(x_letter, xRect)

        # o's
        if up_left_o:
            oRect = o_letter.get_rect(center=(70, 70))
            screen.blit(o_letter, oRect)
        if left_o:
            oRect = o_letter.get_rect(center=(70, 210))
            screen.blit(o_letter, oRect)
        if down_left_o:
            oRect = o_letter.get_rect(center=(70, 350))
            screen.blit(o_letter, oRect)
        if up_o:
            oRect = o_letter.get_rect(center=(210, 70))
            screen.blit(o_letter, oRect)
        if mid_o:
            oRect = o_letter.get_rect(center=(210, 210))
            screen.blit(o_letter, oRect)
        if down_o:
            oRect = o_letter.get_rect(center=(210, 350))
            screen.blit(o_letter, oRect)
        if up_right_o:
            oRect = o_letter.get_rect(center=(350, 70))
            screen.blit(o_letter, oRect)
        if right_o:
            oRect = o_letter.get_rect(center=(350, 210))
            screen.blit(o_letter, oRect)
        if down_right_o:
            oRect = o_letter.get_rect(center=(350, 350))
            screen.blit(o_letter, oRect)
        pygame.display.update()
        if up_left_x and down_left_x and left_x or up_x and down_x and mid_x or up_right_x and down_right_x and right_x or up_left_x and up_x and up_right_x or left_x and mid_x and right_x or down_left_x and down_x and down_right_x or up_left_x and mid_x and down_right_x or up_right_x and mid_x and down_left_x:
            ('x wins')
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_x, win_xRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif up_left_o and down_left_o and left_o or up_o and down_o and mid_o or up_right_o and down_right_o and right_o or up_left_o and up_o and up_right_o or left_o and mid_o and right_o or down_left_o and down_o and down_right_o or up_left_o and mid_o and down_right_o or up_right_o and mid_o and down_left_o:
            print('o wins')
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_o, win_oRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif tiles == 9:
            print('tie')
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(tie, tieRect)
            pygame.display.update()
            time.sleep(1)
            play_again()


def xw():
    global game
    # Variables
    ## x's
    up_left_x = False
    left_x = False
    down_left_x = False
    up_x = False
    mid_x = False
    down_x = False
    up_right_x = False
    right_x = False
    down_right_x = False

    ## w's
    up_left_w = False
    left_w = False
    down_left_w = False
    up_w = False
    mid_w = False
    down_w = False
    up_right_w = False
    right_w = False
    down_right_w = False
    if game == 0:
        game = 5
    turn = 0
    tiles = 0
    colour_x = black
    colour_w = background
    # Font
    font = pygame.font.Font('freesansbold.ttf', 160)
    win_font = pygame.font.Font('freesansbold.ttf', 320)
    indicator_font = pygame.font.Font('freesansbold.ttf', 40)
    x_letter = font.render('x', True, purple)
    w_letter = font.render('w', True, orange)
    win_x = win_font.render('x', True, black)
    win_xRect = win_x.get_rect(center=(X / 2, Y / 2))
    win_w = win_font.render('w', True, black)
    win_wRect = win_w.get_rect(center=(X / 2, Y / 2))
    tie = win_font.render('xw', True, black)
    tieRect = tie.get_rect(center=(X / 2, Y / 2))
    while True:
        indicator_x = indicator_font.render('x turn', True, colour_x)
        indicator_xRect = indicator_x.get_rect(center=(X / 2, 455))
        indicator_w = indicator_font.render('w turn', True, colour_w)
        indicator_wRect = indicator_w.get_rect(center=(X / 2, 455))
        # Pwints To Click For X's And O's
        left = pygame.draw.rect(screen, background, pygame.Rect(0, 140, X / 3, 140))
        bottom_left = pygame.draw.rect(screen, background, pygame.Rect(0, 280, X / 3, 140))
        top_left = pygame.draw.rect(screen, background, pygame.Rect(0, 0, X / 3, 140))
        mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 140, X / 3, 140))
        top_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 0, X / 3, 140))
        bottom_mid = pygame.draw.rect(screen, background, pygame.Rect(X / 3, 280, X / 3, 140))
        right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 140, X / 3, 140))
        top_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 0, X / 3, 140))
        bottom_right = pygame.draw.rect(screen, background, pygame.Rect(2 * X / 3, 280, X / 3, 140))
        if turn % 4 != 0:
            screen.blit(indicator_x, indicator_xRect)
            screen.blit(indicator_w, indicator_wRect)
        else:
            screen.blit(indicator_w, indicator_wRect)
            screen.blit(indicator_x, indicator_xRect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if left.collidepoint(event.pos):
                    print('Mid_Left')
                    turn += 1
                    tiles += 1
                    if turn % 4 == 1:
                        print('x')
                        if left_w:
                            turn -= 1
                            tiles -= 1
                        elif left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            left_x = True
                    else:
                        print('w')
                        if left_x:
                            turn -= 1
                            tiles -= 1
                        elif left_w:
                            turn -= 1
                            tiles -= 1
                        else:
                            left_w = True
                if bottom_left.collidepoint(event.pos):
                    print('Bwttwm_Left')
                    turn += 1
                    tiles += 1
                    if turn % 4 == 1:
                        if down_left_w:
                            turn -= 1
                            tiles -= 1
                        elif down_left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_left_x = True
                    else:
                        print('w')
                        if down_left_x:
                            turn -= 1
                            tiles -= 1
                        elif down_left_w:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_left_w = True
                if top_left.collidepoint(event.pos):
                    print('Twp_Left')
                    turn += 1
                    tiles += 1
                    if turn % 4 == 1:
                        print('x')
                        if up_left_w:
                            turn -= 1
                            tiles -= 1
                        elif up_left_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_left_x = True
                    else:
                        print('w')
                        if up_left_x:
                            turn -= 1
                            tiles -= 1
                        elif up_left_w:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_left_w = True
                if mid.collidepoint(event.pos):
                    print('Mid')
                    turn += 1
                    tiles += 1
                    if turn % 4 == 1:
                        print('x')
                        if mid_w:
                            turn -= 1
                            tiles -= 1
                        elif mid_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            mid_x = True
                    else:
                        print('w')
                        if mid_x:
                            turn -= 1
                            tiles -= 1
                        elif mid_w:
                            turn -= 1
                            tiles -= 1
                        else:
                            mid_w = True
                if top_mid.collidepoint(event.pos):
                    print('Twp_Mid')
                    turn += 1
                    tiles += 1
                    if turn % 4 == 1:
                        print('x')
                        if up_w:
                            turn -= 1
                            tiles -= 1
                        elif up_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_x = True
                    else:
                        print('w')
                        if up_x:
                            turn -= 1
                            tiles -= 1
                        elif up_w:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_w = True
                if bottom_mid.collidepoint(event.pos):
                    print('Bwttwm_Mid')
                    turn += 1
                    tiles += 1
                    if turn % 4 == 1:
                        print('x')
                        if down_w:
                            turn -= 1
                            tiles -= 1
                        elif down_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_x = True
                    else:
                        print('w')
                        if down_x:
                            turn -= 1
                            tiles -= 1
                        elif down_w:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_w = True
                if right.collidepoint(event.pos):
                    print('Mid_Right')
                    turn += 1
                    tiles += 1
                    if turn % 4 == 1:
                        print('x')
                        if right_w:
                            turn -= 1
                            tiles -= 1
                        elif right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            right_x = True
                    else:
                        print('w')
                        if right_x:
                            turn -= 1
                            tiles -= 1
                        elif right_w:
                            turn -= 1
                            tiles -= 1
                        else:
                            right_w = True
                if top_right.collidepoint(event.pos):
                    print('Twp_Right')
                    turn += 1
                    tiles += 1
                    if turn % 4 == 1:
                        print('x')
                        if up_right_w:
                            turn -= 1
                            tiles -= 1
                        elif up_right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_right_x = True
                    else:
                        print('w')
                        if up_right_x:
                            turn -= 1
                            tiles -= 1
                        elif up_right_w:
                            turn -= 1
                            tiles -= 1
                        else:
                            up_right_w = True
                if bottom_right.collidepoint(event.pos):
                    print('Bwttwm_Right')
                    turn += 1
                    tiles += 1
                    if turn % 4 == 1:
                        print('x')
                        if down_right_w:
                            turn -= 1
                            tiles -= 1
                        elif down_right_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_right_x = True
                    else:
                        print('w')
                        if down_right_x:
                            turn -= 1
                            tiles -= 1
                        elif down_right_w:
                            turn -= 1
                            tiles -= 1
                        else:
                            down_right_w = True
        pygame.draw.rect(screen, black, pygame.Rect(X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(2 * X / 3, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(0, 140, X, 5))
        pygame.draw.rect(screen, black, pygame.Rect(0, 280, X, 5))
        if turn % 4 != 0:
            colour_w = black
            colour_x = background
        else:
            colour_x = black
            colour_w = background
            # x's
        if up_left_x:
            xRect = x_letter.get_rect(center=(70, 70))
            screen.blit(x_letter, xRect)
        if left_x:
            xRect = x_letter.get_rect(center=(70, 210))
            screen.blit(x_letter, xRect)
        if down_left_x:
            xRect = x_letter.get_rect(center=(70, 350))
            screen.blit(x_letter, xRect)
        if up_x:
            xRect = x_letter.get_rect(center=(210, 70))
            screen.blit(x_letter, xRect)
        if mid_x:
            xRect = x_letter.get_rect(center=(210, 210))
            screen.blit(x_letter, xRect)
        if down_x:
            xRect = x_letter.get_rect(center=(210, 350))
            screen.blit(x_letter, xRect)
        if up_right_x:
            xRect = x_letter.get_rect(center=(350, 70))
            screen.blit(x_letter, xRect)
        if right_x:
            xRect = x_letter.get_rect(center=(350, 210))
            screen.blit(x_letter, xRect)
        if down_right_x:
            xRect = x_letter.get_rect(center=(350, 350))
            screen.blit(x_letter, xRect)

        # w's
        if up_left_w:
            wRect = w_letter.get_rect(center=(70, 70))
            screen.blit(w_letter, wRect)
        if left_w:
            wRect = w_letter.get_rect(center=(70, 210))
            screen.blit(w_letter, wRect)
        if down_left_w:
            wRect = w_letter.get_rect(center=(70, 350))
            screen.blit(w_letter, wRect)
        if up_w:
            wRect = w_letter.get_rect(center=(210, 70))
            screen.blit(w_letter, wRect)
        if mid_w:
            wRect = w_letter.get_rect(center=(210, 210))
            screen.blit(w_letter, wRect)
        if down_w:
            wRect = w_letter.get_rect(center=(210, 350))
            screen.blit(w_letter, wRect)
        if up_right_w:
            wRect = w_letter.get_rect(center=(350, 70))
            screen.blit(w_letter, wRect)
        if right_w:
            wRect = w_letter.get_rect(center=(350, 210))
            screen.blit(w_letter, wRect)
        if down_right_w:
            wRect = w_letter.get_rect(center=(350, 350))
            screen.blit(w_letter, wRect)
        pygame.display.update()
        if up_left_x and down_left_x and left_x or up_x and down_x and mid_x or up_right_x and down_right_x and right_x or up_left_x and up_x and up_right_x or left_x and mid_x and right_x or down_left_x and down_x and down_right_x or up_left_x and mid_x and down_right_x or up_right_x and mid_x and down_left_x:
            ('x wins')
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_x, win_xRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif up_left_w and down_left_w and left_w or up_w and down_w and mid_w or up_right_w and down_right_w and right_w or up_left_w and up_w and up_right_w or left_w and mid_w and right_w or down_left_w and down_w and down_right_w or up_left_w and mid_w and down_right_w or up_right_w and mid_w and down_left_w:
            print('w wins')
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_w, win_wRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif tiles == 9:
            print('tie')
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(tie, tieRect)
            pygame.display.update()
            time.sleep(1)
            play_again()


def three_player():
    global game
    # Variables
    ## x's
    one_one_x = False
    one_two_x = False
    one_three_x = False
    one_four_x = False
    two_one_x = False
    two_two_x = False
    two_three_x = False
    two_four_x = False
    three_one_x = False
    three_two_x = False
    three_three_x = False
    three_four_x = False
    four_one_x = False
    four_two_x = False
    four_three_x = False
    four_four_x = False

    ## y's
    one_one_o = False
    one_two_o = False
    one_three_o = False
    one_four_o = False
    two_one_o = False
    two_two_o = False
    two_three_o = False
    two_four_o = False
    three_one_o = False
    three_two_o = False
    three_three_o = False
    three_four_o = False
    four_one_o = False
    four_two_o = False
    four_three_o = False
    four_four_o = False

    ## delta
    one_one_Δ = False
    one_two_Δ = False
    one_three_Δ = False
    one_four_Δ = False
    two_one_Δ = False
    two_two_Δ = False
    two_three_Δ = False
    two_four_Δ = False
    three_one_Δ = False
    three_two_Δ = False
    three_three_Δ = False
    three_four_Δ = False
    four_one_Δ = False
    four_two_Δ = False
    four_three_Δ = False
    four_four_Δ = False
    if game == 0:
        game = 6
    turn = 0
    tiles = 0
    colour_x = black
    colour_o = background
    colour_Δ = background
    # Font
    font = pygame.font.Font('freesansbold.ttf', 120)
    win_font = pygame.font.Font('freesansbold.ttf', 320)
    indicator_font = pygame.font.Font('freesansbold.ttf', 40)
    delta_font = pygame.font.Font('freesansbold.ttf', 100)

    x_letter = font.render('x', True, purple)
    o_letter = font.render('o', True, orange)
    delta = delta_font.render('Δ', True, green)
    win_x = win_font.render('x', True, black)
    win_xRect = win_x.get_rect(center=(X / 2, Y / 2))
    win_o = win_font.render('o', True, black)
    win_oRect = win_o.get_rect(center=(X / 2, Y / 2))
    win_Δ = win_font.render('Δ', True, black)
    win_ΔRect = win_x.get_rect(center=(X / 2, Y / 2))
    tie = win_font.render('xoΔ', True, black)
    tieRect = tie.get_rect(center=(X / 2, Y / 2))
    while True:
        indicator_x = indicator_font.render('x turn', True, colour_x)
        indicator_xRect = indicator_x.get_rect(center=(X / 2, 455))
        indicator_o = indicator_font.render('o turn', True, colour_o)
        indicator_oRect = indicator_o.get_rect(center=(X / 2, 455))
        indicator_Δ = indicator_font.render('Δ turn', True, colour_Δ)
        indicator_ΔRect = indicator_Δ.get_rect(center=(X / 2, 455))
        # Points To Click For X's And O's
        one_one = pygame.draw.rect(screen, background, pygame.Rect(0, 0, X / 4, 105))
        one_two = pygame.draw.rect(screen, background, pygame.Rect(0, 105, X / 4, 105))
        one_three = pygame.draw.rect(screen, background, pygame.Rect(0, 210, X / 4, 105))
        one_four = pygame.draw.rect(screen, background, pygame.Rect(0, 315, X / 4, 105))
        two_one = pygame.draw.rect(screen, background, pygame.Rect(X / 4, 0, X / 4, 105))
        two_two = pygame.draw.rect(screen, background, pygame.Rect(X / 4, 105, X / 4, 105))
        two_three = pygame.draw.rect(screen, background, pygame.Rect(X / 4, 210, X / 4, 105))
        two_four = pygame.draw.rect(screen, background, pygame.Rect(X / 4, 315, X / 4, 105))
        three_one = pygame.draw.rect(screen, background, pygame.Rect(X / 2, 0, X / 4, 105))
        three_two = pygame.draw.rect(screen, background, pygame.Rect(X / 2, 105, X / 4, 105))
        three_three = pygame.draw.rect(screen, background, pygame.Rect(X / 2, 210, X / 4, 105))
        three_four = pygame.draw.rect(screen, background, pygame.Rect(X / 2, 315, X / 4, 105))
        four_one = pygame.draw.rect(screen, background, pygame.Rect(3 * X / 4, 0, X / 4, 105))
        four_two = pygame.draw.rect(screen, background, pygame.Rect(3 * X / 4, 105, X / 4, 105))
        four_three = pygame.draw.rect(screen, background, pygame.Rect(3 * X / 4, 210, X / 4, 105))
        four_four = pygame.draw.rect(screen, background, pygame.Rect(3 * X / 4, 315, X / 4, 105))
        if turn % 3 == 1:
            screen.blit(indicator_x, indicator_xRect)
            screen.blit(indicator_Δ, indicator_ΔRect)
            screen.blit(indicator_o, indicator_oRect)
        elif turn % 3 == 2:
            screen.blit(indicator_o, indicator_oRect)
            screen.blit(indicator_x, indicator_xRect)
            screen.blit(indicator_Δ, indicator_ΔRect)
        else:
            screen.blit(indicator_Δ, indicator_ΔRect)
            screen.blit(indicator_o, indicator_oRect)
            screen.blit(indicator_x, indicator_xRect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if one_one.collidepoint(event.pos):
                    print('One_One')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if one_one_o:
                            turn -= 1
                            tiles -= 1
                        elif one_one_Δ:
                            turn -= 1
                            tiles -= 1
                        elif one_one_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_one_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if one_one_x:
                            turn -= 1
                            tiles -= 1
                        elif one_one_Δ:
                            turn -= 1
                            tiles -= 1
                        elif one_one_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_one_o = True
                    else:
                        print('Δ')
                        if one_one_x:
                            turn -= 1
                            tiles -= 1
                        elif one_one_o:
                            turn -= 1
                            tiles -= 1
                        elif one_one_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_one_Δ = True
                if one_two.collidepoint(event.pos):
                    print('One_Two')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if one_two_o:
                            turn -= 1
                            tiles -= 1
                        elif one_two_Δ:
                            turn -= 1
                            tiles -= 1
                        elif one_two_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_two_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if one_two_x:
                            turn -= 1
                            tiles -= 1
                        elif one_two_Δ:
                            turn -= 1
                            tiles -= 1
                        elif one_two_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_two_o = True
                    else:
                        print('Δ')
                        if one_two_x:
                            turn -= 1
                            tiles -= 1
                        elif one_two_o:
                            turn -= 1
                            tiles -= 1
                        elif one_two_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_two_Δ = True
                if one_three.collidepoint(event.pos):
                    print('One_Three')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if one_three_o:
                            turn -= 1
                            tiles -= 1
                        elif one_three_Δ:
                            turn -= 1
                            tiles -= 1
                        elif one_three_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_three_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if one_three_x:
                            turn -= 1
                            tiles -= 1
                        elif one_three_Δ:
                            turn -= 1
                            tiles -= 1
                        elif one_three_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_three_o = True
                    else:
                        print('Δ')
                        if one_three_x:
                            turn -= 1
                            tiles -= 1
                        elif one_three_o:
                            turn -= 1
                            tiles -= 1
                        elif one_three_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_three_Δ = True
                if one_four.collidepoint(event.pos):
                    print('One_Four')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if one_four_o:
                            turn -= 1
                            tiles -= 1
                        elif one_four_Δ:
                            turn -= 1
                            tiles -= 1
                        elif one_four_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_four_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if one_four_x:
                            turn -= 1
                            tiles -= 1
                        elif one_four_Δ:
                            turn -= 1
                            tiles -= 1
                        elif one_four_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_four_o = True
                    else:
                        print('Δ')
                        if one_four_x:
                            turn -= 1
                            tiles -= 1
                        elif one_four_o:
                            turn -= 1
                            tiles -= 1
                        elif one_four_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            one_four_Δ = True
                if two_one.collidepoint(event.pos):
                    print('Two_One')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if two_one_o:
                            turn -= 1
                            tiles -= 1
                        elif two_one_Δ:
                            turn -= 1
                            tiles -= 1
                        elif two_one_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_one_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if two_one_x:
                            turn -= 1
                            tiles -= 1
                        elif two_one_Δ:
                            turn -= 1
                            tiles -= 1
                        elif two_one_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_one_o = True
                    else:
                        print('Δ')
                        if two_one_x:
                            turn -= 1
                            tiles -= 1
                        elif two_one_o:
                            turn -= 1
                            tiles -= 1
                        elif two_one_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_one_Δ = True
                if two_two.collidepoint(event.pos):
                    print('Two_Two')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if two_two_o:
                            turn -= 1
                            tiles -= 1
                        elif two_two_Δ:
                            turn -= 1
                            tiles -= 1
                        elif two_two_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_two_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if two_two_x:
                            turn -= 1
                            tiles -= 1
                        elif two_two_Δ:
                            turn -= 1
                            tiles -= 1
                        elif two_two_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_two_o = True
                    else:
                        print('Δ')
                        if two_two_x:
                            turn -= 1
                            tiles -= 1
                        elif two_two_o:
                            turn -= 1
                            tiles -= 1
                        elif two_two_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_two_Δ = True
                if two_three.collidepoint(event.pos):
                    print('Two_Three')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if two_three_o:
                            turn -= 1
                            tiles -= 1
                        elif two_three_Δ:
                            turn -= 1
                            tiles -= 1
                        elif two_three_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_three_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if two_three_x:
                            turn -= 1
                            tiles -= 1
                        elif two_three_Δ:
                            turn -= 1
                            tiles -= 1
                        elif two_three_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_three_o = True
                    else:
                        print('Δ')
                        if two_three_x:
                            turn -= 1
                            tiles -= 1
                        elif two_three_o:
                            turn -= 1
                            tiles -= 1
                        elif two_three_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_three_Δ = True
                if two_four.collidepoint(event.pos):
                    print('Two_Four')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if two_four_o:
                            turn -= 1
                            tiles -= 1
                        elif two_four_Δ:
                            turn -= 1
                            tiles -= 1
                        elif two_four_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_four_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if two_four_x:
                            turn -= 1
                            tiles -= 1
                        elif two_four_Δ:
                            turn -= 1
                            tiles -= 1
                        elif two_four_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_four_o = True
                    else:
                        print('Δ')
                        if two_four_x:
                            turn -= 1
                            tiles -= 1
                        elif two_four_o:
                            turn -= 1
                            tiles -= 1
                        elif two_four_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            two_four_Δ = True
                if three_one.collidepoint(event.pos):
                    print('Three_One')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if three_one_o:
                            turn -= 1
                            tiles -= 1
                        elif three_one_Δ:
                            turn -= 1
                            tiles -= 1
                        elif three_one_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_one_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if three_one_x:
                            turn -= 1
                            tiles -= 1
                        elif three_one_Δ:
                            turn -= 1
                            tiles -= 1
                        elif three_one_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_one_o = True
                    else:
                        print('Δ')
                        if three_one_x:
                            turn -= 1
                            tiles -= 1
                        elif three_one_o:
                            turn -= 1
                            tiles -= 1
                        elif three_one_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_one_Δ = True
                if three_two.collidepoint(event.pos):
                    print('Three_Two')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if three_two_o:
                            turn -= 1
                            tiles -= 1
                        elif three_two_Δ:
                            turn -= 1
                            tiles -= 1
                        elif three_two_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_two_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if three_two_x:
                            turn -= 1
                            tiles -= 1
                        elif three_two_Δ:
                            turn -= 1
                            tiles -= 1
                        elif three_two_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_two_o = True
                    else:
                        print('Δ')
                        if three_two_x:
                            turn -= 1
                            tiles -= 1
                        elif three_two_o:
                            turn -= 1
                            tiles -= 1
                        elif three_two_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_two_Δ = True
                if three_three.collidepoint(event.pos):
                    print('Three_Three')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if three_three_o:
                            turn -= 1
                            tiles -= 1
                        elif three_three_Δ:
                            turn -= 1
                            tiles -= 1
                        elif three_three_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_three_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if three_three_x:
                            turn -= 1
                            tiles -= 1
                        elif three_three_Δ:
                            turn -= 1
                            tiles -= 1
                        elif three_three_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_three_o = True
                    else:
                        print('Δ')
                        if three_three_x:
                            turn -= 1
                            tiles -= 1
                        elif three_three_o:
                            turn -= 1
                            tiles -= 1
                        elif three_three_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_three_Δ = True
                if three_four.collidepoint(event.pos):
                    print('Three_Four')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if three_four_o:
                            turn -= 1
                            tiles -= 1
                        elif three_four_Δ:
                            turn -= 1
                            tiles -= 1
                        elif three_four_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_four_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if three_four_x:
                            turn -= 1
                            tiles -= 1
                        elif three_four_Δ:
                            turn -= 1
                            tiles -= 1
                        elif three_four_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_four_o = True
                    else:
                        print('Δ')
                        if three_four_x:
                            turn -= 1
                            tiles -= 1
                        elif three_four_o:
                            turn -= 1
                            tiles -= 1
                        elif three_four_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            three_four_Δ = True
                if four_one.collidepoint(event.pos):
                    print('Four_One')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if four_one_o:
                            turn -= 1
                            tiles -= 1
                        elif four_one_Δ:
                            turn -= 1
                            tiles -= 1
                        elif four_one_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_one_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if four_one_x:
                            turn -= 1
                            tiles -= 1
                        elif four_one_Δ:
                            turn -= 1
                            tiles -= 1
                        elif four_one_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_one_o = True
                    else:
                        print('Δ')
                        if four_one_x:
                            turn -= 1
                            tiles -= 1
                        elif four_one_o:
                            turn -= 1
                            tiles -= 1
                        elif four_one_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_one_Δ = True
                if four_two.collidepoint(event.pos):
                    print('Four_Two')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if four_two_o:
                            turn -= 1
                            tiles -= 1
                        elif four_two_Δ:
                            turn -= 1
                            tiles -= 1
                        elif four_two_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_two_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if four_two_x:
                            turn -= 1
                            tiles -= 1
                        elif four_two_Δ:
                            turn -= 1
                            tiles -= 1
                        elif four_two_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_two_o = True
                    else:
                        print('Δ')
                        if four_two_x:
                            turn -= 1
                            tiles -= 1
                        elif four_two_o:
                            turn -= 1
                            tiles -= 1
                        elif four_two_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_two_Δ = True
                if four_three.collidepoint(event.pos):
                    print('Four_Three')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if four_three_o:
                            turn -= 1
                            tiles -= 1
                        elif four_three_Δ:
                            turn -= 1
                            tiles -= 1
                        elif four_three_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_three_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if four_three_x:
                            turn -= 1
                            tiles -= 1
                        elif four_three_Δ:
                            turn -= 1
                            tiles -= 1
                        elif four_three_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_three_o = True
                    else:
                        print('Δ')
                        if four_three_x:
                            turn -= 1
                            tiles -= 1
                        elif four_three_o:
                            turn -= 1
                            tiles -= 1
                        elif four_three_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_three_Δ = True
                if four_four.collidepoint(event.pos):
                    print('Four_Four')
                    turn += 1
                    tiles += 1
                    if turn % 3 == 1:
                        print('x')
                        if four_four_o:
                            turn -= 1
                            tiles -= 1
                        elif four_four_Δ:
                            turn -= 1
                            tiles -= 1
                        elif four_four_x:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_four_x = True
                    elif turn % 3 == 2:
                        print('o')
                        if four_four_x:
                            turn -= 1
                            tiles -= 1
                        elif four_four_Δ:
                            turn -= 1
                            tiles -= 1
                        elif four_four_o:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_four_o = True
                    else:
                        print('Δ')
                        if four_four_x:
                            turn -= 1
                            tiles -= 1
                        elif four_four_o:
                            turn -= 1
                            tiles -= 1
                        elif four_four_Δ:
                            turn -= 1
                            tiles -= 1
                        else:
                            four_four_Δ = True
        pygame.draw.rect(screen, black, pygame.Rect(X / 4, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(X / 2, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(3 * X / 4, 0, 5, 420))
        pygame.draw.rect(screen, black, pygame.Rect(0, 105, X, 5))
        pygame.draw.rect(screen, black, pygame.Rect(0, 210, X, 5))
        pygame.draw.rect(screen, black, pygame.Rect(0, 315, X, 5))
        if turn % 3 == 1:
            colour_o = black
            colour_x = background
            colour_Δ = background
        elif turn % 3 == 2:
            colour_Δ = black
            colour_x = background
            colour_o = background
        else:
            colour_x = black
            colour_o = background
            colour_Δ = background
        # x's
        if one_one_x:
            xRect = x_letter.get_rect(center=(52.5, 52.5))
            screen.blit(x_letter, xRect)
        if one_two_x:
            xRect = x_letter.get_rect(center=(52.5, 157.5))
            screen.blit(x_letter, xRect)
        if one_three_x:
            xRect = x_letter.get_rect(center=(52.5, 262.5))
            screen.blit(x_letter, xRect)
        if one_four_x:
            xRect = x_letter.get_rect(center=(52.5, 367.5))
            screen.blit(x_letter, xRect)
        if two_one_x:
            xRect = x_letter.get_rect(center=(157.5, 52.5))
            screen.blit(x_letter, xRect)
        if two_two_x:
            xRect = x_letter.get_rect(center=(157.5, 157.5))
            screen.blit(x_letter, xRect)
        if two_three_x:
            xRect = x_letter.get_rect(center=(157.5, 262.5))
            screen.blit(x_letter, xRect)
        if two_four_x:
            xRect = x_letter.get_rect(center=(157.5, 367.5))
            screen.blit(x_letter, xRect)
        if three_one_x:
            xRect = x_letter.get_rect(center=(262.5, 52.5))
            screen.blit(x_letter, xRect)
        if three_two_x:
            xRect = x_letter.get_rect(center=(262.5, 157.5))
            screen.blit(x_letter, xRect)
        if three_three_x:
            xRect = x_letter.get_rect(center=(262.5, 262.5))
            screen.blit(x_letter, xRect)
        if three_four_x:
            xRect = x_letter.get_rect(center=(262.5, 367.5))
            screen.blit(x_letter, xRect)
        if four_one_x:
            xRect = x_letter.get_rect(center=(367.5, 52.5))
            screen.blit(x_letter, xRect)
        if four_two_x:
            xRect = x_letter.get_rect(center=(367.5, 157.5))
            screen.blit(x_letter, xRect)
        if four_three_x:
            xRect = x_letter.get_rect(center=(367.5, 262.5))
            screen.blit(x_letter, xRect)
        if four_four_x:
            xRect = x_letter.get_rect(center=(367.5, 367.5))
            screen.blit(x_letter, xRect)

        # o's
        if one_one_o:
            oRect = o_letter.get_rect(center=(52.5, 52.5))
            screen.blit(o_letter, oRect)
        if one_two_o:
            oRect = o_letter.get_rect(center=(52.5, 157.5))
            screen.blit(o_letter, oRect)
        if one_three_o:
            oRect = o_letter.get_rect(center=(52.5, 262.5))
            screen.blit(o_letter, oRect)
        if one_four_o:
            oRect = o_letter.get_rect(center=(52.5, 367.5))
            screen.blit(o_letter, oRect)
        if two_one_o:
            oRect = o_letter.get_rect(center=(157.5, 52.5))
            screen.blit(o_letter, oRect)
        if two_two_o:
            oRect = o_letter.get_rect(center=(157.5, 157.5))
            screen.blit(o_letter, oRect)
        if two_three_o:
            oRect = o_letter.get_rect(center=(157.5, 262.5))
            screen.blit(o_letter, oRect)
        if two_four_o:
            oRect = o_letter.get_rect(center=(157.5, 367.5))
            screen.blit(o_letter, oRect)
        if three_one_o:
            oRect = o_letter.get_rect(center=(262.5, 52.5))
            screen.blit(o_letter, oRect)
        if three_two_o:
            oRect = o_letter.get_rect(center=(262.5, 157.5))
            screen.blit(o_letter, oRect)
        if three_three_o:
            oRect = o_letter.get_rect(center=(262.5, 262.5))
            screen.blit(o_letter, oRect)
        if three_four_o:
            oRect = o_letter.get_rect(center=(262.5, 367.2))
            screen.blit(o_letter, oRect)
        if four_one_o:
            oRect = o_letter.get_rect(center=(367.5, 52.5))
            screen.blit(o_letter, oRect)
        if four_two_o:
            oRect = o_letter.get_rect(center=(367.5, 157.5))
            screen.blit(o_letter, oRect)
        if four_three_o:
            oRect = o_letter.get_rect(center=(367.5, 262.5))
            screen.blit(o_letter, oRect)
        if four_four_o:
            oRect = o_letter.get_rect(center=(367.5, 367.5))
            screen.blit(o_letter, oRect)

        # Delta's
        if one_one_Δ:
            ΔRect = delta.get_rect(center=(52.5, 52.5))
            screen.blit(delta, ΔRect)
        if one_two_Δ:
            ΔRect = delta.get_rect(center=(52.5, 157.5))
            screen.blit(delta, ΔRect)
        if one_three_Δ:
            ΔRect = delta.get_rect(center=(52.5, 262.5))
            screen.blit(delta, ΔRect)
        if one_four_Δ:
            ΔRect = delta.get_rect(center=(52.5, 367.5))
            screen.blit(delta, ΔRect)
        if two_one_Δ:
            ΔRect = delta.get_rect(center=(157.5, 52.5))
            screen.blit(delta, ΔRect)
        if two_two_Δ:
            ΔRect = delta.get_rect(center=(157.5, 157.5))
            screen.blit(delta, ΔRect)
        if two_three_Δ:
            ΔRect = delta.get_rect(center=(157.5, 262.5))
            screen.blit(delta, ΔRect)
        if two_four_Δ:
            ΔRect = delta.get_rect(center=(157.5, 367.5))
            screen.blit(delta, ΔRect)
        if three_one_Δ:
            ΔRect = delta.get_rect(center=(262.5, 52.5))
            screen.blit(delta, ΔRect)
        if three_two_Δ:
            ΔRect = delta.get_rect(center=(262.5, 157.5))
            screen.blit(delta, ΔRect)
        if three_three_Δ:
            ΔRect = delta.get_rect(center=(262.5, 262.5))
            screen.blit(delta, ΔRect)
        if three_four_Δ:
            ΔRect = delta.get_rect(center=(262.5, 367.5))
            screen.blit(delta, ΔRect)
        if four_one_Δ:
            ΔRect = delta.get_rect(center=(367.5, 52.5))
            screen.blit(delta, ΔRect)
        if four_two_Δ:
            ΔRect = delta.get_rect(center=(367.5, 157.5))
            screen.blit(delta, ΔRect)
        if four_three_Δ:
            ΔRect = delta.get_rect(center=(367.5, 262.5))
            screen.blit(delta, ΔRect)
        if four_four_Δ:
            ΔRect = delta.get_rect(center=(367.5, 367.5))
            screen.blit(delta, ΔRect)
        pygame.display.update()

        if one_one_x and one_two_x and one_three_x or one_two_x and one_three_x and one_four_x or two_one_x and two_two_x and two_three_x or two_two_x and two_three_x and two_four_x or three_one_x and three_two_x and three_three_x or three_two_x and three_three_x and three_four_x or four_one_x and four_two_x and four_three_x or four_two_x and four_three_x and four_four_x or one_one_x and two_one_x and three_one_x or two_one_x and three_one_x and four_one_x or one_two_x and two_two_x and three_two_x or two_two_x and three_two_x and four_two_x or one_three_x and two_three_x and three_three_x or two_three_x and three_three_x and four_three_x or one_four_x and two_four_x and three_four_x or two_four_x and three_four_x and four_four_x or one_two_x and two_three_x and three_four_x or one_one_x and two_two_x and three_three_x or two_two_x and three_three_x and four_four_x or two_one_x and three_two_x and four_three_x or four_two_x and three_three_x and two_four_x or four_one_x and three_two_x and two_three_x or three_two_x and two_three_x and one_four_x or three_one_x and two_two_x and one_three_x:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_x, win_xRect)
            pygame.display.update()
            time.sleep(1)
            title()
        elif one_one_o and one_two_o and one_three_o or one_two_o and one_three_o and one_four_o or two_one_o and two_two_o and two_three_o or two_two_o and two_three_o and two_four_o or three_one_o and three_two_o and three_three_o or three_two_o and three_three_o and three_four_o or four_one_o and four_two_o and four_three_o or four_two_o and four_three_o and four_four_o or one_one_o and two_one_o and three_one_o or two_one_o and three_one_o and four_one_o or one_two_o and two_two_o and three_two_o or two_two_o and three_two_o and four_two_o or one_three_o and two_three_o and three_three_o or two_three_o and three_three_o and four_three_o or one_four_o and two_four_o and three_four_o or two_four_o and three_four_o and four_four_o or one_two_o and two_three_o and three_four_o or one_one_o and two_two_o and three_three_o or two_two_o and three_three_o and four_four_o or two_one_o and three_two_o and four_three_o or four_two_o and three_three_o and two_four_o or four_one_o and three_two_o and two_three_o or three_two_o and two_three_o and one_four_o or three_one_o and two_two_o and one_three_o:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_o, win_oRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif one_one_Δ and one_two_Δ and one_three_Δ or one_two_Δ and one_three_Δ and one_four_Δ or two_one_Δ and two_two_Δ and two_three_Δ or two_two_Δ and two_three_Δ and two_four_Δ or three_one_Δ and three_two_Δ and three_three_Δ or three_two_Δ and three_three_Δ and three_four_Δ or four_one_Δ and four_two_Δ and four_three_Δ or four_two_Δ and four_three_Δ and four_four_Δ or one_one_Δ and two_one_Δ and three_one_Δ or two_one_Δ and three_one_Δ and four_one_Δ or one_two_Δ and two_two_Δ and three_two_Δ or two_two_Δ and three_two_Δ and four_two_Δ or one_three_Δ and two_three_Δ and three_three_Δ or two_three_Δ and three_three_Δ and four_three_Δ or one_four_Δ and two_four_Δ and three_four_Δ or two_four_Δ and three_four_Δ and four_four_Δ or one_two_Δ and two_three_Δ and three_four_Δ or one_one_Δ and two_two_Δ and three_three_Δ or two_two_Δ and three_three_Δ and four_four_Δ or two_one_Δ and three_two_Δ and four_three_Δ or four_two_Δ and three_three_Δ and two_four_Δ or four_one_Δ and three_two_Δ and two_three_Δ or three_two_Δ and two_three_Δ and one_four_Δ or three_one_Δ and two_two_Δ and one_three_Δ:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(win_Δ, win_ΔRect)
            pygame.display.update()
            time.sleep(1)
            play_again()
        elif tiles == 16:
            time.sleep(0.5)
            screen.fill(background)
            screen.blit(tie, tieRect)
            pygame.display.update()
            time.sleep(1)
            play_again()


def randomgame():
    global game
    game = 7
    ran_num = random.randint(1, 5)
    screen.fill(background)
    text_font = pygame.font.Font('freesansbold.ttf', 18)
    text21 = text_font.render('Tic Tac Toe'.upper(), True, black)
    text21_rect = text21.get_rect(center=(X / 2, Y / 7))
    screen.blit(text21, text21_rect)

    text22 = text_font.render('3 player'.upper(), True, black)
    text22_rect = text22.get_rect(center=(X / 2, 2 * Y / 7))
    screen.blit(text22, text22_rect)

    text23 = text_font.render('speed'.upper(), True, black)
    text23_rect = text23.get_rect(center=(X / 2, 3 * Y / 7))
    screen.blit(text23, text23_rect)

    text24 = text_font.render('invisible'.upper(), True, black)
    text24_rect = text24.get_rect(center=(X / 2, 4 * Y / 7))
    screen.blit(text24, text24_rect)

    text25 = text_font.render('reverse'.upper(), True, black)
    text25_rect = text25.get_rect(center=(X / 2, 5 * Y / 7))
    screen.blit(text25, text25_rect)

    text26 = text_font.render('???????'.upper(), True, black)
    text26_rect = text26.get_rect(center=(X / 2, 6 * Y / 7))
    screen.blit(text26, text26_rect)
    if ran_num == 1:
        pygame.draw.rect(screen, black, pygame.Rect(X / 2 - 65, Y / 7 - 25, 130, 50), 3)
        pygame.display.update()
        time.sleep(2)
        tictactoe()
        screen.fill(background)
        pygame.display.update()
    elif ran_num == 2:
        pygame.draw.rect(screen, black, pygame.Rect(X / 2 - 65, 2 * Y / 7 - 25, 130, 50), 3)
        pygame.display.update()
        time.sleep(2)
        three_player()
        screen.fill(background)
        pygame.display.update()
    elif ran_num == 3:
        pygame.draw.rect(screen, black, pygame.Rect(X / 2 - 65, 3 * Y / 7 - 25, 130, 50), 3)
        pygame.display.update()
        time.sleep(2)
        speed()
        screen.fill(background)
        pygame.display.update()
    elif ran_num == 4:
        pygame.draw.rect(screen, black, pygame.Rect(X / 2 - 65, 4 * Y / 7 - 25, 130, 50), 3)
        pygame.display.update()
        time.sleep(2)
        screen.fill(background)
        pygame.display.update()
        invisible()
    elif ran_num == 5:
        pygame.draw.rect(screen, black, pygame.Rect(X / 2 - 65, 5 * Y / 7 - 25, 130, 50), 3)
        pygame.display.update()
        time.sleep(2)
        screen.fill(background)
        pygame.display.update()
        reverse()


def back():
    title()


def credits():
    title_font = pygame.font.Font('freesansbold.ttf', 36)
    title = title_font.render('tic-tac-toe'.upper(), True, black)
    title_rect = title.get_rect(center=(X / 2, Y / 4))
    screen.blit(title, title_rect)

    cred_font = pygame.font.Font('freesansbold.ttf', 18)
    cred1 = cred_font.render('made by:'.upper(), True, black)
    cred1_rect = cred1.get_rect(center=(X / 2, 3 * Y / 8))
    screen.blit(cred1, cred1_rect)

    cred2 = cred_font.render('Avi'.upper(), True, black)
    cred2_rect = cred2.get_rect(center=(X / 2, Y / 2))
    screen.blit(cred2, cred2_rect)

    cred3 = cred_font.render('and'.upper(), True, black)
    cred3_rect = cred3.get_rect(center=(X / 2, 5 * Y / 8))
    screen.blit(cred3, cred3_rect)

    cred4 = cred_font.render('Saihaan'.upper(), True, black)
    cred4_rect = cred4.get_rect(center=(X / 2, 3 * Y / 4))
    screen.blit(cred4, cred4_rect)

    secret = pygame.draw.rect(screen, background, pygame.Rect(185, 220, 50, 50), 3)
    arrow = pygame.image.load("arrow.png")
    arrow = pygame.transform.scale(arrow, (40, 40))
    arrowRect = arrow.get_rect()
    arrowRect = arrowRect.move((10, 10))
    screen.blit(arrow, arrowRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrowRect.collidepoint(event.pos):
                    screen.fill(background)
                    back()
                elif secret.collidepoint(event.pos):
                    xw()


def play_again():
    screen.fill(background)
    pygame.display.update()

    title_font = pygame.font.Font('freesansbold.ttf', 36)
    play_text = title_font.render('play again?'.upper(), True, black)
    play_text_rect = play_text.get_rect(center=(X / 2, Y / 4))
    screen.blit(play_text, play_text_rect)

    text_font = pygame.font.Font('freesansbold.ttf', 18)
    yea = text_font.render('yes'.upper(), True, black)
    yea_rect = yea.get_rect(center=(X / 3, Y / 2))
    screen.blit(yea, yea_rect)

    nah = text_font.render('no'.upper(), True, black)
    nah_rect = nah.get_rect(center=(2 * X / 3, Y / 2))
    screen.blit(nah, nah_rect)

    yes = pygame.draw.rect(screen, black, pygame.Rect(75, 220, 130, 50), 3)
    no = pygame.draw.rect(screen, black, pygame.Rect(215, 220, 130, 50), 3)
    pygame.display.update()

    while True:
        global game
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if no.collidepoint(event.pos):
                    title()
                elif yes.collidepoint(event.pos):
                    if game == 1:
                        tictactoe()
                    elif game == 2:
                        invisible()
                    elif game == 3:
                        reverse()
                    elif game == 4:
                        speed()
                    elif game == 5:
                        xw()
                    elif game == 6:
                        three_player()
                    elif game == 7:
                        randomgame()


title()