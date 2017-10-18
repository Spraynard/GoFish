import sys
import unittest

sys.path.append('../../Modules/Players/')
sys.path.append('../../Modules/Engines/')

from HumanPlayer import HumanPlayer
from Bot import Bot

from GoFish.TestGoFishEngine import TestGoFishEngine


class GoFishEngineTests(unittest.TestCase):
	def setUp(self):
		self.humanPlayer = HumanPlayer()
		self.botPlayer = Bot()
		self.engine = TestGoFishEngine(True)

	def test_initial_phase(self):
		# What is necessary for the initial phase to pass?
		# 1. Initially, since I am setting no tricks, the output must show that there are 0 tricks
		# 2. I will give a custom hand, but the output must
		self.engine.setPlayers([self.humanPlayer])
		self.engine.initialize()

		# Want to get the first hand that could possibly be dealt.
		# 	this will be the hand that the player gets, supposedly
		acceptHand = self.engine.returnFirstHand()

		# These variables contain strings which will will be what
		# 	this test is looking to assert equality to
		acceptTrickOutput = "You currently have 0 tricks"
		acceptHandOutput = "%s" % acceptHand

		# This goes through the initial phase of the engine
		self.engine.initialPhase(self.humanPlayer)

		# Full output
		output = sys.stdout.getvalue().strip()

		# Splitting the output is a nice parse to apply to
		# 	variables
		givenTrickOutput = output.split('\n')[0]
		givenHandOutput = output.split('\n')[1]

		self.assertEqual(givenTrickOutput, acceptTrickOutput)
		self.assertEqual(givenHandOutput, acceptHandOutput)

	def test_initial_phase_multiple_tricks(self):
		pass

	def test_decision_phase(self):
		pass

	def test_trading_phase(self):
		pass

	def test_end_phase(self):
		pass

	def tearDown(self):
		self.humanPlayer = None
		self.botPlayer = None
		self.engine = None

if __name__ == '__main__':
	unittest.main(verbosity=2, buffer=True)