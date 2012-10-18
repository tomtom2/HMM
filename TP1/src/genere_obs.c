#include "hmm.h"

int main(int argc, char *argv[]){
	
	int nb_obs;
	char * fichier_hmm, * fichier_obs;
	hmm * Hmm;	
	if(argc != 4){
		fprintf(stderr,"erreur dans les arguments\n");
		fprintf(stderr,"Argument : nb_observation fichier_hmm fichier_observation\n");
		return -1;
	}else{
	
		nb_obs = atoi(argv[1]);
		fichier_hmm = argv[2];
		fichier_obs = argv[3];
		int * obs = malloc(sizeof(int)*nb_obs);

		Hmm = load_hmm(fichier_hmm);
		generation_observable(Hmm,nb_obs,obs);
		save_observation(obs,nb_obs,fichier_obs);
		return 0;

	}

}
