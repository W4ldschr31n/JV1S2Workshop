label interview:
    scene backstage
    show john

    journaliste "Comment est Jean au quotidien? Est-ce que vous acceptez son choix de vie?"
    john "Oh bah vous savez c'est un ptit jeune avec des rêves de ptit jeune ! Boh jcomprends pas tout à ses délires mais il a l'air content. 
    Après c'est vrai que j'aurais préféré qu'il prenne la relève mais que voulez-vous..c'est la vie bouffi."
    journaliste "Cette passion, comment l'a t-il eu ? Cela fait longtemps qu'il s'intéresse au rock?"
    john "Oh bah jsais pô hein ! J'écoute pas de rock et mon ex-femme non plus !  Il a du choper ça à l'école avec ses potes. Vous savez ça remonte hein ! 
    Quelques années déjà. Jpense qu'il a kiffé dès le départ, et ça s'est fait tout seul."
    journaliste "Intéressant en effet. Il semblerait que la passion du rock soit innée chez lui." 
    john "Oh bah la passion c'est un gêne dans notre famille ! Dommage que le fromage n'ait pas suivi. Mon ex-femme était pareille ! Toujours passionnée."
    journaliste "Votre ex-femme? Pouvez-vous nous en dire plus sur elle ? Comment était-elle?"
    john "Elle était là, c'était déjà pas mal. Elle est ensuite partie se marier avec le charcutier de la bourgade d'à côté cette mégère. Je crois qu'elle ne manque pas à Jean: il a oublié son prénom." 
    journaliste "Êtes-vous fier de Jean?"
    john "Très ! Il percera vous verrez ! Plus que Johnny ! Parole de John."

    jump bar

label bar:
    scene bar moyen claire
    show gerant
    narrateur "Nous retrouvons Jean dans ce petit bar, deux jours après sa prestation, bien décidé à convaincre le gérant de le laisser jouer lors d'une soirée. 
    Une chance qui permettrait potentiellement à Jean d'augmenter sa popularité. Nous observons de loin cet entretien. "
    gerant "Non mais je comprend bien ce que vous me demandez, mais j'ai aucune assurance sur la qualité de votre prestation."
    #jauge
    menu :
        "gerant convaincu ?"
        "oui":
            $ gerantcontent=True
        "non":
            $ gerantcontent=False

    if gerantcontent:
        jump prestabar
    else:
        jump rue

label prestabar:
    gerant "Bon d'accord, jte fais confiance. Mais me déçoit pas hein !"
    hide gerant
    show jean
    narrateur "C'est un succès pour Jean, qui trépigne d'impatience, avec une seule idée en tête: faire ses preuves. Un pas de plus vers son rêve. Mais sera-t-il à la hauteur?"
    jean "Je suis content qu'il ait accepté, mais la vraie épreuve commence maintenant. Jdois pas me laisser emporter."
    narrateur "Désormais, Jean doit se préparer pour sa première vraie performance, devant un vrai public. Un trac qu'il ne cache pas."
    hide jean

    scene maison
    show jean:
        xalign 1.0
        yalign 1.0
    show john:
        xalign 0.0
        yalign 1.0

    john "ça va aller mon garçon ! Je sais que tu peux le faire ! C'est pas le public de ce bar miteux qui va t'arrêter !"
    jean "..."
    john "Aller ! Tu peux le faire oh ! Va jusqu'au bout. Tu m'as pas cassé les biiip pendant toutes ces années pour abandonner maintenant."
    narrateur "Après une discussion avec son père, Jean semble enfin aller mieux, et est prêt à en découdre. Quelques jours avant la prestation, Jean se met enfin au travail. 
    Pour se faire, il a fait appel à son meilleur ami Patrick, et même si Jean semble s'être calmé, Patrick, lui, s'inquiète toujours."
    patrick "T'es sûûr de toi? Vraiment? Non parce que..tu sais...beaucoup ont essayé sans succès. C'est dur de faire carrière dans le milieu ! Et puis beaucoup finissent drogués !"
    jean "Mais oui ! C'est mon rêve tu le sais! Je vais pas abandonner pour si peu ! Et puis si ça peut te rassurer, si jamais je me foire, c'qui arrivera pas, ben y'a la fromagerie."
    narrateur "Jean, un homme qui a la chance d'être entouré."

    scene bar moyen sombre
    show jean grand

    narrateur "Nous retrouvons Jean au bar, le jour du concert. Après des journées d'entrainements intensifs, il est fin prêt à en découdre devant le public qui l'attend. 
    En vérité, le public ne l'attend pas vraiment, mais Jean en est persuadé... Nous l'apercevons au loin sur scène, en train de se préparer. Les lumières s'éteignent et le show commence."

    #rythme bar
    menu :
        "jeux rythme 2 win ?"
        "oui":
            $ winjeu2=True
        "non":
            $ winjeu2=False

    if winjeu2:
        jump winjeu2
    else:
        jump losejeu2
    

    label winjeu2:
        hide jean grand
        show jean 
        narrateur "Un show incroyable que nous a offert Jean ce soir. Le commencement d'un rêve, la concrétisation d'une volonté, et peut être le début d'une carrière. 
        De notre place, nous apercevons Jean qui s'entretient avec une autre personne. Mais qui est-elle? Un fois le show terminé, Jean finit par nous rejoindre."
        jean "Vous devinerez jamais qui vient d'me parler ! L'organisateur du festival de rock là, vous savez, Rockbihan, et ben il vient tout juste de m'inviter à jouer sur scène !"
        journaliste "La chance semble enfin vous sourire. Nous allons vous suivre de près désormais."
        narrateur "Jean, l'exemple prouvant que la persévérance peut se montrer payante. En espérant que ce festival soit tout-autant une réussite pour lui."
        jump guitare

    label losejeu2:
        hide jean grand
        show organisateur:
            zoom 0.5
            xalign 0.0
            yalign 0.1

        narrateur "Un show....existant. Une présence....marquante, voire un peu trop. Personne n'aurait pu deviner qu'une guitare pourrait faire un tel vacarme. 
        Et pourtant, Jean arrive vers nous quelques instants plus tard, tout sourire. Il semblerait que l'organisateur du célèbre Rockbihan l'ait invité malgré sa performance ratée. Nous allons à sa rencontre."
        organisateur "J'ai repéré un certain potentiel en lui, bien caché mais existant, enfin j'espère. Mais faites-moi confiance, mon instinct ne me trompe jamais. J'en ferai une star. "
        narrateur "La chance semble enfin sourire à Jean. Nous le suivrons désormais de près. Il nous montre ici que la persévérance peut se montrer payante. En espérant que ce festival soit au moins une réussite pour lui."
        hide maison
        jump guitare

