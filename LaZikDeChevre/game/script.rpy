# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Le jeu commence ici
label start:
    $ jean_inventory = []
    menu optional_name:
        "Que voulez-vous faire?"
        "Jouer au chapitre 1":
            jump chapter_1
        "Test (Nicolas)":
            jump test_nicolas
        "Test (Felix)":
            jump test_felix
        "Test (Baptiste)":
            jump test_corres
        "bar":
            jump bar 
        "choix guitar":
            jump guitare

    return
