define PersuasionChoice = renpy.namedtuple("PersuasionChoice", ["question", "answer", "points"])

define choix_persuation_gerant = [
    [PersuasionChoice("Salut", "Bien le bonjour", 0), PersuasionChoice("Bon toutou", "Non mais oh !", -25), PersuasionChoice("Aidez-moi svp", "Avec plaisir", 30)],
    [PersuasionChoice("Je vous souhaite une bonne journée", "Au revoir", 0), PersuasionChoice("Donne ton fric", "Jamais de la vie", -25), PersuasionChoice("J'aimerais collaborer avec vous", "Bien sûr !", 30)],
]

label persuasion(choices, character, character_image, target_points):
    "J'essaye de persuader [character.name]"
    "Je dois atteindre [target_points] points de persuasion"
    $ current_points = 50
    $ max_points = target_points
    $ persuasion_choices = choices[:]
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
        hide char_im
        return

label .choice_persuasion(choices):
    python:
        menu_options = [(choice.question, choice) for choice in choices]
        choice = renpy.display_menu(menu_options)
        current_points += choice.points
    g "[choice.answer]"
    return

screen persuasion_bar():
    frame:
        hbox:
            vbar:
                value AnimatedValue(current_points, max_points)
