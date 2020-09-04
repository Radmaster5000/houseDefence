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

player = human(3,3,3,3)

level = 3

enemyArray = spawn_zombies(level)

printy('#############################')
printy('ENEMY TURN')

for enemy in enemyArray:
	printy(enemy)

for enemy in enemyArray:
	roll = die_roll(6)
	printy(roll)
	
	if (roll > player.defence):
		printy("the zombie successfully attacks!")
		player.health -= enemy.attack
	else:
		printy("you fight the zombie off")
		player.defence -= enemy.attack
	
printy("player's health = " + str(player.health))
printy("player's defence is = " + str(player.defence))
for enemy in enemyArray:
	printy("zombie health = " + str(enemy.health))

printy("##############################")
printy('PLAYER TURN')

for turns in range(0, player.speed):
	roll = die_roll(6)
	printy(roll)
	
	if (roll > enemyArray[0].defence):
		printy("you successfully attack the zombie!")
		enemyArray[0].health -= player.attack
		if (enemyArray[0].health <= 0):
			printy("You killed the zombie")
			enemyArray.pop(0)
	else:
		printy("you miss the zombie")
		enemyArray[0].defence -= player.attack

for enemy in enemyArray:	
	printy("zombie's health = " + str(enemy.health))
	printy("zombie's defence is = " + str(enemy.defence))

# close the game log text file
f.close()
