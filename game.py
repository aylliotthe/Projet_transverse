from pygame import *
from Utile import *
from player import Player
from plateforme import *
from assets import *
from fin import *
from mapselection import *

class Game:
    def __init__(self,Personnage, Map):
        init()
        font.init()
        self.font = font.SysFont(None, 60)

        self.screen = display.set_mode((TAILLEX, TAILLEY), FULLSCREEN)

        display.set_caption("Jeu")

        self.clock = time.Clock()
        self.running = True
        self.fullscreen = True

        self.font = font.Font("Assets/Jersey10-Regular.ttf", 40)
        self.all_plateforme = sprite.Group()
        self.projectiles_joueur1 = sprite.Group()
        self.projectiles_joueur2 = sprite.Group()
        self.all_players = sprite.Group()
        self.grp_1 = sprite.Group()
        self.grp_2 = sprite.Group()
        self.i1 = HEROES[Personnage[0]]["image"]
        self.i2 = HEROES[Personnage[1]]["image"]

        map_data = MAPS[Map]
        self.background = transform.scale(map_data["fond"], (TAILLEX, TAILLEY))

        mixer.init()
        mixer.music.load("Assets/Musiques/Musique_Ingame.mp3")
        mixer.music.play(loops=-1)



        if "plateformes" in map_data:
            for plat in map_data["plateformes"]:
                plateforme = PlateformeImage(plat["image"], plat["pos"])
                self.all_plateforme.add(plateforme)
        else:
            self.all_plateforme.add(
                PlateformeRect(),
                PlateformeRect(300, 50, TAILLEX / 2 - 75, TAILLEY / 3 - 50),
                PlateformeRect(300, 25, (TAILLEX / 6) - 75, TAILLEY / 2 - 25),
                PlateformeRect(300, 25, TAILLEX - ((TAILLEX / 6) - 100), TAILLEY / 2 - 25)
            )

        self.joueur1 = Player(HEROES[Personnage[0]]["image"], 2, self.projectiles_joueur1, HEROES[Personnage[0]]["projo"])
        self.joueur2 = Player(HEROES[Personnage[1]]["image"], 1, self.projectiles_joueur2, HEROES[Personnage[1]]["projo"])

        self.all_players.add(self.joueur1, self.joueur2)
        self.grp_1.add(self.joueur1)
        self.grp_2.add(self.joueur2)

    def draw_text(self, text, pos, color=(255, 255, 255)):
        surf = self.font.render(text, True, color)
        self.screen.blit(surf, pos)

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
        bouton_menu = Rect(TAILLEX // 2 - 150, TAILLEY // 2 - 50, 350, 100)

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

            draw.rect(self.screen, (200, 0, 0), bouton_menu,border_radius=20)
            texte = self.font.render("Menu principal", True, (255, 255, 255))
            self.screen.blit(texte, (bouton_menu.x + 30, bouton_menu.y + 30))
            display.flip()
            self.clock.tick(15)

    def run(self):
        while self.running:
            for e in event.get():
                if e.type == QUIT:
                    self.running = False
                elif e.type == KEYDOWN:
                    if e.key == K_f:
                        self.fullscreen = not self.fullscreen
                        if self.fullscreen:
                            self.screen = display.set_mode((TAILLEX, TAILLEY), FULLSCREEN)
                        else:
                            self.screen = display.set_mode((TAILLEX, TAILLEY))
                    elif e.key == K_ESCAPE:
                        self.afficher_pause()

            # Gestion des vies
            if self.joueur1.life <= 0:
                self.joueur1.kill()
                return Fin(2,self.i2)
            if self.joueur2.life <= 0:
                self.joueur2.kill()
                return Fin(1,self.i1)

            # Collisions projectiles
            for projectile in self.projectiles_joueur1:
                if sprite.spritecollide(projectile, self.grp_2, False, sprite.collide_mask):
                    projectile.kill()
                    self.joueur2.degat_faible()

            for projectile in self.projectiles_joueur2:
                if sprite.spritecollide(projectile, self.grp_1, False, sprite.collide_mask):
                    projectile.kill()
                    self.joueur1.degat_faible()

            # Updates
            self.all_players.update(self.all_plateforme)
            self.projectiles_joueur1.update()
            self.projectiles_joueur2.update()

            # Affichage
            self.screen.blit(self.background, (0, 0))
            self.all_plateforme.draw(self.screen)
            self.projectiles_joueur1.draw(self.screen)
            self.projectiles_joueur2.draw(self.screen)
            self.all_players.draw(self.screen)

            self.afficher_vie(self.joueur1)
            self.afficher_vie(self.joueur2)

            self.draw_text("J1", (290, 14))
            self.draw_text("J2", (1010, 14))

            display.flip()
            self.clock.tick(FRAMERATE)
        return True

