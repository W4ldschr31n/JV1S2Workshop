default isInRightPlace = {"B-Carre":False,"B-Rond":False,"B-Triangle":False,"G-Carre":False,"G-Rond":False,"G-Triangle":False,"R-Carre":False,"R-Rond":False,"R-Triangle":False,}
init python:

    
    def dragged_func(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == dropped_on.drag_name:
                dragged_items[0].snap(dropped_on.x + 30, dropped_on.y + 50, 0.5)
                dragged_items[0].draggable = False
                isInRightPlace[dragged_items[0].drag_name] = True

                

                win = all(isInRightPlace.values())
                

                if win:
                    renpy.jump("win_corres")
            
                
                
screen drag_drop:
    image "backstage.png"

############################### - timer - ################################# 

    timer 0.1 repeat True action If(remaining_timer > 0, true=SetVariable('remaining_timer', round(remaining_timer - 0.1, 1)), false=Jump("lose_corres"))
    text "Temps restant: [remaining_timer]" xalign 0.5

############################## - movable - ################################

    draggroup:
        drag:
        ### -- ###

            ### - Aspect - ###

            xalign 0.6
            ypos 500
            image "B-Carre.png" zoom 0.55

            ### - Nom - ###

            drag_name "B-Carre"

            ### - Caractèristiques - ###

            drag_raise True
            dragged dragged_func
            draggable True
            droppable False
            drag_offscreen True

        ### -- ###
        drag:
        ### -- ###

            xalign 0.5
            ypos 500
            image "B-Rond.png" zoom 0.55

            drag_name "B-Rond"

            drag_raise True
            dragged dragged_func
            draggable True
            droppable False
            drag_offscreen True

        ### -- ###
        drag:
        ### -- ###

            xalign 0.7
            ypos 500
            image "B-Triangle.png" zoom 0.55

            drag_name "B-Triangle"

            drag_raise True
            dragged dragged_func
            draggable True
            droppable False
            drag_offscreen True

        ### -- ###
        drag:
        ### -- ###

            xalign 0.8
            ypos 500
            image "G-Carre.png" zoom 0.55

            drag_name "G-Carre"

            drag_raise True
            dragged dragged_func
            draggable True
            droppable False
            drag_offscreen True

        ### -- ###
        drag:
        ### -- ###

            xalign 0.3
            ypos 500
            image "G-Rond.png" zoom 0.55

            drag_name "G-Rond"

            drag_raise True
            dragged dragged_func
            draggable True
            droppable False
            drag_offscreen True

        ### -- ###
        drag:
        ### -- ###

            xalign 0.1
            ypos 500
            image "G-Triangle.png" zoom 0.55

            drag_name "G-Triangle"

            drag_raise True
            dragged dragged_func
            draggable True
            droppable False
            drag_offscreen True

        ### -- ###
        drag:
        ### -- ###

            xalign 0.2
            ypos 500
            image "R-Carre.png" zoom 0.55

            drag_name "R-Carre"

            drag_raise True
            dragged dragged_func
            draggable True
            droppable False
            drag_offscreen True

        ### -- ###
        drag:
        ### -- ###

            xalign 0.9
            ypos 500
            image "R-Rond.png" zoom 0.55

            drag_name "R-Rond"

            drag_raise True
            dragged dragged_func
            draggable True
            droppable False
            drag_offscreen True

        ### -- ###
        drag:
        ### -- ###

            xalign 0.4
            ypos 500
            image "R-Triangle.png" zoom 0.55

            drag_name "R-Triangle"

            drag_raise True
            dragged dragged_func
            draggable True
            droppable False
            drag_offscreen True

        ### -- ###

############################ - not movable - ##############################

        drag:
        ### -- ###

            align(0.1, 0.2)
            image "NM-B-Carre.png" xysize(150, 150)

            drag_name "B-Carre"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.2, 0.2)
            image "NM-B-Rond.png" xysize(150, 150)

            drag_name "B-Rond"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.3, 0.2)
            image "NM-B-Triangle.png" xysize(150, 150)

            drag_name "B-Triangle"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.4, 0.2)
            image "NM-G-Carre.png" xysize(150, 150)

            drag_name "G-Carre"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.5, 0.2)
            image "NM-G-Rond.png" xysize(150, 150)

            drag_name "G-Rond"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.6, 0.2)
            image "NM-G-Triangle.png" xysize(150, 150)

            drag_name "G-Triangle"

            draggable False

        ### -- ###
        drag:
        ### -- ###
        
            align(0.7, 0.2)
            image "NM-R-Carre.png" xysize(150, 150)

            drag_name "R-Carre"

            draggable False

        ### -- ###
        drag:
        ### -- ###
        
            align(0.8, 0.2)
            image "NM-R-Rond.png" xysize(150, 150)

            drag_name "R-Rond"

            draggable False

        ### -- ###
        drag:
        ### -- ###
        
            align(0.9, 0.2)
            image "NM-R-Triangle.png" xysize(150, 150)

            drag_name "R-Triangle"

            draggable False

        ### -- ###

############################## - labels - ##################################

label drag_win:

    scene backstage
    

    jump post_corres

label drag_lose:

    scene backstage

    jump post_corres

label minigame_corres:
    $ remaining_timer = 20
    "Branchez les cables en cliquant, glissant et déposant les bons embouts dans les bonnes prises. Faites vite avant le début du concert !"
    call screen drag_drop


label win_corres:
    show jean happy at center:
        zoom 0.3
    narrateur "Jean surmonte le stress et réussit à installer son matériel à temps. Il peut commencer sa performance avec confiance."
    $ resultat_corres = True
    return

label lose_corres:
    show jean sad at center:
        zoom 0.3
    narrateur "Jean succombe au stress, il ne réussit pas à installer son matériel à temps. Nous espérons que cela n'impactera pas trop sa perfomance."
    $ resultat_corres = False
    return