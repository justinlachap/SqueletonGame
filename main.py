import os
from time import sleep

import pygame

import background
import player

FPS = 0.1
player1 = player.Player(image=pygame.image.load(os.path.join('assets', 'Skeleton', 'Skeleton Walk.png')), x=0, y=250,
                        health=0, isAlive=True)
background1 = background.Background(width=500, height=300,
                                    image=pygame.image.load(os.path.join('assets', 'background.png')), rel_x=0, blity=0,
                                    x=0)

while player1.isAlive:
    sleep(FPS)
    background1.blit()
    background1.update()
    player1.blit(background1.world)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player1.isAlive = False
        if event.type == pygame.VIDEORESIZE:
            background1.world = pygame.display.set_mode((event.w, event.h),
                                                        pygame.RESIZABLE)
    pygame.display.update()
