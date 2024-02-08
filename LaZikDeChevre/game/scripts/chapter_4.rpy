label flashback:
    scene bg boulangerie with fade
    show viktor at left:
        zoom 0.5
    viktor "{cps=25}Vous verrez ! J'ai les capacité pour réussir. C'est pas que je n'ai pas le talent, c'est juste que le monde ne m'a pas encore découvert."
    journaliste "{cps=25}Vous êtes optimiste, ça fait plaisir à voir !"
    viktor "{cps=25}Optimiste ? Je suis réaliste. J'ai les capacités, y'en a pas deux comme moi. Certains producteurs me contactent déjà, et je suis invité à des concerts."
    viktor "Un fils de boulanger paumé en Sologne qui devient une star internationale, ça court pas les rues. Et puis, même si y'en avait, ils ne m'arriveraient pas à la cheville: c'est un fait. "
    narrateur "{cps=25}Après cet interview, notre journaliste en était resté sans voix."
    hide viktor
    narrateur "{cps=25}Ce drôle de personnage qu'était Viktor semblait avoir un avenir prometteur." 
    narrateur "{cps=25}Il n'avait besoin de personne, mais est-ce que les gens avaient besoin de lui? Future vedette ou simple caprice irréalisable, qui se cachait vraiment derrière Viktor, cet adolescent à l'ego surdimensionné ?"
    jump pre_stade

label pre_stade:
    scene maison with fade
    show jean happy at center:
        zoom 0.3
    narrateur "{cps=25}Le lendemain du festival, nous retrouvons Jean chez lui après une bonne nuit de sommeil bien méritée. Il nous accueille chaleureusement, le sourire aux lèvres."
    jean "{cps=25}Je n'arrive toujours pas à croire ce qui est arrivé hier. C'est vraiment incroyable. Au fait, j'vous ai pas dit !"
    jean "L'organisateur de Rockbihan, vous vous souvenez que je l'avais croisé au bar et qu'il m'avait invité ? Et ben j'ai reçu une nouvelle proposition ! "
    journaliste "{cps=25}Une proposition? Dites-nous en plus. "
    jean "{cps=25}Dans quelques mois, y'aura un grand concert au Stade de France."
    journaliste "{cps=25}Le concert de Metallica oui, les stars mondiales du rock métal."
    jean "{cps=25}Ouais, bah c'est le même organisateur. Apparemment cette année, ils n'ont personne pour jouer en ouverture de la soirée. 
    Du coup il a décidé d'organiser un mini-concert entre le Pétrisseur et moi."
    narrateur "{cps=25}Jean et le Pétrisseur. Une rivalité qui n'a pas échappée au public: fan de musique, mais aussi de drama. En voyant ça, l'organisateur aurait-il vu une opportunité? 
    Jean, naïf, pense seulement qu'il s'agit de musique, mais dans cette compétition, un autre facteur entrera en jeu: l'acting."
    show jean trepigne
    journaliste "{cps=25}Vous allez donc devoir défier le Pétrisseur, un challenge de haut niveau. Tout commence par un nom de scène, en avez-vous choisi un ? Comptez-vous garder 'Jean' ? "
    jean "{cps=25}J'avais déjà ma petite idée avant de commencer ouais: Rocklette. Vous en pensez quoi? J'trouve que ça claque un max."
    narrateur "{cps=25}Un nom qui inspire le respect et le fromage, voici l'identité choisie par Jean. Un premier pas vers ce duel entre rockstars."
    scene garage
    show john happy at right:
        zoom 0.5
    show jean rock happy at center:
        zoom 0.3
    narrateur "Désormais, ce sont des mois d'entraînement acharné qui vont accompagner Jean, toujours épaulé par son père. Des mois d'impatience pour les fans, qui suivent avec passion les progrès de leur star favorite."
    narrateur "Jean réussira t-il à sortir vainqueur ? Nous le découvrirons dans quelques mois."
    jump stade

