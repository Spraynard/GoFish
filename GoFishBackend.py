#The Following code is a GoFish backend
#Rules:
# * Use 1 Deck of 52 Cards
# * Players are dealt seven random cards
# * Remaining cards make up the pool for users to Go Fish from
# * A turn consists of the current player selecting a card from their hand, and asking an opponent if they have any cards of the same rank
# * If the opponent has a card(s) of that rank, the opponent must give the card(s) to the player who requested it and that player gets another turn
# * If the opponent does not have any cards of that rank, the requesting player must Go Fish and draw a random card from the pool; ending that player's turn
# * As soon as a player collects a book of four cards of the same rank (ex. four Jacks or four 3s), they must lay their book down; removing the cards from their hand
# * If a player has no cards in their hand, they must draw from the pool; if the pool is empty, that player is out of the game
# * The game is over when all 13 sets of four, books, have been matched
# * The player with the most books is determined the winner

import random
import pico

class Player(object):
	"""PLayer object, All the commands that the player will use in the game are here."""
	def __init__(self, hand):
		self.hand = hand

	def sortHand(self):
		for i in range(1, len(self.hand)):
			temp = self.hand[i]
			j = i
			while j > 0 and self.hand[j-1] > temp:
				self.hand[j] = self.hand[j-1]
				self.hand[j-1] = temp
				j -= 1

	def showHand(self):
		return self.hand

	def hasCard(self, card):
		return card in self.hand

	def giveCard(self, card):
		# Command used to give a card to another player
		if not (card in self.hand):
			return "You don't have that card, something's up."
		else:
			for c in self.hand:
				if c == card:
					return c

	def takeCard(self, card):
		self.cards.append(card)

	def removeCard(self, card):
		self.cards.remove(card)

	def handJSON(self):
		jsonHand = []

		for c in self.hand:
			jsonHand.append(c.cardJs())

		return jsonHand

class Bot(Player):
	"""Bot object, which is a player. There are taunts available to bots to rouse up the player whenver they make a mistake"""
	def __init__(self, hand):
		self.hand = hand
		self.taunts = ["You're going to have to try harder than that!",
						"I thought that I was playing a real person, not a bot!",
						"What the heck are you doing?",
						"Dang, I didn't know I was playing a baby tonight"]

class Deck(pico.Pico):
	""" The deck object which holds all the cards the players will be using"""

	def __init__(self):

		self.deck = []

		cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		suits = ["Clubs", "Spades", "Diamonds", "Hearts"]

		for s in suits:
			for c in cards:
				self.deck.append(Card(c,s))

		random.shuffle(self.deck)

	def currentAmount(self):
		return len(self.deck)

	def listCards(self):

		for i in range(0, len(self.deck)):
			print self.deck[i]

	def hasCard(self, card):

		if card in self.deck:
			return True
		return False

	def dealHand(self):
		hand = []

		for i in range(7):
			drawnCard = self.deck.pop()
			hand.append(drawnCard)

		return hand

	def giveJSON(self):
		jsonArray = []

		for c in self.deck:
			jsonArray.append(c.cardJs())

		return jsonArray

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

class Card(object):
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

def getDeck():
	return Deck().giveJSON()

deck = Deck().giveJSON()
print deck