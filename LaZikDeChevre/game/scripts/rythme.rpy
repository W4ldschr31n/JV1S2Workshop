init python:
    config.screen_width=1920
    config.screen_height=1080
    X_GUITAR = 1000
    Y_GUITAR = 500
    import time
    import pygame
    MOUSEBUTTONDOWN=pygame.MOUSEBUTTONDOWN
    
    class MiniGameRythmNote:
        def __init__(self, sprite, speed, timerStart):
            self.sprite = sprite
            self.speed = speed
            self.timerStart = timerStart
            self.show = manager.create(sprite)
            self.show.x = -64
            self.show.y = Y_GUITAR
            self.moving = False
            
        def update(self):
            if store.t + self.timerStart < time.time():
                self.moving = True
                self.x = self.x + self.speed
            else:
                pass
            
        @property
        def x(self):
            return self.show.x
        @x.setter
        def x(self, value):
            self.show.x = value
            
        @property
        def y(self):
            return self.show.y
        @y.setter
        def y(self, value):
            self.show.y = value
            
    def sprites_update(st):
        for sprite in notes[:]:
            sprite.update()
            if sprite.x > X_GUITAR + 40:
                sprite.show.destroy()
                notes.remove(sprite)
                store.misses += 1
        return 0.05
        
    def sprites_event(ev, x, y, st):
        if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
            for sprite in notes[:]:
                if sprite.moving:
                    if X_GUITAR - 40 <= int(sprite.x) <= X_GUITAR + 40:
                        store.hits += 1
                        sprite.show.destroy()
                        notes.remove(sprite)
                        break
            else:
                store.misses += 1
                notes[0].show.destroy()
                notes.pop(0)
        renpy.restart_interaction()
        if not notes:
            return True

    note1 = Image("note1.png")
    note2 = Image("note2.png")
    note3 = Image("note3.png")

    speedRythme1 = 20
    frequenceFast = 0.3
    frequenceMedium = 0.5
    frequenceSlow = 1.0
    
define sequenceRythme1 = [
    (note3, frequenceFast),
    (note3, frequenceFast),
    (note1, frequenceSlow),
    (note1, frequenceSlow),
    (None, 2),
    (note2, frequenceMedium),
    (note1, frequenceSlow),
    (None, 3),
    (note3, frequenceFast),
    (note3, frequenceFast),
    (note3, frequenceFast),
]
screen screen_minigame_rythme:
    text "Réussi: [hits], Raté: [misses]!" xalign 0.5
    text ["Notes restantes "+str(len(notes))] xalign 0.5 yalign 0.1
    add "guitare.png" xalign 0.5 yalign 0.5
    frame:
        area (X_GUITAR-40, Y_GUITAR-100, 80, 200)


label minigame_rythme(sequence, difficulte):
    python:
        hits = 0
        misses = 0
        t = time.time()
        
        manager = SpriteManager(update=sprites_update, event=sprites_event)
        notes = []
        timerStart = 0
        for step in sequenceRythme1:
            timerStart += step[1]
            if step[0] is not None:
                notes.append(MiniGameRythmNote(step[0], speedRythme1, timerStart))
        renpy.show_screen("screen_minigame_rythme")
        renpy.show("_", what=manager, zorder=1)
        
    while notes:
        $ result = ui.interact()
    hide screen screen_minigame_rythme
    hide _
    $ accuracy = round(hits* 100 / (hits+misses), 2)
    call fin_rythm(accuracy, difficulte)

    return

label fin_rythm(accuracy, difficulte):
    ""
    "Précision : [accuracy]\%"
    image fini = ConditionSwitch("accuracy > 70 + difficulte", "bigwin.jpg", "accuracy > 50 + difficulte", "smallwin.jpg", "True", "lose.jpg")
    scene fini with fade
    pause 3
    hide fini
    g "allo"
    g "oskour"
    return