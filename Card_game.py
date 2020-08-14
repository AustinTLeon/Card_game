class Player():
	def __init__(self):
		name = ''
		hand = []
	def changeName(self, name):
	"""This method allows you to change the name of select player"""
		self.name = name

class Game():

	currentPlayers = [Player()]
	numOfPlayers = 0

	def __init__(self, name, gameType):
		
		self.name = name
		self.gameType = gameType

	def addPlayers(self, num):
	"""This adds a given num of players and adds 1 to the total num of player for the game"""	
		for x in range(num):
			Game.numOfPlayers += 1
			self.currentPlayers.append('Player: {}'.format(str(Game.numOfPlayers)))


	def showPlayers(self):
	"""Prints all the players in game"""
		print(self.currentPlayers)

class Poker(Game):
	max_hand_size = 5
