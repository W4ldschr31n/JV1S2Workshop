init python:
    X_GUITAR = 960
    Y_GUITAR = 500
    import time
    import pygame
    MOUSEBUTTONDOWN=pygame.MOUSEBUTTONDOWN
    
    class MiniGameRythmNote:
        def __init__(self, sprite, note_sound, speed, timerStart, isGood):
            self.sprite = sprite
            self.note_sound = note_sound
            self.speed = speed
            self.timerStart = timerStart
            self.show = manager.create(sprite)
            self.show.x = -200
            self.show.y = Y_GUITAR - 32
            self.moving = False
            self.isGood = isGood
            
        def update(self):
            if store.t + self.timerStart <= time.time():
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
            if sprite.x > X_GUITAR + 32:
                if sprite.isGood:
                    store.misses += 1
                    renpy.sound.play("GUITAR_MISS.ogg")
                else:
                    store.hits += 1
                sprite.show.destroy()
                notes.remove(sprite)
        return 0.05
        
    def sprites_event(ev, x, y, st):
        if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
            for sprite in notes[:]:
                if sprite.moving:
                    if X_GUITAR - 128 <= int(sprite.x) <= X_GUITAR + 32:
                        if sprite.isGood:
                            store.hits += 1
                            renpy.sound.play("GUITAR_%s.ogg"%sprite.note_sound)
                        else:
                            store.misses += 1
                            renpy.sound.play("GUITAR_MISS.ogg")
                        sprite.show.destroy()
                        notes.remove(sprite)
                        break
            else:
                store.misses += 1
                renpy.sound.play("GUITAR_MISS.ogg")
        renpy.restart_interaction()
        if not notes:
            return True

    note1 = Image("note1.png")
    note2 = Image("note2.png")
    note3 = Image("note3.png")
    note4 = Image("note4.png")

    speedRythme1 = 20
    speedRythme2 = 30
    speedRythme3 = 40
    frequenceFast = 0.3
    frequenceMedium = 0.6
    frequenceSlow = 1.2
    
screen screen_minigame_rythme:
    text "Réussi: [hits], Raté: [misses]" xalign 0.5
    text ["Notes restantes "+str(len(notes))] xalign 0.5 yalign 0.1
    add "note_target.png" xalign 0.5 yalign 0.5


label minigame_rythme(sequence, difficulte, speedRythme):
    "Cliquez quand les notes atteignent le rond central."
    python:
        hits = 0
        misses = 0
        t = time.time()
        
        manager = SpriteManager(update=sprites_update, event=sprites_event)
        notes = []
        timerStart = 0
        for step in sequence:
            timerStart += step[2]
            if step[0] is not None:
                notes.append(MiniGameRythmNote(step[0], step[1], speedRythme, timerStart, step[3]))
        renpy.show("_", what=manager, zorder=1)
        renpy.show_screen("screen_minigame_rythme")
        
        ui.interact()
    hide screen screen_minigame_rythme
    hide _
    $ accuracy = round(hits* 100 / (hits+misses), 2)
    call fin_rythm(accuracy, difficulte) from _call_fin_rythm

    return

label fin_rythm(accuracy, difficulte):
    "Précision : [accuracy]\%"
    if accuracy > 70 + difficulte:
        $ score_minigame_rythme = 3
        "Quelle incroyable performance !"
    elif accuracy > 50 + difficulte:
        $ score_minigame_rythme = 2
        "La performance est agréable à écouter."
    else:
        $ score_minigame_rythme = 1
        "La performance n'est pas convaincante."
    return
