import random
from classesAndFunctions import *

# opens the game log text file where each move will be copied down
# currently opens with "w", so overwrites the last session
# look at using "a" to append the file but stamp each session with a date/time at this point 
f = open("gameLog.txt", "w")

# custom function to print to the console and to the game log file at the same time
def printy(text):
	print(text)
	print(text, file=f)

player = human(3,3,3,6)

level = 3

enemyArray = spawn_zombies(level)

printy('#############################')
printy('ENEMY TURN')


for enemy in enemyArray:
	roll = die_roll(6)
	printy("The enemy roles an attack: " + str(roll))
	
	if (roll > player.defence):
		printy("the zombie successfully attacks!")
		player.health -= enemy.attack
	else:
		printy("you fight the zombie off")
		player.defence -= enemy.attack
	
printy("player's health = " + str(player.health))
printy("player's defence is = " + str(player.defence))
for enemy in enemyArray:
	printy(str(enemy.uid) + "'s health = " + str(enemy.health))

printy("##############################")
printy('PLAYER TURN')

# Initialise target outside of attack loop
# This identifies the target in the enemyArray
target = 0

for turns in range(0, player.speed):
	
	if (len(enemyArray) == 0):
		print("Congrats! You won!")
		quit()

	# It the target variable reaches the end of the array, reset it
	if (target >= len(enemyArray)):
		target = 0

	roll = die_roll(6)
	printy("The player rolled a: " + str(roll))
	
	if (roll > enemyArray[target].defence):
		printy("you successfully attack " + enemyArray[target].uid)
		enemyArray[target].health -= player.attack
		if (enemyArray[target].health <= 0):
			printy("You killed " + enemyArray[target].uid)
			enemyArray.pop(target)
			target -= 1
	else:
		printy("you miss the zombie")
		enemyArray[target].defence -= player.attack

	# Increment variable to target the next enemy in the array
	target += 1
for enemy in enemyArray:	
	printy(enemy.uid + "'s health = " + str(enemy.health))
	printy(enemy.uid + "'s defence is = " + str(enemy.defence))

# close the game log text file
f.close()
