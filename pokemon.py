import moves

class Pokemon(object):
	
	#Set the pokemon's name at the inicialization
	def __init__(self, name, level, type1, type2, hp, attack, defense, special, speed):
		self.name = name
		self.level = level
		self.type1 = type1
		self.type2 = type2
		
		#Set status on constructor
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.special = special
		self.speed = speed
		
#	#Set the pokemon's status
#	def status(self, hp, attack, defense, special, speed):
#		self.hp = hp
#		self.attack = attack
#		self.defense = defense
#		self.special = special
#		self.speed = speed
		
	#Set the pokemon's moves, moves are objects of Moves type for a better organization
	def moves(self, name1, name2, name3, name4):
		self.move1 = moves.Moves(name1)
		self.move2 = moves.Moves(name2)
		self.move3 = moves.Moves(name3)
		self.move4 = moves.Moves(name4)