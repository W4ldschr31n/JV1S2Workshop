init python:
    class Item:
        def __init__(self,name,image):
            self.name = name
            self.image = image

default cable_recupere = False
default mediator_recupere = False
default micro_recupere = False


label chapter_1:
    scene bg table_fromage
    narrateur "{cps=25}En France, des milliers d'artisans produisent chaque jour un produit emblématique de la culture gastronomique de notre pays, qui accompagne presque chaque repas des français: le fromage."
    narrateur "{cps=25}Chaque région possède ses spécialités vendues dans des fromageries, et nous allons suivre aujourd'hui l'une d'entre elles."

    scene fromagerie
    narrateur "{cps=25}Dans cette petite boutique du Morbihan, les amateurs de fromage sont comblés. Coulommiers, Pont-l'Évêque, ou bien Roquefort, toutes les perles de notre terroir sont réunies sur un plateau."
    narrateur "{cps=25}Une vie de senteurs, bien appréciée de John, fromager depuis 20 ans."
    show john at left:
        zoom 0.5
    john "{cps=25}Alors ici on est dans l'affinerie, c'est là où reposent tous nos magnifiques fromages et où ils prennent leurs goûts. C'est un métier de patience et c'est vrai qu'il faut en être passionné."
    journaliste "{cps=25}Et vous êtes seul pour vous occuper de tout ça ?"
    john "{cps=25}Oh non, je bosse avec mon fils, Jean."
    show jean at right:
        zoom 0.3
    journaliste "{cps=25}Malheureusement, Jean ne semble pas suivre le même rêve que son père, et aspire à une vie plus mouvementée. Épaulant son père au quotidien, sa petite vie tranquille ne lui convient plus."
    hide john
    jean "{cps=25}C'est vrai que parfois je rêve d'un peu plus... *rires* J'aime bien le fromage, mais une vie entière c'est un peu long. "
    show jean rock
    journaliste "{cps=25}Son passe temps? Jouer du rock dans son garage. Un hobby qui contraste bien avec ses petites habitudes dans la boutique."
    show jean happy
    jean "{cps=25}J'adore assister à des concerts dans un bar pas loin et j'ai toujours aimé le rock. Mais je veux pas me limiter à ça. Mon but ultime ça serait d'atteindre l'international."
    journaliste "{cps=25}Pour atteindre ce but, Jean s'entraîne énormément en autodidacte. Après quelques négociations, il nous autorise enfin une petite session privée."

    scene garage
    $ guit_inventory = [guitarebase]
    show screen inventory

    show jean rock at center:
        zoom 0.3

    jean "{cps=25}Voilà mon garage, ma scène à moi on peut dire. Elle est modeste mais fonctionnelle, et puis ici les voisins n'entendent pas donc ça évite les plaintes."
    journaliste '{cps=25}Pour cette présentation, Jean a choisi de nous jouer un morceau de sa composition intitulé "liberté fromagère".'

    #premier mini jeux (tuto rythme)
    call minigame_rythme_garage

    $ wingame = resultat_rythme_garage >= 2
    if wingame:
        jump winjeu1 
    else:
        jump losejeu1

label winjeu1:
    show jean rock happy:
        zoom 0.3
    narrateur "{cps=25}Avec un talent indéniable pour la guitare, Jean possède les qualités pour percer dans le milieu du rock."
    narrateur "{cps=25}Mais en a-t-il l'étoffe?"
    narrateur "{cps=25}Un rêve que beaucoup de personnes abandonne, mais Jean semble déterminé à ne pas laisser tomber."
    jean "{cps=25}J'en rêve depuis que je suis tout petit. C'est vraiment quelque chose qui me tient à coeur, et j'suis pas prêt d'abandonner."
    jump interview
label losejeu1:
    show jean rock sad
    narrateur  "{cps=25}La détermination: un facteur nécessaire, mais qui ne fait pas tout."
    narrateur "{cps=25}Un rêve certain, avec un accomplissement douteux."
    narrateur "{cps=25}Ce qui est bien, c'est que Jean possède une marge de progression conséquente, en effet, plus bas que ça c'est compliqué. Heureusement, Jean ne semble pas décidé à abandonner." 
    show jean rock happy
    jean "{cps=25}C'est vrai que je dois m'améliorer, mais j'aime les challenges."
    jump interview





