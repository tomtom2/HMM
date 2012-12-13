#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys, os
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
src = CURRENT_PATH.replace("tests", "baumwelch")

sys.path.append(src)
from BW import HMM_BW



class BaumWelchInit(unittest.TestCase):
	""" Tester la reussite de l'initialisation """
	def setUp(self):
		listObservables = ["je", "ne", "suis", "pas", "un", "hero"]
		self.hmm = HMM_BW(listObservables, 5)

	def test_stat_init(self):
		states = self.hmm.states
		size = len(states)
		assert(size==14)

	def test_Pi_init(self):
		Pi = self.hmm.Pi
		size = len(Pi)
		assert(size==14)

	def test_alpha_init(self):
		alpha = self.hmm.alpha
		sizeI = len(alpha)
		sizeJ = len(alpha[0])
		assert(sizeI==6)
		assert(sizeJ==14)

	def test_beta_init(self):
		beta = self.hmm.beta
		sizeI = len(beta)
		sizeJ = len(beta[0])
		assert(sizeI==6)
		assert(sizeJ==14)

	def test_transitions_init(self):
		transitions = self.hmm.transitions
		sizeI = len(transitions)
		sizeJ = 0
		for key in transitions:
			sizeJ = len(transitions[key])
			break

		assert(sizeI==14)
		assert(sizeJ==14)

	def test_emissions_init(self):
		emissions = self.hmm.emissions
		sizeI = len(emissions)
		sizeJ = 0
		for key in emissions:
			sizeJ = len(emissions[key])
			break
		assert(sizeI==6)
		assert(sizeJ==14)

class BaumWelchIterate(unittest.TestCase):
	""" Tester la reussite des réestimations """
	def setUp(self):
		listObservables = ["je", "ne", "suis", "pas", "un", "hero"]
		self.hmm = HMM_BW(listObservables, 5)

	def test_setAlpha(self):
		alpha_0 = self.hmm.alpha[1]['A']
		self.hmm.setAlpha()
		alpha_1 = self.hmm.alpha[1]['A']

		assert(not alpha_0 == alpha_1)

	def test_setBeta(self):
		beta_0 = self.hmm.beta[0]['A']
		self.hmm.setBeta()
		beta_1 = self.hmm.beta[0]['A']

		assert(not beta_0 == beta_1)

	def test_iterations(self):
		self.hmm.iterate()
		assert(1==2)






if __name__=='__main__':
    unittest.main() # main se charge de collecter les tests