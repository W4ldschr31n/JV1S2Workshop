# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Le jeu commence ici
label start:

    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    e " bonjours j'aime la prog"

    menu optional_name:
        "Que voulez-vous faire?"
        "Jouer au chapitre 1":
            jump chapter_1
        "Test (Nicolas)":
            jump test_nicolas
        "Test (Felix)":
            jump test_felix       

    return
