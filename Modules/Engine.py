class Engine:
	# Controls the start, turn, and checks of the actual game.
	def __init__(self):
		self.Players = False
		self.Deck = False
		self.currentPlayer = False

	def getDeck(self):
		# Summary: Gives the deck object out.
		# Returns: `self.Deck` - Deck Object
		return self.Deck

	def setDeck(self, new_deck):
		# Summary: Sets
		# Input: `new_deck` - The new value of the deck object I want to set to
		# Returns: Void
		self.Deck = new_deck

	# Player Handling Fuctionality Goes Here
	def getCurrentPlayer(self):
		return self.currentPlayer

	def setCurrentPlayer(self, player):
		self.currentPlayer = player

	def setPlayers(self, players):
		self.Players = players

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
	# End Player Handling Functionality

	# Hand Drawing Functionality goes here
	def drawCard(self):
		deck = self.getDeck()
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

	# Game Action Functionality
	def congratulations(self, player):
		print "Congratulations %s, you have won the game!" % player

	def takeTurn(self, player):
		pass

	# End Game Action Functionality

	# Game Status Functionality
	def gameOver(self, player):
		pass
	# End Game Status Functionality

	def gameStart(self):
		self.dealHands()
		self.setCurrentPlayer(self.getPlayers()[0])

		while true:
			current_player = self.getCurrentPlayer()
			if self.gameOver(current_player):
				return self.congratulations(current_player)

	def initialize(self):
		self.gameStart()