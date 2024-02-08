

label loges:
    scene bg loges
    hide screen mediator
    hide screen micro
    hide screen loges
    show screen salle
    show screen gradin
    show screen party
    if not cable_recupere:
        show screen cable
    narrateur "vers"
    $ ui.interact ()
    

label vers_scene:
    scene bg_scene
    hide screen mediator
    hide screen cable
    hide screen salle
    show screen loges
    show screen gradin
    show screen party
    if not micro_recupere:
        show screen micro
    narrateur "vers"
    $ ui.interact ()
    

label gradin:
    scene bg gradin:
        zoom 0.5
    hide screen micro
    hide screen cable
    hide screen gradin
    show screen salle
    show screen loges
    show screen party
    if not mediator_recupere:
        show screen mediator
    narrateur "vers"
    $ ui.interact ()
    

