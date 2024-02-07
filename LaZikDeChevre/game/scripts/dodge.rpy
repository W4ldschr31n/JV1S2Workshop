init python:
    import time
    import pygame
    KEY_D = pygame.K_RIGHT
    KEY_Q = pygame.K_LEFT
    speed_player = 50
    size_player = 64
    TIMER_MAX = 20
    
    class MiniGameDodgePlayer:
        def __init__(self, sprite, speed):
            self.sprite = sprite
            self.speed = speed
            self.show = manager.create(sprite)
            self.show.x = 960
            self.show.y = 600
        
        def update(self):
            self.x += self.speed
            
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
            

    class MiniGameDodgeProjectile:
        def __init__(self, sprite, speed, xpos):
            self.sprite = sprite
            self.speed = speed
            self.show = manager.create(sprite)
            self.show.x = xpos
            self.show.y = 0
            
        def update(self):
            self.y = self.y + self.speed
            
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
            
    def sprites_update_dodge(st):
        for sprite in projectiles[:]:
            sprite.update()
            if sprite.y > 1080:
                sprite.show.destroy()
                projectiles.remove(sprite)
        
        player.update()
        spawn_projectiles()
        store.remaining_timer = round(TIMER_MAX - st, 1)
        return 0.05
        
    def sprites_event_dodge(ev, x, y, st):
        keys = pygame.key.get_pressed()
        if keys[KEY_Q]:
            player.speed = -speed_player
        elif keys[KEY_D]:
            player.speed = speed_player
        else:
            player.speed = 0
        for sprite in projectiles:
            if (
                player.x - size_player < sprite.x < player.x + size_player
                and
                player.y - size_player < sprite.y < player.y + size_player
            ):
                return False
        
        if store.remaining_timer <= 0:
            return True
        renpy.restart_interaction()

    def spawn_projectiles():
        projectiles.append(MiniGameDodgeProjectile(Text('O'), 50, renpy.random.randint(0, 1920)))

        # if ev.type == KEYDOWN and ev.key == 1:
        #     for sprite in notes[:]:
        #         if sprite.moving:
        #             if X_GUITAR - 40 <= int(sprite.x) <= X_GUITAR + 40:
        #                 if sprite.isGood:
        #                     store.hits += 1
        #                 else:
        #                     store.misses += 1
        #                 sprite.show.destroy()
        #                 notes.remove(sprite)
        #                 break
        #     else:
        #         store.misses += 1
        #         # nearly hit
        #         if notes[0].x >= X_GUITAR - 100:
        #             notes[0].show.destroy()
        #             notes.pop(0)
        # renpy.restart_interaction()
        # if not notes:
        #     return True

    # note1 = Image("note1.png")
    # note2 = Image("note2.png")
    # note3 = Image("note3.png")
    # note4 = Image("note4.png")

    # speedRythme1 = 20
    # frequenceFast = 0.3
    # frequenceMedium = 0.5
    # frequenceSlow = 1.0

screen screen_minigame_dodge:
    text "Temps restant: [remaining_timer]" xalign 0.5
    # add "guitare.png" xalign 0.5 yalign 0.5
    # frame:
    #     area (X_GUITAR-40, Y_GUITAR-100, 80, 200)


label minigame_dodge:
    python:
        remaining_timer = TIMER_MAX
        # t = time.time()
        
        manager = SpriteManager(update=sprites_update_dodge, event=sprites_event_dodge)
        projectiles = []
        player = MiniGameDodgePlayer(Text('P'), speed_player)
        renpy.show_screen("screen_minigame_dodge")
        renpy.show("_", what=manager, zorder=1)
        
        result = ui.interact()
    hide screen screen_minigame_dodge
    hide _
    # $ accuracy = round(hits* 100 / (hits+misses), 2)
    call fin_dodge()

    return

label fin_dodge():
    "C'est fini"
    # "Précision : [accuracy]\%"
    # image fini = ConditionSwitch("accuracy > 70 + difficulte", "bigwin.jpg", "accuracy > 50 + difficulte", "smallwin.jpg", "True", "lose.jpg")
    # scene fini with fade
    # pause 3
    # hide fini
    # g "allo"
    # g "oskour"
    return
