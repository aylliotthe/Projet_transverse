from pygame import *
from mapselection import MapSelectionScreen
from assets import HEROES

class HeroSelectionScreen:
    def __init__(self):
        init()
        self.screen = display.set_mode((1000, 600))
        display.set_caption("Selection des héros")
        self.font = font.Font("Assets/Jersey10-Regular.ttf", 40)
        self.clock = time.Clock()
        self.running = True
        self.background = image.load("Assets/background_home_screen.png")
        self.background = self.background.convert()
        self.screen.blit(self.background, (0, 0))

        self.heroes = []
        for hero in HEROES.keys():
            self.heroes.append({
                "name": HEROES[hero]["name"],
                "image": HEROES[hero]["image"],
                "thumb": transform.scale(HEROES[hero]["image"], (100, 100)),
                "clé": hero,
            })

        self.selected_heroes = [None, None]

    def draw_text(self, text, pos, color=(255, 255, 255)):
        surf = self.font.render(text, True, color)
        self.screen.blit(surf, pos)

    def draw_button(self, text, rect, mouse_pos, click):
        color = (200, 0, 0) if rect.collidepoint(mouse_pos) else (100, 0, 0)
        draw.rect(self.screen, color, rect,border_radius=20)
        self.draw_text(text, (rect.x + 30, rect.y + 3))
        return click and rect.collidepoint(mouse_pos)

    def run(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            mouse_pos = mouse.get_pos()
            click = False

            for e in event.get():
                if e.type == QUIT:
                    self.running = False
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    click = True

            self.draw_text("Selectionnez votre heros", (370, 20))

            for i, hero in enumerate(self.heroes):
                x = 150 + i * 150
                y = 100
                rect = Rect(x, y, 100, 100)
                self.screen.blit(hero["thumb"], (x, y))

                if click and rect.collidepoint(mouse_pos):
                    if self.selected_heroes[0] == hero:
                        self.selected_heroes[0] = None
                    elif self.selected_heroes[1] == hero:
                        self.selected_heroes[1] = None
                    elif self.selected_heroes[0] is None:
                        self.selected_heroes[0] = hero
                    elif self.selected_heroes[1] is None:
                        self.selected_heroes[1] = hero

            if self.selected_heroes[0]:
                self.draw_text(f"Joueur 1: {self.selected_heroes[0]['name']}", (90, 250))
                self.screen.blit(transform.scale(self.selected_heroes[0]['image'], (160, 150)), (120, 300))
            if self.selected_heroes[1]:
                self.draw_text(f"Joueur 2: {self.selected_heroes[1]['name']}", (670, 250))
                self.screen.blit(transform.scale(self.selected_heroes[1]['image'], (150, 150)), (710, 300))

            if self.selected_heroes[0] and self.selected_heroes[1]:
                btn_rect = Rect(425, 500, 150, 50)
                if self.draw_button("Valider", btn_rect, mouse_pos, click):
                    self.selected_heroes[0],self.selected_heroes[1] = self.selected_heroes[0]['clé'],self.selected_heroes[1]['clé']
                    return MapSelectionScreen(self.selected_heroes)

            display.flip()
            self.clock.tick(60)

