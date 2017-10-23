import sys

sys.path.append('../')
sys.path.append('../../Cards')
sys.path.append('../../Players')

from Engine import *

from HumanPlayer import HumanPlayer
from Bot import Bot

class GoFishEngine(Engine):
	def __init__(self):
		super(GoFishEngine, self).__init__()
		self.trickCount = 0

	# Game Action Functionality
	def getMasterTrickCount(self):
		return self.trickCount

	def displayHand(self, player):
		print player.showHand()

	def displayCurrentPlayerInfo(self, player):
		if isinstance(player, Bot):
			# No need to display if 
			# 	the player is a bot
			return
		player.displayTricks()
		player.displayHand()

	def playerAskLoop(self, choiceListLength):
		choice = None
		while True:
			choice = int(raw_input("Please enter your choice: ")) - 1
			if (choice < 0) or (choice >= choiceListLength):
				print "\nError: That is not one of the player choices"
			else:
				break
		return choice

	def choosePlayerToAsk(self, player):
		choiceList = list(self.getPlayers())
		choiceList.remove(player)
		choice = False

		if isinstance(player, Bot):
			import random
			# Implement Bot() player to ask
			player.setChosenPlayer(random.choice(choiceList))
		else:
			# Implement Player() player to ask
			print "Which player will you ask a card from?"
			for i in range(len(choiceList)):
				print "#%s: %s" % ((i + 1), choiceList[i])
			choice = self.playerAskLoop(len(choiceList))

		player.setChosenPlayer(choiceList[choice])

	def chooseCard(self, player):
		from Card import Card

		if isinstance(player, Bot):
			# Implement Bot Card Choosing. Game will not work without this. What I eventually want to to is
				#  1. Bot looks through hand for cards they have
				#  2. Of cards that bot has, look for the rank in which you have the most of.
				#  2a. If you have multiple ranks with the same amount, break by choosing randomly
				#  3. As for the selected rank from an opponent.
				player.chooseCard()
		else:
			rank = None

			if not self.variant:
				while True:
					rank = raw_input("What card rank do you want to ask for (e.g. 2 - Ace)?: ").lower().title()
					flagCard = Card(rank)
					if not flagCard.acceptableRank():
						print "\nError: That is not an acceptable card rank. Please choose again."
					elif not player.hasCard(flagCard):
						print "\nError: You don't even have any of those cards in your hand! Try again."
					else:
						player.setChosenCard(Card(rank))
						break
			# if self.variant == 1:
			# 	suit = None
			# 	while True:
			# 		suit = str(raw_input("What card suit do you want to ask for (e.g. 'Clubs', 'Spades')?: ")).lower().title()
			# 		if not suit in correctInputDict['suits']:
			# 			print "That is not an acceptable card suit. Please choose again"
			# 		else:
			# 			break

	def askForCardRank(self, player):
		chosenPlayerCardCount = False
		chosenPlayerGiveArray = False

		chosenPlayer = player.getChosenPlayer()
		chosenCard = player.getChosenCard()

		player.talk('ask')

		if chosenPlayer.hasCard(chosenCard):
			# Count how many cards there are of that cardRank in the player's hand
			# 	give feedback based on the amount of cards.
			player.guessedCorrectly()
			chosenPlayer.concedeDefeat(chosenCard)
			if isinstance(chosenPlayer, Bot):
				chosenPlayer.talk('exclaim')
			else:
				chosenPlayer.talk('defeat')
			chosenPlayer.giveToPlayer(player)
		else:
			if isinstance(chosenPlayer, Bot):
				# If the other player is a bot, they will taunt the shit out of you
				# 	and probably make you really sad af.
				print chosenPlayer.tauntPlayer()
			else:
				chosenPlayer.talk('victory')
				
	def setTricks(self, player):
		# Based on what was scanned, the player will take out the tricks within
		# 	their hand and add it to their total trick count!
		pass

	# End Game Action Functionality

	# Player Handling Functionality
	def listPlayersHands(self):
		players = self.getPlayers()

		for p in players:
			# print p + ': ' + p.showHand()
			print "%s: %s" % (p, p.showHand())
	# End Player Handling Functionality

	def dealHands(self):
		deck = self.getDeck()
		players = self.getPlayers()

		for p in players:
			p.drawHand(deck)
	# Phases Coded Here

	# Game Phases Here
	def initialPhase(self, player):
		self.displayCurrentPlayerInfo(player)

	def decisionPhase(self, player):
		self.choosePlayerToAsk(player)
		self.chooseCard(player)

	def tradingPhase(self, player):		
		self.askForCardRank(player)
		# Player state is valuable after they ask for card.
		if not player.gotGuess():
			deck = self.getDeck()
			player.drawCard(deck)

		player.resetChosenVariables()

	def winConditionsMet(self):
		return self.getMasterTrickCount() == 13

	def endPhase(self, player):
		if player.gotGuess():
			# If the player has a good guess (e.g. they asked another player for a card that they
			# 	had in their hand and they actually had one or more of those cards in their hand)

			# Resetting the player's guess for next turn :)
			player.resetGuess()
		else:
			# If the player had to draw from the pile because they guessed badly.
			
			# Eh this is weird.
			# Not sorted any time before?
			player.sortHand()

			player.lookForTricks()
			player.setTricks(self.getMasterTrickCount())

			self.addPlayerIndex()

		if self.winConditionsMet():
			self.toggleGameOver()
		else:
			self.takeTurn()


	# End Game Phases

	def takeTurn(self):
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
		player = self.getCurrentPlayer()

		self.initialPhase(player)
		self.decisionPhase(player)
		self.tradingPhase(player)
		self.endPhase(player)