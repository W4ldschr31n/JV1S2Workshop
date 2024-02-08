# define sequenceRythme1 = [
#     (note3, frequenceFast, True),
#     (note3, frequenceFast, True),
#     (note1, frequenceSlow, True),
#     (note4, frequenceFast, False),
#     (note1, frequenceSlow, True),
#     (None, 2, True),
#     (note2, frequenceMedium, True),
#     (note1, frequenceSlow, True),
#     (None, 3, True),
#     (note3, frequenceFast, True),
#     (note4, frequenceFast, False),
#     (note3, frequenceFast, True),
#     (note3, frequenceFast, True),
# ]
define sequence_rythme_1 = [
    (note1, 1, frequenceMedium, True),
    (note1, 1, frequenceMedium, True),
    (note1, 1, frequenceMedium, True),
    (note2, 2, frequenceMedium, True),
    (note3, 3, frequenceMedium, True),
    (note2, 2, frequenceSlow, True),
    (note1, 1, frequenceSlow, True),
    (note3, 3, frequenceMedium, True),
    (note2, 2, frequenceMedium, True),
    (note2, 2, frequenceMedium, True),
    (note1, 1, frequenceMedium, True),
]

label minigame_rythme_1:
    call minigame_rythme(sequence_rythme_1, 0)
    "Minigame Fini"
    if score_minigame_rythme >= 3:
        "Quelle incroyable performance !"
    elif score_minigame_rythme >= 2:
        "La performance est agréable à écouter."
    else:
        "La performance n'est pas convaincante."