label stade:
    scene bg stade with fade
    narrateur "{cps=25}Cela fait désormais 6 mois que avons laissé Jean, alias Rocklette, à son entraînement. Aux aguets, nous le suivions comme beaucoup de ses fans sur les réseaux sociaux." 
    narrateur "À la suite du festival, la montée en puissance de notre nouvelle vedette fut presque instantanée. Une côte de popularité explosive et une inquiétude grandissante chez son plus grand adversaire: le Pétrisseur." 
    narrateur "Durant ces derniers mois, lui aussi s'est beaucoup entrainé avec comme objectif non plus de conquérir la scène, mais d'écraser son ennemi juré." 
    narrateur "La foule se presse devant le stade de France, tout le monde attend le Choc des Artisans. Deux histoires similaires, pourtant un seul d'entre eux en sortira vainqueur."
    narrateur "Après avoir patienté plusieurs heures, nous retrouvons Jean dans les loges."

    scene bg loges
    show jean rock at center:
        zoom 0.3
    journaliste "{cps=25}Bonsoir Rocklette, cela fait une éternité qu'on ne vous avait pas vu. Comment allez-vous ?"
    show jean rock happy
    rocklette "{cps=25}Ça va parfaitement ! Je ne me suis jamais senti aussi bien. Je crois que la voie de la réussite me convient bien, mais je n'ai pas encore atteint mon but ultime."
    rocklette "Pour ça, je dois battre le Pétrisseur et même si j'ai eu des doutes à un moments, cette fois j'en suis sûr: je suis prêt."
    narrateur "{cps=25}Un discours motivant que nous offre Rocklette. Le jeune garçon un peu naïf aux rêves incertains que nous avions rencontré pour la première fois il y a maintenant un an a subi une montée en puissance 
    fulgurante que personne ne soupçonnait. Pas même lui."
    narrateur "La star nous propose alors de l'accompagner dans ses préparatifs."
    "Aidez Jean à trouver un câble, un médiator et un micro en vous déplaçant entre les différentes salles."
    jump vers_loges

label concert_stade:
    scene bg stade

    default result_stade = 0

    call minigame_rythme_stade
    $ result_stade = score_minigame_rythme

    $ guit_inventory.pop()
    $ guit_inventory.pop()
    $ guit_inventory.pop()


    if result_stade >= 2:
        jump winjeu5
    else:
        jump losejeu5


        label winjeu5:
            show jean rock happy at center:
                zoom 0.3
            narrateur "{cps=25}Un spectacle démentiel: qui aurait cru qu'une telle montée était possible ? La foule en délire ne cesse d'applaudir pendant plusieurs minutes.
            La victoire avait été définie dès les premières notes."
            show petrisseur angry at right:
                zoom 0.3
            show jean rock at left
            narrateur "Le Pétrisseur monte sur scène et rejoint son rival. Alors que la soiée allait continuer, la soirée tourne au drame."
            narrateur "Toujours sur la scène, le Pétrisseur, en proie à la rage, fonce sur Rocklette et lui lance des projectiles: une scène ahurissante que personne n'aurait pu prédire."
            hide jean
            hide petrisseur
            call minigame_dodge
            if win_minigame_dodge:
                jump winjeu6
            else:
                jump losejeu6

        label winjeu6:
            show jean happy at center:
                zoom 0.3
            narrateur "{cps=25}C'est incroyable, Rocklette esquive sans difficulté les projectiles envoyés par son rival. Le Pétrisseur finit par être appréhendé par la sécurité sous les yeux écarquillés du public."
            show jean trepigne
            narrateur "Un silence de mort s'installe, plus personne n'ose rien dire. Soudain, les applaudissements reprennent, comme si rien ne s'était passé."
            jump evac
        
        label losejeu6:
            narrateur "{cps=25}Sous la pluie de pâtisseries, Rocklette tombe à la renverse. La sécurité monte sur scène et emmène au loin le Pétrisseur, toujours fou de rage."
            narrateur "Un silence pesant règne parmi la foule, plus personne n'ose rien dire."
            narrateur "Les applaudissements reprennent alors petit à petit, non sans gêne, avant de reprendre définitivement comme si rien ne s'était passé."

            jump evac


    label losejeu5:
        scene bg stade
        narrateur "{cps=25}Une déception, comment décrire autrement le ressenti des fans? Peut-être était-ce à cause du stress ou de l'angoisse, dans tous les cas la performance fut un échec."
        narrateur " Des notes irrégulières jouées maladroitement. Mais qu'a donc fait Rocklette durant ces 6 mois?  Une éxécution: voila ce à quoi nous venons d'assister."
        narrateur " Une défaite cuisante et la honte qui se lit sur le visage de celui que nous suivons depuis maintenant un an. Comment expliquer ce phénomène? Pouvons nous même l'expliquer?"
        narrateur " Sans comprendre comment, nous sommes témoin d'une scène ahurissante: la foule qui était hésitante, entre applaudissements et huées, se met soudainement à lancer des projectiles 
        sur la scène afin de manifester leur mécontentement. "
        call minigame_dodge
        if win_minigame_dodge:
            jump winjeu7
        else:
            jump losejeu7


    label winjeu7:
        narrateur"{cps=25}Malgré sa performance, il semblerait qu'il reste de l'énergie à Rocklette. Suffisamment au moins pour esquiver les nombreux projectiles envoyés par les fans mécontents. 
        La star est forcée d'être évacuée tandis que la foule réclame un remboursement. Nous quittons également le stade, toujours choqués par la scène à laquelle nous venons d'assister."
        jump chute

    label losejeu7:
        narrateur "{cps=25}Que ce soit en musique ou en agilité, il semblerait que ce ne soit pas un bon jour pour Rocklette. Sous la pluie de projectiles, la star tombe à la renverse, 
        toujours sous les insultes du public." 
        narrateur "La sécurité arrive afin d'évacuer notre rockstar dont la montée fut aussi spectaculaire que la chute. La foule hurle, réclamant un remboursement." 
        narrateur "Nous quittons également le stade, toujours choqués par la scène à laquelle nous venons d'assister."
        jump chute

