define sequence_rythme_stade = [
    (note1, 1, frequenceFast, True),
    (note1, 1, frequenceFast, True),
    (note2, 2, frequenceMedium, True),
    (note2, 2, frequenceMedium, True),
    (note3, 3, frequenceMedium, True),
    (note2, 2, frequenceSlow, True),
    (note1, 1, frequenceFast, True),
    (note3, 3, frequenceMedium, True),
    (note2, 2, frequenceMedium, True),
    (note2, 2, frequenceMedium, True),
    (note1, 1, frequenceMedium, True),
]

label minigame_rythme_stade:
    call minigame_rythme(sequence_rythme_stade, 0)
    "Minigame Fini"
    if score_minigame_rythme >= 3:
        "Quelle incroyable performance !"
    elif score_minigame_rythme >= 2:
        "La performance est agréable à écouter."
    else:
        "La performance n'est pas convaincante."
    return