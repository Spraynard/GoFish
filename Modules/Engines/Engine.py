import sys

sys.path.append('../../Modules/Cards/')
sys.path.append('../../Modules/Players/')

from Deck import Deck
from Card import Card

class Engine(object):
	# Controls the start, turn, and checks of the actual game.
	def __init__(self, test = False):
		self.players = None
		self.deck = None
		self.playerIndex = 0
		self.variant = None
		self.test = test

# All Engines will have this obtaining and setting deck functionality
	def getDeck(self):
		# Summary: Gives the deck object out.
		# Returns: `self.deck` - Deck Object
		return self.deck

	def setDeck(self):
		# Summary: Sets
		# Input: `new_deck` - The new value of the deck object I want to set to
		# Returns: Void
		self.deck = Deck()
		self.getDeck().initialize()

# All Engines will handle getting and setting current players with this functionality
	def getPlayers(self):
		return self.players

	def setPlayers(self, players):
		self.players = players


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

# All Engines will have a game loop. Unsure if it will be set this way throughout
	def gameLoop(self):
		# Will stop when there is a player that has gotten the winning conditions of the game
		while not self.gameOver():
			# Getting the current player for the turn
			current_player = self.getCurrentPlayer()
			self.takeTurn(current_player)

# All Engines will have a game that will end :)
	def gameOver(self):
		pass

# All Engines, at end game, will congratulate players
	def congratulations(self, player):
		print "Congratulations %s, you have won the game!" % player


	def gameStart(self):
		self.dealHands()
		self.gameLoop()
		self.endGame()

	def initialize(self):
		self.setDeck()
		self.gameStart()