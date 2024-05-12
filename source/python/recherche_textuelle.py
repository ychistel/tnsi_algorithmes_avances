fichier = open('../doc/Vingt_mille_lieues_sous_les_mers_Texte_entier.txt','r',encoding="utf-8")
livre = fichier.read()
fichier.close


def nombre_occurrence(texte,motif):
    compteur = 0
    i = 0
    while i < len(texte):
        occurrence = texte.find(motif,i)
        if occurrence == -1:
            return compteur
        else:
            compteur += 1
            i = occurrence + 1

def correspondance(texte,motif,i):
    j = 0
    while j < len(motif):
        if texte[i+j] == motif[j]:
            j += 1
        else:
            return False
    return True

def recherche(texte,motif):
    i = 0
    while i < len(texte):
        if correspondance(texte,motif,i):
            return i
        else:
            i = i + 1
    return -1

# -----------------------------------------------
# Algorithme Boyer Moore Horspool
# -----------------------------------------------

def dict_motif(motif):
    d = {}
    for i in range(len(motif)):
        d[motif[i]] = i
    return d

def decalage(texte,motif,dico,i):
    j = len(motif)-1
    while j >= 0:
        if texte[i+j] == motif[j]:
            j -= 1
        else:
            if texte[i+j] not in dico.keys():
                return j + 1
            else:
                d = j - dico[texte[i+j]]
                if d < 0:
                    d = 1
                return d
    return 0

def bmh(texte,motif):
    i = 0
    cpt = 0
    d = dict_motif(motif)
    while i <= len(texte)-len(motif):
        decale = decalage(texte,motif,d,i)
        cpt += 1
        #print(f'on décale {motif} de {decale} caractères à droite') 
        if decale == 0:
            print(cpt)
            return i
        else:
            i = i + decale
    return -1

texte = 'hippopotame'
motif = 'pop'
bmh(texte,motif)