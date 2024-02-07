transform custom_zoom:
    zoom 0.2
transform custom_zoom2:
    zoom 0.4

define guitrouge = Item ("guitare1","guitare1.png")
define guitbleu = Item ("guitare2","guitare2.png")
define guitvert = Item ("guitare3","guitare3.png")
define cable = Item ("cable","cable.png")

screen choixguit:
    imagebutton:
        xpos 200
        ypos 200
        idle "guitare1.png"
        at custom_zoom2
        action Jump("choix1")

    imagebutton:
        xpos 600
        ypos 200
        idle "guitare2.png"
        at custom_zoom2
        action Jump ("choix2")

    imagebutton:
        xpos 1000
        ypos 200
        idle "guitare3.png"
        at custom_zoom2
        action Jump ("choix3")


label choix1:
    $ guit_inventory.append(guitrouge)
    narrateur "ouai la meilleur"
    jump festival

label choix2:
    $ guit_inventory.append(guitbleu)
    narrateur "ouai la meilleur"
    jump festival
    

label choix3:
    $ guit_inventory.append(guitvert)
    narrateur "ouai la meilleur"
    jump festival
    



screen inventory:
    hbox:
        for i in guit_inventory:
            frame:
                xmargin 10
                ymargin 10
                add i.image zoom 0.1
                
screen loges:
    textbutton "loges":
        background "black"
        xpos 900
        ypos 700
        action Jump ("loges")

screen concert:
    textbutton "concert": 
        background "black"
        xpos 1700
        ypos 500
        action Jump ("concert")
        
screen gradin:
    textbutton "gradin":
        background "black"
        xpos 100
        ypos 500
        action Jump ("gradin")

screen cable:
    imagebutton:
        idle "cable.png"
        action Call ("recup_inventory")

label recup_inventory:
    $ guit_inventory.append(cable)
    $ cable_recupere = True
    return
    

    

