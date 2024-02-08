define sequence_rythme_garage = [
    (note1, 1, frequenceMedium, True),
    # (note1, 1, frequenceMedium, True),
    # (note1, 1, frequenceMedium, True),
    # (note2, 2, frequenceMedium, True),
    # (note3, 3, frequenceMedium, True),
    # (note2, 2, frequenceSlow, True),
    # (note1, 1, frequenceSlow, True),
    # (note3, 3, frequenceMedium, True),
    # (note2, 2, frequenceMedium, True),
    # (note2, 2, frequenceMedium, True),
    # (note1, 1, frequenceMedium, True),
]
default resultat_rythme_garage = 0
label minigame_rythme_garage:
    call minigame_rythme(sequence_rythme_garage, 0)
    $ resultat_rythme_garage = score_minigame_rythme
    "Chanson terminée"
    if resultat_rythme_garage >= 3:
        "Quelle incroyable performance !"
    elif resultat_rythme_garage >= 2:
        "La performance est agréable à écouter."
    else:
        "La performance n'est pas convaincante."
    return

define sequence_rythme_bar = [
    (note1, 1, frequenceMedium, True),
    # (note1, 1, frequenceMedium, True),
    # (note1, 1, frequenceMedium, True),
    # (note2, 2, frequenceMedium, True),
    # (note3, 3, frequenceMedium, True),
    # (note2, 2, frequenceSlow, True),
    # (note1, 1, frequenceSlow, True),
    # (note3, 3, frequenceMedium, True),
    # (note2, 2, frequenceMedium, True),
    # (note2, 2, frequenceMedium, True),
    # (note1, 1, frequenceMedium, True),
]
default resultat_rythme_bar = 0
label minigame_rythme_bar:
    call minigame_rythme(sequence_rythme_bar, 0)
    $ resultat_rythme_bar = score_minigame_rythme
    "Chanson terminée"
    if resultat_rythme_bar >= 3:
        "Quelle incroyable performance !"
    elif resultat_rythme_bar >= 2:
        "La performance est agréable à écouter."
    else:
        "La performance n'est pas convaincante."
    return

define sequence_rythme_rue = [
    (note1, 1, frequenceMedium, True),
    # (note1, 1, frequenceMedium, True),
    # (note1, 1, frequenceMedium, True),
    # (note2, 2, frequenceMedium, True),
    # (note3, 3, frequenceMedium, True),
    # (note2, 2, frequenceSlow, True),
    # (note1, 1, frequenceSlow, True),
    # (note3, 3, frequenceMedium, True),
    # (note2, 2, frequenceMedium, True),
    # (note2, 2, frequenceMedium, True),
    # (note1, 1, frequenceMedium, True),
]
default resultat_rythme_rue = 0
label minigame_rythme_rue:
    call minigame_rythme(sequence_rythme_rue, 0)
    $ resultat_rythme_rue = score_minigame_rythme
    "Chanson terminée"
    if resultat_rythme_rue >= 3:
        "Quelle incroyable performance !"
    elif resultat_rythme_rue >= 2:
        "La performance est agréable à écouter."
    else:
        "La performance n'est pas convaincante."
    return
