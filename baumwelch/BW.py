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

	def __init__(self, listObservables, listOfStates, count):
		self.iterationCount = count
		self.listObservables = listObservables
		self.states = listOfStates
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

		self.gamma = range(len(self.listObservables))
		for index in range(len(self.beta)):
			dictOfStates = {}
			for key in self.states:
				dictOfStates[key] = 0.0
			self.gamma[index] = dictOfStates


	def initHmm(self, listObservables):

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
		# init alpha(i, 1) = Pi(i) #
		for state in self.Pi:
			self.alpha[0][state] = self.Pi[state]

		# iterate forward #
		for index in range(len(self.listObservables) - 1):
			for j in self.Pi:
				sumAlpha = 0.0
				for etat in self.states:
					sumAlpha = sumAlpha + self.alpha[index][etat]*self.emissions[self.listObservables[index]][etat]*self.transitions[etat][j]
				self.alpha[index+1][j] = sumAlpha

		

	def setBeta(self):
		# init beta(i, T) = E(i, o_t) #
		for state in self.states:
			self.beta[len(self.listObservables)-1][state] = self.emissions[self.listObservables[len(self.listObservables)-1]][state]

		# iterate backward #
		for index in range(len(self.listObservables) - 2, -1, -1):
			for j in self.states:
				sumBeta = 0.0
				for etat in self.states:
					sumBeta = sumBeta + self.beta[index+1][etat]*self.emissions[self.listObservables[index+1]][etat]*self.transitions[etat][j]
				self.beta[index][j] = sumBeta



	def setGamma(self):
		# iterate forward #
		for index in range(len(self.listObservables)):
			for j in self.states:
				sumGamma = 0.0
				for etat in self.states:
					sumGamma = sumGamma + self.alpha[index][etat]*self.beta[index][etat]
				#self.gamma[index][j] = 0.0
				if not sumGamma == 0.0:
					self.gamma[index][j] = (self.alpha[index][j]*self.beta[index][j])/sumGamma



	def setPi(self):
		for state in self.states:
			self.Pi[state] = self.gamma[0][state]

	def setT(self):
		#init proba pt for the calcul of transition probabilities
		p = range(len(self.listObservables)-1)
		for index in range(len(p)):
			p[index] = {}
			for i in self.states:
				p[index][i] = {}
				for j in self.states:
					p[index][i][j] = 0.0

		#calcul of partiel transition proba
		for t in range(len(p)):
			for i in self.states:
				sumOnStates = 0.0
				for j in self.states:
					sumOnStates = sumOnStates + self.alpha[t][j]*self.beta[t][j]
					p[t][i][j] = self.alpha[t][j]*self.beta[t+1][j]*self.emissions[self.listObservables[t]][j]*self.transitions[i][j]
				for j in self.states:
					#p[t][i][j] = 0.0
					if not sumOnStates == 0.0:
						p[t][i][j] = p[t][i][j]/sumOnStates

		#calcul of transition probabilities
		for i in self.states:
			for j in self.states:
				sumOnP = 0.0
				sumOnGamma = 0.0
				for t in range(len(p)):
					sumOnP = sumOnP + p[t][i][j]
					sumOnGamma = sumOnGamma + self.gamma[t][i]
				#self.transitions[i][j] = 0.0
				if not sumOnGamma == 0.0:
					self.transitions[i][j] = sumOnP/sumOnGamma



	def setE(self):
		for observable in self.emissions:
			for state in self.states:
				sumGammaForObservable = 0.0
				sumGammaTotal = 0.0
				for t in range(len(self.listObservables)):
					sumGammaTotal = sumGammaTotal + self.gamma[t][state]
					if self.listObservables[t] == observable:
						sumGammaForObservable = sumGammaForObservable + self.gamma[t][state]
				#self.emissions[observable][state] = 0.0
				if not sumGammaTotal == 0.0:
					self.emissions[observable][state] = sumGammaForObservable/sumGammaTotal

	def iterate(self):
		for i in range(self.iterationCount):
			self.setAlpha()
			self.setBeta()
			self.setGamma()
			self.setPi()
			self.setT()
			self.setE()
