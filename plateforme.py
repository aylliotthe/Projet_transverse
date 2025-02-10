from pygame import *
from Utile import *

class Plateforme(sprite.Sprite):
    def __init__(self,longueur = TAILLEX, hauteur = 50,x = 0,y = TAILLEY - (TAILLEY / 3)):
        super().__init__()
        self.image = Surface((longueur, hauteur))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def check_collision(self, player):
        return self.rect.colliderect(player.rect)
