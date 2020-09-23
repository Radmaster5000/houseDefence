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

p = re.compile('player')
s = re.compile('safehouse')
safehouseStat = re.compile('(s\w+)\s(\w)', re.IGNORECASE)

#attempt to parse any input
twoWordInput = re.compile('(\w+)\s(\w+)', re.IGNORECASE)



# if the player's input is saved as choice
# example... choice = 'player strength'

grouped = twoWordInput.match(choice)


grouped.group() # 'player strength'
grouped.group(1) # 'player'
grouped.group(2) # 'strength'




