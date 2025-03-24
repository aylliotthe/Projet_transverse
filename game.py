from pygame import *
from Utile import *
from player import Player
from plateforme import PlateformeRect

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



    def run(self):
        plateforme1 = PlateformeRect()
        plateforme2 = PlateformeRect(300,50, TAILLEX / 2 -75, TAILLEY/3 -50)
        plateforme3 = PlateformeRect(300,25, (TAILLEX / 6) -75, TAILLEY/2 -25)
        plateforme4 = PlateformeRect(300,25, TAILLEX - ((TAILLEX / 6) -100), TAILLEY/2-25)

        self.all_plateforme.add(plateforme1, plateforme2,plateforme3,plateforme4)

        joueur1 = Player("Assets/Kitty.png",2,self.projectiles_joueur1,"Assets/KittyProjo.png")
        self.all_players.add(joueur1)
        joueur2 = Player("Assets/Messi.png",1,self.projectiles_joueur2,"Assets/MessiProjo.png")
        self.all_players.add(joueur2)

        while self.running:
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

            joueur1.update(self.all_plateforme)
            joueur2.update(self.all_plateforme)

            self.projectiles_joueur1.update()
            self.projectiles_joueur2.update()

            self.screen.fill((0,0,0))
            self.all_plateforme.draw(self.screen)
            self.projectiles_joueur1.draw(self.screen)
            self.projectiles_joueur2.draw(self.screen)
            self.all_players.draw(self.screen)


            display.flip()
            self.clock.tick(FRAMERATE)


        quit()
        exit()