init python:

    isInRightPlace = {"Yellow":False,"Green":False,"Blue":False,"Pink":False}
    win = True

    def dragged_func(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == dropped_on.drag_name:
                dragged_items[0].snap(dropped_on.x - 50, dropped_on.y - 50, 0.5)
                dragged_items[0].set_child(Solid(("#ff0000"), xysize = (250, 250)))
                dragged_items[0].draggable = False
                isInRightPlace[dragged_items[0].drag_name] = True

                print(isInRightPlace)

                isInRightPlaceList = [isInRightPlace["Yellow"],isInRightPlace["Green"],isInRightPlace["Blue"],isInRightPlace["Pink"]]

                win = all(isInRightPlaceList)
                print(win)

                if win:
                    renpy.jump("win_corres")
            
                
                
screen drag_drop:
    image "bar moyen claire.png"

############################### - timer - ################################# 

    timer 0.1 repeat True action If(remaining_timer > 0, true=SetVariable('remaining_timer', round(remaining_timer - 0.1, 1)), false=Return(True))
    text "Temps restant: [remaining_timer]" xalign 0.5

############################## - movable - ################################

    draggroup:
        drag:
        ### -- ###

            ### - Aspect - ###

            align(0.2, 0.5)
            image Solid("#ffda94") xysize(50, 100)

            ### - Nom - ###

            drag_name "Yellow"

            ### - Caractèristiques - ###

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.4, 0.5)
            image Solid("#1f9414") xysize(50, 100)

            drag_name "Green"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.6, 0.5)
            image Solid("#403dff") xysize(50, 100)

            drag_name "Blue"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.8, 0.5)
            image Solid("#ff94fa") xysize(50, 100)

            drag_name "Pink"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###

############################ - not movable - ##############################

        drag:
        ### -- ###

            align(0.2, 0.2)
            image Solid("#ffda94") xysize(50, 50)

            drag_name "Yellow"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.4, 0.2)
            image Solid("#1f9414") xysize(50, 50)

            drag_name "Green"

            draggable False

        ### -- ###
        drag:
        ### -- ###
        
            align(0.6, 0.2)
            image Solid("#403dff") xysize(50, 50)

            drag_name "Blue"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.8, 0.2)
            image Solid("#ff94fa") xysize(50, 50)

            drag_name "Pink"

            draggable False

        ### -- ###

############################# - win screen - ###############################

screen drag_win:
    image "bar moyen sombre.png"


screen drag_lose:
    image "garage.png"


############################# - go screen - ################################

label test_corres:
    $ remaining_timer = 30

    call screen drag_drop

    jump lose_corres

    return

label win_corres:

    call screen drag_win

label lose_corres:

    call screen drag_lose