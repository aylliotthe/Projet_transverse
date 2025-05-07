from pygame import *

from instructions import Instructions
from playerselection import HeroSelectionScreen

import pygame

# Initialiser Pygame et le module mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Assets/Musiques/music_menu.mp3")
pygame.mixer.music.play(loops=-1)


class HomeScreen:
    def __init__(self):
        init()
        self.screen = display.set_mode((1000, 600))
        display.set_caption("Heroes Battle - Accueil")
        self.font = font.Font("Assets/Jersey10-Regular.ttf", 40)
        self.clock = time.Clock()
        self.running = True
        self.background = image.load("Assets/background_home_screen.png")
        self.background = self.background.convert()
        self.screen.blit(self.background, (0,0))

    def draw_text(self, text, pos, color=(255, 255, 255)):
        surf = self.font.render(text, True, color)
        self.screen.blit(surf, pos)

    def draw_button(self, text, rect, mouse_pos, click):
        color = (200, 0, 0) if rect.collidepoint(mouse_pos) else (100, 0, 0)
        draw.rect(self.screen, color, rect, border_radius=20)
        self.draw_text(text, (rect.x + 20, rect.y + 8))
        return click and rect.collidepoint(mouse_pos)

    def run(self):
        while self.running:
            mouse_pos = mouse.get_pos()
            click = False

            for e in event.get():
                if e.type == QUIT:
                    self.running = False
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    click = True

            self.draw_text("Bienvenue dans Heroes Battle", (300, 150))

            play_btn = Rect(400, 350, 200, 60)
            quit_btn = Rect(400, 500, 200, 60)
            info_btn = Rect(400, 430, 200, 60)


            if self.draw_button("    Jouer", play_btn, mouse_pos, click):
                return HeroSelectionScreen()
            if self.draw_button("    Quitter", quit_btn, mouse_pos, click):
                return False
            if self.draw_button("Instructions", info_btn, mouse_pos, click):
                return Instructions()
            
            display.flip()
            self.clock.tick(60)

