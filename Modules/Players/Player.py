class Player:
	"""Player object, All the commands that the player will use in the game are here."""
	def __init__(self, name = False):
		self.hand = False
		self.name = name

	def __eq__(self, other):
		return self.name == other.name

	def __repr__(self):
		return str(self.name) or "Player"

	def __str__(self):
		if type(self.name) == int:
			return "Player #%s" % self.name
		return "'%s'" % self.name or "Player"
		
	def sortHand(self):
		for i in range(1, len(self.hand)):
			temp = self.hand[i]
			j = i
			while j > 0 and self.hand[j-1] > temp:
				self.hand[j] = self.hand[j-1]
				self.hand[j-1] = temp
				j -= 1

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

	def hasCard(self, card):
		return card in self.hand

	def giveCard(self, card):
		# Command used to give a card to another player
		if not (card in self.hand):
			raise Exception("You don't have that card, something's up.")
		else:
			for c in self.hand:
				if c == card:
					return c

	def takeCard(self, card):
		self.cards.append(card)

	def removeCard(self, card):
		self.cards.remove(card)