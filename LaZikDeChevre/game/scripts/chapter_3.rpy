label guitare:
    scene maison with fade
    show jean at left:
        zoom 0.3
    show john happy at right:
        zoom 0.5


    narrateur "Nous retrouvons ensuite Jean et son père John dans leur salon. John est content d'apprendre la nouvelle, il se réjouit pour son fils. Jean en profite alors pour lui faire part de sa demande. Il voudrait une nouvelle guitare."
    show john worried:
        zoom 0.3
    john "Tu veux une nouvelle guitare ? Mais celle que tu as est déjà très bien !"
    hide john
    hide jean

    jump persuasion_john


label persuasion_john_succes:
    show jean happy at left:
        zoom 0.3
    show john at right:
        zoom 0.5
    narrateur "Jean a réussi à convaincre John de lui acheter une guitare, il va maintenant pouvoir choisir celle qu'il préfère."
    john "Bon c'est d'accord ! Tu m'as convaincu bien joué. Tu la mérites amplement."
    scene black
    show journal at truecenter
    call screen choixguit

label persuasion_john_fail:
    show jean sad at right:
        zoom 0.3
    show john worried at left:
        zoom 0.3
    john "Désolé mais c'est non. On verra plus tard ok? Quand j'aurai plus d'argent."
    narrateur "Jean n'aura pas su convaincre son père John de lui acheter une nouvelle guitare. Il continuera donc son aventure avec son premier instrument."
    jump festival

label festival:
    scene garage with fade
    show jean at center:
        zoom 0.3
    narrateur "Quelques semaines après, nous retrouvons Jean chez lui, le matin même du festival. Le trac est présent mais ne semble pas égaler son excitation."
    jean "Vous vous rendez compte ? Depuis le temps que j'en rêve ! C'est une occasion qui ne se représentera pas de sitôt alors je veux donner mon maximum. Pas question que j'oublie mon matos."
    journaliste "Cela ne vous fait pas peur de passer d'un petit bar à une scène plus grande ? C'est un changement drastique qui pourrait en rendre malade plus d'un."
    show jean happy at center:
        zoom 0.3
    jean "Je sais garder la tête froide, j'dois tenir ça de mon père et de ses fromages. J'veux surtout pas gâcher ma chance. Bon, vous pourriez me laisser le temps que je finisse de me préparer?"
    narrateur "Nous laissons donc Jean à ses occupations."
    scene festival with fade
    narrateur "Pendant ce temps, nous décidons de nous rendre sur les lieux du festival." 
    show petrisseur angry at center:
        yalign 1
        zoom 0.5

    narrateur "Nous rencontrons l'une des têtes d'affiche: le Pétrisseur. Le boulanger métalleux qui pétrit ses ennemis comme il pétrit la pâte."
    narrateur "C'est une nouvelle vedette qui remplit l'affiche depuis maintenant 2 ans sans laisser aucune place à ses concurrents."
    journaliste "Monsieur le Pétrisseur, que pensez-vous du nouvel artiste intégré à l'affiche, Jean? Il semblerait qu'il soit fils d'artisan, comme vous. Pensez-vous qu'il va réussir?"
    show petrisseur hautain
    petrisseur "Non. Il ne peut y en avoir qu'un, et ça sera moi."
    narrateur "C'est sur ces paroles rudes que nous laisse le Pétrisseur, un artiste doué, mais également bien connu pour son sale caractère."
    scene festival with fade
    show jean at center:
        zoom 0.3
    narrateur "À la tombée de la nuit, nous retrouvons une fois de plus notre artiste en herbe en train de se préparer. Concentré, aucun détail ne lui échappe."
    show jean angry
    jean "L'équipe technique a oublié de préparer mon passage, je vais devoir brancher tous mes câbles moi-même."
    
    call minigame_corres from _call_minigame_corres

    jump post_corres


