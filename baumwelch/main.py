from BW import HMM_BW
import os, sys


hmm_determine = True
perturbation = False
coef = 0.001

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
hmm_viterbi = CURRENT_PATH.replace("baumwelch", "hmm-python")
data = CURRENT_PATH.replace("baumwelch", "data")
sys.path.append(hmm_viterbi)
import viterbi
import encodageHmm as encod
import apprentissage as app
import random


def encodeTestAsMatrix3n():
    T = []
    
    f = open(data+"/BWtest")
    for line in f:
        l = []
        if line != "\n":
            l = line.replace("\n", "").split("\t")
        else:
            l = ["", ""]
        t = [l[0], l[1], ""]
        T.append(t)

    return T



listState = encod.get_categories(data+"/voc_etats")
listState.append("")

test_table = encodeTestAsMatrix3n()

listObservables = range(len(test_table))
for k in range(len(test_table)):
	listObservables[k] = test_table[k][0]

### On construit un hmm avec le fichier d'apprentissage ###
S = app.get_Pi_T_E()
I = S[0]
T = S[1]
E = S[2]
if perturbation:
    for obs in listObservables:
        for state in listState:
            if obs in E and not state=="":
                E[obs][state]+=(random.random()-0.5)*coef
###########################################################
hmm = HMM_BW(listObservables, listState, 1)

if hmm_determine:
    hmm.Pi = I
    hmm.Pi[""] = 0.0
    T[""] = hmm.Pi
    for state in hmm.Pi:
        T[state][""] = 0.01
    hmm.transitions = T
    hmm.transitions[""] = {}
    E[""] = hmm.Pi
    for obs in hmm.listObservables:
        E[obs][""] = 0.0
    E[""][""] = 1.0

    hmm.emissions = E
    hmm.emissions[""] = {}
    for key in hmm.Pi:
        hmm.transitions[""][key] = hmm.Pi[key]
        hmm.emissions[""][key] = hmm.Pi[key]

for state in hmm.emissions[""]:
	if state == "":
		hmm.emissions[""][state] = 1.0
	else:
		hmm.emissions[""][state] = 0.0


def get_precision(table):
    conteur = 0
    for index in range(len(table)):
        if table[index][1] == table[index][2]:
            conteur += 1
    precision = float(conteur)/(len(table))
    return precision

table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.transitions[""], hmm.transitions, hmm.emissions)

print str(viterbi.get_precision(table)*100)[0:4]+"% correct"
print "on lance les reestimations:"

hmm.iterate()
table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.transitions[""], hmm.transitions, hmm.emissions)
print str(get_precision(table)*100)[0:5]+"% correct"

hmm.iterate()
table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.transitions[""], hmm.transitions, hmm.emissions)
print str(get_precision(table)*100)[0:5]+"% correct"

print "on applique une perturbation sur la matrice d'emission:"
hmm.perturbation(0.00001)
print str(viterbi.get_precision(table)*100)[0:4]+"% correct"
print "on itere a nouveau:"
hmm.iterate()
table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.transitions[""], hmm.transitions, hmm.emissions)
print str(get_precision(table)*100)[0:5]+"% correct"
