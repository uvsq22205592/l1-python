#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0]*86400 + temps[1]*3600 +temps[2]*60 + temps[3]

temps = (3,23,1,35)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    t = [0,0,0,0]
    t[0] = seconde//86400
    t[1] = (seconde%86400)//3600
    t[2] = (seconde%3600)//60
    t[3] = seconde%60
    
    return (t[0],t[1],t[2],t[3])
    
temps = secondeEnTemps(100000)
print(temps)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")