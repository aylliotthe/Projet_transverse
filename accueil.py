import pygame
import sys

def main():
    pygame.init()

    # --- Config ---
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Heroes Battle - Menu")
    font = pygame.font.Font("Assets/Jersey10-Regular.ttf", 40 )
    clock = pygame.time.Clock()

    # --- Assets ---
    # Replace with your actual image filenames
    HEROES = [
        {"name": "Hello Kitty", "image": pygame.image.load("Assets/Personnage/CharaKitty/Kitty.png")},
        {"name": "Messi", "image": pygame.image.load("Assets/Personnage/CharaMessi/Messi.png")},
        {"name": "Poto", "image": pygame.image.load("Assets/player.png")},
    ]

    MAPS = [
        {"name": "Chatelet", "image": pygame.image.load("Assets/Map/Chatelet/ChateletMAP.png")},
        {"name": "Nether", "image": pygame.image.load("Assets/Map/Nether/NetherMap.png")},
    ]

    # Resize images for thumbnails
    for hero in HEROES:
        hero["thumb"] = pygame.transform.scale(hero["image"], (100, 100))

    for map_ in MAPS:
        map_["thumb"] = pygame.transform.scale(map_["image"], (200, 150))

    # --- States ---
    STATE_HOME = "home"
    STATE_HERO_SELECT = "hero_select"
    STATE_MAP_SELECT = "map_select"
    state = STATE_HOME

    selected_heroes = [None, None]  # [player1, player2]
    selected_map = None

    # --- UI Elements ---
    def draw_text(text, pos, color=(255, 255, 255)):
        surf = font.render(text, True, color)
        screen.blit(surf, pos)

    def draw_button(text, rect, mouse_pos, click):
        color = (200, 0, 0) if rect.collidepoint(mouse_pos) else (100, 0, 0)
        pygame.draw.rect(screen, color, rect)
        draw_text(text, (rect.x + 10, rect.y + 10))
        return click and rect.collidepoint(mouse_pos)

    # --- Main Loop ---
    running = True
    while running:
        screen.fill((30, 30, 30))
        mouse_pos = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        if state == STATE_HOME:
            draw_text("Bienvenue dans Heroes Battle", (SCREEN_WIDTH // 2 - 200, 150))
            play_btn = pygame.Rect(SCREEN_WIDTH // 2 - 100, 250, 200, 60)
            quit_btn = pygame.Rect(SCREEN_WIDTH // 2 - 100, 330, 200, 60)

            if draw_button("Jouer", play_btn, mouse_pos, click):
                state = STATE_HERO_SELECT
            if draw_button("Quitter", quit_btn, mouse_pos, click):
                running = False

        elif state == STATE_HERO_SELECT:
            draw_text("Selectionnez votre heros", (SCREEN_WIDTH//2 - 150, 20))

            for i, hero in enumerate(HEROES):
                x = 150 + i * 150
                y = 100
                rect = pygame.Rect(x, y, 100, 100)
                screen.blit(hero["thumb"], (x, y))

                if click and rect.collidepoint(mouse_pos):
                    if selected_heroes[0] == hero:
                        selected_heroes[0] = None
                    elif selected_heroes[1] == hero:
                        selected_heroes[1] = None
                    elif selected_heroes[0] is None:
                        selected_heroes[0] = hero
                    elif selected_heroes[1] is None:
                        selected_heroes[1] = hero

            if selected_heroes[0]:
                draw_text(f"Joueur 1: {selected_heroes[0]['name']}", (20, 250))
                screen.blit(pygame.transform.scale(selected_heroes[0]['image'], (150, 150)), (20, 300))

            if selected_heroes[1]:
                draw_text(f"Joueur 2: {selected_heroes[1]['name']}", (SCREEN_WIDTH - 220, 250))
                screen.blit(pygame.transform.scale(selected_heroes[1]['image'], (150, 150)), (SCREEN_WIDTH - 220, 300))

            if selected_heroes[0] and selected_heroes[1]:
                if draw_button("Valider", pygame.Rect(SCREEN_WIDTH//2 - 75, 500, 150, 50), mouse_pos, click):
                    state = STATE_MAP_SELECT

        elif state == STATE_MAP_SELECT:
            draw_text("Selectionnez la map", (SCREEN_WIDTH//2 - 150, 20))

            for i, map_ in enumerate(MAPS):
                x = 100 + i * 280
                y = 100
                rect = pygame.Rect(x, y, 200, 150)
                screen.blit(map_["thumb"], (x, y))
                if click and rect.collidepoint(mouse_pos):
                    selected_map = map_

            if selected_map:
                draw_text(f"Map selectionnee : {selected_map['name']}", (SCREEN_WIDTH//2 - 150, 300))
                screen.blit(pygame.transform.scale(selected_map['image'], (300, 200)), (SCREEN_WIDTH//2 - 150, 350))
                if draw_button("Jouer", pygame.Rect(SCREEN_WIDTH//2 - 75, 560, 150, 40), mouse_pos, click):
                    print(f"Jouer avec {selected_heroes[0]['name']} et {selected_heroes[1]['name']} sur la map {selected_map['name']}")
                    running = False  # À remplacer par le lancement du jeu

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

