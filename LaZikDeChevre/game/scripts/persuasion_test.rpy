default persuasion_tree_test = PersuasionTree(
    {
        0: [PersuasionChoice("Salut", "Bien le bonjour", 0, 0), PersuasionChoice("Bon toutou", "Non mais oh !", -25, 2), PersuasionChoice("Aidez-moi svp", "Avec plaisir", 30, 1)],
        1: [PersuasionChoice("Je vous souhaite une bonne journée", "Au revoir", 0, 1), PersuasionChoice("Donne ton fric", "Jamais de la vie", -25, END_BRANCH), PersuasionChoice("J'aimerais collaborer avec vous", "Bien sûr !", 30, END_BRANCH)],
        2: [PersuasionChoice("Adios raclure", "Ne reviens jamais", -10, END_BRANCH), PersuasionChoice("Milles excuses", "Mouais", 0, 2), PersuasionChoice("J'aimerais collaborer avec vous", "Et pourquoi j'accepterais ?", 10, END_BRANCH)]
    }
)


label persuasion_test:
    call persuasion(persuasion_tree_test, g, "gerant")
    if persuasion_win:
        jump persuasion_test_succes
    else:
        jump persuasion_test_fail

label persuasion_test_fail:
    show gerant angry
    g "tu vas souffrir"
    return

label persuasion_test_succes:
    show gerant happy
    g "ça passe pour aujourd'hui"
    return