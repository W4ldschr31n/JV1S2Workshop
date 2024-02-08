init python:
    PersuasionChoice = renpy.namedtuple("PersuasionChoice", ["question", "answer", "points", "next_branch"])
    END_BRANCH = -1
    class PersuasionTree:
        def __init__(self, indexed_branches, contextual_choice=None):
            self.indexed_branches = indexed_branches
            self.current_branch = 0
            self.contextual_choice = contextual_choice

        def get_choices(self):
            if not self.has_choices():
                return []

            choices = self.indexed_branches[self.current_branch]

            if self.contextual_choice is not None:
                return choices + [self.contextual_choice]

            return choices 

        def select_choice(self, choice):
            if choice == self.contextual_choice:
                self.current_branch = self.current_branch if self.contextual_choice.next_branch != END_BRANCH else END_BRANCH
                self.contextual_choice = None
            else:
                if choice.points == 0:
                    self.indexed_branches[self.current_branch].remove(choice)
                self.current_branch = choice.next_branch

        def has_choices(self):
            return self.current_branch != END_BRANCH

default max_persuasion_points = 100

label persuasion(pt, character, character_image):
    "Vous allez essayer de persuader [character.name]"
    "Vous devez faire monter la barre de persuasion en choisissant les bons dialogues !"
    $ current_points = 50
    $ character_to_persuade = character
    $ persuasion_tree = pt
    show screen persuasion_bar
    show expression character_image as char_im:
        xalign 0.5
        zoom 0.5
    character_to_persuade "Je vous écoute"

    jump persuasion_loop

label persuasion_loop:
    $ next_choices = persuasion_tree.get_choices()
    call .choice_persuasion(next_choices)
    if persuasion_tree.has_choices():
        jump persuasion_loop
    else:
        $ persuasion_win = current_points >= 50
        hide char_im
        hide screen persuasion_bar
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
