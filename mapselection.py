from pygame import *
from game import Game

class MapSelectionScreen:
    def __init__(self, selected_heroes):
        init()
        self.screen = display.set_mode((1000, 600))
        display.set_caption("Selection de la map")
        self.font = font.Font("Assets/Jersey10-Regular.ttf", 40)
        self.clock = time.Clock()
        self.running = True
        self.selected_heroes = selected_heroes
        self.background = image.load("Assets/background_home_screen.png")
        self.background = self.background.convert()
        self.screen.blit(self.background, (0, 0))

        self.maps = [
            {"name": "Chatelet", "image": image.load("Assets/Map/Chatelet/ChateletMAP.png")},
            {"name": "Nether", "image": image.load("Assets/Map/Nether/NetherMap.png")},
            {"name": "Backroom", "image": image.load("Assets/Map/Backroom/BackroomMAP.png")},
        ]
        for map_ in self.maps:
            map_["thumb"] = transform.scale(map_["image"], (180, 130))

        self.selected_map = None

    def draw_text(self, text, pos, color=(255, 255, 255)):
        surf = self.font.render(text, True, color)
        self.screen.blit(surf, pos)

    def draw_button(self, text, rect, mouse_pos, click):
        color = (200, 0, 0) if rect.collidepoint(mouse_pos) else (100, 0, 0)
        draw.rect(self.screen, color, rect,border_radius=20)
        self.draw_text(text, (rect.x + 40, rect.y + 7))
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

            self.draw_text("Selectionnez la map", (330, 20))

            for i, map_ in enumerate(self.maps):
                x = 100 + i * 280
                y = 100
                rect = Rect(x, y, 200, 150)
                self.screen.blit(map_["thumb"], (x, y))
                self.draw_text(map_["name"], (x + 50, y + 160))

                if click and rect.collidepoint(mouse_pos):
                    self.selected_map = map_

            if self.selected_map:
                self.draw_text(f"Map selectionnée : {self.selected_map['name']}", (330, 300))
                self.screen.blit(transform.scale(self.selected_map['image'], (300, 200)), (350, 350))

                btn_rect = Rect(425, 530, 160, 60)
                if self.draw_button("Jouer", btn_rect, mouse_pos, click):
                    return Game(self.selected_heroes, self.selected_map['name'])

            display.flip()
            self.clock.tick(60)
