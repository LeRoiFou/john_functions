"""
Les décorateurs singleton

On peut créer des décorateurs dans des classes et dans ce cas on dit que la classe qui a un décorateur est une classe
singleton, ce qui signifie qu'elle ne peut être instanciée qu'une seule fois.

À titre d'exemple : la création d'une base de données...

Éditeur : Laurent REYNAUD
Date : 01-12-2020
"""


def singleton(c):
    myDict = {}

    def getInstance(*args, **kwargs):
        """Si la classe n'est pas dans mon dictionnaire, ajout des données de la classe dans le dictionnaire"""
        if c not in myDict:
            myDict[c] = c(*args, **kwargs)
        return myDict[c]

    return getInstance


@singleton
class MyClass:

    def __init__(self, val):
        """Constructeur"""
        self.val = val

    @property
    def getVal(self):
        """Getter"""
        return self.val


myItem1 = MyClass('premier')
myItem2 = MyClass('second')
"""Comme la classe est déjà 'décorée' par le décorateur singleton, lors de l'instanciation du premier objet myItem1, 
l'instanciation du deuxième objet myItem2 n'a aucun effet car un décorateur singleton a été mis sur la classe MyClass"""

print(f"Valeur de 'myItem1' : {myItem1.val}, valeur de 'myItem2' : {myItem2.val}")
