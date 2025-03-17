from pygame import *
from Utile import *
from vecteur import Vecteur

class Projetcile(sprite.sprite):
    def __init__(self, image_path : str):
        super().__init__()
        self.image = image.load(image_path).convert_alpha()
        self.image = transform.scale(self.image, (75, 75))
        self.mask = mask.from_surface(self.image)
        