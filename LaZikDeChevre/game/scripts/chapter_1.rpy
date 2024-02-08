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





