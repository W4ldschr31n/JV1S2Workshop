

label vers_loges:
    scene bg loges
    hide screen mediator
    hide screen micro
    hide screen loges
    show screen salle
    show screen gradin
    show screen party
    if not cable_recupere:
        show screen cable
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
    $ ui.interact ()
    

label vers_gradin:
    scene bg gradin
    hide screen micro
    hide screen cable
    hide screen gradin
    show screen salle
    show screen loges
    show screen party
    if not mediator_recupere:
        show screen mediator
    $ ui.interact ()
    

