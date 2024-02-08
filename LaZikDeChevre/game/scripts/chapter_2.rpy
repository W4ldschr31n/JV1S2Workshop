label interview:
    scene bg salle interview
    journaliste "{cps=25}Revenons interroger John sur son fils."
    show john assis at center:
        zoom 0.5
    journaliste "{cps=25}Comment est Jean au quotidien? Est-ce que vous acceptez son choix de vie?"
    show john assis ok
    john "{cps=25}Oh bah vous savez c'est un ptit jeune avec des rêves de p'tit jeune ! Boh j'comprends pas tout à ses délires mais il a l'air content. 
    Après c'est vrai que j'aurais préféré qu'il prenne la relève mais que voulez-vous.. c'est la vie bouffi."
    journaliste "{cps=25}Cette passion, comment l'a t-il eue ? Est-ce que cela fait longtemps qu'il s'intéresse au rock?"
    show john assis
    john "{cps=25}Oh bah j'sais pô hein ! J'écoute pas de rock et mon ex-femme non plus !  Il a du choper ça à l'école avec ses potes. Vous savez ça remonte hein ! 
    Quelques années déjà. Jpense qu'il a kiffé dès le départ, et ça s'est fait tout seul."
    journaliste "{cps=25}Intéressant en effet. Il semblerait que la passion du rock soit innée chez lui." 
    show john assis sad
    john "{cps=25}Oh bah la passion c'est un gène dans notre famille ! Dommage que le fromage n'ait pas suivi. Mon ex-femme était pareille ! Toujours passionnée."
    journaliste "{cps=25}Votre ex-femme? Pouvez-vous nous en dire plus sur elle ? Comment était-elle?"
    show john assis very sad
    john "{cps=25}Elle était là, c'était déjà pas mal. Elle est ensuite partie se marier avec le charcutier de la bourgade d'à côté cette mégère. Je crois qu'elle ne manque pas à Jean: il a oublié son prénom." 
    journaliste "{cps=25}Êtes-vous fier de Jean?"
    show john assis happy
    john "{cps=25}Très ! Il percera vous verrez ! Plus que Johnny ! Parole de John."

    jump bar

label bar:
    if resultat_rythme_garage >= 3:
        scene bg bar grand sombre
    elif resultat_rythme_garage >= 2:
        scene bg bar moyen sombre
    else:
        scene bg bar petit sombre
    show gerant at left:
        zoom 0.5
    show jean trepigne at right:
        zoom 0.3
    narrateur "{cps=25}Nous retrouvons Jean dans ce petit bar, deux jours après sa prestation, bien décidé à convaincre le gérant de le laisser jouer lors d'une soirée, dans 5 jours."
    narrateur "Une chance qui permettrait potentiellement à Jean d'augmenter sa popularité. Nous observons de loin cet entretien. "
    gerant "{cps=25}\[...\] Non mais je comprend bien ce que vous me demandez, mais j'ai aucune assurance sur la qualité de votre prestation."
    hide gerant
    hide jean
    jump persuasion_gerant


