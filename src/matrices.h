#ifndef __MATRICES__
#define __MATRICES__

#include<stdio.h>
#include<stdlib.h>

void affiche_matrice(double ** mat, int nbe, int T);
void libere_matrice(double **mat, int l);
double **alloue_matrice(int l, int c);

#endif
