class Player:
    def __init__(self,image, x,y,health,isAlive):
        self.image = image
        self.x = x
        self.y = y
        self.health = health
        self.isAlive = isAlive


    def blit(self, background):
        background.blit(self.image, (self.x, self.y))

