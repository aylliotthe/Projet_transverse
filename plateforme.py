from pygame import *
from Utile import *

class PlateformeRect(sprite.Sprite):
    def __init__(self, longueur : float =TAILLEX,
                 hauteur : float =50,
                 x : float =0,
                 y : float = TAILLEY - (TAILLEY / 4)):
        super().__init__()
        self.image = Surface((longueur, hauteur))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = mask.from_surface(self.image)


