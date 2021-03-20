import pygame


class Background:

    def __init__(self, image, height, width, rel_x, blity, x):
        self.image = image
        self.height = height
        self.width = width
        self.rel_x = rel_x
        self.blity = blity
        self.x = x
        self.world = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    def blit(self):
        self.world.blit(self.image, (self.rel_x - self.image.get_rect().width, self.blity))
        if self.rel_x < self.width:
            self.world.blit(self.image, (self.rel_x, self.blity))

    def update(self):
        self.x -= 5
        self.rel_x = self.x % self.image.get_rect().width
