GCC = gcc -W -Wall -ggdb
LIB = -lm

OBJ = hmm.o somme_log.o matrices.o

.PHONY: clean


ALL: genere_obs

genere_obs:  genere_obs.c $(OBJ)
	$(GCC) $(LIB) genere_obs.c $(OBJ) -o genere_obs

hmm.o: hmm.c hmm.h
	$(GCC) -c hmm.c -o hmm.o

somme_log.o: somme_log.c somme_log.h
	$(GCC) -c somme_log.c -o somme_log.o

matrices.o: matrices.c matrices.h
	$(GCC) -c matrices.c -o matrices.o


clean:
	rm *.o
	rm genere_obs
