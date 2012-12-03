#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys, os
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
src = CURRENT_PATH.replace("tests", "baumwelch")

sys.path.append(src)
import BW



class BaumeWelch(unittest.TestCase):
	""" Tester la reussite"""

	def test_stat_init(self):
		stats = BW.initHmm()[0]
		size = len(stats)
		assert(size==14)




if __name__=='__main__':
    unittest.main() # main se charge de collecter les tests