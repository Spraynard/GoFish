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

from Modules.Cards.Card import Card
from Modules.Cards.Deck import Deck
from Modules.Players.Player import Player
from Modules.Players.Bot import Bot
from Modules.Engine import Engine

Deck = Deck()
Player = Player()
Bot = Bot()
Engine = Engine([Player, Bot], Deck)

def initializeGoFish():
	Engine.initialize()

if __name__ == "__main__":
	initializeGoFish()