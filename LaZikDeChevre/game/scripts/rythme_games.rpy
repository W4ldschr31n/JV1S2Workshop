define sequence_rythme_garage = [
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
default resultat_rythme_garage = 0
label minigame_rythme_garage:
    call minigame_rythme(sequence_rythme_garage, 0, speedRythme1)
    $ resultat_rythme_garage = score_minigame_rythme
    "Chanson terminée"
    return

define sequence_rythme_bar = [
    (note1, 1, frequenceMedium, True),
    (note2, 3, frequenceMedium, True),
    (note3, 5, frequenceMedium, True),
    (note2, 1, frequenceSlow, True),
    (note2, 3, frequenceMedium, True),
    (note3, 6, frequenceSlow, True),
    (note3, 5, frequenceFast, True),
    (note1, 1, frequenceSlow, True),
    (note2, 3, frequenceMedium, True),
    (note3, 5, frequenceMedium, True),
    (note2, 3, frequenceSlow, True),
    (note1, 1, frequenceMedium, True),
]
default resultat_rythme_bar = 0
label minigame_rythme_bar:
    call minigame_rythme(sequence_rythme_bar, 0, speedRythme2)
    $ resultat_rythme_bar = score_minigame_rythme
    return

define sequence_rythme_rue = [
    (note1, 1, frequenceMedium, True),
    (note1, 3, frequenceMedium, True),
    (note1, 3, frequenceMedium, True),
    (note1, 3, frequenceMedium, True),
    (note1, 4, frequenceMedium, True),
    (note1, 3, frequenceMedium, True),
    (note1, 3, frequenceSlow, True),
    (note1, 4, frequenceFast, True),
    (note1, 5, frequenceFast, True),
    (note1, 5, frequenceMedium, True),
    (note1, 5, frequenceMedium, True),
    (note1, 6, frequenceMedium, True),
    (note1, 5, frequenceMedium, True),
]
default resultat_rythme_rue = 0
label minigame_rythme_rue:
    call minigame_rythme(sequence_rythme_rue, 0, speedRythme2)
    $ resultat_rythme_rue = score_minigame_rythme
    return


define sequence_rythme_festival = [
    (note1, 6, frequenceFast, True),
    (note1, 6, frequenceMedium, True),
    (note2, 8, frequenceFast, True),
    (note2, 6, frequenceFast, True),
    (note3, 5, frequenceFast, True),
    (note2, 3, frequenceMedium, True),
    (note1, 2, frequenceMedium, True),

    (note1, 6, frequenceSlow, True),
    (note1, 6, frequenceMedium, True),
    (note2, 8, frequenceFast, True),
    (note2, 6, frequenceFast, True),
    (note3, 5, frequenceFast, True),
    (note2, 3, frequenceFast, True),
    (note1, 4, frequenceFast, True),
    (note1, 3, frequenceFast, True),
    (note1, 2, frequenceFast, True),
]
default resultat_rythme_festival = 0
label minigame_rythme_festival:
    call minigame_rythme(sequence_rythme_festival, 0, speedRythme2)
    $ resultat_rythme_festival = score_minigame_rythme
    return

define sequence_rythme_stade = [
    (note1, 1, frequenceFast, True),
    (note1, 4, frequenceFast, True),
    (note1, 7, frequenceFast, True),
    (note1, 4, frequenceFast, True),
    (note4, 4, frequenceFast, False),
    (note1, 4, frequenceFast, True),
    (note1, 3, frequenceFast, True),
    (note4, 1, frequenceMedium, False),
    (note1, 1, frequenceFast, True),
    (note1, 4, frequenceFast, True),
    (note1, 7, frequenceFast, True),
    (note1, 4, frequenceFast, True),
    (note4, 4, frequenceFast, False),
    (note1, 8, frequenceFast, True),
    (note1, 7, frequenceFast, True),

    (note1, 1, frequenceSlow, True),
    (note1, 4, frequenceFast, True),
    (note1, 7, frequenceFast, True),
    (note1, 4, frequenceFast, True),
    (note4, 4, frequenceFast, False),
    (note1, 4, frequenceFast, True),
    (note1, 3, frequenceFast, True),
    (note4, 1, frequenceMedium, False),
    (note1, 1, frequenceFast, True),
    (note1, 4, frequenceFast, True),
    (note1, 7, frequenceFast, True),
    (note1, 4, frequenceFast, True),
    (note4, 4, frequenceFast, False),
    (note1, 8, frequenceFast, True),
    (note1, 7, frequenceFast, True),
]

default resultat_rythme_stade = 0
label minigame_rythme_stade:
    call minigame_rythme(sequence_rythme_stade, 0, speedRythme3)
    $ resultat_rythme_stade = score_minigame_rythme
    return