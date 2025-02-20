def syracuse(n):
    l=[]
    l.append(n)
    while n != 1:
        if n%2 == 0:
            n=n//2
        else:
            n=n*3+1
        l.append(n)
    return l

N=int(input("Syracuse de : "))
print("Syracuse de",N,"nous donne :",syracuse(N))

#3)

def testeConjecture(n_max):
    for i in range (1,n_max):
        syracuse(i)
    return True
print(testeConjecture(10000))

#4)

def tempsVol(n):
    vol = len(syracuse(n))-1
    return(vol)

print("Le temps de vol de", 3, "est", tempsVol(3))

#5)

def tempsVolListe(n_max):
    liste_temps_vol = []
    for i in range(1,n_max+1):
        liste_temps_vol.append(tempsVol(i))
    return (liste_temps_vol)

N=int(input("Temps de vol de 1 à : "))
print("La liste de temps de vol de 1 à",N,tempsVolListe(N))

#6)

def tempsVolListe(n_max,max=None):
    liste_temps_vol = []
    max=tempsVol(1),1
    for i in range(1,n_max+1):
        liste_temps_vol.append(tempsVol(i))
        if tempsVol(i) > max[0]:
            max = tempsVol(i),i
    return (liste_temps_vol,max)

N=int(input("Temps de vol de 1 à : "))
print("La liste de temps de vol de 1 à",N,"est :",tempsVolListe(N)[0],"et son maximum est",tempsVolListe(N)[1][0],"atteint en",tempsVolListe(N)[1][1])

#7)

def altitude(n_max):
    max=0,0
    for i in range(1,n_max-1):
        for k in syracuse(i):
            if max[0] < k:
                max=k,i
    return max

N=int(input("Altitude de 1 jusqu'à : "))
print("L'altitude maximale de",N,"est :",altitude(N)[0],"atteint en :",altitude(N)[1])
