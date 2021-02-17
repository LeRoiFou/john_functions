"""
Les décorateurs

Par principe chaque fonction a une seule instruction, un decorateur prend en charge des instructions communes à
plusieurs autres fonctions

Éditeur : Laurent REYNAUD
Date : 01-12-2020
"""

import time


def tictac(f):
    def modif_function(*args, **kwargs):
        """Fonction ayant pour arguments un paramètre non nommé '*args' de type liste et un paramètre nommé '**kwargs'
         de type dictionnaire"""
        before = time.time()  # début du temps d'exécution de la fonction
        f(*args, **kwargs)  # lancement de la fonction d'exécution (fonctions sum1 et sum2 détaillés ci-après)
        after = time.time()  # fin du temps d'exécution de la fonction
        duration = after - before  # durée du temps d'exécution de la fonction
        print(f"Temps d'exécution de la fonction {f.__name__} : {duration:.5f} secondes.")

    return modif_function  # ATTENTION : return de la fonction 'modif_function' sans les parenthèses !!!


@tictac
def sum1(maxi):
    """Somme du chiffre 1 au chiffre désigné avec la boucle for in range"""
    tot = 0
    for i in range(1, maxi + 1):
        tot += i
    print(f"Somme des entiers entre 1 et {maxi} = {tot}.")


@tictac
def sum2(maxi):
    """Somme du chiffre 1 au chiffre désigné avec la boucle while"""
    tot = 0
    i = 1
    while i < maxi + 1:
        tot += i
        i += 1
    print(f"Somme des entiers entre 1 et {maxi} = {tot}.")


sum1(100_000)
sum2(100_000)
