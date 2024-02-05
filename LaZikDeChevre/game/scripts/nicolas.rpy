init python:
    PersuasionChoice = renpy.namedtuple("PersuasionChoice", ["question", "answer", "points"])

    class Persuasion:
        def __init__(choices, character, target_points):
            self.choices = choices
            self.character = character
            self.target_points = target_points
define choix_persuation_gerant = [
    [PersuasionChoice("Salut", "Bien le bonjour", 0), PersuasionChoice("Bon toutou", "Non mais oh !", -25), PersuasionChoice("Aidez-moi svp", "Avec plaisir", 30)],
    [PersuasionChoice("Je vous souhaite une bonne journée", "Au revoir", 0), PersuasionChoice("Donne ton fric", "Jamais de la vie", -25), PersuasionChoice("J'aimerais collaborer avec vous", "Bien sûr !", 30)],
]
define g = Character("Gérant", image="gerant")
default points_popularite = 0
label test_nicolas:
    "Salut moi c'est Nicolas"
    call persuasion(choix_persuation_gerant, g, "gerant", 100)
    hide char_im
    if persuasion_win:
        jump persuasion_gerant_succes
    else:
        jump persuasion_gerant_fail


label display_popularite:
    "J'ai [points_popularite] points de popularite"
    return

label persuasion(choices, character, character_image, target_points):
    "J'essaye de persuader [character.name]"
    "Je dois atteindre [target_points] points de persuasion"
    $ current_points = 50
    $ max_points = target_points
    $ persuasion_choices = choices
    show screen persuasion_bar
    show expression character_image as char_im
    character "Alors ça vient?"

    jump persuasion_loop

label persuasion_loop:
    $ next_choices = persuasion_choices.pop(0)
    call .choice_persuasion(next_choices)
    if persuasion_choices:
        jump persuasion_loop
    else:
        $ persuasion_win = current_points >= max_points
        return
    # show expression character_image + " angry" as char_im
    # character "Tu vas parler oui !?"
    
    

label .choice_persuasion(choices):
    python:
        menu_options = [(choice.question, choice) for choice in choices]
        choice = renpy.display_menu(menu_options)
        current_points += choice.points
    g "[choice.answer]"
    return

label persuasion_gerant_fail:
    show gerant angry
    g "tu vas souffrir"
    return

label persuasion_gerant_succes:
    show gerant happy
    g "ça passe pour aujourd'hui"
    return

screen persuasion_bar():
    frame:
        hbox:
            vbar:
                value AnimatedValue(current_points, max_points)
