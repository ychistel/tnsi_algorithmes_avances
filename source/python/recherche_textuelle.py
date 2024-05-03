fichier = open('../doc/Vingt_mille_lieues_sous_les_mers_Texte_entier.txt','r',encoding="utf-8")
livre = fichier.read()
fichier.close


def nombre_occurrence(texte,motif):
    compteur = 0
    i = 0
    while True:
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
