class Player(object):
	"""Player object, All the commands that the player will use in the game are here."""
	def __init__(self, name = False):
		self.hand = False
		self.name = name
		self.tricks = False

	def __eq__(self, other):
		return self.name == other.name

	def __repr__(self):
		return str(self.name) or "Player"

	def __str__(self):
		if type(self.name) == int:
			return "Player #%s" % self.name
		return "'%s'" % self.name or "Player"
	
	# Trick functionality
	def addTrick(self):
		self.tricks += 1

	def getTricks(self):
		return self.tricks

	def hasTricks(self):
		return not (self.getTricks == False)

	# End Trick Functionality
	
	def sortHand(self):
		for i in range(1, len(self.hand)):
			temp = self.hand[i]
			j = i
			while j > 0 and self.hand[j-1] > temp:
				self.hand[j] = self.hand[j-1]
				self.hand[j-1] = temp
				j -= 1

	def getHand(self):
		return self.hand

	def hasHand(self):
		if (self.hand):
			return True
		return False

	def insertHand(self, hand):
		if not self.hasHand():
			self.hand = hand
		else:
			raise Exception("This player already has a hand!!!")

	def showHand(self):
		return self.hand

# Code for player specific TRADING PHASE operations

	def hasCardRank(self, rank):
		# Non variant version of hasCard.
		# This version just plain checks to see if the player has
		# 	any cards of given rank in their hands.
		hand = self.getHand()
		rank_hand = []
		for c in hand:
			rank_hand.append(c.getRank())
		return rank in rank_hand

	def countCardRank(self, rank):
		hand = self.getHand()
		counter = 0
		for c in hand:
			if rank == c.getRank():
				counter += 1
		return counter

	def giveCards(self, rank, count):
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

	def takeCard(self, card):
		self.hand.append(card)

	def takeCards(self, cardArray):
		for c in cardArray:
			self.takeCard(c)

	def removeCard(self, card):
		self.hand.remove(card)

# End TRADING PHASE operation code