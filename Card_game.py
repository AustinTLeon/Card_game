class Game():
	name = ''
	game_type = ''
	current_players = {}

	def __init__(self, name, game_type):
		
		self.name = name
		self.game_type = game_type

	def add_players(self, player):
		self.current_players[player] = player.hand

	def show_current_players(self):
		for name, hand in self.current_players.items():
			return '{} is in the game.'.format(name)

class Player():
	name = ''
	hand = []
	def __init__(self, name):
		self.name = name

class Poker(Game):
	max_hand_size = 5

josh = Player('josh')

poker = Poker('Poker','Cards')

poker.add_players(josh)

poker.show_current_players




