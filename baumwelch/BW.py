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

	def __init__(self, listObservables, count):
		self.iterationCount = count
		self.listObservables = listObservables
		self.initHmm(listObservables)

		# init the alpha and beta grids #
		self.alpha = range(len(self.listObservables))
		for index in range(len(self.alpha)):
			dictOfStates = {}
			for key in self.states:
				dictOfStates[key] = 1.0/len(self.states)
			self.alpha[index] = dictOfStates

		self.beta = range(len(self.listObservables))
		for index in range(len(self.beta)):
			dictOfStates = {}
			for key in self.states:
				dictOfStates[key] = 1.0/len(self.states)
			self.beta[index] = dictOfStates


	def initHmm(self, listObservables):
		self.states = encod.get_categories(data+"/voc_etats")

		self.Pi = {}
		for key in self.states:
			self.Pi[key] = 1.0/len(self.states)

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
		iterations = 0
		while iterations < self.iterationCount:
			iterations = iterations + 1
