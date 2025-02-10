from pygame import *
from Utile import *
from vecteur import Vecteur
VECTEUR_GRAVITE = Vecteur(0, GRAVITE)

class Player1(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image.load("C:\Users\eliot\Documents\P1 (24-25)\Semestre 2\Projet transverse\Assets\player2.jpg").convert_alpha()
        self.image = transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.accel_air = ACCELERATION_AIR
        self.accel_sol = ACCELERATION_SOL
        self.masse = MASSE
        self.speed_max = VITESSE_MAX_LATERALE_AIR

        self.vecteur_position = Vecteur(TAILLEX / 2, 0)
        self.vecteur_vitesse = Vecteur(0, 0)
        self.vecteur_acceleration = Vecteur(0, 0)
        self.au_sol = False

    def saut(self):
        if self.au_sol:
            self.au_sol = False
            return Vecteur(0, -FORCE_SAUT)
        return Vecteur(0, 0)

    def move(self, *plateformes):
        sol = None
        for plateforme in plateformes:
            personnage_tombe = self.vecteur_vitesse.y > 0 

            if plateforme.check_collision(self):  
                if personnage_tombe and self.vecteur_position.x + self.rect.width > plateforme.rect.x and self.vecteur_position.x < plateforme.rect.x + plateforme.rect.width:
                    sol = plateforme
                    self.au_sol = True
                    break  
            else:
                self.au_sol = False

        keys = key.get_pressed()
        vecteur_mouvement = Vecteur(0, 0)

        if not self.au_sol:
            if keys[K_LEFT]:
                vecteur_mouvement = Vecteur(-self.accel_air, 0)
            elif keys[K_RIGHT]:
                vecteur_mouvement = Vecteur(self.accel_air, 0)
        else:
            if keys[K_LEFT]:
                vecteur_mouvement = Vecteur(-self.accel_sol, 0)
            elif keys[K_RIGHT]:
                vecteur_mouvement = Vecteur(self.accel_sol, 0)


        vecteur_poids = self.masse * VECTEUR_GRAVITE
        vecteur_resistance = Vecteur(0, 0)
        if  self.au_sol:
            vecteur_resistance = -1*vecteur_poids

        vecteur_saut = Vecteur(0, 0)
        if keys[K_UP]:
            vecteur_saut = self.saut()

        self.vecteur_acceleration = vecteur_poids + vecteur_mouvement + vecteur_saut + vecteur_resistance
        self.vecteur_vitesse = self.vecteur_vitesse + self.vecteur_acceleration * DT

        if not self.au_sol and  self.vecteur_vitesse.x > self.speed_max:
            self.vecteur_vitesse.x = self.speed_max
        elif not self.au_sol and  self.vecteur_vitesse.x < -self.speed_max:
            self.vecteur_vitesse.x = -self.speed_max

        self.vecteur_position = (self.vecteur_position +
                                 self.vecteur_vitesse * DT +
                                 0.5 * self.vecteur_acceleration * DT ** 2)

        if self.au_sol:
            self.vecteur_position.y = sol.rect.y - self.rect.height +1
            self.vecteur_vitesse.y = 0
            self.vecteur_vitesse.x = self.vecteur_vitesse.x * FROTTEMENT

    def update(self, *plateformes):
        self.move(*plateformes)
        self.rect.x = int(self.vecteur_position.x)
        self.rect.y = int(self.vecteur_position.y)

