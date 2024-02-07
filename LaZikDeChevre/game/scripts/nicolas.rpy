define g = Character("Gérant", image="gerant")
default points_popularite = 0
default persuasion_win = False
default win_minigame_dodge = False
label test_nicolas:
    # scene fromagerie
    "Salut moi c'est Nicolas"
    menu:
        "Qu'est-ce que je vais tester?"
        "Persuasion":
            jump test_persuasion
        "Rythme":
            jump test_rythme
        "Dodge":
            jump test_dodge
    


label test_persuasion:
    jump persuasion_gerant

label test_rythme:
    call minigame_rythme(sequenceRythme1, 0)
    "A plus"
    return

label test_dodge:
    call minigame_dodge
    "Dans le bus [win_minigame_dodge]"
    return