label prestabar:
    show gerant happy at center:
        zoom 0.5
    gerant "{cps=25}Bon d'accord, j'te fais confiance. Mais me déçoit pas hein ! À dans 5 jours."
    hide gerant
    show jean happy at center:
        zoom 0.3
    narrateur "{cps=25}C'est un succès pour Jean, qui trépigne d'impatience, avec une seule idée en tête: faire ses preuves. Un pas de plus vers son rêve. Mais sera-t-il à la hauteur?"
    show jean trepigne
    jean "{cps=25}Je suis content qu'il aie accepté, mais la vraie épreuve commence maintenant. J'dois pas me laisser emporter."
    narrateur "{cps=25}Jean va maintenant devoir se préparer pour sa prochaine performance, sa première devant un vrai public. Il ne cache pas son anxiété."
    hide jean
    scene maison
    narrateur "{cps=25}Nous sommes dans la maison de John et Jean, nous assistons à un moment de motivation paternelle."
    show jean sad at right:
        zoom 0.3
    show john happy at left:
        zoom 0.5

    john "{cps=25}Ça va aller mon garçon ! Je sais que tu peux le faire ! C'est pas le public de ce bar miteux qui va t'arrêter !"
    jean "{cps=10}..."
    john "{cps=25}Aller ! Tu peux le faire oh ! Va jusqu'au bout. Tu m'as pas cassé les biiip pendant toutes ces années pour abandonner maintenant."
    hide john
    show jean
    narrateur "{cps=25}Après une discussion avec son père, Jean semble enfin aller mieux, et est prêt à en découdre. Quelques jours avant la prestation, Jean se met enfin au travail. 
    Pour se faire, il a fait appel à son meilleur ami Patrick, et même si Jean semble s'être calmé, Patrick, lui, s'inquiète toujours."
    show patrick angry at left:
        zoom 0.5
    patrick "{cps=25}T'es sûr de toi? Vraiment? Non parce que..tu sais...beaucoup ont essayé sans succès. C'est dur de faire carrière dans le milieu ! Et puis beaucoup finissent drogués !"
    jean "{cps=25}Mais oui ! C'est mon rêve tu le sais! Je vais pas abandonner pour si peu ! Et puis si ça peut te rassurer, si jamais je me foire, c'qui arrivera pas, ben y'a la fromagerie."
    show patrick
    show jean happy
    narrateur "{cps=25}Jean, un homme qui a la chance d'être entouré."

    if resultat_rythme_garage >= 3:
        scene bg bar grand clair
    elif resultat_rythme_garage >= 2:
        scene bg bar moyen clair
    else:
        scene bg bar petit clair
    show jean rock:
        xalign 0.4
        yalign 0.2
        zoom 0.2

    narrateur "{cps=25}Nous retrouvons Jean au bar, le jour du concert. Après des journées d'entrainements intensifs, il est fin prêt à en découdre devant le public qui l'attend."
    narrateur "En vérité, le public ne l'attend pas vraiment, mais Jean en est persuadé... Nous l'apercevons au loin sur scène, en train de se préparer. Les lumières s'éteignent et le show commence."

    #rythme bar
    call minigame_rythme_bar

    $ wingame = resultat_rythme_bar >= 2
    if wingame:
        jump winjeu2
    else:
        jump losejeu2
    

    label winjeu2:
        show jean rock happy
        narrateur "{cps=25}Un show incroyable que nous a offert Jean ce soir. Le commencement d'un rêve, la concrétisation d'une volonté, et peut être le début d'une carrière. 
        De notre place, nous apercevons Jean qui s'entretient avec une autre personne. Mais qui est-elle? Un fois le show terminé, Jean finit par nous rejoindre."
        jean "{cps=25}Vous devinerez jamais qui vient d'me parler ! L'organisateur du festival de rock là, vous savez, Rockbihan, et ben il vient tout juste de m'inviter à jouer sur scène !"
        journaliste "{cps=25}La chance semble enfin vous sourire. Nous allons vous suivre de près désormais."
        narrateur "{cps=25}Jean, l'exemple prouvant que la persévérance peut se montrer payante. En espérant que ce festival soit tout-autant une réussite pour lui."
        jump guitare

    label losejeu2:
        show jean rock sad

        narrateur "{cps=25}Un show... peu attrayant. Une présence....marquante, voire un peu trop. Personne n'aurait pu deviner qu'une guitare pourrait faire un tel vacarme. 
        Et pourtant, Jean arrive vers nous quelques instants plus tard, tout sourire."
        show jean happy at center:
            zoom 0.2
        jean "{cps=25}J'ai rencontré l'organisateur du célèbre festival du Rockbihan, il m'a invité malgré ma performance ratée !"
        hide jean
        narrateur "{cps=25}Nous allons à la rencontre de l'organisateur en question, un peu plus loin dans la salle."
        show organisateur:
            zoom 0.5
            xalign 0.0
            yalign 0.1
        organisateur "{cps=25}J'ai repéré un certain potentiel en lui, bien caché mais existant, enfin j'espère. Mais faites-moi confiance, mon instinct ne me trompe jamais. J'en ferai une star. "
        hide organisateur
        narrateur "{cps=25}La chance semble enfin sourire à Jean. Nous le suivrons désormais de près. Il nous montre ici que la persévérance peut se montrer payante. En espérant que ce festival soit au moins une réussite pour lui."
        jump guitare

label rue:
    scene bar moyen claire
    show jean sad at right:
        zoom 0.3
    show gerant angry at left:
        zoom 0.5
    gerant "{cps=25}Très drôle ! Aller, retourne jouer ailleurs. Tu me fais perdre mon temps."
    jean "{cps=25}Mais..c'est mon rêve ! Vous allez vraiment me refuser ça comme ça ?!" 
    gerant "{cps=25}Oui."
    hide jean
    narrateur "{cps=25}C'est sur ces dernières paroles que le gérant expulsa Jean. Désemparé, celui-ci refusa de rentrer chez lui. Nous laissant seul sur le trottoir, sans nouvelles depuis maintenant des semaines."
    scene bg salle interview
    narrateur "{cps=25}C'était sans compter sur l'intervention de son père, à qui nous avons enfin pu parler, mais peut-être trop tard."

    show john assis at center:
        zoom 0.5

    john "{cps=25}Ah..c'est vrai que ça a été très difficile pour lui. J'le vois plus. Plus de discussion. Boh, ça lui passera bien un jour. Il est tenace le ptiot."
    show john assis sad
    narrateur "{cps=25}Mais en prononçant ses mots, John lui-même ne semblait pas convaincu. Nous décidons alors de le laisser seul et d'aller prendre l'air."
    

    if resultat_rythme_garage >= 2:
        scene bg rue grand
    else:
        scene bg rue petit
    show jean at center:
        zoom 0.5
    narrateur "{cps=25}Quelle surprise quand nous découvrons Jean en plein concert de rue. Nous décidons de le laisser finir avant d'aller à sa rencontre."
    hide jean
    #jeux de rythme rue
    call minigame_rythme_rue

    $ wingame = resultat_rythme_rue >= 2
    if wingame:
        jump winjeu3
    else:
        jump losejeu3

    label winjeu3:
        narrateur "{cps=25}Une performance formidable que nous a proposé Jean, nous dévoilant son plein potentiel. Une foule en délire, les yeux scintillants: le début d'un rêve qui se concrétise."
        show jean at right:
            zoom 0.5
        narrateur "{cps=25}Nous retrouvons Jean quelques temps après sa prestation, avec la mine radieuse. Jean, que ressentez-vous en ce moment?"
        jean "{cps=25}C'était magique. Je pourrais même pas vous dire ce que j'ai ressenti, j'arrive toujours pas à y croire ! En plus, un des organisateurs du festival Rockbihan m'a invité ! 
        Faut à tout prix que je l'annonce à mon père."
        journaliste "{cps=25}La chance semble enfin vous sourire. Nous allons vous suivre de près désormais."
        narrateur "{cps=25}Jean nous montre ici que la persévérance peut se montrer payante. En espérant que ce festival soit tout-autant une réussite pour lui."
        jump guitare

    label losejeu3:
        narrateur "{cps=25}Un fiasco, comment décrire autrement l'évènement dont nous avons été témoin."
        jump findrogue


    