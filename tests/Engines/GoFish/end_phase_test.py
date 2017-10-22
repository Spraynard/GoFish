import sys
import unittest

sys.path.append('../../../Modules/Players/')
sys.path.append('../../../Modules/Engines/')
sys.path.append('../../../Modules/Cards/')

from Bot import Bot
from HumanPlayer import HumanPlayer
from GoFishCard import GoFishCard as Card
from GoFish.TestGoFishEngine import TestGoFishEngine

class EndPhaseEngineTests(unittest.TestCase):
	
	def setUp(self):
		self.humanPlayer = HumanPlayer().randomName()
		self.botPlayer = Bot()
		self.engine = TestGoFishEngine(True)

	# Insert Tests Here
	def testEndPhase(self):
		pass
	
	def tearDown(self):
		self.humanPlayer = None
		self.botPlayer = None
		self.engine = None

if __name__ == '__main__':
	unittest.main(verbosity = 2, buffer = True)