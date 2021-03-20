import os
from time import sleep

import pygame

import background
import player

FPS = 0.1
player1 = player.Player(x=0, health=0, isAlive=True)
background1 = background.Background(width=500, height=500,
                                    image=pygame.image.load(os.path.join('assets', 'background.png')), blitx=0, blity=0)

while player1.isAlive:
    sleep(FPS)
    background1.blit()
    background1.moves()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player1.isAlive = False
        if event.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
            background1.world = pygame.display.set_mode((event.w, event.h),
                                                        pygame.RESIZABLE)
    pygame.display.update()
