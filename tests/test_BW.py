#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys, os
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
src = CURRENT_PATH.replace("tests", "baumwelch")

sys.path.append(src)
from BW import HMM_BW



class BaumWelchInit(unittest.TestCase):
	""" Tester la reussite"""
	def setUp(self):
		listObservables = ["je", "ne", "suis", "pas", "un", "hero"]
		self.hmm = HMM_BW(listObservables)

	def test_stat_init(self):
		states = self.hmm.states
		size = len(states)
		assert(size==14)

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




if __name__=='__main__':
    unittest.main() # main se charge de collecter les tests