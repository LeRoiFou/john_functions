"""
Spécificités dans les fonctions

Changement de valeur d'une variable globale :
    -> def locale_globale()

Lambda (fonctions anonymes) :
    -> def fonction()
    -> fonction = lambda...

Fonction générateur avec l'instructeur yield :
    -> def ma_liste()
    -> def generateur()

Déclaration d'une fonction avec un nombre d'argument < au nombre d'argument paramétré dans la fonction :
    -> def parametrer()
    -> def reparametrer()

Déclaration désordonnée des arguments d'une fonction lors de son appel :
    -> def melanger()

Nombre infini d'arguments précédés d'une '*' ou de deux '**' pour le dictionnaire:
    -> def inventorier()
    -> def inventorier_bis()
    -> def lister_dico()
    -> def inventorier_tout()

Fonctions héritées : fonction appelant d'autres fonctions
    -> def partie_1()
    -> def partie_2()
    -> def partie_3()
    -> def partie_4()
    -> def partie_phrase()

Fonctions héritées : la récursivité (fonction s'appelant elle-même)
    -> def factoriel()

Fonctions héritées : les fonctions callback (fonction(s) passée(s) en argument(s) dans une autre fonction)
    -> def puissance()
    -> def racine_carre()
    -> def operation()

Éditeur : Laurent REYNAUD
Date : 18-10-2020
"""
from math import *
import sys

"""--------------------------------------------------------------------------------------------------------------------  
Les variables globales dans les fonctions : l'instruction globale permet de recourir à une variable d'une fonction   
dans une autre fonction, ce qui équivaut dans une POO à une variable de classe  
--------------------------------------------------------------------------------------------------------------------"""


def calculer(chiffre1, chiffre2):
    """La variable res va être utilisée dans une autre fonction ci-après, on la déclare donc en global"""
    global res
    res = chiffre1 + chiffre2


def afficher():
    """La variable res étant globale, elle n'est donc pas à redéfinir dans cette fonction ;)"""
    print(f"Résultat = {res}")


calculer(2, 3)
afficher()

"""--------------------------------------------------------------------------------------------------------------------  
La fonction lambda permet d'alléger les fonctions simples en les déclarant sur une seul ligne seulement. Elle se   
déclare de la manière suivante :   
-> 'NomFonction'   
-> 'lambda argument' au lieu et place de 'NomFonction(arguments)' 
-> bloc d'instruction 
-> si un return est présent dans la fonction classique, il n'a pas à être mentionné dans la fonction lambda  
--------------------------------------------------------------------------------------------------------------------"""


def fonction(*args):
    """Fonction classique"""
    print(*args)


fonction(2, 3, 4, 5, 6, 7, 8, 9, 10)

"""Fonction lambda"""
fonction = lambda *args: print(*args)  # fonction lambda -> nom_fonction = lambda arguments: expression
fonction(2, 3, 4, 5, 6, 7, 8, 9, 10)

"""--------------------------------------------------------------------------------------------------------------------  
Fonction générateur avec l'instruction 'yield' : cette instruction simplifie les fonctions qui ont des boucles et elle 
exige peut de mémoire lors de son exécution par rapport à une fonction classique 
--------------------------------------------------------------------------------------------------------------------"""

"""Déclaration d'une liste de 5 composants"""
donnees = [i for i in range(0, 10, 2)]


def ma_liste(arg):
    """1ère situation avec une instruction return pour afficher toutes les données"""
    tab = []
    for i in arg:
        p = f"Hello number {i} :"
        tab.append(p)
    return tab


for i in ma_liste(donnees): print(i)


def generateur(arg):
    """""2ème situation avec l'instruction yield pour afficher toutes les données :     
    les instructions sont beaucoup plus simplifiées qu'avec un itérateur classique"""""
    for i in arg:
        yield f"Hello number : {i}"


for i in generateur(donnees): print(i)  # Affichage des données en tant que 'générateur'

"""Cette fois-ci la liste passe de 5 composants à 10 000 composants..."""
mes_donnees = [i for i in range(0, 10_000)]

ma_liste = ma_liste(mes_donnees)
print(sys.getsizeof(ma_liste))  # avec un itérateur classique, on a utilisé 42 5888 octets de mémoire
mon_generateur = generateur(mes_donnees)
print(sys.getsizeof(mon_generateur))  # avec un générateur, on a utilisé 56 octets de mémoire...

"""--------------------------------------------------------------------------------------------------------------------  
Déclaration d'une fonction avec un nombre d'argument < au nombre d'argument paramétré dans la fonction  
--------------------------------------------------------------------------------------------------------------------"""


def parametrer(nom_personne='Marcel', message='hello !'):
    """Possibilité de déclarer aucun argument lors de l'appel de la fonction, alors que celle-ci est paramétrée en
    argument(s). Attention : il faut toujours mettre les paramètres initialisés en derniers arguments de la fonction"""
    print(f"{nom_personne} a dit {message}")


parametrer()  # Aucun argument n'est déclaré lors de l'appel de la fonction alors qu'elle est paramétrée de 2 arguments


def reparametrer(nom_personne, message='salut'):
    """Autre situation : dans cet exemple lors de l'appel de la fonction, on déclare un seul argument alors que la
    fonction est paramétrée avec deux arguments. Rappel : le paramètre initialisé 'message' est en dernier argument de
    la fonction, car les paramètres non initiliasés (ici 'nom_personne') doivent être déclarés en 1er en arguments"""
    print(f"{nom_personne} a dit {message}")


reparametrer('John')  # Un seul argument est déclaré lors de l'appel de la foction alors qu'elle comporte deux arguments

