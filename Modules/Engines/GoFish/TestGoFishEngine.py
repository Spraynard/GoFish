from GoFishEngine import GoFishEngine

class TestGoFishEngine(GoFishEngine):
	def __init__(self, test = False):
		super(TestGoFishEngine, self).__init__()
		if not test:
			raise Exception("This engine is only reserved for tests")

	def returnFirstHand(self):
		return self.deck.cards[-7:len(self.deck.cards)]

	def initialize(self):
		# Don't want to start a game unless specifically
		# 	tell it that I want to start the game in the test.
		self.setDeck()
		self.dealHands()

