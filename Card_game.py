import random
class Player():
	def __init__(self, name = None):
		if name != None:
			self.name = name
		else:
			pass
		self.hand = []
	def changeName(self, name):
		self.name = name

class Deck():
	def __init__(self):
		self.deck = []
	def createDeck(self):
		suites = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
		values = [ 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
		for suite in suites:
        
			for value in values:
            
				if value not in self.deck:
                
					self.deck.append(suite + ':' + value)

	def shuffleDeck(self):
        
		return random.shuffle(self.deck)

class Game():

	currentPlayers = []
	numOfPlayers = 0

	def __init__(self, name, gameType):
		
		self.name = name
		self.gameType = gameType

	def addPlayers(self,num):
		for x in range(num):
			Game.numOfPlayers += 1
			self.currentPlayers.append(Player('Player: {}'.format(str(Game.numOfPlayers))))


	def showPlayers(self):
		for x in self.currentPlayers:
			print('{} has a hand of:'.format(x.name) + str(x.hand) + "\n")

class Poker(Game):
	max_hand_size = 5
	numOfDeck = 0

	def addDeck(self):
		poker.deck = Deck()

	def drawCards(self, name):
		num = len(self.deck.deck)-1
		randNum = random.randint(1, num)
		for x in self.currentPlayers:
			if name == x.name:
				if len(x.hand) < self.max_hand_size:
					x.hand.insert(len(x.hand), self.deck.deck.pop(randNum))
				else:
					print('Hand is Full')
			else:
				pass
