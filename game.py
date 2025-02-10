from pygame import *
from Utile import *
from player import Player1
from plateforme import Plateforme

class Game:
    def __init__(self):
        init()
        self.screen = display.set_mode((TAILLEX,TAILLEY))
        display.set_caption("Jeu")
        self.clock = time.Clock()
        self.running = True
        self.all_sprites = sprite.Group()
        self.fullscreen = False

    def run(self):
        plateforme1 = Plateforme()
        plateforme2 = Plateforme(400,50, TAILLEX / 3, TAILLEY/3)

        self.all_sprites.add(plateforme1, plateforme2)
        joueur1 = Player1()
        self.all_sprites.add(joueur1)

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

            joueur1.update(plateforme1, plateforme2)

            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)

            display.flip()
            self.clock.tick(FRAMERATE)

        quit()
        exit()