

label loges:
    scene loges
    hide screen mediator
    hide screen micro
    hide screen loges
    show screen concert
    show screen gradin
    show screen party
    if not cable_recupere:
        show screen cable
    narrateur "vers"
    $ ui.interact ()
    

label concert:
    scene concert
    hide screen mediator
    hide screen cable
    hide screen concert
    show screen loges
    show screen gradin
    show screen party
    if not micro_recupere:
        show screen micro
    narrateur "vers"
    $ ui.interact ()
    

label gradin:
    scene gradin
    hide screen micro
    hide screen cable
    hide screen gradin
    show screen concert
    show screen loges
    show screen party
    if not mediator_recupere:
        show screen mediator
    narrateur "vers"
    $ ui.interact ()
    

