init python:
    class Item:
        def __init__(self,name,image):
            self.name = name
            self.image = image

default cable_recupere = False
#default verif = False

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
    narrateur "En france ..."

    scene fromagerie
    show john:
        xalign 0.0
        yalign 1.0
        
    narrateur "Dans cette petite boutique du Morbihan,"
    john "Alors ici on est dans l'affinerie"
    journaliste "Et vous êtes seul pour vous occuper de tout ça ?"
    john "Oh non je bosse avec mon fils, Jean."
    journaliste "Malheureusement"

    hide john
    show jean:
        xalign 1.0
        yalign 1.0

    jean "C'est vrai que parfois je rêve d'un peu plus."
    journaliste "Son passe temps?"
    jean "J'adore assister à des concerts dans un bar..."
    journaliste "Pour atteindre ce but,"

    scene garage
    show jean

    jean "Voila mon garage,"
    journaliste "Pour cette présentation"

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
    narrateur "Avec un talent indéniable pour la guitare"
    jump interview
label losejeu1:
    narrateur  ".....la détermination"
    jump interview

label interview:
    scene backstage
    show john

    journaliste "Comment est Jean au quotidien? Est ce que vous acceptez son choix de vie?"
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
    narrateur "Nous retrouvons Jean dans ce petit bar"
    gerant "Non mais je comprend"
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
    gerant "Bon d'accord"
    hide gerant
    show jean
    narrateur "C'est un succès pour Jean"
    jean " Je suis content qu'il ait accepté"
    narrateur "Désormais, Jean doit se préparer"
    hide jean

    scene maison
    show jean:
        xalign 1.0
        yalign 1.0
    show john:
        xalign 0.0
        yalign 1.0

    john "ça va aller mon garçon !"
    jean "..."
    john "Aller ! Tu peux le faire oh !"
    narrateur "Après une discussion avec son père"
    patrick "T'es sûûr de toi?"
    jean "Mais oui !"
    narrateur "Jean"

    scene bar moyen sombre
    show jean grand

    narrateur "Nous retrouvons Jean au bar"
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
        narrateur "Un show incroyable que nous a offert"
        jean "Vous devinerez jamais qui vient d'me parler"
        journaliste "La chance semble enfin vous sourire"
        narrateur "Jean nous montre ici que la persévérance peut se montrer payante"
        jump guitare

    label losejeu2:
        hide jean grand
        show organisateur:
            zoom 0.5
            xalign 0.0
            yalign 0.1

        narrateur "Un show....existant"
        organisateur "J'ai repéré un certain potentiel en lui"
        narrateur "La chance semble enfin sourire à"
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
    narrateur "C'est sur ces dernières"

    scene backstage
    show john

    john "ah..."
    narrateur "Mais en ..."

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
        journaliste "Une performance ..."
        jean "C'etait magique ..."
        journaliste "La chance..."
        narrateur "Jean nous..."
        jump guitare

    label losejeu3:
        narrateur "Un fiasco..."
        jump findrogue


label guitare:
    $ guit_inventory = []
    show screen inventory


    scene maison
    show john
    narrateur "Nous retrouvons ensuite..."
    john "Il va te falloir..."
    hide john
    scene journal:
        zoom 3
    call screen choixguit


label festival:
    scene festival debut
    show jean
    narrateur "Nous retrouvons..."
    jean "Vous vous..."
    journaliste "Cela ..."
    jean "Je sais garder..."
    narrateur "Nous laissons..."
    hide jean
    show petrisseur
    journaliste "Monsieur..."
    petrisseur "Non..."
    narrateur "C'est sur ..."
    hide petrisseur
    #jeu correspondance

    narrateur "Après..."

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
        narrateur "Nous..."
        petrisseur "Quelle honte ..."
        show jean:
            xalign 1.0
            yalign 1.0
        jean "Eh..."
        petrisseur "Je ne suis ..."
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
    narrateur "vous avez perdu"
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
    

