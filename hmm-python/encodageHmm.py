#!/usr/bin/python
# -*- coding: utf-8 -*-

def encode(file_path):
    '''pre-traite les fichiers en vue de l'encodage (gestion des sauts de ligne notamment)'''
    T = []
    
    f = open(file_path)
    for line in f:
        T.append(line.replace("\n", ""))

    return T


def get_categories(file_path):
    '''pre-traite les fichiers en vue de l'encodage (gestion des sauts de ligne notamment)'''
    T = []
    
    f = open(file_path)
    for line in f:
        T.append(line.replace("\n", ""))

    return T


if __name__=='__main__':
    import os

    CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
    T= encode(CURRENT_PATH.replace("hmm-python", "data"+"/voc_observables"))
    print len(T)
