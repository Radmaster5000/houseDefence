#created in anticipation of creating players with different stats
import random

class human:
	
	def __init__(self, health, attack, defence, speed):
		self.health = health
		self.attack = attack
		self.defence = defence
		self.speed = speed
	
class enemy:
	
	def __init__(self, health, attack, defence, uid):
		self.health = health
		self.attack = attack
		self.defence = defence
		self.uid = uid

def die_roll(n):
	return random.randint(0, n)

def printy(text, textFile):
	print(text)
	print(text, file=textFile)

def round(roundNum, playerObj, textFile):
	level = roundNum
	player = playerObj
	f = textFile
	enemyArray = spawn_zombies(level)
	printy('ROUND NUMBER ' + str(level), f)
	printy('NUMBER OF ENEMIES ' + str(len(enemyArray)), f)

	printy('#############################',f)
	printy('ENEMY TURN',f)


	for enemy in enemyArray:
		roll = die_roll(6)
		printy("The enemy roles an attack: " + str(roll),f)
	
		if (roll > player.defence):
			printy("the zombie successfully attacks!",f)
			player.health -= enemy.attack
		else:
			printy("you fight the zombie off",f)
			player.defence -= enemy.attack
	
	printy("player's health = " + str(player.health),f)
	printy("player's defence is = " + str(player.defence),f)
	for enemy in enemyArray:
		printy(str(enemy.uid) + "'s health = " + str(enemy.health),f)

	printy("##############################",f)
	printy('PLAYER TURN',f)

	# Initialise target outside of attack loop
	# This identifies the target in the enemyArray
	target = 0

	for turns in range(0, player.speed):
		
		if (len(enemyArray) == 0):
			# THIS NEEDS CHANGING. WILL REPEAT FOR PLAYER'S SPEED EVEN IF ARRAY IS EMPTY
			print("Congrats! You killed all the zombies")
		else:	
		
			# It the target variable reaches the end of the array, reset it
			if (target >= len(enemyArray)):
				target = 0
	
			roll = die_roll(6)
			printy("The player rolled a: " + str(roll),f)
	
			if (roll > enemyArray[target].defence):
				printy("you successfully attack " + enemyArray[target].uid,f)
				enemyArray[target].health -= player.attack
				if (enemyArray[target].health <= 0):
					printy("You killed " + enemyArray[target].uid,f)
					enemyArray.pop(target)
					target -= 1
			else:
				printy("you miss the zombie",f)
				enemyArray[target].defence -= player.attack

		# Increment variable to target the next enemy in the array
		target += 1
	for enemy in enemyArray:	
		printy(enemy.uid + "'s health = " + str(enemy.health),f)
		printy(enemy.uid + "'s defence is = " + str(enemy.defence),f)

	return player

def spawn_zombies(number_of_enemies):
	array_of_zombies = []
	for i in range(number_of_enemies):
		uid = 'zombie'+str(i)
		zombie = enemy(3,1,3, uid)
		array_of_zombies.append(zombie)
	return array_of_zombies