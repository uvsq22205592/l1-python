#2)

carre_mag=[
[4,14,15,1],
[9,7,6,12],
[5,11,10,8],
[16,2,3,13]]


L = [[0] * 4 for i in range(4)] #Crée 4 listes avec 0 en valeurs
L[0][0], L[1][0], L[2][0], L[3][0] = 4, 9, 5, 16
L[0][1], L[1][1], L[2][1], L[3][1] = 14, 7, 11, 2
L[0][2], L[1][2], L[2][2], L[3][2] = 15, 6, 10, 3
L[0][3], L[1][3], L[2][3], L[3][3] = 1, 12, 8, 13

#3)

carre_pas_mag=[
[4,14,15,1],
[9,7,6,12],
[5,11,10,8],
[16,2,7,13]]

#4)
"""
def afficheCarre(carre):
    k=0
    for j in range(len(carre)):
        for i in range(len(carre)):
            if L[i][j] >= k:
                k=L[i][j]
        a=1
        while k < a:
            a = a*10
                        

afficheCarre(L)
"""

def afficheCarre(carre):
    for i in carre:
        print(i)
    print("")

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)

#5)

def testLignesEgales(carre):
    test = []
    for i in carre:
        test.append(sum(i))
    if test.count(test[0]) == len(test):
        return(test[0])
    elif test.count(test[0]) != len(test):
        return(-1)

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

#6)

def testColonnesEgales(carre):
    test = []
    for i in carre:
        test.append(sum(i))
    if test.count(test[0]) == len(test):
        return(test[0])
    elif test.count(test[0]) != len(test):
        return(-1)

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))