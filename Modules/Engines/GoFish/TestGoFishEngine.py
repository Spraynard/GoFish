from GoFishEngine import GoFishEngine

class TestGoFishEngine(GoFishEngine):
	def __init__(self, test = False):
		super(TestGoFishEngine, self).__init__()
		if not test:
			raise Exception("This engine is only reserved for tests")

	def returnFirstHand(self):
		import copy 
		# return self.deck.cards[-7:len(self.deck.cards)]
		deck_copy = copy.copy(self.getDeck().getCards())
		hand = []
		for i in range(7):
			hand.append(deck_copy.pop())
		return hand

	# def playerAskLoop(self, choiceListLength):
	# 	print "This is the test ask loop"
	# 	print "This is the choice list length: %s" % choiceListLength
	# 	choice = None
	# 	while True:
	# 		choice = int(raw_input("Please enter your choice: ")) - 1
	# 		print "This is the choice: %s" % choice
	# 		if choice < choiceListLength:
	# 			break
	# 	return choice

	def choosePlayerToAsk(self, player):
		if self.test:
			print "current player: %s" % player
			print "self.getPlayers: %s" % self.getPlayers()
			print "choiceList: %s" % choiceList
			choiceList.remove(player)
			print "choiceList without current player: %s" % choiceList

		return super(TestGoFishEngine, self).choosePlayerToAsk(player)

	def chooseCard(self, player):
		return super(TestGoFishEngine, self).chooseCard(player)

	def initialize(self):
		# Don't want to start a game unless specifically
		# 	tell it that I want to start the game in the test.
		self.setDeck()
