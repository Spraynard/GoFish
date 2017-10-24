import sys
import unittest

sys.path.append('../../../Modules/Players/')
sys.path.append('../../../Modules/Engines/')
sys.path.append('../../../Modules/Cards/')

from Bot import Bot
from HumanPlayer import HumanPlayer
from GoFishCard import GoFishCard as Card
from GoFish.TestGoFishEngine import TestGoFishEngine

# Question: How can I test the end phase?
# 
# 	First, what does the end phase of the Go Fish program do? Steps listed below:
# 
# 		1. If Player was able to correctly guess a card in another player's hand:
# 			- Internal player class state relating to guesses is RESET.
# 			- Any tricks in the player's hand are taken out.
# 			- The same player is able to take another turn of the game if the game is not ended
# 			- If the game is ended we end that shit.
# 		
# 		2. If Player did not correctly guess a card in another player's hand:
# 			- Player sorts their hand; populating internal player sortDict in the process
# 			- Player then `looks for tricks` within the sort Dict (any grouping that has 4 cards)
# 			- Player then `sets the tricks`. Upticking internal player trick count, as well as
# 				the engine's master trick count.
# 			- Player index is upticked, causing the next player to be available for the next turn
# 
# 		3. Game ends if 13 tricks are made. 13 * 4 = 52 so that means that all cards are down on the table
# 			- The player with the most tricks wins the game!
# 			
class EndPhaseEngineTests(unittest.TestCase):
	
	def setUp(self):
		self.humanPlayer = HumanPlayer().randomName()
		self.botPlayer = Bot()
		self.engine = TestGoFishEngine(True)

	# Insert Tests Here
	def testEndPhaseCorrect(self):
		pass

	def testEndPhaseCorrectOneTrick(self):
		pass

	def testEndPhaseCorrectMultipleTricks(self):
		pass

	def testEndPhaseCorrectEndGame(self):
		pass

	def testEndPhaseIncorrectNoTricks(self):
		pass

	def testEndPhaseIncorrectOneTrick(self):
		pass

	def testEndPhaseIncorrectMultipleTricks(self):
		pass

	def testEndPhaseIncorrectEndGame(self):
		pass
	
	def tearDown(self):
		self.humanPlayer = None
		self.botPlayer = None
		self.engine = None

if __name__ == '__main__':
	unittest.main(verbosity = 2, buffer = True)