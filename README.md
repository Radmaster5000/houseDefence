# houseDefence

A basic die-rolling based fighting game between a single survivor and a growing number of zombies.

Added a custom print function that will print to the console and also save the output in a text file. Currently overwrites the last textlog when a new game is started.

************************

UPDATE: 23/09/20

Currently playing with regex and parsing the player's inputs when upgrading. Probably not going to look like I'm doing much for a while as I try to get my head round this.


***************


UPDATE: 16/09/20

Added a safehouse. This acts as the first line of defence for the player. The zombies will attack the safehouse before they attack the player. 

Most of the basics are working. Player fights zombies with random levels of sucess. Starts with one zombie, increasing by one each round. If the player kills a zombie, they earn a point. 

At the end of each round, player can choose to upgrade their stats by spending the points they've earned. 

************************

## TODO:


<ul>
	<li>Clean up upgrade system (catching misspellings, etc)</li>
	<li>Allow the safehouse to be upgraded as well as the player</li>
	<li>Implement a command list so the player can take a more active role</li>
	<li>Implement a way of saving multiple games to the text log (possibly make a folder to save old games)</li>
	<li>Tidy up the text</li>
</ul>