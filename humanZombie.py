import random
from classesAndFunctions import *

# opens the game log text file where each move will be copied down
# currently opens with "w", so overwrites the last session
# look at using "a" to append the file but stamp each session with a date/time at this point 
f = open("gameLog.txt", "w")

# custom function to print to the console and to the game log file at the same time

points = 0
player = human(3,3,3,3)
safehouse = building(3,3,3)

oldEnemyArray = []
i = 1

while (player.health > 0):
	

	printy("",f)
	printy("",f)
	
	safehouse, player, oldEnemyArray, points = round(i, safehouse, player, oldEnemyArray, points, f)

	printy("",f)
	printy("",f)

	safehouse, player, points = round_interval(safehouse, player, points, f)

	i+=1

printy("player's health = " + str(player.health),f)
printy("player's defence is = " + str(player.defence),f)
printy(points,f)
# close the game log text file
f.close()
