import re

string1 = 'player'
string2 = 'player speed'
string3 = 'playerspeed'
string4 = 'Player speed'
string5 = 'Player Speed'
string6 = 'PlayerSpeed'
string7 = 'PLAYERSPEED'

string8 = 'safehouse'
string9 = 'safehouse defence'
string10 = 'safehousedefence'
string11 = 'Safehouse defence'
string12 = 'Safehouse Defence'
string13 = 'SafehouseDefence'
string14 = 'SAFEHOUSEDEFENCE'

pl = re.compile('player', re.IGNORECASE)
sa = re.compile('safehouse', re.IGNORECASE)
he = re.compile('health', re.IGNORECASE)
at = re.compile('attack', re.IGNORECASE)
de = re.compile('defence', re.IGNORECASE) 
sp = re.compile('speed', re.IGNORECASE) 

safehouseStat = re.compile('(s\w+)\s(\w)', re.IGNORECASE)

#attempt to parse any input
twoWordInput = re.compile('(\w+)\s(\w+)', re.IGNORECASE)



# if the player's input is saved as choice
# example... choice = 'player strength'
choice = string4

parsed = twoWordInput.match('PLAYER ATTACK')


parsed.group() # 'player strength'
parsed.group(1) # 'player'
parsed.group(2) # 'strength'

if (pl.match(parsed.group(1))):
	if (he.match(parsed.group(2))):
		print('increased player health')
		print('decrement points')
		print('print player stats')
	elif (at.match(parsed.group(2))):
		print('increased player attack')
		print('decrement points')
		print('print player stats')
	elif (de.match(parsed.group(2))):
		print('increased player defence')
		print('decrement points')
		print('print player stats')
	elif (sp.match(parsed.group(2))):
		print('increased player speed')
		print('decrement points')
		print('print player stats')
	else:
		print('re-loop player')
		# print error message and re-loop
elif (sa.match(parsed.group(1))):
	if (he.match(parsed.group(2))):
		print('increased safehouse health')
		print('decrement points')
		print('print safehouse stats')
	elif (at.match(parsed.group(2))):
		print('increased safehouse attack')
		print('decrement points')
		print('print safehouse stats')
	elif (de.match(parsed.group(2))):
		print('increased safehouse defence')
		print('decrement points')
		print('print safehouse stats')
	else:
		print('re-loop safehouse')
		# print error message and re-loop
else:
	print('re-loop epic fail')
	# print error message and re-loop



