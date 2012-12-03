#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys, os
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
src = CURRENT_PATH.replace("tests", "baumwelch")

sys.path.append(src)
import BW



class BaumWelchInit(unittest.TestCase):
	""" Tester la reussite"""

	def test_stat_init(self):
		stats = BW.initHmm("obs")[0]
		size = len(stats)
		assert(size==14)

	def test_transitions_init(self):
		listObservables = ["je", "ne", "suis", "pas", "un", "hero"]
		transitions = BW.initHmm(listObservables)[1]
		sizeI = len(transitions)
		sizeJ = 0
		for key in transitions:
			sizeJ = len(transitions[key])
			break

		assert(sizeI==14)
		assert(sizeJ==14)

	def test_emissions_init(self):
		listObservables = ["je", "ne", "suis", "pas", "un", "hero"]
		emissions = BW.initHmm(listObservables)[2]
		sizeI = len(emissions)
		sizeJ = 0
		for key in emissions:
			sizeJ = len(emissions[key])
			break
		print emissions
		assert(sizeI==6)
		assert(sizeJ==14)




if __name__=='__main__':
    unittest.main() # main se charge de collecter les tests