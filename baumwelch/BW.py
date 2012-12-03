#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
data = CURRENT_PATH.replace("baumwelch", "data")
hmm_python = CURRENT_PATH.replace("baumwelch", "hmm-python")

sys.path.append(hmm_python)

import encodageHmm as encod
import apprentissage as app



def initHmm():
	states = encod.get_categories(data+"/voc_etats")
	transitions = []
	emissions = []

	return [states, transitions, emissions]


def setBeta():
	a = 1+1
	#for element in grid:
	#	do sth
