import sys

sys.path.append('../Cards/')
class Engine:
	# Controls the start, turn, and checks of the actual game.
	def __init__(self):
		self.players = False
		self.deck = False
		self.playerIndex = 0
		self.variant = False

# All Engines will have this obtaining and setting deck functionality
	def getDeck(self):
		# Summary: Gives the deck object out.
		# Returns: `self.deck` - Deck Object
		return self.deck

	def setDeck(self):
		# Summary: Sets
		# Input: `new_deck` - The new value of the deck object I want to set to
		# Returns: Void
		from Cards.Deck import Deck
		self.deck = Deck()

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