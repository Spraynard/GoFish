import sys

sys.path.append('../')
sys.path.append('../../Cards')
sys.path.append('../../Players')

from Engine import *

from HumanPlayer import HumanPlayer
from Bot import Bot

class GoFishEngine(Engine):
	def __init__(self, test = False):
		super(GoFishEngine, self).__init__()

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

	def displayHand(self, player):
		print player.showHand()

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
			player.setChosenPlayer(random.choice(choiceList))
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

		player.setChosenPlayer(choiceList[choice])

	def chooseCard(self, player):
		from Cards.Card import Card

		if isinstance(player, Bot):
			# Implement Bot Card Choosing. Game will not work without this. What I eventually want to to is
				#  1. Bot looks through hand for cards they have
				#  2. Of cards that bot has, look for the rank in which you have the most of.
				#  2a. If you have multiple ranks with the same amount, break by choosing randomly
				#  3. As for the selected rank from an opponent.
				pass
		else:
			rank = False
			# suit = False

			if not self.variant:
				while True:
					rank = str(raw_input("What card rank do you want to ask for (e.g. 2 - Ace)?: ")).lower().title()
					flagCard = Card(rank)
					if not testCard.acceptableRank():
						print "That is not an acceptable card rank. Please choose again"
					elif not player.hasCard(flagCard):
						print "You don't even have any of those cards in your hand! Try again."
					else:
						player.setChosenCard(Card(rank))
			# if self.variant == 1:
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

		print "\"Hey %s, Do you have any %ss?\"" % (chosenPlayer, chosenCard.getRank())
		if chosenPlayer.hasCard(chosenCard):
			# Count how many cards there are of that cardRank in the player's hand
			# 	give feedback based on the amount of cards.
			player.guessedCorrectly()

			chosenPlayerCardCount = chosenPlayer.countRelevantCards(chosenCard)
			chosenPlayerGiveArray = chosenPlayer.giveRelevantCards(chosenCard, chosenPlayerCardCount)
			
			if isinstance(chosenPlayer, Bot):
				print chosenPlayer.exclaim() % (chosenPlayerCardCount, chosenPlayerGiveArray)
			else:
				print "I do have %s cards. Here they are: %s" % (chosenPlayerCardCount, chosenPlayerGiveArray)

			player.takeRelevantCards(chosenPlayerGiveArray)

		else:
			if isinstance(chosenPlayer, Bot):
				# If the other player is a bot, they will taunt the shit out of you
				# 	and probably make you really sad af.
				print chosenPlayer.tauntPlayer()
			else:
				print "\"I sure do not %s\"" % player

	def resethand(self, player):
		# Player will sort their hand. This bunches up the similar ranked cards with
		# 	each other, for good visibility.
		pass
		player.sortHand()

	def scanHand(self, player):
		# Player finds groups of four within their hand.
		pass

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
			player.drawSingleCard(deck)

		player.resetChosenVariables()

	def endPhase(self, player):
		if player.gotGuess():
			# If the player has a good guess (e.g. they asked another player for a card that they
			# 	had in their hand and they actually had one or more of those cards in their hand)

			# Resetting the player's guess for next turn :)
			player.resetGuess()
			self.takeTurn(player)
		else:
			# If the player had to draw from the pile because they guessed badly.
			self.resethand(player)
			self.scanHand(player)
			# self.setTricks(player:

	# End Game Phases

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
		self.decisionPhase(player)
		self.tradingPhase(player)
		self.endPhase(player)