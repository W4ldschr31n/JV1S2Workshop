label guitare:
    $ guit_inventory = []
    show screen inventory


    scene maison
    show john
    narrateur "Nous retrouvons ensuite Jean et son père John dans leur salon. John content d'apprendre la nouvelle, se réjouit pour son fils avant de lui faire une proposition des plus alléchantes."
    john "Il va te falloir une vraie guitare désormais fils. Regarde moi donc ça, c'est une collègue qui me l'a passé, choisi celle qui te plait."
    hide john
    scene journal:
        zoom 3
    call screen choixguit

label festival:
    scene festival debut
    show jean
    narrateur "Nous retrouvons Jean chez lui, quelques heures avant le début du festival. Le trac est présent mais ne semble pas égaler son excitation."
    jean "Vous vous rendez compte ? Depuis le temps que j'en rêve ! C'est une occasion qui ne se représentera pas de sitôt alors je veux donner mon maximum. Pas question que j'oublie mon matos."
    journaliste "Cela ne vous fait pas peur de passer d'un petit bar à une scène plus grande ? C'est un changement drastique qui pourrait en rendre malade plus d'un."
    jean "Je sais garder la tête froide, j'dois tenir ça de mon père et de ses fromages. J'veux surtout pas gâcher ma chance. Bon, vous pourriez me laisser le temps que je finisse de me préparer?"
    narrateur "Nous laissons donc Jean à ses occupations."
    hide jean
    show petrisseur
    narrateur "Pendant ce temps, nous décidons de nous rendre sur les lieux du festival où nous rencontrons l'une des têtes d'affiche: le Petrisseur qui pétrie ses ennemis comme il pétrie la mie. 
    La nouvelle vedette qui rempli l'affiche depuis maintenant 2 ans sans laisser aucune place à ses adversaires."
    journaliste "Monsieur le Petrisseur, que pensez-vous du nouvel artiste intégré à l'affiche, Jean? Il semblerait qu'il soit fils d'artisan, comme vous. Pensez-vous qu'il va réussir?"
    petrisseur "Non. Il peut y en avoir qu'un, et c'est moi."
    narrateur "C'est sur ces paroles rustres que nous laisse le Petrisseur, une vedette douée, mais aussi bien connue pour son sale caractère.
    À la tombée de la nuit, nous retrouvons une fois de plus notre artiste en herbe en train de se préparer. Concentré, aucun détail ne lui échappe."
    hide petrisseur
    #jeu correspondance

    narrateur "Après tant de préparation et d'appréhension, ça y est, c'est le grand moment pour Jean qui monte sur scène."

    #jeu de rythme festival
    menu :
        "jeux rythme vs rival win ?"
        "oui":
            $ winjeu4=True
        "non":
            $ winjeu4=False

    if winjeu4:
        jump winjeu4
    else:
        jump losejeu4

    label winjeu4:
        show jean:
            xalign 1.0
            yalign 1.0
        narrateur "Une mine..."
        journaliste "Bonsoir..."
        jean " Tout va ..."
        narrateur "un homme surpirs..."
        journaliste "Monsieur..."
        show petrisseur:
            xalign 0.0
            yalign 1.0
        petrisseur "C'est a moi..."
        narrateur "L'homme..."
        jump flashback 

    label losejeu4:
        show petrisseur:
            xalign 0.0
            yalign 1.0
        narrateur "Nous retrouvons les deux rivaux principaux de la scène en plein milieu d'un conflit explosif."
        petrisseur "Quelle honte tu nous fais ! T'aurais jamais du monter sur scène. Ta musique pue comme ton fromage."
        show jean:
            xalign 1.0
            yalign 1.0
        jean "Eh ! Tu me parles pas comme ça hein. Tout le monde peut se foirer à un moment ou un autre, et t'es pas différent !"
        petrisseur "Je ne suis pas un raté comme toi ! J'ai réussi moi ! Voila ce qui arrive quand tu défies le roi, le PETRISSEUR."
        narrateur "Après.."
        petrisseur "Il etait.."
        narrateur "C'est..."
        scene fromagerie
        narrateur "Revetu.."
        show jean
        jean "Vous..."
        jump fin_rival