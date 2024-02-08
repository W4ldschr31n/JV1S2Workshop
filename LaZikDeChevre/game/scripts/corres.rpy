init python:

    isInRightPlace = {"Yellow":False,"Green":False,"Blue":False,"Pink":False}
    win = True

    def dragged_func(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_name == dropped_on.drag_name:
                dragged_items[0].snap(dropped_on.x + 7, dropped_on.y + 25, 0.5)
                dragged_items[0].draggable = False
                isInRightPlace[dragged_items[0].drag_name] = True

                print(isInRightPlace)

                isInRightPlaceList = [isInRightPlace["Yellow"],isInRightPlace["Green"],isInRightPlace["Blue"],isInRightPlace["Pink"]]

                win = all(isInRightPlaceList)
                print(win)

                if win:
                    renpy.jump("win_corres")
            
                
                
screen drag_drop:
    image "backstage.png"

############################### - timer - ################################# 

    timer 0.1 repeat True action If(remaining_timer > 0, true=SetVariable('remaining_timer', round(remaining_timer - 0.1, 1)), false=Return(True))
    text "Temps restant: [remaining_timer]" xalign 0.5

############################## - movable - ################################

    draggroup:
        drag:
        ### -- ###

            ### - Aspect - ###

            align(0.6, 0.8)
            image "B-Carre.png"

            ### - Nom - ###

            drag_name "B-Carre"

            ### - Caractèristiques - ###

            drag_raise True
            dragged dragged_func
            draggable True
            # drag_offscreen True

        ### -- ###
        drag:
        ### -- ###

            align(0.5, 0.8)
            image "B-Rond.png"
            drag_name "B-Rond"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.4, 0.8)
            image "B-Triangle.png"

            drag_name "B-Triangle"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.8, 0.8)
            image "G-Carre.png"

            drag_name "G-Carre"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.3, 0.8)
            image "G-Rond.png"

            drag_name "G-Rond"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.1, 0.8)
            image "G-Triangle.png"

            drag_name "G-Triangle"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.2, 0.8)
            image "R-Carre.png"

            drag_name "R-Carre"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.9, 0.8)
            image "R-Rond.png"

            drag_name "R-Rond"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###
        drag:
        ### -- ###

            align(0.7, 0.8)
            image "R-Triangle.png"

            drag_name "R-Triangle"

            drag_raise True
            dragged dragged_func
            draggable True

        ### -- ###

############################ - not movable - ##############################

        drag:
        ### -- ###

            align(0.1, 0.2)
            image "NM-B-Carre.png" xysize(100, 100)

            drag_name "B-Carre"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.2, 0.2)
            image "NM-B-Rond.png" xysize(100, 100)

            drag_name "B-Rond"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.3, 0.2)
            image "NM-B-Triangle.png" xysize(100, 100)

            drag_name "B-Triangle"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.4, 0.2)
            image "NM-G-Carre.png" xysize(100, 100)

            drag_name "G-Carre"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.5, 0.2)
            image "NM-G-Rond.png" xysize(100, 100)

            drag_name "G-Rond"

            draggable False

        ### -- ###
        drag:
        ### -- ###

            align(0.6, 0.2)
            image "NM-G-Triangle.png" xysize(100, 100)

            drag_name "G-Triangle"

            draggable False

        ### -- ###
        drag:
        ### -- ###
        
            align(0.7, 0.2)
            image "NM-R-Carre.png" xysize(100, 100)

            drag_name "R-Carre"

            draggable False

        ### -- ###
        drag:
        ### -- ###
        
            align(0.8, 0.2)
            image "NM-R-Rond.png" xysize(100, 100)

            drag_name "R-Rond"

            draggable False

        ### -- ###
        drag:
        ### -- ###
        
            align(0.9, 0.2)
            image "NM-R-Triangle.png" xysize(100, 100)

            drag_name "R-Triangle"

            draggable False

        ### -- ###

############################# - win screen - ###############################

screen drag_win:
    image "bar moyen sombre.png"


screen drag_lose:
    image "garage.png"

############################# - go screen - ################################

label test_corres:
    $ remaining_timer = 300000

    call screen drag_drop

    jump lose_corres

    return

label win_corres:

    call screen drag_win

label lose_corres:

    call screen drag_lose