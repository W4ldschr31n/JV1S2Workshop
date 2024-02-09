default persuasion_tree_gerant = PersuasionTree(
    {
        0: [PersuasionChoice("Supplier", "Arrête de geindre, ça m'agace !", -10, 1), PersuasionChoice("Menacer", "Tu te crois supérieur, sale mioche ?", -30, 2), PersuasionChoice("Lever les yeux au ciel", "Tu viens de lever les yeux au ciel ?", 0, 0), PersuasionChoice("Persuader", "Intéressant, continue.", 10, 3)],
        1: [PersuasionChoice("Insister", "Sors de mon bar, tu es insupportable !", -10, END_BRANCH), PersuasionChoice("S'excuser", "Bon, bon... ne prenons pas la mouche.", 0, 1), PersuasionChoice("Expliquer calmement", "D'accord, ça peut être intéressant.", 30, 3)],
        2: [PersuasionChoice("S'offusquer", "Va faire ton caprice ailleurs !", -30, END_BRANCH), PersuasionChoice("Soupirer", "Le culot que tu as est impressionant !", -10, END_BRANCH), PersuasionChoice("S'excuser", "Hmm...", 0, 2)],
        3: [PersuasionChoice("Faire des éloges", "Tu vas me faire rougir !", 30, END_BRANCH), PersuasionChoice("Se vanter", "Tu te prends pour le roi du monde ?", -10, END_BRANCH), PersuasionChoice("Argumenter", "C'est vrai que ça serait bénéfique...", 10, END_BRANCH)],
    }
)


label persuasion_gerant:
    python:
        if resultat_rythme_garage >= 3:
            contextual_choice = PersuasionChoice("Montrer la vidéo de sa performance", "Tu as un talent incroyable !", 100, END_BRANCH)
        elif resultat_rythme_garage >= 2:
            contextual_choice = PersuasionChoice("Montrer la vidéo de sa performance", "Pas mal pour un débutant.", 10, 0)
        else:
            contextual_choice = PersuasionChoice("Montrer la vidéo de sa performance", "Euh... non merci.", -100, END_BRANCH)
        persuasion_tree_gerant.contextual_choice = contextual_choice
    call persuasion(persuasion_tree_gerant, gerant, "gerant")
    if persuasion_win:
        jump persuasion_gerant_succes
    else:
        jump persuasion_gerant_fail

label persuasion_gerant_fail:
    jump rue

label persuasion_gerant_succes:
    jump prestabar