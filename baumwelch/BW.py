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
		self.initHmm(listObservables)

	def initHmm(self, listObservables):
		self.states = encod.get_categories(data+"/voc_etats")
		self.transitions = {}
		for state in self.states:
			self.transitions[state] = {}
			for secondState in self.states:
				self.transitions[state][secondState] = 1.0/len(self.states)

		self.emissions = {}
		for observable in listObservables:
			self.emissions[observable] = {}
			for state in self.states:
				self.emissions[observable][state] = 1.0/len(self.states)

		return [self.states, self.transitions, self.emissions]

	def setAlpha(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def setBeta(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def setGamma(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def setPi(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def setT(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def setE(self):
		a = 1+1
		#for element in grid:
		#	do sth

	def iterate(self):
		while 0 > 0.01:
			pass
			a = 1
