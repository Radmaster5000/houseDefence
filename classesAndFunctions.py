#created in anticipation of creating players with different stats
import random

class human:
	
	def __init__(self, health, attack, defence, speed):
		self.health = health
		self.attack = attack
		self.defence = defence
		self.speed = speed
	
	
class enemy:
	
	def __init__(self, health, attack, defence):
		self.health = health
		self.attack = attack
		self.defence = defence

def die_roll(n):
	return random.randint(0, n)


def spawn_zombies(number_of_enemies):
	array_of_zombies = []
	for i in range(number_of_enemies):
		zombie = enemy(3,1,3)
		array_of_zombies.append(zombie)
	return array_of_zombies
	