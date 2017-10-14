from Player import Player

class Bot(Player):
	"""Bot object, which is a player. There are taunts available to bots to rouse up the player whenver they make a mistake"""
	def __init__(self):
		self.taunts = ["You're going to have to try harder than that!",
						"I thought that I was playing a real person, not a bot!",
						"What the heck are you doing?",
						"Dang, I didn't know I was playing a baby tonight"]
		self.name = False
		self.hand = False

	def __repr__(self):
		return self.name or "Bot"