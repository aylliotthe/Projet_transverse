##  Projet Transverse - Heroes Battle
Ce projet est un  platformer 2D réalisé avec **Pygame**, dans le cadre du *projet transverse*. Il propose une **sélection de personnages**, une **sélection de carte**, et un **lancement de partie** avec mécaniques de plateforme et d’affrontement.

## Contributeurs
  - **MASSON Eliot**
  - **KHELIF Malik**
  - **ALBADORO Nicolas**
  - **BENATMANE Laetitia**
  - **LE CLANCHE Nicolas** 


---

## Description

Le jeu propose une expérience dynamique :

1. Lancement via un écran d’accueil.
2. Sélection des personnages.
3. Sélection de la carte.
4. Début de la partie dans un environnement interactif avec plateformes, projectiles et gestion des vies.

**---

##  Fonctionnalités

- **Écran d’accueil** *(via `homescreen.py`)*
- **Sélection de héros** avec sprites personnalisés :
  - Hello Kitty 🐱
  - Messi ⚽
  - Altego 🦊 
  - Pizzaiolo 🍕
  - 
- **Sélection de la map** avec prévisualisation :
  - Châtelet
  - Nether
  - 
- **Système de combat** avec projectiles et points de vie (cœurs)
---

##  Spécifications

- **Langage** : Python 3.x  
- **Librairie** : Pygame  
- **Outils** : Git / GitHub  

---

##  Installation

### Prérequis

- Python 3.x  
- Pygame (`pip install pygame`)

### Lancer le jeu

```bash
python main.py
Exemple d’utilisation
text
Copier
Modifier
> Lancement du jeu...
> Affichage de l’écran d’accueil
> Choix du personnage : Messi
> Choix de la map : Nether
> Début de la partie : 2 personnages s’affrontent avec projectiles et plateformes
> Les cœurs affichent les points de vie restants

🗂️ Arborescence du projet
bash
Copier
Modifier
├── main.py                # Lancer ce programme
├── assets.py              
├── mapselection.py        
├── homescreen.py          
├── game.py
├── instructions.py
├── mapselection.py
├── playerselection.py
├── projectile.py
├── vecteur.py
├── player.py                      
├── fin.py
├── Assets/               
│   ├── background_home_screen.png
│   ├── Coeur.png / Demi_coeur.png
│   ├── Map/
│   │   ├── Chatelet/
│   │   └── Nether/
│   └── Personnage/
│       ├── CharaKitty/
│       ├── CharaMessi/
│       ├── CharaAltego/
│       └── CharaPizzaiolo/**
