class HumanPlayer(object):
	"""Player object, All the commands that the player will use in the game are here."""
	def __init__(self, name = False):		
		import uuid

		self.hand = False
		self.name = name
		self.tricks = False

		# Internal Player's Responses to questions posed by engine
		self.guess = False
		self.chosenPlayer = False
		self.chosenCard = False

		# Internal Player's ID
		self.id = uuid.uuid4()

	def __eq__(self, other):
		return self.id == other.id

	def __repr__(self):
		return str(self.name) or "Player"

	def __str__(self):
		if type(self.name) == int:
			return "Player #%s" % self.name
		return "'%s'" % self.name or "Player"
	
	# |-------------Player to Player Interaction Functionality---------------|

	def getChosenPlayer(self):
		return self.chosenPlayer

	def setChosenPlayer(self, player):
		self.chosenPlayer = player

	def getChosenCard(self):
		return self.chosenCard

	def setChosenCard(self, card):
		self.chosenCard = card

	def resetChosenVariables(self):
		self.chosenPlayer = False
		self.chosenCard = False

	# |_____________End Player to Player Interaction Functionality-----------|
	# Guess Functionalty

	def setGuess(self, bool)
		if not type(bool) == bool:
			raise Exception("You have to set a boolean value (True/False)")
		self.guess = bool

	def gotGuess(self):
		return self.guess

	def resetGuess(self):
		self.setGuess("False")

	def guessedCorrectly(self):
		self.setGuess("True")

	# End Guess Functionality

	# Trick functionality

	def addTrick(self):
		self.tricks += 1

	def getTricks(self):
		return self.tricks

	def hasTricks(self):
		return not (self.getTricks == False)

	# End Trick Functionality

	# Player Hand Functionality
	def getHand(self):
		return self.hand

	def hasHand(self):
		if (self.hand):
			return True
		return False

	def showHand(self):
		return self.hand

	# NEEDS ATTENTION - OCTOBER 17th, 2017
	def sortHand(self):
		# Go through the hand. Will group similar cards within
		# 	sortingDict and then group them. Sorting dict may be used
		# 	to find out if a group can become a trick. I don't know
		sortingDict = {}

		for c in self.gethand():
			cardRank = c.getRank()
			if not cardRank in sortingDict:
				sortingDict[cardRank] = []
			sortingDict[cardRank].append(c)

	# End Player Hand Functionality

	#|---------Drawing or Taking Cards Functionality--------|

	def takeCard(self, card):
		self.hand.append(card)

	def takeRelevantCards(self, cardArray):
		for c in cardArray:
			self.takeCard(c)

	def drawSingleCard(self, deck):
		# Summary: Draws a single card from the deck and then adds it to the player's hand
		# Input: `Deck` - The deck being used by the players. 
		# Return: Void
		try:
			card = deck.pop()
			self.takeCard(card)
		except:
			return False

	def drawHand(self, deck):
		for i in range(7):
			self.drawSingleCard(deck)

	# |--------End Drawing or Taking Cards Functionality-----|

	# Code for player specific TRADING PHASE operations
	def hasSpecificCard(self, card):
		pass

	def hasCard(self, flagCard):
		# Non variant version of hasCard.
		# This version just plain checks to see if the player has
		# 	any cards of given rank in their hands.
		hand = self.getHand()
		flagCardRank = flagCard.getRank()
		rank_hand = []
		for c in hand:
			rank_hand.append(c.getRank())
		return flagCardRank in rank_hand

	def countRelevantCards(self, rank):
		hand = self.getHand()
		counter = 0
		for c in hand:
			if rank == c.getRank():
				counter += 1
		return counter

	def giveRelevantCards(self, rank, count):
		# Giving cards means finding the cards of the specific rank
		# 	in the hand, taking them out of the hand, and then presenting
		# 	them to the player to take.
		giveArray = [0 for i in range(count)]
		gArrayIndex = 0

		hand = self.getHand()

		for i in range(len(hand)):
			c = hand[i]
			if c.getRank() == rank:
				# Appending it to the array of cards you're going to give
				giveArray[gArrayIndex] = c
				gArrayIndex += 1
				# Removing it from the player's hand
				self.removeCard(c)

		# Check at the end. If there is a zero in giveArray something is wrong
		if 0 in giveArray:
			raise Exception("There is something wrong with either the count\
							or with how the giveArray is being filled up.")

		return giveArray

	def removeCard(self, card):
		self.hand.remove(card)

	# End TRADING PHASE operation code