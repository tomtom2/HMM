#include"hmm.h"



hmm *allocate_hmm(int nbe, int nbo)
{
  hmm *h;
  int i,j;

  h = malloc(sizeof(hmm));
  if(h == NULL){
    fprintf(stderr, "erreur d'allocation\n");
    exit(1);
  }
  h->nbe = nbe;
  h->nbo = nbo;

  /* allocation de la matrice de transition */

  for(i = 0; i < nbe; i++){
    h->T = malloc(nbe * sizeof(double *));
    if(h->T == NULL){
      fprintf(stderr, "erreur d'allocation\n");
      exit(1);
    }
    for(j = 0; j < nbe; j++){
      h->T[j] = malloc(nbe * sizeof(double));
      if(h->T[j] == NULL){
	fprintf(stderr, "erreur d'allocation\n");
	exit(1);
      }
    }
  }
  
  /* allocation de la matrice d'emission */

  for(i = 0; i < nbe; i++){
    h->E = malloc(nbe * sizeof(double *));
    if(h->E == NULL){
      fprintf(stderr, "erreur d'allocation\n");
      exit(1);
    }
    for(j = 0; j < nbo; j++){
      h->E[j] = malloc(nbo * sizeof(double));
      if(h->E[j] == NULL){
	fprintf(stderr, "erreur d'allocation\n");
	exit(1);
      }
    }
  }
  
  /* allocation de la matrice des probabilites initiales */
  h->PI = malloc(nbe * sizeof(double));
  if(h->PI == NULL){
    fprintf(stderr, "erreur d'allocation\n");
    exit(1);
  }

  return h;
}

void print_hmm(hmm *h, char *file_name)
{
  int  i,j;
  FILE *f = stdout;

  if(file_name)
    f = fopen(file_name, "w");
  else
    f = stdout;

  fprintf(f, "#nb etats\n");
  fprintf(f, "%d\n", h->nbe);
  fprintf(f, "#nb observables\n");
  fprintf(f, "%d\n", h->nbo);
  fprintf(f, "#probabilites initiales\n");
  for(i=0; i < h->nbe; i++){
    fprintf(f, "%f\n", exp(h->PI[i]));
  }

  fprintf(f, "#probabilites de transition\n");
  for(i=0; i < h->nbe; i++){
    for(j=0; j < h->nbe; j++){
      fprintf(f, "%f\n", exp(h->T[i][j]));
    }
  }

  fprintf(f, "#probabilites d'emission\n");
  for(i=0; i < h->nbe; i++){
    for(j=0; j < h->nbo; j++){
      fprintf(f, "%f\n", exp(h->E[i][j]));
    }
  }
  if(file_name)
    fclose(f);
}

void ligne_suivante(FILE *f, char *buff)
{
  do{
    fgets (buff, LONG_LIGNE, f);
  } while(buff[0] == '#');
}

hmm *load_hmm(char *file_name)
{
  char buff[LONG_LIGNE];
  FILE *f = fopen(file_name, "r");
  hmm *h;
  int nbe, nbo;
  int i,j;

  if(f == NULL){
    fprintf(stderr, "impossible d'ouvrir le fichier %s\n", file_name);
    exit(1);
  }

  /* lecture du nombre d'etats */
  do{
    fgets (buff, LONG_LIGNE, f);
  } while(buff[0] == '#');
  
  sscanf(buff, "%d", &nbe);

  /* lecture du nombre de symboles d'emission */
  do{
    fgets (buff, LONG_LIGNE, f);
  } while(buff[0] == '#');
  
  sscanf(buff, "%d", &nbo);
  
  /* allocation du hmm */
  h = allocate_hmm(nbe, nbo);

  /* lecture des proba initiales */


  do{
    fgets (buff, LONG_LIGNE, f);
  } while(buff[0] == '#');
  
  i = 0;
  while(i < nbe){
    do{
      fgets (buff, LONG_LIGNE, f);
    } while(buff[0] == '#');
    sscanf(buff, "%lf", &(h->PI[i]));
    h->PI[i] = log(h->PI[i]);
    i++;
  }



  /* lecture des proba de transition */

  do{
    fgets (buff, LONG_LIGNE, f);
  } while(buff[0] == '#');

  i = 0;
  while(i < nbe){
    j = 0;
    while(j < nbe){
      do{
	fgets (buff, LONG_LIGNE, f);
      } while(buff[0] == '#');
      sscanf(buff, "%lf", &(h->T[i][j]));
      h->T[i][j] = log(h->T[i][j]);
      j++;
    }
    i++;
  }


  /* lecture des proba d'emssion */

  do{
    fgets (buff, LONG_LIGNE, f);
  } while(buff[0] == '#');

  i = 0;
  while(i < nbe){
    j = 0;
    while(j < nbo){
      do{
	fgets (buff, LONG_LIGNE, f);
      } while(buff[0] == '#');
      sscanf(buff, "%lf", &(h->E[i][j]));
      h->E[i][j] = log(h->E[i][j]);
      j++;
    }
    i++;
  }




  fclose(f);
  return h;
}


int *charge_observables(char *file_name, int T)
{
  FILE *f = fopen(file_name, "r");
  char buff[LONG_LIGNE];
  int t = 0;
  int *o = malloc(T * sizeof(int));
  
  if(o == NULL){
    fprintf(stderr, "erreur d'allocation\n");
    exit(1);
  }

  if(f == NULL){
    fprintf(stderr, "impossible d'ouvrir le fichier %s\n", file_name);
    exit(1);
  }
  
  while(!feof(f) && t < T){
    fgets (buff, LONG_LIGNE, f);
    sscanf(buff, "%d", &o[t]);
    t++;
  }
  if(t != T){
    fprintf(stderr, "ATTENTION, le fichier \"%s\" contient moins de %d observables !\n", file_name, T); 
  }

  return o;

}

double my_random2(){

	double r;

	r = (double)((rand())/(double)RAND_MAX);
	return r;

}





void generation_observable(hmm*Hmm,int n, int * obs){

	int i,o,etat,pred;
	double r,proba;

	srand(time(NULL));

	// Generation de l'etat initial

	r = my_random2();
	
	proba = 0;
	etat=-1;
	
	while(r>=proba && etat < Hmm->nbe-1){
		etat++;
		proba += pow(base_e, Hmm->PI[etat]);
	}

	//generation des observables

	for(i=0;i<n;i++){
		r = my_random2();
		proba = 0;
		o=-1;

		while(r>=proba && o < Hmm->nbo-1){
			o++;
			proba += pow(base_e, Hmm->E[etat][o]);
		}

		obs[i] = o;

		// Generation de l'etat suivant

		r = my_random2();

		proba = 0;
		pred = etat;
		etat=-1;

		while(r>=proba && etat < Hmm->nbe-1){
			etat++;
			proba += pow(base_e, Hmm->T[pred][etat]);
		}
	}

}

void save_observation(int * obs, int n, char * fich){

	int i;
	FILE * fichier = fopen(fich, "w+");
	for(i=0;i<n;i++){
		fprintf(fichier,"%d\n",obs[i]);
	}

	fclose(fichier);
}
