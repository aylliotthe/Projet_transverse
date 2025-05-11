from pygame import *


class Fin:
    def __init__(self, n_joueur, image_joueur):
        init()
        self.screen = display.set_mode((1000, 600))
        display.set_caption("Heroes Battle - Fin")
        self.font = font.Font("Assets/Jersey10-Regular.ttf", 60)
        self.clock = time.Clock()
        self.running = True
        self.background = transform.scale(image.load("Assets/victory_screen.png"), (1000, 600))
        self.background = self.background.convert()
        self.screen.blit(self.background, (0, 0))
        self.n_joueur = n_joueur
        self.image_joueur = transform.scale(image_joueur, (160, 160))

   #Permet d'importer la classe HomeScreen sans créer de beug
    def retour(self):
        from homescreen import HomeScreen
        return HomeScreen()

   #Permet de créer un texte blanc et de le placer sur une certaine position
    def draw_text(self, text, pos, color=(255, 255, 255)):
        surf = self.font.render(text, True, color)
        self.screen.blit(surf, pos)

   #Permet de céer un bouton intéractif lorsque la souris passe dessus
    def draw_button(self, text, rect, mouse_pos, click):
        color = (200, 0, 0) if rect.collidepoint(mouse_pos) else (100, 0, 0)
        draw.rect(self.screen, color, rect, border_radius=20)
        self.draw_text(text, (rect.x + 20, rect.y + 2))
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

            self.draw_text(f'Le joueur {self.n_joueur} a gagné !', (280, 250)) #Affiche le gagnant
            self.screen.blit(self.image_joueur, (400,340))

            retour_btn = Rect(790, 3, 200, 70)   #Crée un rectancle

            if self.draw_button('Rejouer', retour_btn, mouse_pos, click):  #puis dessine le bouton rejouer
                return self.retour()


            display.flip()
            self.clock.tick(60)
