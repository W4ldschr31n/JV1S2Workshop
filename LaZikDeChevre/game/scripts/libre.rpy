

label loges:
    scene loges
    hide screen loges
    show screen concert
    show screen gradin
    if not cable_recupere:
        call screen cable
    narrateur "vers"
    $ ui.interact ()
    

label concert:
    scene concert
    hide screen concert
    show screen loges
    show screen gradin
    narrateur "vers"
    $ ui.interact ()
    

label gradin:
    scene gradin
    hide screen gradin
    show screen concert
    show screen loges
    narrateur "vers"
    $ ui.interact ()
    