label rue:
    scene bar moyen claire
    show jean:
        xalign 1.0
        yalign 1.0
    show gerant:
        xalign 0.0
        yalign 1.0
    gerant "Très drôle ! Aller, retourne jouer ailleurs. Tu me fais perdre mon temps."
    jean "Mais..c'est mon rêve ! Vous allez vraiment me refuser ça comme ça ?!" 
    gerant "Oui."
    narrateur "C'est sur ces dernières paroles que le gérant expulsa Jean. Désemparé, celui-ci refusa de rentrer chez lui. Nous laissant seul sur le trottoir, sans nouvelles depuis maintenant des semaines. 
    C'était sans compter l'intervention de son père, à qui nous enfin pu parler, mais peut-être trop tard."

    scene backstage
    show john

    john "Ah..c'est vrai que ça a été très difficile pour lui. J'le vois plus. Plus de discussion. Boh, ça lui passera bien un jour. Il est tenace le ptiot."
    narrateur "Mais en prononçant ses mots, John lui-même ne semblait pas convaincu. Nous décidons alors de le laisser seul et d'aller prendre l'air. 
    Quelle surprise quand nous découvrons Jean en plein concert de rue. Nous décidons de le laisser finir avant d'aller à sa rencontre."

    scene rue
    #jeux de rythme rue
    menu :
        "jeux rythme rue win ?"
        "oui":
            $ winjeu3=True
        "non":
            $ winjeu3=False

    if winjeu3:
        jump winjeu3
    else:
        jump losejeu3

    label winjeu3:
        journaliste "Une performance formidable que nous a proposé Jean, nous dévoilant son plein potentiel. Une foule en délire, les yeux scintillants: le début d'un rêve qui se concrétise. 
        Nous retrouvons Jean quelques temps après sa prestation, avec la mine radieuse. Jean, que ressentez-vous en ce moment?"
        jean "C'était magique. Je pourrai même pas vous dire ce que j'ai ressenti, j'arrive toujours pas à y croire ! En plus, un des organisateurs du festival Rockbihan m'a invité ! 
        Faut à tout prix que je l'annonce à mon père."
        journaliste "La chance semble enfin vous sourire. Nous allons vous suivre de près désormais."
        narrateur "Jean nous montre ici que la persévérance peut se montrer payante. En espérant que ce festival soit tout-autant une réussite pour lui.
        Switch scène salon"
        jump guitare

    label losejeu3:
        narrateur "Un fiasco, comment décrire autrement l'évènement dont nous avons été témoin."
        jump findrogue


    