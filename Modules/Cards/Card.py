def cardRankToNum(rank):
	if rank == "Ace":
		return 14
	elif rank == "King":
		return 13
	elif rank == "Queen":
		return 12
	elif rank == "Jack":
		return 11
	else:
		return int(rank)

def cardSuitRank(suit):
	if suit == "Diamonds":
		return 0
	elif suit == "Hearts":
		return 1
	elif suit == "Clubs":
		return 2
	elif suit == "Spades":
		return 3

class Card:
	""" Card class, which gives all the behavior of the card object. Takes in a value (e.g. 1 - Ace) and a 
		suit (e.g. "Spades", "Clubs") and makes a card object off of that with those values
		
	"""

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __eq__(self, other):
		return (self.value == other.value) and (self.suit == other.suit)

	def __lt__(self, other):
		c1 = cardSuitRank(self.suit), cardRankToNum(self.value)
		c2 = cardSuitRank(other.suit), cardRankToNum(other.value)
		return c1 < c2

	def __gt__(self, other):
		c1 = cardSuitRank(self.suit), cardRankToNum(self.value)
		c2 = cardSuitRank(other.suit), cardRankToNum(other.value)
		return c1 > c2

	def __repr__(self):
		return "Card(" + str(self.value) + ", " + str(self.suit) + ")"

	def __str__(self):
		return self.value + " of " + self.suit

	def getValue(self):
		return self.value

	def getSuit(self):
		return self.suit

	def cardJs(self):
		cardValue = {
			"value" : self.value,
			"suit" : self.suit
		}
		return cardValue