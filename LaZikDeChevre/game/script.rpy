# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Le jeu commence ici
label start:
    menu optional_name:
        "Que voulez-vous faire?"
        "Jouer au chapitre 1":
            jump chapter_1 
        "Jouer au chapitre 2":
            $ guit_inventory  = [guitarebase]
            show screen inventory
            jump guitare
        "Jouer au chapitre 3":
            $ guit_inventory  = [guitbleu]
            show screen inventory
            jump pre_stade

    return
