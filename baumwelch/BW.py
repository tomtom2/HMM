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


class HMM_BW(object):

	def __init__(self, listObservables):
		self.listObservables = listObservables
		initHmm(self, listObservables)

	def initHmm(self, listObservables):
		self.states = encod.get_categories(data+"/voc_etats")
		self.transitions = {}
		for state in states:
			self.transitions[state] = {}
			for secondState in states:
				self.transitions[state][secondState] = 1.0/len(states)

		self.emissions = {}
		for observable in listObservables:
			self.emissions[observable] = {}
			for state in states:
				self.emissions[observable][state] = 1.0/len(states)

		return [states, transitions, emissions]


	def setBeta(self):
		a = 1+1
		#for element in grid:
		#	do sth
