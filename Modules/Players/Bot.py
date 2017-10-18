from HumanPlayer import HumanPlayer

class Bot(HumanPlayer):
	"""Bot object, which is a player. There are taunts available to bots to rouse up the player whenver they make a mistake"""
	def __init__(self, name = False):
		super(Bot, self).__init__()
		self.taunts = ["You're going to have to try harder than that!\"",
						"I thought that I was playing a real person, not a bot!\"",
						"What the heck are you doing?\"",
						"Dang, I didn't know I was playing a baby tonight\""]
		
		self.rejections = ["\"No", "\"Nope", "\"I sure do not", "\"Hahaha, no", "\"You wish!"]
		
		self.exclamations = ["\"Dammit, I have %s cards of that rank. Here's your damn cards: %s\"",
							 "\"Wow, you're really good at this! I have %s cards of that rank. Here they are you scallywag: %s\"",
							 "\"Are you cheating? I have %s cards of that rank. Take em ya dingus! %s\""]

	def __repr__(self):
		return self.name or "Bot"

	def tauntPlayer(self):
		import random
		return random.choice(self.rejections) + random.choice(self.taunts)
	
	def exclaim(self):
		import random
		return random.choice(self.exclamations)

	def raiseNeededCard(self):
		if not self.hasHand():
			raise Exception("This bot doesn't have a hand!")
