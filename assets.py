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
    },
    "CharaAltego": {
        "name": "Altego",
        "image" : charger_image("Personnage/CharaAltego/Altego.png", (tailleImagePersonnage, tailleImagePersonnage)),
        "projo": charger_image("Personnage/CharaAltego/AltegoProjo.png", (tailleImagePersonnage, tailleImagePersonnage))
    },
    "CharaPizzaiolo": {
        "name": "Pizzaiolo",
        "image" : charger_image("Personnage/CharaPizzaiolo/Pizzaiolo.png", (tailleImagePersonnage, tailleImagePersonnage)),
        "projo": charger_image("Personnage/CharaPizzaiolo/PizzaioloProjo.png", (tailleImagePersonnage, tailleImagePersonnage))
    }
}

MAPS = {
    "Chatelet": {
        "name": "Châtelet - Les Halles",
        "fond": charger_image("Map/Chatelet/ChateletMAP.png"),
        "plateformes": [
            {"image": charger_image("Map/Chatelet/ChateletMAPPlat1.png"), "pos": (590, 564)},
            {"image": charger_image("Map/Chatelet/ChateletMAPPlat2.png"), "pos": (-2, 367)},
        ],
    },
    "Nether": {
        "name": "Nether",
        "fond": charger_image("Map/Nether/NetherMap.png"),
        "plateformes": [
            {"image": charger_image("Map/Nether/NetherMAPPlat1.png"), "pos": (524, 575.5)},
            {"image": charger_image("Map/Nether/NetherMAPPlat2.png"), "pos": (436, 383.5)},
            {"image": charger_image("Map/Nether/NetherMAPPlat3.png"), "pos": (133, 218)},
            {"image": charger_image("Map/Nether/NetherMAPPlat4.png"), "pos": (555, 110)},
        ],

    },
    "Backroom": {
        "name": "Backroom",
        "fond": charger_image("Map/Backroom/BackroomMAP.png"),
        "plateformes": [
            {"image": charger_image("Map/Backroom/BackroomMAPPlat1.png"), "pos": (320,480)},
            {"image": charger_image("Map/Backroom/BackroomMAPPlat2.png"), "pos": (1000,570)},
            {"image": charger_image("Map/Backroom/BackroomMAPPlat3.png"), "pos": (640,260)},
        ],
    }
}