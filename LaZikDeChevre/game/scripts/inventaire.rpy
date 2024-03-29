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

define guitarebase = Item("guitare0","guitare0.png")
define guitrouge = Item ("guitare1","guitare1.png")
define guitbleu = Item ("guitare2","guitare2.png")
define guitvert = Item ("guitare3","guitare3.png")
define guitviolet = Item ("guitare4","guitare4.png")
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
    $ guit_inventory.pop()
    $ guit_inventory.append(guitrouge)
    narrateur "Une guitare haute en couleurs, qui aidera Jean à se démarquer sur scène."
    jump festival

label choix2:
    $ guit_inventory.pop()
    $ guit_inventory.append(guitbleu)
    narrateur "Une guitare d'apparence classique, pour un artiste au parcours hors du commun."
    jump festival
    

label choix3:
    $ guit_inventory.pop()
    $ guit_inventory.append(guitvert)
    narrateur "Une guitare onéreuse, mais quand on aime, rien n'a de prix."
    jump festival

label choix4:
    $ guit_inventory.pop()
    $ guit_inventory.append(guitviolet)
    narrateur "La guitare dont Jean rêve depuis des mois."
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


default salle_actuelle = "vers_loges"

screen loges:
    textbutton "Loges":
        background "black"
        xpos 900
        ypos 700
        action [SetVariable ("store.salle_actuelle","vers_loges"), Jump ("vers_loges")]

screen salle:
    textbutton "Scène": 
        background "black"
        xpos 1700
        ypos 500
        action [SetVariable ("store.salle_actuelle","vers_scene"), Jump ("vers_scene")]
        
screen gradin:
    textbutton "Gradin":
        background "black"
        xpos 100
        ypos 500
        action [SetVariable ("store.salle_actuelle","vers_gradin"), Jump ("vers_gradin")]

screen party:
    textbutton "Vers le concert ":
        background "black"
        xpos 900
        ypos 100
        action Jump ("validation")

label validation:
    if all([cable_recupere, mediator_recupere, micro_recupere]):
        hide screen salle
        hide screen loges
        hide screen gradin
        hide screen party
        scene bg stade
        narrateur "La nuit tombe, l'excitation est à son paroxysme: la foule ne tient plus en place. Enfin, la première star monte sur scène: le Pétrisseur lance les hostilités."
        show petrisseur hautain at center:
            zoom 0.2
        narrateur "Moi c'est le Pétrisseur, je suis ici pour vous en mettre plein les oreilles avec ma nouvelle musique: 'Éclair au spectacle' !"
        show petrisseur angry
        narrateur "Le pétrisseur enchaîne les notes à une vitesse folle, son talent semble inégalable."
        narrateur "Les quelques minutes de sa prestation semblent avoir été jouées en quelques secondes. Des fans en délire, la tête résonnante : le niveau entre Rockbihan et ce soir n'est clairement plus le même."
        show petrisseur hautain
        narrateur "Une progression impressionnante qui témoigne de la rage de vaincre de la fameuse rockstar qui conquiert les scènes depuis plus de deux ans et qui ne semble pas prête de s'arrêter. "
        hide petrisseur

        jump concert_stade
    else :
        narrateur "Il vous manque des objets, il vous faut un câble, un médiator et un micro."
        $ print(salle_actuelle)
        $ renpy.jump(salle_actuelle)

screen cable:
    imagebutton:
        idle "cable.png" at custom_cable
        action Jump ("recup_cable")

screen mediator:
    imagebutton:
        idle "mediator.png" at custom_mediator
        action Jump ("recup_mediator")

screen micro:
    imagebutton:
        idle "micreau.png" at custom_micro
        action Jump ("recup_micro")



label recup_cable:
    $ guit_inventory.append(cable)
    $ cable_recupere = True
    hide screen cable
    "Vous avez trouvé le câble."
    jump vers_loges

label recup_mediator:
    $ guit_inventory.append(mediator)
    $ mediator_recupere = True
    hide screen mediator
    "Vous avez trouvé le médiator."
    jump vers_gradin

label recup_micro:
    $ guit_inventory.append(micro)
    $ micro_recupere = True
    hide screen micro
    "Vous avez trouvé le micro."
    jump vers_scene


    

    

