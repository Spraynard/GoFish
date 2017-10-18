class Engine:
	# Controls the start, turn, and checks of the actual game.
	def __init__(self):
		self.Players = False
		self.Deck = False
		self.playerIndex = 0
		self.variant = False

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
	def _getPlayerIndex(self):
		return self.playerIndex

	def _addPlayerIndex(self):
		players = self.getPlayers()

		if (self._getPlayerIndex() + 1) == len(players):
			self.playerIndex = 0
		else:
			self.playerIndex += 1

	def getCurrentPlayer(self):
		return self.getPlayers()[self._getPlayerIndex()]

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
	def displayTricks(self, player):
		if player.hasTricks():
			trick_n = player.getTricks()
			if (trick_n == 1):
				print "You currently have %s trick" % trick_n
			else:
				print "You currently have %s tricks" % trick_n
		else:
			print "You currently have 0 tricks"

	def displayhand(self, player):
		player.showHand()


	def displayCurrentPlayerInfo(self, player):
		if isinstance(player, Bot):
			# No need to display if the player is a bot
			return
		self.displayTricks(player)
		self.displayHand(player)

	def choosePlayerToAsk(self, player):
		choiceList = self.getPlayers.remove(player)
		choice = False

		if isinstance(player, Bot):
			# Implement Bot() player to ask
			return random.choice(choiceList)
		else:
			# Implement Player() player to ask
			print "Which player will you ask a card from?"
			for i in range(len(choiceList)):
				print "#%s: %s" % ((i + 1), choiceList[i])
			while true:
				try:
					choice = int(raw_input("Please enter your choice: ")) - 1
					if choice < len(choiceList):
						if choice < 0:
							raise IndexError
						break
				except IndexError:
					# Handles if a player were to put in a stupid number (like 1,000,000) or 0
					print "Your choice is not listed"
				except:
					print "Please enter a number."

		return choiceList[choice]

	def chooseCard(self, player):
		from Cards.Card import Card

		t_card = False
		correctInputDict = {
			'suits' : ["Clubs", "Spades", "Diamonds", "Hearts"],
			'ranks' : ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		}

		if isinstance(player, Bot):
			# Implement Bot Card Choosing. Game will not work without this. What I eventually want to to is
				#  1. Bot looks through hand for cards they have
				#  2. Of cards that bot has, look for the rank in which you have the most of.
				#  2a. If you have multiple ranks with the same amount, break by choosing randomly
				#  3. As for the selected rank from an opponent.
		else:
			rank = False
			suit = False

			while True:
				rank = str(raw_input("What card rank do you want to ask for (e.g. 2 - Ace)?: ")).lower().title()
				if not rank in correctInputDict['ranks']:
					print "That is not an acceptable card rank. Please choose again"
				else if not player.hasCard(rank):
					print "You don't even have any of those cards in your hand! Try again."
				else:
					return rank
			if self.variant == 1:
				while True:
					suit = str(raw_input("What card suit do you want to ask for (e.g. 'Clubs', 'Spades')?: ")).lower().title()
					if not suit in correctInputDict['suits']:
						print "That is not an acceptable card suit. Please choose again"
					else:
						break

	# Phases Coded Here

	def initialPhase(self, player):
		self.displayCurrentPlayerInfo(player)

	def decisionPhase(self, player):
		other = self.choosePlayerToAsk(player)
		card = self.chooseCard(player)

		return (card, other)

	def tradingPhase(self, player, decTuple):
		rank = decTuple[0]
		otherPlayer = decTuple[1]

		cardCount = False
		giveArray = False
		goodGuess = False


		print "\"Hey %s, Do you have any %ss?\"" % (otherPlayer, rank)
		if otherPlayer.hasCard(rank):
			# Count how many cards there are of that rank in the player's hand
			# 	give feedback based on the amount of cards.
			goodGuess = True
			cardCount = otherPlayer.countCards(rank)
			giveArray = otherPlayer.giveCards(rank, cardCount)
			
			if isinstance(otherPlayer, Bot):
				print otherPlayer.exclaim() % (cardCount, giveArray)
			else:
				print "I do have %s cards. Here they are: %s" % (cardCount, giveArray)

			player.takeCards(giveArray)
		else:
			if isinstance(otherPlayer, Bot):
				# If the other player is a bot, they will taunt the shit out of you
				# 	and probably make you really sad af.
				print otherPlayer.tauntPlayer()
			else:
				print "\"I sure do not %s\"" % player
			player.drawSingleCard(self.getDeck())

		return goodGuess


	def endPhase(self, player, goodGuess):
		if goodGuess:
			# If the player has a good guess (e.g. they asked another player for a card that they
			# 	had in their hand and they actually had one or more of those cards in their hand)
			self.takeTurn(player)
		else:
			# If the player had to draw from the pile because they guessed badly.
			# self.scanHand(player)
			# self.setTricks(player:

	# End Phase Codes
	def takeTurn(self, player):
		# Turn consists of:
		# 	INITIAL PHASE
		# 	- Displaying player's hand and amount of tricks (if any)
		# 	DECISION PHASE
		# 	- choosing which player to ask for a card
		#  	- choosing which card to ask of them
		# 	TRADING PHASE
		# 	- If other player has card, give card(s) to asking player
		# 	- If other player does not have card, asking player draws one card from deck
		# 	END PHASE
		# 	- Scan hand to see if there are any tricks available
		# 	- If four tricks, player wins
		self.initialPhase(player)
		(rank, other) = self.decisionPhase(player)
		goodGuess = self.tradingPhase(player, (rank, other))
		endPhase(player, goodGuess)

	
	def endTurn(self):
		pass

	def gameLoop(self):
		# Will stop when there is a player that has gotten the winning conditions of the game
		while not self.gameOver():
			# Getting the current player for the turn
			current_player = self.getCurrentPlayer()
			self.takeTurn(current_player)


	def congratulations(self, player):
		print "Congratulations %s, you have won the game!" % player


	# End Game Action Functionality

	# Game Status Functionality
	def gameOver(self, player):
		return False
	# End Game Status Functionality

	def gameStart(self):
		self.dealHands()
		self.gameLoop()
		self.endGame()

	def initialize(self):
		self.gameStart()