label chute:
    narrateur "{cps=25}Les jours passent, mais le sujet reste le même. Partout sur les réseaux, tout le monde ne parle que d'une seule chose: la chute de Rocklette. Une ascension percutante, 
    tout comme la descente." 
    narrateur "Personne ne semble comprendre ce qu'il s'est réellement passé lors de cet affrontement. Sans surprise, le vainqueur désigné fut le Pétrisseur."
    narrateur "Il prit d'ailleurs un malin plaisir à s'exprimer sur sa réussite tout en expliquant que la défaite de Rocklette était inévitable. Notre jeune star disparue alors des réseaux sociaux, 
    sans aucune explication."
    narrateur "C'est seulement quelques semaines plus tard que John nous autorisa une brève interview."
    journaliste"{cps=25}Bonjour John, merci d'avoir accepté notre invitation. Cela fait quelques semaines maintenant depuis l'agression au Stade de France, comment le vivez-vous?"
    show john angry at center:
        zoom 0.4
    john "{cps=25}Comment je le vis moi? Qu'est-ce qu'on s'en fout ! C'est Jean l'important !! Il ne sort plus de sa chambre ! Il ne fait plus rien et vous me demandez comment je vais ?"
    journaliste "{cps=25}Je vous demande pardon...j'ai été maladroit. Ce n'est pas ce que je voulais dire."
    show john sad at center:
        zoom 0.4
    john "{cps=25}Je sais, pardonnez-moi, je suis vraiment fatigué...Je ne sais plus quoi faire. Ca fait des semaines et rien ne marche. Je sais qu'il a besoin de temps, 
    mais il est vraiment au plus mal et ça me brise le cœur. Il voit psy maintenant qui lui file des médocs mais j'ai l'impression que ce n'est pas suffisant."
    journaliste "{cps=25}Je vois. Nous sommes de tout cœur avec vous. Est-ce qu'on peut faire quelque chose pour vous aider? "
    show john at center:
        zoom 0.4
    john "{cps=25}Arrêter d'en parler. Jean a besoin qu'on l'oublie quelques temps. Des articles circulent déjà sur sa dépression, il n'a pas besoin qu'on en rajoute."
    jump end_bad

label evac:
    narrateur "{cps=25}Rocklette, toujours sous le choc de l'agression est évacué par des agents de sécurité."
    hide jean
    narrateur "Les spectateurs huent son rival déjà parti. Nous décidons de rester un peu, mais la foule finit également par être évacuée. Ce n'est qu'une semaine plus tard que John, le père de Rocklette, 
    finira par nous accorder une interview."
    scene maison with fade
    show john at center:
        zoom 0.5
    journaliste "{cps=25}Bonjour John, merci d'avoir accepté notre invitation. Cela fait une semaine maintenant depuis l'agression du Pétrisseur au Stade de France, comment le vivez-vous?"
    show john angry
    john "{cps=25}Oh bah je l'aurais bien transformé en toast au chèvre l'autre là. Vous croyez quoi? Evidemment que je le déteste ! 
    Ce gosse a crisé parce qu'il a perdu et a ruiné l'un des plus beaux moments de la vie de mon fils ! On a déjà porté plainte, j'espère qu'il ne s'en tirera pas comme ça."
    journaliste "{cps=25}C'est compréhensible en effet. Sachez d'ailleurs que vous avez tout notre soutien et que tous les fans vous soutiennent également. 
    Est-ce que Jean, enfin Rocklette, va mieux depuis sa sortie de scène? On avait remarqué qu'il avait fait une pause sur les réseaux sociaux. "
    show john
    john "{cps=25}Jean? Il est tenace, un peu de repos et ça ira mieux. J'le connais le jeunot, il a besoin de s'isoler un peu pour réfléchir c'est normal, mais il revient toujours en force. 
    C'est un trait de famille. Nous, personne ne peut nous mettre au sol éternellement. "
    journaliste "{cps=25}Nous sommes ravis de l'entendre. En espérant avoir son retour d'ici peu, nous continuerons de l'attendre."
    john "{cps=25}Faut bien hein."
    journaliste "{cps=25}Merci pour ce bref entretien John. Nous sommes de tout cœur avec vous."
    jump fin_good
