init python:
    class Item:
        def __init__(self,name,image):
            self.name = name
            self.image = image

default cable_recupere = False
default mediator_recupere = False
default micro_recupere = False


define narrateur = Character ("  ",what_italic=True)
define journaliste = Character ("journaliste",color="#7714d3")
define john = Character ("John",color="#caad2c")
define jean = Character ("Jean",color="#75D7E4")
define gerant = Character ("Gerant",color="#ad591c")
define patrick = Character ("Patrick",color="#25a94f")
define organisateur = Character("Organisateur",color="#75D7E4")
define petrisseur = Character("Petrisseur",color="#cf4242")
define viktor = Character("viktor",color="#d86169")
define rocklette = Character ("Rocklette",color="#1a909f")

label chapter_1:
    
    
    scene frometon
    narrateur "En France des milliers d'artisans produisent chaque jour un produit emblématique de la culture gastronomique de notre pays qui accompagne chaque repas des français, le fromage.
    Chaque régions possede ses spécialités que vendent les fromagerie, et nous allons suivre aujourd'hui l'une d'entre elles."

    scene fromagerie
    show john:
        xalign 0.0
        yalign 1.0
        
    narrateur "Dans cette petite boutique du Morbihan, les amateurs de fromage sont comblés. Coulommiers, Pont-l'Évêque, ou bien Roquefort, toutes les perles de notre terroir sont réunies sur un plateau.
    Une vie de senteur, bien appréciée de John, fromager depuis 20 ans."
    john "Alors ici on est dans l'affinerie, c'est là où reposent tous nos magnifiques fromages et où ils prennent leurs goûts. C'est un métier de la patience et c'est vrai qu'il faut en être passionné."
    journaliste "Et vous êtes seul pour vous occuper de tout ça ?"
    john "Oh non je bosse avec mon fils, Jean."
    journaliste "Malheureusement, Jean ne semble pas suivre le même rêve que son père, et aspire à une vie plus mouvementée. Épaulant son père au quotidien, sa petite vie tranquille ne lui convient plus."

    hide john
    show jean:
        xalign 1.0
        yalign 1.0

    jean "C'est vrai que parfois je rêve d'un peu plus. rire J'aime bien le fromage, mais une vie entière c'est un peu long. "
    journaliste "Son passe temps? Jouer du rock dans son garage. Un hobby qui contraste bien avec ses petites habitudes dans la boutique."
    jean "J'adore assister à des concerts dans un bar pas loin et j'ai toujours aimé le rock. Mais je veux pas me limiter à ça. Mon but ultime ça serait d'atteindre l'international."
    journaliste "Pour atteindre ce but, Jean s'entraine énormément en autodidacte. Après quelques négociations, il nous autorise enfin une petite session privée."

    scene garage
    show jean

    jean "Voilà mon garage, ma scène à moi on peut dire. Elle est modeste mais fonctionnelle, et puis ici les voisins n'entendent pas donc ça évite les plaintes."
    journaliste 'Pour cette présentation, Jean a choisi de nous jouer un morceau de sa composition intitulé "liberté fromagère".'

    #premier mini jeux (tuto rythme)

    menu :
        "est ce que tu as gagné ou perdu ?"
        "gagné":
            $ wingame=True
        "perdu":
            $ wingame=False
    #recupéré le score du jeux pour plus tard
    if wingame:
        jump winjeu1 
    else:
        jump losejeu1

label winjeu1:
    narrateur "Avec un talent indéniable pour la guitare, Jean possède les qualités pour percer dans le milieu du rock. Mais en a-t'il l'étoffe? 
    Un rêve que beaucoup de personnes abandonne, mais Jean semble déterminé à ne pas laisser tomber."
    jean "J'en rêve depuis que je suis tout petit. C'est vraiment quelque chose qui me tient à coeur, et j'suis pas prêt d'abandonner."
    jump interview
label losejeu1:
    narrateur  " .....la détermination. Un facteur nécessaire, mais qui ne fait pas tout. Un rêve certain, avec un accomplissement douteux. 
    Ce qui est bien, c'est que Jean possède une marge de progression conséquente, en effet, plus bas que ça c'est compliqué. Heureusement, Jean ne semble pas décidé à abandonner." 
    jean "C'est vrai que je dois m'améliorer, mais j'aime les challenges."
    jump interview

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


label flashback:
    scene boulangerie
    show viktor
    viktor "Vus verrez !"
    journaliste " Vous ..."
    viktor "Optimiste..."
    narrateur "Apres cette"
    jump pre_stade

label pre_stade:
    scene maison
    show jean
    narrateur "Le lendemain"
    jean "comment"
    journaliste "une proposition"
    jean "Dans quelque mois"
    journaliste "Un grand concert"
    jean "ouai bha"
    narrateur "Jean et le petrisseur"
    journaliste "vous allez"
    jean "j'avais"
    narrateur "Un nom qui "
    jump stade

label stade:
    scene stade
    narrateur "Cela"

    scene loges
    journaliste "BOnsoir"
    rocklette "Ca va "
    narrateur "un discour"
    jump loges

label concert_stade:
    scene stade
    narrateur "Laissant"

    #jeux de rythme final
    menu :
        "jeux rythme stade win ?"
        "oui":
            $ winjeu5=True
        "non":
            $ winjeu5=False

    if winjeu5:
        jump winjeu5
    else:
        jump losejeu5


        label winjeu5:
            narrateur "Un si beau"
            #jeu esquive

            menu :
                "jeu esquive win ?"
                "oui":
                    $ winjeu6=True
                "non":
                    $ winjeu6=False

        if winjeu6:
            jump winjeu6
        else:
            jump losejeu6

        label winjeu6:
            narrateur "C'est incroyable"
            jump evac
        
        label losejeu6:
            narrateur "Sous la plui"
            jump evac


    label losejeu5:
        scene stade
        narrateur "une deception,"

    menu :
        "jeux rythme stade win ?"
        "oui":
            $ winjeu7=True
        "non":
            $ winjeu7=False

    if winjeu7:
        jump winjeu7
    else:
        jump losejeu7


    label winjeu7:
        narrateur"malgré"
        jump chute

    label losejeux7:
        narrateur "Que ce soit en musique"
        jump chute

label chute:
    narrateur "Les joueur"
    journaliste"Bonjours"
    john "Comment"
    journaliste "Je vous "
    john "Je sais "
    journaliste "Je vois"
    john "Arreter "

    narrateur "C'est sur"
    jump end_bad

label evac:
    narrateur "Rocklette"
    journaliste "Bonjours john"
    john "oh bah"
    journaliste "C'est compréhensible"
    john "Jean"
    journaliste "Nous sommes"
    john "Faut"
    journaliste"Merci"

    narrateur"Nous obtiendron"
    jump fin_good

label findrogue:
    scene losedrogue
    narrateur "Jean, consumé par la haine et la déception, s'empressa de ranger ses affaires en pestant avant de nous adresser un dernier regard et de s'éloigner. 
    Nous apprendrons quelques temps plus tard que Jean a succombé au vice de la drogue. 
    Il est revenu peu après en nous proposant une interview avec un gouda, affirmant que les vaches complotaient: nous avons évidemment refusé."
    return
label fin_rival:
    scene lose_rival
    narrateur "Malgré.."
    return
label fin_good:
    scene win
    narrateur "bravo"
    return
label end_bad:
    scene lose_normal
    narrateur "DOMAJ"
    return
    

