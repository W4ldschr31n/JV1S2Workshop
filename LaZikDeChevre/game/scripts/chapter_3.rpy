label guitare:
    $ guit_inventory = []
    show screen inventory


    scene maison
    show jean at left:
        zoom 0.3
    show john at right:
        zoom 0.5


    narrateur "Nous retrouvons ensuite Jean et son père John dans leur salon. John est content d'apprendre la nouvelle, il se réjouit pour son fils. Jean en profite alors pour lui faire part de sa demande. Il voudrait une nouvelle guitare. ."
    show john worried:
        zoom 0.3
    john "Une nouvelle guitare ?"
    hide john
    hide jean

    jump persuasion_john


label persuasion_john_succes:
    narrateur "Jean a réussi à convaincre John de lui acheter une guitare, il va maintenant pouvoir choisir celle qu'il préfère."
    scene black:
    show journal at truecenter
    call screen choixguit

label persuasion_john_fail:
    jump festival

label festival:
    scene festival
    show jean at center:
        zoom 0.3
    narrateur "Nous retrouvons Jean chez lui, quelques heures avant le début du festival. Le trac est présent mais ne semble pas égaler son excitation."
    jean "Vous vous rendez compte ? Depuis le temps que j'en rêve ! C'est une occasion qui ne se représentera pas de sitôt alors je veux donner mon maximum. Pas question que j'oublie mon matos."
    journaliste "Cela ne vous fait pas peur de passer d'un petit bar à une scène plus grande ? C'est un changement drastique qui pourrait en rendre malade plus d'un."
    show jean heureux at center:
        zoom 0.3
    jean "Je sais garder la tête froide, j'dois tenir ça de mon père et de ses fromages. J'veux surtout pas gâcher ma chance. Bon, vous pourriez me laisser le temps que je finisse de me préparer?"
    narrateur "Nous laissons donc Jean à ses occupations."
    hide jean
    show petrisseur angry at center:
        yalign 1
        zoom 0.5

    narrateur "Pendant ce temps, nous décidons de nous rendre sur les lieux du festival où nous rencontrons l'une des têtes d'affiche: le Petrisseur qui pétrie ses ennemis comme il pétrie la mie. 
    La nouvelle vedette qui rempli l'affiche depuis maintenant 2 ans sans laisser aucune place à ses adversaires."
    journaliste "Monsieur le Petrisseur, que pensez-vous du nouvel artiste intégré à l'affiche, Jean? Il semblerait qu'il soit fils d'artisan, comme vous. Pensez-vous qu'il va réussir?"
    petrisseur "Non. Il peut y en avoir qu'un, et c'est moi."
    narrateur "C'est sur ces paroles rustres que nous laisse le Petrisseur, une vedette douée, mais aussi bien connue pour son sale caractère.
    À la tombée de la nuit, nous retrouvons une fois de plus notre artiste en herbe en train de se préparer. Concentré, aucun détail ne lui échappe."
    hide petrisseur
    
    #jump test_corres

    narrateur "Après tant de préparation et d'appréhension, ça y est, c'est le grand moment pour Jean qui monte sur scène."

    default result_festival = 0

    call minigame_rythme_festival
    $ result_festival = score_minigame_rythme


    if result_festival >= 2:
        jump winjeu4
    else:
        jump losejeu4

    label winjeu4:
        show jean at center:
            zoom 0.3
        narrateur "Une mine dépitée, le visage surpris, et un exploit dont le Petrisseur ne s'attendait pas. Depuis 2 ans, c'est à lui que revenait le monopole de la scène du Rockbihan, désormais, 
        il semblerait qu'une nouvelle star fasse son apparition. Ce n'est plus lui que la foule acclame, mais bel et bien Jean qui lui non plus n'en revient pas. Nous le retrouvons, bouche bée, derrière la scène. "
        journaliste "Bonsoir Jean ! Quel spectacle vous nous avez offert ce soir. C'était comme diraient les jeunes: un banger. Comment avez-vous vécu ce moment avec toutes ces personnes réunies pour vous entendre?"
        jean "Tout va tellement vite! J'arrive pas à y croire: c'est vraiment incroyable. J'ai du mal à réaliser que ce moment n'est plus qu'un rêve. C'est ça qu'on appelle le destin ?"
        show jean trepigne at center:
            zoom 0.3
        narrateur "Un homme surpris de sa montée folle. Des spectateurs qui le sont encore plus.  Nous laissons Jean se reposer un peu, et décidons d'aller à la rencontre du Petrisseur. 
        L'homme semble être dans un piteux état."
        journaliste "Monsieur le Petrisseur, comment vivez-vous cet instant? Vous sentez-vous trahi par vos fans? Comptez-vous soutenir cette étoile montante?"
        hide jean trepigne
        show petrisseur angry at center:
            yalign 1
            zoom 0.5

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