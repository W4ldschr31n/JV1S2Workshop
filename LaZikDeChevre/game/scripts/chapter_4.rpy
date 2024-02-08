label flashback:
    scene boulangerie
    show viktor
    viktor "Vus verrez !"
    journaliste " Vous ..."
    viktor "Optimiste..."
    narrateur "Apres cette"
    jump pre_stade

label pre_stade:
    scene maison
    show jean
    narrateur "Le lendemain"
    jean "comment"
    journaliste "une proposition"
    jean "Dans quelque mois"
    journaliste "Un grand concert"
    jean "ouai bha"
    narrateur "Jean et le petrisseur"
    journaliste "vous allez"
    jean "j'avais"
    narrateur "Un nom qui "
    jump stade

label stade:
    scene stade
    narrateur "Cela"

    scene loges
    journaliste "BOnsoir"
    rocklette "Ca va "
    narrateur "un discour"
    jump loges

label concert_stade:
    scene stade
    narrateur "Laissant"

    #jeux de rythme final
    menu :
        "jeux rythme stade win ?"
        "oui":
            $ winjeu5=True
        "non":
            $ winjeu5=False

    if winjeu5:
        jump winjeu5
    else:
        jump losejeu5


        label winjeu5:
            narrateur "Un si beau"
            #jeu esquive

            menu :
                "jeu esquive win ?"
                "oui":
                    $ winjeu6=True
                "non":
                    $ winjeu6=False

        if winjeu6:
            jump winjeu6
        else:
            jump losejeu6

        label winjeu6:
            narrateur "C'est incroyable"
            jump evac
        
        label losejeu6:
            narrateur "Sous la plui"
            jump evac


    label losejeu5:
        scene stade
        narrateur "une deception,"

    menu :
        "jeux rythme stade win ?"
        "oui":
            $ winjeu7=True
        "non":
            $ winjeu7=False

    if winjeu7:
        jump winjeu7
    else:
        jump losejeu7


    label winjeu7:
        narrateur"malgré"
        jump chute

    label losejeux7:
        narrateur "Que ce soit en musique"
        jump chute

label chute:
    narrateur "Les joueur"
    journaliste"Bonjours"
    john "Comment"
    journaliste "Je vous "
    john "Je sais "
    journaliste "Je vois"
    john "Arreter "

    narrateur "C'est sur"
    jump end_bad

label evac:
    narrateur "Rocklette"
    journaliste "Bonjours john"
    john "oh bah"
    journaliste "C'est compréhensible"
    john "Jean"
    journaliste "Nous sommes"
    john "Faut"
    journaliste"Merci"

    narrateur"Nous obtiendron"
    jump fin_good