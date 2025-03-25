from pygame import *
from Utile import *
from player import Player
from plateforme import PlateformeRect
from assets import *

class Game:
    def __init__(self):
        init()
        self.screen = display.set_mode((TAILLEX,TAILLEY))
        display.set_caption("Jeu")
        self.clock = time.Clock()
        self.running = True
        self.fullscreen = False

        self.all_plateforme = sprite.Group()
        self.projectiles_joueur1 = sprite.Group()
        self.projectiles_joueur2 = sprite.Group()
        self.all_players = sprite.Group()
        self.grp_1 = sprite.Group()
        self.grp_2 = sprite.Group()

    def afficher_vie(self, joueur):
        if joueur.num == 2:
            x = 50
            y = 10
            k = 1
        else:
            x = TAILLEX - 50
            y = 10
            k = -1

        nb_vie = joueur.life

        for i in range(nb_vie//2):
            self.screen.blit(coeurImage, (x, y))
            x += k * 50

        nb_vie = nb_vie % 2

        for i in range(nb_vie):
            self.screen.blit(demicoeurImage, (x, y))
            x += k * 50

    def run(self):
        plateforme1 = PlateformeRect()
        plateforme2 = PlateformeRect(300,50, TAILLEX / 2 -75, TAILLEY/3 -50)
        plateforme3 = PlateformeRect(300,25, (TAILLEX / 6) -75, TAILLEY/2 -25)
        plateforme4 = PlateformeRect(300,25, TAILLEX - ((TAILLEX / 6) -100), TAILLEY/2-25)

        self.all_plateforme.add(plateforme1, plateforme2,plateforme3,plateforme4)

        joueur1 = Player(kittyImage,2,self.projectiles_joueur1,"Assets/Personnage/CharaKitty/KittyProjo.png")
        self.all_players.add(joueur1)
        self.grp_1.add(joueur1)
        joueur2 = Player(messiImage,1,self.projectiles_joueur2,"Assets/Personnage/CharaMessi/MessiProjo.png")
        self.all_players.add(joueur2)
        self.grp_2.add(joueur2)

        while self.running:

            if joueur1.life <= 0:
                joueur1.kill()
            if joueur2.life <= 0:
                joueur2.kill()

            for e in event.get():
                if e.type == QUIT:
                    self.running = False
                if e.type == KEYDOWN:
                    if e.key == K_f: 
                        self.fullscreen = not self.fullscreen
                        if self.fullscreen:
                            self.screen = display.set_mode((0, 0), FULLSCREEN)
                        else:
                            self.screen = display.set_mode((TAILLEX, TAILLEY))

            for projectile in self.projectiles_joueur1:
                collisions = sprite.spritecollide(projectile,self.grp_2, False, sprite.collide_mask)
                if collisions:
                    projectile.kill()
                    joueur2.degat_faible()

            for projectile in self.projectiles_joueur2:
                collisions = sprite.spritecollide(projectile,self.grp_1, False, sprite.collide_mask)
                if collisions:
                    projectile.kill()
                    joueur1.degat_faible()

            joueur1.update(self.all_plateforme)
            joueur2.update(self.all_plateforme)

            self.projectiles_joueur1.update()
            self.projectiles_joueur2.update()

            self.screen.fill((0,0,0))
            self.all_plateforme.draw(self.screen)
            self.projectiles_joueur1.draw(self.screen)
            self.projectiles_joueur2.draw(self.screen)
            self.all_players.draw(self.screen)
            
            self.afficher_vie(joueur1)
            self.afficher_vie(joueur2)

        
            display.flip()
            self.clock.tick(FRAMERATE)


        quit()
        exit()