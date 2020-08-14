class Game():
	name = ''
	game_type = ''
	current_players = {}

	def __init__(self, name, game_type):
		
		self.name = name
		self.game_type = game_type

	def add_players(self, player):
		self.current_players[player] = player.hand
		
class Player():
	name = ''
	hand = []
	def __init__(self, name):
		self.name = name

class Poker(Game):
	max_hand_size = 5






