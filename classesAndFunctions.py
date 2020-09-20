#created in anticipation of creating players with different stats
import random

class building:
	def __init__(self, health, attack, defence):
		self.health = health
		self.attack = attack
		self.defence = defence

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

def endScene(levelValue, textFile):
	level = levelValue - 1
	f = textFile
	printy("Game Over.", f)
	printy("You survived " + str(level) + " rounds",f)
	printy("Thank you for playing.", f)
	quit()

def enemyStats(enemyArray, textFile):
	enemyArray = enemyArray
	f = textFile

	printy("", f)
	printy('######################################',f)
	printy('             ENEMY TURN',f)
	printy("######################################", f)
	printy("#            ENEMY STATS             #", f)
	printy("#------------------------------------#", f)
	printy("# NUMBER OF ENEMIES: "+str(len(enemyArray))+"               #", f)
	printy("######################################", f)


def houseStats(safehouseObj, textFile):
	safehouse = safehouseObj
	f = textFile

	printy("######################################", f)
	printy("#        SAFEHOUSE STATS             #", f)
	printy("#------------------------------------#", f)
	printy("#   HEALTH  |   ATTACK  |   DEFENCE  #", f)
	printy("#     "+str(safehouse.health)+"     |      "+str(safehouse.attack)+"    |     "+str(safehouse.defence)+"      #",f)
	printy("######################################", f)


def playerStats(playerObj, textFile):
	player = playerObj
	f = textFile


	printy("######################################", f)
	printy("#           PLAYER STATS             #", f)
	printy("#------------------------------------#", f)
	printy("# HEALTH | ATTACK | DEFENCE | SPEED  #", f)
	printy("#   "+str(player.health)+"    |    "+str(player.attack)+"   |   "+str(player.defence)+"     |   "+str(player.speed)+"    #",f)
	printy("######################################", f)


def printy(text, textFile):
	print(text)
	print(text, file=textFile)

def round(roundNum, safehouseObj, playerObj, oldEnemyArray, pointsValue, textFile):
	level = roundNum
	safehouse = safehouseObj
	player = playerObj
	oldEnemyArray = oldEnemyArray
	points = pointsValue
	f = textFile
	
	# create the enemies for this round and add any surviving enemies from the last round
	enemyArray = spawn_zombies(level)
	for enemy in oldEnemyArray:
		enemyArray.append(enemy)

	printy('ROUND NUMBER ' + str(level), f)
	printy('NUMBER OF ENEMIES ' + str(len(enemyArray)), f)
	printy('POINTS ' + str(points), f)

	printy("######################################",f)
	printy('             PLAYER TURN',f)
	playerStats(player, f)
	

	# Initialise target outside of attack loop
	# This identifies the target in the enemyArray
	target = 0

	for turns in range(0, player.speed):
		
		
		# It the target variable reaches the end of the array, reset it
		if (target >= len(enemyArray)):
			target = 0
	
		roll = die_roll(6)
		printy("", f)
		printy("The player rolled a: " + str(roll),f)

		# if the player rolls higher than the enemy's defence, they attack
		if (roll > enemyArray[target].defence):
			printy("you successfully attack " + enemyArray[target].uid,f)
			enemyArray[target].health -= player.attack
			if (enemyArray[target].health <= 0):
				printy("You killed " + enemyArray[target].uid,f)
				points += 1
				enemyArray.pop(target)
				if (len(enemyArray) == 0):
					printy("Congrats! You killed all the zombies", f)
					break
				target -= 1
	
		# if the player rolls lower than the enemy's defence, the attack deplete's the enemy's defence stat
		else:
			printy("you miss the zombie",f)
			enemyArray[target].defence -= player.attack
	
	enemyStats(enemyArray, f)
	
	# Increment variable to target the next enemy in the array
	target += 1
	for enemy in enemyArray:	
		printy(enemy.uid + "'s health = " + str(enemy.health),f)
		printy(enemy.uid + "'s defence is = " + str(enemy.defence),f)


	if (len(enemyArray) == 0):
		printy("There are no zombies left to attack you.", f)
	else:	
		for enemy in enemyArray:
			roll = die_roll(6)
			printy("The enemy roles an attack: " + str(roll),f)
			if (safehouse.health >0):
				# zombie attacks the safehouse
				if (roll > safehouse.defence):
					printy("the zombie successfully attacks the safehouse!",f)
					safehouse.health -= enemy.attack
					if (safehouse.health <= 0):
						printy("Your safehouse is compromised. The zombies are getting in!",f)
				else:
					printy("The house's defences fight off the zombie",f)
					safehouse.defence -= enemy.attack
			else:
				if (roll > player.defence):
					printy("the zombie successfully attacks you!",f)
					player.health -= enemy.attack
					if (player.health <= 0):
						printy("The zombie kills you. You're dead, son!", f)
						endScene(level, f)
				else:
					printy("you fight the zombie off",f)
					player.defence -= enemy.attack
		
		for enemy in enemyArray:
			printy(str(enemy.uid) + "'s health = " + str(enemy.health),f)
	

	return safehouse, player, enemyArray, points

def round_interval(safehouseObj, playerObj, pointsValue, textFile):
	safehouse = safehouseObj
	player = playerObj
	points = pointsValue
	f = textFile
	printy("####################################", f)
	printy("It's the calm before another storm", f)
	printy("You have " + str(points) + " to spend.", f)
	printy("What would you like to upgrade?", f)

	printy("", f)
	playerStats(player, f)
	houseStats(safehouse, f)
	printy("", f)
	
	while (points > 0):

		#create a parser that will separate building and player stats

		choice = input("> ")
		if (choice == 'health'):
			points -= 1
			player.health += 1
			playerStats(player, f)
		elif (choice == 'attack'):
			points -= 1
			player.attack += 1
			playerStats(player, f)
		elif (choice == 'defence'):
			points -= 1
			player.defence += 1
			playerStats(player, f)
		elif (choice == 'speed'):
			points -= 1
			player.speed += 1
			playerStats(player, f)
		elif (choice == 'safehouse health'):
			points -= 1
			safehouse.health += 1
			houseStats(safehouse, f)
		elif (choice == 'safehouse attack'):
			points -= 1
			safehouse.attack += 1
			houseStats(safehouse, f)
		elif (choice == 'safehouse defence'):
			points -= 1
			safehouse.defence += 1
			houseStats(safehouse, f)
		else:
			return safehouse, player, points
	return safehouse, player, points		

def spawn_zombies(number_of_enemies):

	array_of_zombies = []
	for i in range(number_of_enemies):
		uid = '<zombie '+str(number_of_enemies)+'/'+str(i+1)+'>'
		zombie = enemy(3,1,3, uid)
		array_of_zombies.append(zombie)
	return array_of_zombies