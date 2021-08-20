# A demo for python-dungeon
This demo can be used as an example for what games made with python-dungeon can look like. It features two paths for the player to take, with a final boss at the end. My original goal was to create a text adventure in Python. Then I forked this project and made python-dungeon, which is really just the same thing but the custom assets I created for this demo were stripped away and documentation for all of the files was added. That is also the reason python-dungeon is a fork of the demo and not the other way around :) 
## Installation
python-dungeon depends on only one Python package not in the standard library. Use `pip install xlrd` to install the necessary module. It is needed for the program to parse the spreadsheet file.

## How to Play
As the player, your default actions are to move north, south, east, or west (if the path permits), and to view your inventory. When you walk onto a tile with an item on it, you can grab that item, and if it is a weapon, equip it. The way combat works is quite interesting. Every weapon you pick up has a list of 'techniques', which are special keywords you must use when typing in your attack. However, attack commands are made up one other part. Each enemy you face will also have a list of keywords associated with it. That list is called 'weaknesses'. You must also include an enemy weakness in your attack command.
#### The format for the attack in this:
`technique` `weakness`
An example list of techniques would be: [slice, stab, cut, throw]
An example list of weaknesses would be: [eyes, arms, head, legs]
To land an attack, you must use a valid combination of techniques and weaknesses.

At the beginning of the game, you will be asked if you want to play on hard mode. Hard mode is how the game was intended to be played. On easy mode, each turn you will be given a list of attacks you can perform on the enemy. On hard mode, you must read the description of the enemy to infer what it's weaknesses will be, as well as what you weapon's techniques are.

### Credit
Project: text-adventure-tut https://github.com/phillipjohnson/text-adventure-tut
Copyright (c) 2014 Phillip Johnson
License https://github.com/phillipjohnson/text-adventure-tut/blob/master/LICENSE.txt
