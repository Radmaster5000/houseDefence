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

def spawn_zombies(number_of_enemies):
	array_of_zombies = []
	for i in range(number_of_enemies):
		zombie = enemy(3,1,3)
		array_of_zombies.append(zombie)
	return array_of_zombies
	

player = human(3,3,3,3)

level = 3

enemyArray = spawn_zombies(level)

print('#############################')
print('ENEMY TURN')

for enemy in enemyArray:
	print(enemy)

for enemy in enemyArray:
	roll = die_roll(6)
	print(roll)
	
	if (roll > player.defence):
		print("the zombie successfully attacks!")
		player.health -= enemy.attack
	else:
		print("you fight the zombie off")
		player.defence -= enemy.attack
	
print("player's health = " + str(player.health))
print("player's defence is = " + str(player.defence))
for enemy in enemyArray:
	print("zombie health = " + str(enemy.health))

print("##############################")
print('PLAYER TURN')

for turns in range(0, player.speed):
	roll = die_roll(6)
	print(roll)
	
	if (roll > enemyArray[0].defence):
		print("you successfully attack the zombie!")
		enemyArray[0].health -= player.attack
		if (enemyArray[0].health <= 0):
			print("You killed the zombie")
			enemyArray.pop(0)
	else:
		print("you miss the zombie")
		enemyArray[0].defence -= player.attack

for enemy in enemyArray:	
	print("zombie's health = " + str(enemy.health))
	print("zombie's defence is = " + str(enemy.defence))
