#$ jean_inventory = []
#
#    $ tome = Item ("tome","Tome.png")
#    show screen inventory



screen coucou:
    frame:
        xpos 20
        ypos 20
        text "coucou":
            size 40
        
screen fromage:
    imagebutton:
        xpos 190
        ypos 450
        idle "Tome.png"
        at custom_zoom
        action [Hide("coucou"),Jump ("tomeclic")]

transform custom_zoom:
    zoom 0.2


screen inventory:
    hbox:
        for i in jean_inventory:
            frame:
                add i.image


label tomeclic:
    $ jean_inventory.append(tome)

    narrateur "bravo tu a trouvé la tome"