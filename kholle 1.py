#exercice 1
print("Exercice 1 :\n")

a = "9476"
print(len(a))
""" car la variable a est une chaîne de caractères """

print('')
#exercice2
print("Exercice 2\n")

saint_nectaire = True
salers = False

pompe_aux_pommes = False
guenilles = True

if (saint_nectaire == True or salers == True) and (pompe_aux_pommes == True or guenilles == True):
    print("Fromage et dessert")
else:
    print("Fromage ou dessert")

print('')
#exercice 3
print("Exercice 3\n")

from random import *

def nbr(n):
    total=0
    min=999
    for loop in range(n):
        k=randrange(100,999)
        total+=k
        if k < min:
            min = k
    moyenne=total/n
    return moyenne, min

N=int(input("Choisissez un nombre : "))
print("La moyenne est :",nbr(N)[0],"et le minimum est :",nbr(N)[1])
