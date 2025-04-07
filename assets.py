from os import path
from pygame import *

def charger_image(nom_image, taille=None):
    image_path = path.join(path.dirname(__file__), 'Assets', nom_image)
    try:
        img = image.load(image_path)
        if taille:
            img = transform.scale(img, taille)
        return img
    except FileNotFoundError:
        print(f"Erreur : L'image '{nom_image}' est introuvable dans {image_path}.")
        return None
    

tailleImageCoeur = 50
tailleImagePersonnage = 60

# Charger les images
coeurImage = charger_image("Coeur.png", (tailleImageCoeur, tailleImageCoeur))
demicoeurImage = charger_image("Demi_coeur.png", (tailleImageCoeur, tailleImageCoeur))



HEROES = {
    "CharaKitty": {
        "name": "Hello Kitty",
        "image": charger_image("Personnage/CharaKitty/kitty.png", (tailleImagePersonnage, tailleImagePersonnage)),
        "projo": charger_image("Personnage/CharaKitty/ProjoKitty.png", (tailleImagePersonnage, tailleImagePersonnage))
    },
    "CharaMessi": {
        "name": "Messi",
        "image": charger_image("Personnage/CharaMessi/messi.png", (tailleImagePersonnage, tailleImagePersonnage)),
        "projo": charger_image("Personnage/CharaMessi/MessiProjo.png", (tailleImagePersonnage, tailleImagePersonnage))
    },
    "Poto": {
        "name": "Poto",
        "image": charger_image("player.png", (tailleImagePersonnage, tailleImagePersonnage)),
        "projo": charger_image("Projoplayer.png", (tailleImagePersonnage, tailleImagePersonnage))
    }
}