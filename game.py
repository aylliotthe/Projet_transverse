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
        self.all_sprites = sprite.Group()
        self.all_plateforme = sprite.Group()

        self.fullscreen = False



    def run(self):
        plateforme1 = PlateformeRect()
        plateforme2 = PlateformeRect(300,50, TAILLEX / 2 -75, TAILLEY/3 -50)
        plateforme3 = PlateformeRect(300,25, (TAILLEX / 6) -75, TAILLEY/2 -25)
        plateforme4 = PlateformeRect(300,25, TAILLEX - ((TAILLEX / 6) -100), TAILLEY/2-25)

        self.all_plateforme.add(plateforme1, plateforme2,plateforme3,plateforme4)
        self.all_sprites.add(plateforme1, plateforme2,plateforme3,plateforme4)

        joueur1 = Player("Assets/player.png",2)
        self.all_sprites.add(joueur1)
        joueur2 = Player("Assets/player.png",1)
        self.all_sprites.add(joueur2)

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

            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)

            display.flip()
            self.clock.tick(FRAMERATE)

        quit()
        exit()