"""
Les décorateurs

Par principe chaque fonction a une seule instruction, un decorateur prend en charge des instructions communes à
plusieurs autres fonctions

Même exemple que le script précédent mais cette fois-ci on a recours à un décorateur : en 'réduisant' les fonctions, on
a plus que 4 lignes, l'aspect visuel est plus appréciable.
Mais on ne peut pas appliquer un décorateur sur une fonction lambda

Éditeur : Laurent REYNAUD
Date : 01-12-2020
"""


def decorator(f):
    def modif(*args, **kwargs):
        """Fonction ayant pour arguments un paramètre non nommé '*args' de type liste et un paramètre nommé '**kwargs'
         de type dictionnaire"""
        print('1ère ligne !')
        print('2ème ligne !')
        print('3ème ligne !')
        f(*args, **kwargs)
        print('5ème ligne !')
        print('6ème ligne !')
        print('7ème ligne !')

    return modif


@decorator
def fourth_line():
    print('4ème ligne !')


fourth_line()
