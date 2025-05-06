from pygame import *
from playerselection import HeroSelectionScreen

class HomeScreen:
    def __init__(self):
        init()
        self.screen = display.set_mode((1000, 600))
        display.set_caption("Heroes Battle - Accueil")
        self.font = font.Font("Assets/Jersey10-Regular.ttf", 40)
        self.clock = time.Clock()
        self.running = True

    def draw_text(self, text, pos, color=(255, 255, 255)):
        surf = self.font.render(text, True, color)
        self.screen.blit(surf, pos)

    def draw_button(self, text, rect, mouse_pos, click):
        color = (200, 0, 0) if rect.collidepoint(mouse_pos) else (100, 0, 0)
        draw.rect(self.screen, color, rect)
        self.draw_text(text, (rect.x + 10, rect.y + 10))
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

            self.screen.fill((30, 30, 30))
            self.draw_text("Bienvenue dans Heroes Battle", (300, 150))

            play_btn = Rect(400, 250, 200, 60)
            quit_btn = Rect(400, 330, 200, 60)

            if self.draw_button("Jouer", play_btn, mouse_pos, click):
                return HeroSelectionScreen()
            if self.draw_button("Quitter", quit_btn, mouse_pos, click):
                return False
            
            display.flip()
            self.clock.tick(60)

  