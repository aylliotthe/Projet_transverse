from pygame import *
from Utile import *
from vecteur import Vecteur

VECTEUR_GRAVITE = Vecteur(0, GRAVITE)

class Player(sprite.Sprite):
    def __init__(self, image_path : str,
                 num_joueur: int):
        super().__init__()
        self.image = image.load(image_path).convert_alpha()
        self.image = transform.scale(self.image, (75, 75))
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.accel_air = ACCELERATION_AIR
        self.accel_sol = ACCELERATION_SOL
        self.masse = MASSE
        self.speed_max = VITESSE_MAX_LATERALE_AIR

        self.vecteur_position = Vecteur(TAILLEX / 2, 0)
        self.vecteur_vitesse = Vecteur(0, 0)
        self.vecteur_acceleration = Vecteur(0, 0)

        self.au_sol = False
        self.en_saut = False

        if num_joueur == 1:
            self.touches = [K_LEFT,K_RIGHT,K_UP]
        elif num_joueur == 2:
            self.touches = [K_q,K_d,K_z]

    def collision(self, grp_plateforme):
        """Détecte et résout les collisions avec les plateformes."""
        self.au_sol = False

        temp_rect = self.rect.copy()
        temp_rect.x = int(self.vecteur_position.x)
        temp_rect.y = int(self.vecteur_position.y)

        for plateforme in grp_plateforme:
            if temp_rect.colliderect(plateforme.rect):
                dx = (temp_rect.x + temp_rect.width / 2) - (plateforme.rect.x + plateforme.rect.width / 2)
                dy = (temp_rect.y + temp_rect.height / 2) - (plateforme.rect.y + plateforme.rect.height / 2)

                overlap_x = (temp_rect.width + plateforme.rect.width) / 2 - abs(dx)
                overlap_y = (temp_rect.height + plateforme.rect.height) / 2 - abs(dy)
            
                if overlap_x > overlap_y: # Collision verticale
                    if dy > 0:  # Collision par le bas (le joueur tombe sur la plateforme)
                        self.vecteur_position.y += overlap_y
                        self.vecteur_vitesse.y = 0
                        self.au_sol = True
                        self.en_saut = True
                    else:  # Collision par le haut (le joueur saute contre la plateforme)
                        self.vecteur_position.y -= overlap_y
                        self.vecteur_vitesse.y = 0
                        self.au_sol = True 
                        self.en_saut = False
                else:  # Collision horizontale
                    if dx > 0:  # Collision côté droit
                        self.vecteur_position.x += overlap_x
                        self.vecteur_vitesse.x = 0
                        self.au_sol = True  
                        self.en_saut = True
                    else:  # Collision côté gauche
                        self.vecteur_position.x -= overlap_x
                        self.vecteur_vitesse.x = 0
                        self.au_sol = True 
                        self.en_saut = True


    def saut(self):
        """Gère le saut du joueur."""
        if self.au_sol and not self.en_saut: 
            self.en_saut = True 
            self.au_sol = False
            return Vecteur(0, -FORCE_SAUT) 
        return Vecteur(0, 0) 

    def appliquer_frottement(self):
        if self.au_sol:
            self.vecteur_vitesse.x *= FROTTEMENT

    def limiter_vitesse(self):
        if not self.au_sol and self.vecteur_vitesse.x > self.speed_max:
            self.vecteur_vitesse.x = self.speed_max
        elif not self.au_sol and self.vecteur_vitesse.x < -self.speed_max:
            self.vecteur_vitesse.x = -self.speed_max

    def move(self):
        keys = key.get_pressed()
        vecteur_mouvement = Vecteur(0, 0)

        if not self.au_sol:
            if keys[self.touches[0]]:
                vecteur_mouvement = Vecteur(-self.accel_air, 0)
            elif keys[self.touches[1]]:
                vecteur_mouvement = Vecteur(self.accel_air, 0)
        else:
            if keys[self.touches[0]]:
                vecteur_mouvement = Vecteur(-self.accel_sol, 0)
            elif keys[self.touches[1]]:
                vecteur_mouvement = Vecteur(self.accel_sol, 0)
        
        
        vecteur_saut = Vecteur(0, 0)
        if keys[self.touches[2]]:
            vecteur_saut = self.saut()

        vecteur_poids = self.masse * VECTEUR_GRAVITE
        vecteur_resistance = Vecteur(0, 0)
        if self.au_sol:
            vecteur_resistance = -1*vecteur_poids

        self.vecteur_acceleration = vecteur_poids + vecteur_mouvement + vecteur_saut + vecteur_resistance
        self.vecteur_vitesse = self.vecteur_vitesse + self.vecteur_acceleration * DT

        self.appliquer_frottement()

        self.limiter_vitesse()

        self.vecteur_position = (
            self.vecteur_position +
            self.vecteur_vitesse * DT +
            0.5 * self.vecteur_acceleration * (DT ** 2)
        )

    def update(self, grp_plateforme):
        self.move()
        self.collision(grp_plateforme)

        self.vecteur_position.x = max(0, min(self.vecteur_position.x, TAILLEX - self.rect.width))

        self.rect.x = int(self.vecteur_position.x)
        self.rect.y = int(self.vecteur_position.y)