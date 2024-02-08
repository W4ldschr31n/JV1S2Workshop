transform custom_zoom:
    zoom 0.2
transform custom_zoom2:
    zoom 0.4

transform custom_cable:
    zoom 0.2
    xalign 0.55
    yalign 0.8

transform custom_micro:
    zoom 0.2
    xalign 0.91
    yalign 0.85

transform custom_mediator:
    zoom 0.05
    xalign 0.045
    yalign 0.3

define guitrouge = Item ("guitare1","guitare1.png")
define guitbleu = Item ("guitare2","guitare2.png")
define guitvert = Item ("guitare3","guitare3.png")
define guitviolet = Item ("guitare4","guitar4.png")
define cable = Item ("cable","cable.png")
define mediator = Item ("mediator","mediator.png")
define micro = Item ("micro","micreau.png")


screen choixguit:
    grid 2 2:
        imagebutton:
            xpos 180
            ypos 140
            idle "guitare1.png"
            at custom_zoom2
            action Jump("choix1")

        imagebutton:
            xpos 120
            ypos 100
            idle "guitare2.png"
            at custom_zoom2
            action Jump ("choix2")

        imagebutton:
            xpos 200
            ypos 200
            idle "guitare3.png"
            at custom_zoom2
            action Jump ("choix3")
        
        imagebutton:
            xpos 120
            ypos 180
            idle "guitare4.png"
            at custom_zoom2
            action Jump ("choix4")


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
    frame :
        ymargin 10
        xmargin 10
        hbox:
            for i in guit_inventory:
                frame:
                    background "#ffffff"
                    xmargin 10
                    ymargin 10
                    add i.image zoom 0.1
                
screen loges:
    textbutton "loges":
        background "black"
        xpos 900
        ypos 700
        action Jump ("loges")

screen salle:
    textbutton "Scène": 
        background "black"
        xpos 1700
        ypos 500
        action Jump ("vers_scene")
        
screen gradin:
    textbutton "gradin":
        background "black"
        xpos 100
        ypos 500
        action Jump ("gradin")

screen party:
    textbutton "vers le concert ":
        background "black"
        xpos 900
        ypos 100
        action Call ("validation")

label validation:
    if all([cable_recupere, mediator_recupere, micro_recupere]):
        hide screen salle
        hide screen loges
        hide screen gradin
        narrateur "La nuit tombe, l'excitation est à son paroxysme: la foule ne tient plus en place. Enfin, la première star monte sur scène: le Petrisseur lance les hostilités. 
        Ces quelques minutes semblent avoir été jouées en quelques secondes. Des fans en délire, la tête résonnante : le niveau entre Rockbihan et ce soir n'est clairement plus le même. 
        Une progression impressionnante qui témoigne de la rage de vaincre de la fameuse rockstar qui conquit les scènes depuis plus de 2 ans et qui ne semble pas prête de s'arrêter.  
        A peine avons-nous eu le temps de souffler que Rocklette entre en scène confiant, et sans un mot entame sa prestation. "
        jump concert_stade
    else :
        narrateur "Il vous manque des objet"
        return

screen cable:
    imagebutton:
        idle "cable.png" at custom_cable
        action Call ("recup_cable")

screen mediator:
    imagebutton:
        idle "mediator.png" at custom_mediator
        action Call ("recup_mediator")

screen micro:
    imagebutton:
        idle "micreau.png" at custom_micro
        action Call ("recup_micro")



label recup_cable:
    $ guit_inventory.append(cable)
    $ cable_recupere = True
    hide screen cable
    jump loges

label recup_mediator:
    $ guit_inventory.append(mediator)
    $ mediator_recupere = True
    hide screen mediator
    jump gradin

label recup_micro:
    $ guit_inventory.append(micro)
    $ micro_recupere = True
    hide screen micro
    jump vers_scene


    

    

