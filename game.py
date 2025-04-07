from pygame import *
from Utile import *
from player import Player
from plateforme import PlateformeRect
from assets import *

class Game:
    def __init__(self):
        init()
        font.init()
        self.font = font.SysFont(None, 60)

        self.screen = display.set_mode((TAILLEX, TAILLEY), FULLSCREEN)
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
            x, y, direction = 50, 10, 1
        else:
            x, y, direction = TAILLEX - 50, 10, -1

        for _ in range(joueur.life // 2):
            self.screen.blit(coeurImage, (x, y))
            x += direction * 50

        if joueur.life % 2:
            self.screen.blit(demicoeurImage, (x, y))

    def afficher_pause(self):
        paused = True
        bouton_menu = Rect(TAILLEX // 2 - 150, TAILLEY // 2 - 50, 300, 100)

        while paused:
            for event_pause in event.get():
                if event_pause.type == QUIT:
                    self.running = False
                    return
                if event_pause.type == KEYDOWN and event_pause.key == K_ESCAPE:
                    return
                if event_pause.type == MOUSEBUTTONDOWN and bouton_menu.collidepoint(event_pause.pos):
                    self.running = False
                    return

            draw.rect(self.screen, (200, 0, 0), bouton_menu)
            texte = self.font.render("Menu principal", True, (255, 255, 255))
            self.screen.blit(texte, (bouton_menu.x + 30, bouton_menu.y + 30))
            display.flip()
            self.clock.tick(15)

    def run(self):
        # Plateformes
        self.all_plateforme.add(
            PlateformeRect(),
            PlateformeRect(300, 50, TAILLEX / 2 - 75, TAILLEY / 3 - 50),
            PlateformeRect(300, 25, (TAILLEX / 6) - 75, TAILLEY / 2 - 25),
            PlateformeRect(300, 25, TAILLEX - ((TAILLEX / 6) - 100), TAILLEY / 2 - 25)
        )

        # Joueurs
        joueur1 = Player(kittyImage, 2, self.projectiles_joueur1, "Assets/Personnage/CharaKitty/KittyProjo.png")
        joueur2 = Player(messiImage, 1, self.projectiles_joueur2, "Assets/Personnage/CharaMessi/MessiProjo.png")

        self.all_players.add(joueur1, joueur2)
        self.grp_1.add(joueur1)
        self.grp_2.add(joueur2)

        while self.running:
            for e in event.get():
                if e.type == QUIT:
                    self.running = False
                elif e.type == KEYDOWN:
                    if e.key == K_f:
                        self.fullscreen = not self.fullscreen
                        if self.fullscreen:
                            self.screen = display.set_mode((0, 0), FULLSCREEN)
                        else:
                            self.screen = display.set_mode((TAILLEX, TAILLEY))
                    elif e.key == K_ESCAPE:
                        self.afficher_pause()

            # Gestion des vies
            if joueur1.life <= 0:
                joueur1.kill()
            if joueur2.life <= 0:
                joueur2.kill()

            # Collisions projectiles
            for projectile in self.projectiles_joueur1:
                if sprite.spritecollide(projectile, self.grp_2, False, sprite.collide_mask):
                    projectile.kill()
                    joueur2.degat_faible()

            for projectile in self.projectiles_joueur2:
                if sprite.spritecollide(projectile, self.grp_1, False, sprite.collide_mask):
                    projectile.kill()
                    joueur1.degat_faible()

            # Updates
            self.all_players.update(self.all_plateforme)
            self.projectiles_joueur1.update()
            self.projectiles_joueur2.update()

            # Affichage
            self.screen.fill((0, 0, 0))
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