label post_corres :

    show jean rock

    narrateur "{cps=25}Après tant de préparation et d'appréhension, ça y est, c'est le grand moment pour Jean qui monte sur scène pour interpréter 'Ça rock fort'."

    default result_festival = 0

    call minigame_rythme_festival from _call_minigame_rythme_festival
    $ result_festival = score_minigame_rythme


    if result_festival >= 2:
        jump winjeu4
    else:
        jump losejeu4

    label winjeu4:
        show jean at left:
            zoom 0.3
        show petrisseur angry at right:
            zoom 0.3
        narrateur "{cps=25}La foule est en délire ! Un exploit auquel le Pétrisseur, la mine dépitée, ne s'attendait pas. Depuis 2 ans, c'est à lui que revenait le monopole de la scène du Rockbihan."
        show jean happy
        narrateur "Désormais, il semblerait qu'une nouvelle star fasse son apparition. Ce n'est plus lui que la foule acclame, mais bel et bien Jean qui lui non plus n'en revient pas. Nous le retrouvons, bouche bée, derrière la scène. "
        hide petrisseur
        show jean happy at center
        journaliste "{cps=25}Bonsoir Jean ! Quel spectacle vous nous avez offert ce soir. C'était comme diraient les jeunes: un 'banger'. Comment avez-vous vécu ce moment avec toutes ces personnes réunies pour vous entendre ?"
        jean "{cps=25}Tout va tellement vite! J'arrive pas à y croire: c'est vraiment incroyable. J'ai du mal à réaliser que ce je vie n'est plus seulement un rêve. C'est ça qu'on appelle le destin ?"
        show jean trepigne at center:
            zoom 0.3
        narrateur "{cps=25}Jean est surpris de sa montée folle. Les spectateurs qui le sont encore plus. Nous laissons Jean se reposer un peu, et décidons d'aller à la rencontre du Pétrisseur. 
        L'homme semble être dans un piteux état."
        hide jean trepigne
        show petrisseur angry at center:
            yalign 1
            zoom 0.5

        journaliste "{cps=25}Monsieur le Pétrisseur, comment vivez-vous cet instant? Vous sentez-vous trahi par vos fans? Comptez-vous soutenir cette étoile montante?"
        petrisseur "{cps=25}C'est à MOI que ces applaudissements reviennent !! MOI ET PERSONNE D'AUTRE !! Stupidités !  Je n'ai rien à envier à ce fromager de pacotille ! 
        Jamais il ne me surpassera, il en est incapable !"
        show petrisseur hautain
        petrisseur "Que ce gueux retourne d'où il vienne: dans le purin et la moisissure."
        narrateur "{cps=25}L'homme part sur ces mots. Comme un lointain souvenir, des images nous reviennent: celles d'un ado fils de boulanger et prêt à tout pour intégrer le monde du rock."
        hide petrisseur
        scene black
        narrateur "En effet, quelques années auparavant, nous avions rencontré Viktor, alias le Pétrisseur, dans sa petite boulangerie de Sologne."
        jump flashback 

    label losejeu4:
        show jean rock sad at right
        show petrisseur moqueur at left:
            zoom 0.3
        narrateur "{cps=25}Nous retrouvons les deux rivaux principaux de la scène en plein milieu d'un conflit explosif."
        petrisseur "{cps=25}Quelle honte tu nous fais ! T'aurais jamais du monter sur scène. Ta musique pue comme ton fromage."
        show jean angry at right:
            zoom 0.3
        jean "{cps=25}Eh ! Tu me parles pas comme ça hein. Tout le monde peut se foirer à un moment ou un autre, et t'es pas différent !"
        show petrisseur hautain at left:
            zoom 0.3
        petrisseur "{cps=25}Je ne suis pas un raté comme toi ! J'ai réussi moi ! Voila ce qui arrive quand tu défies le roi, le PETRISSEUR."
        show jean sad
        narrateur "{cps=25}Après cette altercation, Jean semble déboussolé et demande à être seul. Nous nous éloignons donc, et retrouvons son rival."
        hide jean
        show petrisseur at center
        narrateur "Le Pétrisseur rit aux éclats, fier de sa victoire: comme un adulte ayant battu un enfant à la course. "
        petrisseur "{cps=25}Il n'était pas fait pour ça. Soit t'as le rock dans le sang, soit tu l'as pas. Faut vraiment que des gens arrêtent de prendre 
        exemple sur moi en pensant qu'ils peuvent réussir: je suis l'exception, l'élu."
        hide petrisseur
        show jean sad at center:
            zoom 0.3
        narrateur "{cps=25}C'est sur ces paroles que nous quittons la vedette afin de rejoindre Jean qui se tient quelques mètres plus loin, pensif, l'air abattu."
        jump fin_rival
        