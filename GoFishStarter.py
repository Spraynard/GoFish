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
from random import shuffle as shuffle

from Modules.Cards.Card import Card
from Modules.Cards.Deck import Deck
from Modules.Players.Player import Player
from Modules.Players.Bot import Bot
from Modules.Engine import Engine

class GoFishStarter:
	def __init__(self):
		self.deck = Deck().initialize()
		self.players = []
		self.engine = Engine()

	# Code for addition of players and general player code
	def getPlayers(self):
		return self.players

	def getPlayerN(self):
		return len(self.getPlayers)

	def addPlayer(self, player):
		self.players.append(player)

	def addPlayers(self, player_n, bot_n):
		player_bucket = []
		player_obj = Player()
		bot_obj = Bot()

		player_names = False

		for i in range(player_n):
			player_bucket.append(player_obj)

		for i in range(bot_n):
			player_bucket.append(bot_obj)

		shuffle(player_bucket)

		for p in player_bucket:
			self.addPlayer(p)

# Question: How is this function supposed to know
# 			how many players there are if players
# 			and bots get added at the same time?!

	def askBotN(self):
		bot_n = False
		# The number to fill up the card table
		tot_bots = 4 - self.getPlayerN
		if tot_bots == 0:
			return False
		if tot_bots < 2:
			return tot_bots

		while True:
			try:
				t_bot_n = int(raw_input("Please enter the number of bots: "))
			except:
				print "Nope, need to enter a number between 1 and %s" % tot_bots
				continue
			if not t_bot_n:
				bot_n = 1
				break
			else
				if t_bot_n > tot_bots:
					print "You can't have more than %s bots right now" % tot_bots
				else:
					# Limiting to one bot
					bot_n = 1
					break
		return bot_n

	def askPlayerN(self):
		player_n = False
		
		while True:
			try:
				t_player_n = int(raw_input("Please enter the number of human players: "))
			except:
				print "Nope need to enter a # between 1 and 4"
				continue
			if not t_player_n:
				player_n = 1
				break
			else:
				if t_player_n > 4:
					print "You can't have more than four players"
				else:
					# Limiting the amount of players to 1 right now
					player_n = 1
					# player_n = t_player_n
					break
		return player_n

	# End Code for Addition of Players
	def initializeGoFish(self):
		print "Welcome to another round of the famous game, Go Fish!"
		player_n = self.askPlayerN()
		bot_n = self.askBotN()
		# After asking, add the players to `self.players`
		self.addPlayers(player_n, bot_n)

if __name__ == "__main__":
	GoFishStarter().initializeGoFish()