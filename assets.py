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
        "image": charger_image("Personnage/CharaKitty/Kitty.png", (tailleImagePersonnage, tailleImagePersonnage)),
        "projo": charger_image("Personnage/CharaKitty/KittyProjo.png", (tailleImagePersonnage, tailleImagePersonnage))
    },
    "CharaMessi": {
        "name": "Messi",
        "image": charger_image("Personnage/CharaMessi/Messi.png", (tailleImagePersonnage, tailleImagePersonnage)),
        "projo": charger_image("Personnage/CharaMessi/MessiProjo.png", (tailleImagePersonnage, tailleImagePersonnage))
    }
}

MAPS = {
    "Chatelet": {
        "name": "Chatelet",
        "fond": charger_image("Map/Chatelet/ChateletMAP.png"),
        "nb_plateforme": 2,
        "plateformes": [
            {"image": charger_image("Map/Chatelet/ChateletMAPPlat1.png"), "pos": (590, 564)},
            {"image": charger_image("Map/Chatelet/ChateletMAPPlat2.png"), "pos": (-2, 367)},
        ],
    },
    "Nether": {
        "name": "Nether",
        "image": charger_image("Map/Nether/NetherMap.png", (1000, 600)),
    }
}