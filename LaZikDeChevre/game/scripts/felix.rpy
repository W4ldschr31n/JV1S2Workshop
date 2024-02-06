transform custom_zoom:
    zoom 0.2
transform custom_zoom2:
    zoom 0.1



screen choixguit:
    imagebutton:
        xpos 200
        ypos 200
        idle "guitare1.png"
        at custom_zoom2
        action Jump("choix1")

    #imagebutton:
    #    xpos 600
    #    ypos 200
    #    idle "guitare2.png"
    #    at custom_zoom2
    #    action Jump ("choix2")
#
    #imagebutton:
    #    xpos 1000
    #    ypos 200
    #    idle "guitare3.png"
    #    at custom_zoom2
    #    action Jump ("choix3")
#


screen inventory:
    hbox:
        for i in guit_inventory:
            frame:
                add i.image


