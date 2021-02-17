"""
Les décorateurs

Par principe chaque fonction a une seule instruction, un decorateur prend en charge des instructions communes à
plusieurs autres fonctions

Dans l'exemple ci-dessous, on déclare des fonctions lambda sans recourir aux décorateurs

Éditeur : Laurent REYNAUD
Date : 01-12-2020
"""

first_line = lambda: print('1ère ligne !')

second_line = lambda: print('2ème ligne !')

third_line = lambda: print('3ème ligne !')

fourth_line = lambda: print('4ème ligne !')

fifth_line = lambda: print('5ème ligne !')

sixth_line = lambda: print('6ème ligne !')

seventh_line = lambda: print('7ème ligne !')

first_line()
second_line()
third_line()
fourth_line()
fifth_line()
sixth_line()
seventh_line()
