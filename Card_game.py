class Player():
	def __init__(self):
		name = ''
		hand = []
	def changeName(self, name):
		self.name = name

class Game():

	currentPlayers = [Player()]
	numOfPlayers = 0

	def __init__(self, name, gameType):
		
		self.name = name
		self.gameType = gameType

	def addPlayers(self):
		Game.numOfPlayers += 1
		self.currentPlayers.append('Player: {}'.format(str(Game.numOfPlayers)))


	def showPlayers(self):
		print(self.currentPlayers)

class Poker(Game):
	max_hand_size = 5
