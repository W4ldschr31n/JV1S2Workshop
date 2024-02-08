default persuasion_tree_john = PersuasionTree(
    {
        0: [PersuasionChoice("Supplier", "C'est tout ce que tu as pour me convaincre ?", 0, 0), PersuasionChoice("Argumenter", "J'écoute", 10, 1), PersuasionChoice("Complimenter", "Tu sais que je déteste l'hypocrisie ?", -10, 2), PersuasionChoice("Ne rien dire", "Tu as perdu ta langue ?", 0, 3)],
        1: [PersuasionChoice("Je vais être une rockstar !", "J'ai confiance en toi", 10, END_BRANCH), PersuasionChoice("Je veux une guitare !", "C'est pas un argument ça.", 0, 1), PersuasionChoice("Tu es mon père !", "Et ? Ça ne m'oblige à rien.", -10, END_BRANCH)],
        2: [PersuasionChoice("Insister", "Hm, tu le penses vraiment ?", 10, END_BRANCH), PersuasionChoice("S'excuser", "Allez, c'est fini.", 0, END_BRANCH), PersuasionChoice("Pleurer", "Sérieusement ?", -20, END_BRANCH)],
        3: [PersuasionChoice("Ne rien dire", "Tu te moque de moi, c'est ça ?", -20, END_BRANCH), PersuasionChoice("Bégayer", "Eh, respire !", 0, 3), PersuasionChoice("Pleurer", "Jean, tu n'es plus un gosse ! Oh allez, pleure pas...", 10, END_BRANCH)],
    }
)


label persuasion_john:
    $ contextual_choice = PersuasionChoice("Prendre par les sentiments", "C'est vrai que c'est ton rêve", 10, END_BRANCH)
    $ persuasion_tree_john.contextual_choice = contextual_choice
    call persuasion(persuasion_tree_john, john, "john")
    if persuasion_win:
        jump persuasion_john_succes
    else:
        jump persuasion_john_fail
