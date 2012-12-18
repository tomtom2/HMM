from BW import HMM_BW
import os, sys


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
hmm_viterbi = CURRENT_PATH.replace("baumwelch", "hmm-python")
data = CURRENT_PATH.replace("baumwelch", "data")
sys.path.append(hmm_viterbi)
import viterbi
import encodageHmm as encod


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
listState.append('')

test_table = encodeTestAsMatrix3n()

listObservables = range(len(test_table))
for kk in range(len(test_table)):
	listObservables[kk] = test_table[kk][0]

hmm = HMM_BW(listObservables, listState, 1)
for state in hmm.emissions[""]:
	if state == "":
		hmm.emissions[""][state] = 1.0
	else:
		hmm.emissions[""][state] = 0.0


def get_precision(table):
    conteur = 0
    conteur_blankLines = 0
    for index in range(len(table)):
        if table[index][1] == table[index][2]:
            conteur += 1
    precision = float(conteur)/(len(table) - conteur_blankLines)
    return precision

table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.transitions[""], hmm.transitions, hmm.emissions)

print str(viterbi.get_precision(table)*100)[0:4]+"% correct"
print "on lance les reestimations:"
hmm.iterate()
table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.transitions[""], hmm.transitions, hmm.emissions)
print str(get_precision(table)*100)[0:4]+"% correct"

hmm.iterate()
table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.transitions[""], hmm.transitions, hmm.emissions)
print str(get_precision(table)*100)[0:4]+"% correct"

hmm.iterate()
table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.transitions[""], hmm.transitions, hmm.emissions)
print str(get_precision(table)*100)[0:4]+"% correct"

