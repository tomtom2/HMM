#include"matrices.h"

void affiche_matrice(double ** mat, int nbe, int T){
  int i,t;
  for(i=0; i< nbe; i++){
    for(t=0; t< T; t++)
      printf("%f \t", mat[i][t]);
    printf("\n");
  }
}


void libere_matrice(double **mat, int l)
{
  int i;
  if(mat){
    for(i=0; i < l; i++){
      free(mat[i]);
    }
    free(mat);
  }
}

double **alloue_matrice(int l, int c)
{
  double **mat;
  int i;
  
  mat = malloc (l * sizeof(double *));
  if(mat == NULL){
    fprintf(stderr, "probleme d'allocation\n");
    exit(1);
  }
  for(i=0; i < l; i++){
    mat[i] = malloc(c * sizeof(double));
    
    if(mat[i] == NULL){
      fprintf(stderr, "probleme d'allocation i\n");
      exit(1);
    }
  }
  return mat;
}


