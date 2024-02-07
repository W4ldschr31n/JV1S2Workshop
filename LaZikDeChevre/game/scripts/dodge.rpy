init python:
    import time
    import pygame
    KEY_D = pygame.K_RIGHT
    KEY_Q = pygame.K_LEFT
    speed_player = 50
    size_player = 64
    TIMER_MAX = 5
    
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
        renpy.restart_interaction()

    def spawn_projectiles():
        projectiles.append(MiniGameDodgeProjectile(Text('O'), 50, renpy.random.randint(0, 1920)))

screen screen_minigame_dodge:
    timer 0.1 repeat True action If(remaining_timer > 0, true=SetVariable('remaining_timer', round(remaining_timer - 0.1, 1)), false=Jump("fin_dodge_win"))
    text "Temps restant: [remaining_timer]" xalign 0.5

label minigame_dodge:
    python:
        remaining_timer = TIMER_MAX
        manager = SpriteManager(update=sprites_update_dodge, event=sprites_event_dodge)
        projectiles = []
        player = MiniGameDodgePlayer(Text('P'), speed_player)
        renpy.show_screen("screen_minigame_dodge")
        renpy.show("_", what=manager, zorder=1)
        
        result = ui.interact()
    jump fin_dodge_lose

label fin_dodge_win:
    hide screen screen_minigame_dodge
    hide _
    "Gagné"
    $ win_minigame_dodge = True
    return

label fin_dodge_lose:
    hide screen screen_minigame_dodge
    hide _
    "Perdu"
    $ win_minigame_dodge = False
    return