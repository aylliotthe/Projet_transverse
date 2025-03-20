from pygame import *
from Utile import *
from vecteur import Vecteur

class Projectile(sprite.Sprite):
    def __init__(self, image_path: str, position: Vecteur, vitesse: Vecteur):
        super().__init__()
        self.original_image = image.load(image_path).convert_alpha()
        self.image = transform.scale(self.original_image, (50, 50)) 
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(position.x, position.y))

        self.vitesse = vitesse 
        self.angle = 0 

    def update(self):
        self.rect.x += self.vitesse.x
        self.rect.y += self.vitesse.y

        # Rotation du projectile
        self.angle += VITESSE_ROTATION  # Ajuste la vitesse de rotation
        self.image = transform.rotate(self.original_image, self.angle)
        self.image = transform.scale(self.image, (50, 50)) 

        self.rect = self.image.get_rect(center=self.rect.center)  # Maintient la position après rotation

        # Suppression si le projectile sort de l'écran
        if self.rect.right < 0 or self.rect.left > TAILLEX or self.rect.bottom < 0 or self.rect.top > TAILLEY:
            self.kill()
