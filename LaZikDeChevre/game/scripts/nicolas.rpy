define g = Character("Gérant", image="gerant")
default points_popularite = 0
default persuasion_win = False
label test_nicolas:
    # scene fromagerie
    "Salut moi c'est Nicolas"
    menu:
        "Qu'est-ce que je vais tester?"
        "Persuasion":
            jump test_persuasion
        "Rythme":
            jump test_rythme
    


label test_persuasion:
    call persuasion(choix_persuation_gerant, g, "gerant", 100)
    if persuasion_win:
        jump persuasion_gerant_succes
    else:
        jump persuasion_gerant_fail

label persuasion_gerant_fail:
    show gerant angry
    g "tu vas souffrir"
    return

label persuasion_gerant_succes:
    show gerant happy
    g "ça passe pour aujourd'hui"
    return

label test_rythme:
    call minigame_rythme(sequenceRythme1, 0)
    "A plus"