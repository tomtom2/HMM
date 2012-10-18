#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import encodageHmm as encod
import time as t



CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
data = CURRENT_PATH.replace("hmm-python", "data")



def getCategoryDict():
    #le tableau des catégories
    Cat = encod.get_categories(data+"/voc_etats")
    dico = {}
    for c in Cat:
        dico[c] = 0
    return dico



def get_Pi_T_E():

    #le tableau des observables
    Tab = encod.encode(data+"/voc_observables")

    #le tableau des catégories
    Cat = encod.get_categories(data+"/voc_etats")



    #initialisation du nombre d'occurences des différentes catégories en début de phrase
    I = {}
    for c in Cat:
        I[c] = 0

    occur_cat = {}
    for c in Cat:
        occur_cat[c] = 0


    #initialisation de la matrice des occurences des bigrames: T[i, j] = nombre de bigrammes (cj, ci)
    T = {}
    for i in Cat:
        T[i] = getCategoryDict()

    #initialisation de la matrice d'emissions des observables: T[i, j] = nombre d'observable o[j] de categorie c[i]
    E = {}
    for i in Tab:
        E[i] = getCategoryDict()



    base_app = []
    file_app = open(data+"/train")
    start_sentence = True

    categorie_before = ""
    for line in file_app:
        
        if line != "\n":
            
            observable = line.split("\t")[0]
            categorie = line.split("\t")[1].replace("\n", "")

            #remplissage de E (les occurence d'emission et des categories)
            E[observable][categorie] = E[observable][categorie] + 1
            occur_cat[categorie] = occur_cat[categorie] + 1

            #remplissage de I (les début de phrases)
            if start_sentence:
                 I[categorie] = I[categorie] + 1
                 start_sentence = False
                 categorie_before = categorie

            elif line != "\n":
                #remplissage de T (les occurence des binomes)
                T[categorie_before][categorie] = T[categorie_before][categorie] + 1
                categorie_before = categorie

        else:
            start_sentence = True

    #############################
    # normalisation et écriture #
    #############################
    
    # Pi(c)
    N = 0
    for c in I:
        N = N + I[c]
    for c in I:
        I[c] = float(I[c])/N
        
    
    # T(c1, c2)
    for c1 in T:
        for c2 in T[c1]:
            T[c1][c2] = float(T[c1][c2])/occur_cat[c1]
            
    
    
    # E(c, m)
    for m in E:
        for c in E[m]:
            E[m][c] = float(E[m][c])/occur_cat[c]
    #print E
    return [I, T, E]


def make_hmm():
    start = t.time()
    path = CURRENT_PATH + "/hmm.txt"
    print path
    if os.path.exists(path):
        return 0
    S = get_Pi_T_E()
    I = S[0]
    T = S[1]
    E = S[2]

    f = open(path, 'w')

    f.write('#nb etats\n')
    f.write(str(len(I)) + '\n')
    f.write('#nb observables\n')
    f.write(str(len(E)) + '\n')

    f.write('#probabilites initiales\n')
    for c in I:
        f.write(str(I[c])+'\n')

    f.write('#probabilites de transition\n')
    for c1 in T:
        for c2 in T[c1]:
            f.write(str(T[c1][c2])+'\n')

    f.write('#probabilites d\'emission\n')
    for o in E:
        for c in E[o]:
            f.write(str(E[o][c])+'\n')
    f.close()
    return "hmm created in " + str(t.time() - start) + " seconds!"



if __name__=='__main__':
    print make_hmm()