"""--------------------------------------------------------------------------------------------------------------------  
Déclaration désordonnée des arguments d'une fonction lors de son appel  
--------------------------------------------------------------------------------------------------------------------"""


def melanger(nom_personne, message, age):
    """Les arguments déclarées lors de l'appel de la fonction peuvent ne pas suivre l'ordre des arguments paramétrés
     dans la fonction"""
    print(f"{nom_personne} a dit '{message}' et il a {age} ans")


melanger(age=25, message='salut !', nom_personne='John')  # Nom des arguments instruits lors de l'appel de la fonction

"""--------------------------------------------------------------------------------------------------------------------  
Nombre infini d'arguments précédés d'une '*' ou de deux '**' pour le dictionnaire  
--------------------------------------------------------------------------------------------------------------------"""


def inventorier(*list_items):
    """Un argument précédé d'une '*' signifie que nous avons un nombre infini d'arguments, et la boucle for in ci-après
    liste les arguments déclarés lors de l'appel de la fonction.
    Contrairement à Java, on ne peut pas surcharger une fonction / une méthode sur Python, mais le recours à cette
    instruction '*' équivaut à une surcharge de fonctions / de méthodes"""
    for item in list_items:
        print(item)


inventorier('épée')
inventorier('épée', 'arc', 'hache', 'bouclier', 'cape')


def inventorier_bis(statut, *mes_articles, article1='épee', article2='bouclier'):
    """Une fonction paramétrée peut avoir comme argument un nombre infini d'arguments et des arguments listés : afin de
    bien distinguer le nombre infini d'arguments et les arguments listés, il faut instruire le nom de l'argument listé
    lors de l'appel de la fonction"""
    print(f"Statut : {statut}")
    for i, item in enumerate(mes_articles):
        print(f"Article n° {i + 1} à disposition : {item}")
    print(f"Autre arme : {article1}")
    print(f"Autre protection : {article2}")


inventorier_bis('soldat', 'arc', 'hache', 'cape', article1='épÉe', article2='bouclier')


def lister_dico(**mon_dico):
    """Un argument précédé de deux '*' est utilisé pour lister les éléments d'un dictionnaire dont on ne connait pas
    leurs nombres précis : c'est au programmeur utilisateur de lister les éléments à déclarer dans le dictionnaire"""
    for k, v in mon_dico.items():
        print(f"Pour la {k} la valeur est {v}")


lister_dico(cle_1=[1, 5.565, 'test'], cle_2=('salut', 'au revoir'), cle_3={'dico :': {8, 6.1561, 'ok'}})


def inventorier_tout(statut, *mes_articles, article1='épee', article2='bouclier', **mon_dico, ):
    """Cette fonction combine les 3 fonctions précédentes : l'argument de deux '**' pour le dictionnaire doit toujours
    être classé en dernier de la fonction paramétrée"""
    print(f"Statut : {statut}")
    for i, item in enumerate(mes_articles):
        print(f"Article n° {i + 1} à disposition : {item}")
    print(f"Autre arme : {article1}")
    print(f"Autre protection : {article2}")
    for k, v in mon_dico.items():
        print(f"Pour la {k} la valeur est {v}")


inventorier_tout('soldat', 'arc', 'hache', 'cape', article1='épÉe', article2='bouclier',
                 cle_1=[1, 5.565, 'test'], cle_2=('salut', 'au revoir'), cle_3={'dico :': {8, 6.1561, 'ok'}})

"""--------------------------------------------------------------------------------------------------------------------  
Fonctions héritées : fonction appelant d'autres fonctions  
--------------------------------------------------------------------------------------------------------------------"""


def partie_1():
    """Fonctions héritées : cas d'une fonction appelant une autre fonction"""
    return 'Je'


def partie_2():
    return 'suis'


def partie_3():
    return 'une'


def partie_4():
    return 'phrase !'


def phrase():
    """La fonction phrase() appelle les fonctions précédentes : partie_1(), partie_2(), partie_3() et partie_4()"""
    return f"{partie_1()} {partie_2()} {partie_3()} {partie_4()}"


print(phrase())  # résultat : Je suis une phrase !

"""--------------------------------------------------------------------------------------------------------------------  
Fonctions héritées : la récursivité (fonction s'appelant elle-même)  
--------------------------------------------------------------------------------------------------------------------"""


def factoriel(n):
    """Dans cet exemple, on a recours au factoriel qui se calcul de la manière suivante :
    4! = 1 x 2 x 3 x 4
    6! = 1 x 2 x 3 x 4 x 5 x 6
    Dans cette fonction, on considère que n! = n * (n-1)! puisque pour 4! par exemple :
    4! = 4 * 3!
    3! = 3 * 2!
    2! = 2 * 1
    Donc :
    2! = 2
    3! = 3 * 2 = 6
    4! = 4 * 24
    Et dans cas on est dans une situation de récursivité, puisque la fonction factoriel s'appelle elle-même"""
    if n == 0 or n == 1:
        return 1

    return n * factoriel(n - 1)


print(factoriel(4))

"""--------------------------------------------------------------------------------------------------------------------  
Fonctions héritées : les fonctions callback (fonction(s) passée(s) en argument(s) dans une autre fonction)  
--------------------------------------------------------------------------------------------------------------------"""

puissance = lambda x: pow(x, 2)

racine_carre = lambda x: sqrt(x)

operation = lambda fct, valeur: fct(valeur)
"""Cette fonction a comme premier argument l'appel d'une des deux autres fonctions ci-avant (puissance et  
racine_carre) ce qui permet de désigner quel type d'opération est à choisir et en deuxième argument la valeur  
désignée pour obtenir le résultat souhaité"""

print(operation(puissance, 9))
print(operation(racine_carre, 9))
