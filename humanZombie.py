import random

#created in anticipation of creating players with different stats
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
	

player = human(3,3,3,3)
zombie = enemy(3,1,3)

level = [zombie]

print('#############################')
print('ENEMY TURN')

for enemies in level:
	roll = die_roll(6)
	print(roll)
	
	if (roll > player.defence):
		print("the zombie successfully attacks!")
		player.health -= zombie.attack
	else:
		print("you fight the zombie off")
		player.defence -= zombie.attack
	
print("player's health = " + str(player.health))
print("player's defence is = " + str(player.defence))

print("##############################")
print('PLAYER TURN')

for turns in range(0, player.speed):
	roll = die_roll(6)
	print(roll)
	
	if (roll > zombie.defence):
		print("you successfully attack the zombie!")
		zombie.health -= player.attack
	else:
		print("you miss the zombie")
		zombie.defence -= player.attack
	
print("zombie's health = " + str(zombie.health))
print("zombie's defence is = " + str(zombie.defence))
