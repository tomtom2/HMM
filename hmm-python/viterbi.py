#!/usr/bin/python
# -*- coding: utf-8 -*-

import encodageHmm as encod
import apprentissage as app
import os




CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
data = CURRENT_PATH.replace("hmm-python", "data")


def encodeTestAsMatrix3n():
    '''Obtenir les données dans une matrice 3D'''
    T = []
    
    f = open(data+"/test")
    for line in f:
        l = []
        if line != "\n":
            l = line.replace("\n", "").split("\t")
        else:
            l = ["", ""]
        t = [l[0], l[1], ""]
        T.append(t)

    return T


def getMaxEmission(E, observable):
    '''Recherche la categorie avec le maximum de probabilité d\'emission '''
    maxProba = 0
    categorieSelected = ""
    for categorie in E[observable]:
        e = 0.00001
        if E[observable][categorie]>0:
            e = E[observable][categorie]
        if e > maxProba:
            maxProba = e
            categorieSelected = categorie
    return categorieSelected


def get_class_max_proba_transition(I, T, E, categorie1, observable2):
    '''Retourne la catgorie avec le maximum de probabilité de transition'''
    maxProba = 0
    categorieSelected = ""
    for categorie in I:
        t = 0.00001
        e = 0.00001
        if T[categorie1][categorie]>0:
            t = T[categorie1][categorie]
        if E[observable2][categorie]>0:
            e = E[observable2][categorie]

        probaCategorie_o2 = t * e

        if probaCategorie_o2 > maxProba:
            maxProba = probaCategorie_o2
            categorieSelected = categorie
    return categorieSelected

def get_classes_max_proba_initiales(I, E, o_initial):
    '''Retourne la catégorie avec le maximum de probabilité initiale'''
    maxProba = 0
    categorieSelected = ""
    for categorie in I:
        i = 0.0000001
        e = 0.0000001
        if I[categorie]>0:
            i = I[categorie]
        if E[o_initial][categorie]>0:
            e = E[o_initial][categorie]

        probaCategorie_o_initial = i * e

        if probaCategorie_o_initial > maxProba:
            maxProba = probaCategorie_o_initial
            categorieSelected = categorie
    return categorieSelected



def determinerClassesParViterbi():
    '''Utilisation de l'algorithme de Viterbi pour determiner la classe des observables'''

    S = app.get_Pi_T_E()
    I = S[0]
    T = S[1]
    E = S[2]

    test_table = encodeTestAsMatrix3n()
    reading_observable_initiale = True

    for index in range(len(test_table)):
        if test_table[index][0] != "":
            if reading_observable_initiale:
                reading_observable_initiale = False
                test_table[index][2] = get_classes_max_proba_initiales(I, E, test_table[index][0])
            else:
                test_table[index][2] = get_class_max_proba_transition(I, T, E, test_table[index-1][1], test_table[index][0])

        else:
            reading_observable_initiale = True

    return test_table


def determinerClassesParMethodeNaive():
    '''Déterminer la classe en utilisant une methode naive : prendre l'état dont la probabilité est maximale pour l'observable (on ne prends pas en compte les probabilités de transition'''

    S = app.get_Pi_T_E()
    I = S[0]
    T = S[1]
    E = S[2]

    print T

    test_table = encodeTestAsMatrix3n()

    for index in range(len(test_table)):
        if test_table[index][0] != "":
            test_table[index][2] = getMaxEmission(E, test_table[index][0])

    return test_table



def get_precision(table):
    '''Calcule la précision de notre algorithme de Viterbi sur les données que l'on avait'''
    conteur = 0
    conteur_blankLines = 0
    for index in range(len(table)):
        if table[index][1] == table[index][2] and table[index][1] != "":
            conteur += 1
        elif table[index][1] == "":
            conteur_blankLines += 1
    precision = float(conteur)/(len(table) - conteur_blankLines)
    return precision


if __name__=='__main__':
    table = determinerClassesParViterbi()
    print "Viterbi -> "+str(get_precision(table)*100)[0:4]+"% correct"
    tableNaif = determinerClassesParMethodeNaive()
    print "algo naif -> "+str(get_precision(tableNaif)*100)[0:4]+"% correct"

