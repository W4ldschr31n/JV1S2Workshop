

define sequence_rythme_festival = [
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

label minigame_rythme_festival:
    call minigame_rythme(sequence_rythme_festival, 0)
    "Minigame Fini"
    if score_minigame_rythme >= 3:
        "Quelle incroyable performance !"
    elif score_minigame_rythme >= 2:
        "La performance est agréable à écouter."
    else:
        "La performance n'est pas convaincante."
    return


    