from BW import HMM_BW
import os, sys


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
hmm_viterbi = CURRENT_PATH.replace("baumwelch", "hmm-python")
data = CURRENT_PATH.replace("baumwelch", "data")
sys.path.append(hmm_viterbi)
import viterbi
import encodageHmm as encod



listState = ["", "CL", "ADV", "V", "D", "N"] #encod.get_categories(data+"/voc_etats")
listObservables = ["", "je", "ne", "suis", "pas", "un", "hero"]
etats_reels = ["", "CL", "ADV", "V", "ADV", "D", "N"]
hmm = HMM_BW(listObservables, listState, 1)

test_table = range(len(listObservables))
for index in range(len(listObservables)):
	test_table[index] = range(3)
	test_table[index][0] = listObservables[index]
	test_table[index][1] = etats_reels[index]
	test_table[index][2] = ""

table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.Pi, hmm.transitions, hmm.emissions)
hmm.emissions[''] = {"":1.0, "CL":0.0, "ADV":0.0, "V":0.0, "ADV":0.0, "D":0.0, "N":0.0}
for obs in hmm.emissions:
	if not obs == "":
		hmm.emissions[obs][""] = 0.0

print hmm.emissions
print table
print "on lance les reestimations:"
hmm.iterate()
table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.Pi, hmm.transitions, hmm.emissions)
print hmm.emissions
print table

print "on lance les reestimations:"
hmm.iterate()
table = viterbi.determinerClassesAvecDonneeExternes(test_table, hmm.Pi, hmm.transitions, hmm.emissions)
print hmm.emissions
print table
