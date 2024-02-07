init python:
    PersuasionChoice = renpy.namedtuple("PersuasionChoice", ["question", "answer", "points"])
    class PersuasionTree:
        def __init__(self, branches):
            self.all_branches = branches
            self.profondeur = 0
            self.alignement = "neutral"

        def get_choices(self):
            return self.all_branches[self.profondeur][self.alignement] if self.has_choices() else []

        def select_choice(self, choice):
            if choice.points < 0:
                self.alignement = "negative"
                self.profondeur += 1
            elif choice.points > 0:
                self.alignement = "positive"
                self.profondeur += 1
            else:
                self.get_choices().remove(choice)

        def has_choices(self):
            return self.profondeur < len(self.all_branches)

define persuasion_tree_gerant = PersuasionTree([
    {"neutral": [PersuasionChoice("Salut", "Bien le bonjour", 0), PersuasionChoice("Bon toutou", "Non mais oh !", -25), PersuasionChoice("Aidez-moi svp", "Avec plaisir", 30)]},
    {
        "positive": [PersuasionChoice("Je vous souhaite une bonne journée", "Au revoir", 0), PersuasionChoice("Donne ton fric", "Jamais de la vie", -25), PersuasionChoice("J'aimerais collaborer avec vous", "Bien sûr !", 30)],
        "negative": [PersuasionChoice("Adios raclure", "Ne reviens jamais", -10), PersuasionChoice("Milles excuses", "Mouais", 0), PersuasionChoice("J'aimerais collaborer avec vous", "Et pourquoi j'accepterais ?", 10)]
    },
])

define max_persuasion_points = 100

label persuasion(pt, character, character_image):
    "J'essaye de persuader [character.name]"
    "Je dois atteindre [max_persuasion_points] points de persuasion"
    $ current_points = 50
    $ character_to_persuade = character
    $ persuasion_tree = pt
    show screen persuasion_bar
    show expression character_image as char_im
    character_to_persuade "Alors ça vient?"

    jump persuasion_loop

label persuasion_loop:
    $ next_choices = persuasion_tree.get_choices()
    call .choice_persuasion(next_choices)
    if persuasion_tree.has_choices():
        jump persuasion_loop
    else:
        $ persuasion_win = current_points >= 50
        hide char_im
        return

label .choice_persuasion(choices):
    python:
        menu_options = [(choice.question, choice) for choice in choices]
        choice = renpy.display_menu(menu_options)
        current_points += choice.points
        persuasion_tree.select_choice(choice)
    if choice.points < 0:
        show expression character_image + " angry" as char_im
    elif choice.points > 0:
        show expression character_image + " happy" as char_im
    else:
        show expression character_image as char_im
    character_to_persuade  "[choice.answer]"
    return

screen persuasion_bar():
    frame:
        hbox:
            vbar:
                value AnimatedValue(current_points, max_persuasion_points)
