import random

from Card import Card

class Deck:
	""" The deck object which holds all the cards the players will be using"""

	def __init__(self):

		self.deck = []

		cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		suits = ["Clubs", "Spades", "Diamonds", "Hearts"]

		for s in suits:
			for c in cards:
				self.deck.append(Card(c,s))

		random.shuffle(self.deck)

	def __repr__(self):
		return self.deck

	def currentAmount(self):
		return len(self.deck)

	def listCards(self):

		for i in range(0, len(self.deck)):
			print self.deck[i]

	def hasCard(self, card):

		if card in self.deck:
			return True
		return False