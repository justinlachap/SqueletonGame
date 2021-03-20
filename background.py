import pygame


class Background:

    def __init__(self, image, height, width, blitx, blity):
        self.image = image
        self.height = height
        self.width = width
        self.blitx = blitx
        self.blity = blity
        self.world = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    def blit(self):
        self.world.blit(self.image, (self.blitx, self.blity))

    def moves(self):
        self.blitx -= 3
