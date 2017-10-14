class Engine:
	# Controls the start, turn, and checks of the actual game.
	def __init__(self, Players, Deck):
		self.Players = Players
		self.Deck = Deck

	def getDeck(self):
		# Summary: Gives the deck object out.
		# Returns: `self.Deck` - Deck Object
		return self.Deck

	def setDeck(self, new_deck):
		# Summary: Sets
		# Input: `new_deck` - The new value of the deck object I want to set to
		# Returns: Void
		self.Deck = new_deck

	def getPlayers(self):
		return self.Players

	def listPlayers(self):
		_players = self.getPlayers()

		print "Current Players: "
		for p in _players:
			print p

	def listPlayersHands(self):
		_players = self.getPlayers()

		for p in _players:
			# print p + ': ' + p.showHand()
			print "%s: %s" % (p, p.showHand())

	# hand Drawing Functionality goes here
	def drawCard(self):
		deck = self.getDeck()
		print "This is the deck: ", deck
		card = deck.pop()
		self.setDeck(deck)

		return card

	def drawHand(self):
		hand = []

		for i in range(7):
			drawnCard = self.drawCard()
			hand.append(drawnCard)

		return hand

	def dealHand(self):
		hand = self.drawHand()

		return hand

	def dealHands(self):
		_players = self.getPlayers()
		playerHand = False

		for p in _players:
			playerHand = self.dealHand()
			p.insertHand(playerHand)

	# End Hand Drawing Functionality
	def initialize(self):
		self.listPlayers()
		self.dealHands()
		self.listPlayersHands()