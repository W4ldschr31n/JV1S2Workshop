# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Le jeu commence ici
label start:
    menu optional_name:
        "Que voulez-vous faire?"
        "Jouer depuis le début de l'histore":
            jump chapter_1 
        "Jouer depuis le milieu de l'histoire":
            $ guit_inventory  = [guitarebase]
            show screen inventory
            jump guitare
        "Jouer la fin de l'histoire":
            $ guit_inventory  = [guitbleu]
            show screen inventory
            jump pre_stade

    return
