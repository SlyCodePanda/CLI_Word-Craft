# CLI - Word Craft

This is a basic word game ran in the command line.

## The Game
A random letter is generated between A and Z.<br>
The player is asked to give words that start with generated letter.<br>
Player can be awarded 3 strikes before they are out and their final score is awarded. Each word is worth 1 point unless 
the generated letter given is one of the following: X, Z, U, Y, W.<br>
Each valid word given is stored and calculated at the end of the game, and high scores are stored in a text doc.<br>
The list of given words passed by the user is checked every round to make sure there is no duplicates given.<br>
### Strike System
Strikes are awarded to player for the following actions:
* Duplicate word given.
* A word is given that is not in the dictionary (spelt wrong or jibberish).
* A word is given that does not start with the generated letter.

## Setup
1. install python3
2. download this repository
3. install the requirements of the repository pip install -r requirements.txt
4. run `python3 word-craft.py` with one of the following flags inside of the folder called CLI_Word-Craft
```
usage: word-craft.py [-h] [-r | -n]

optional arguments:
  -h, --help     show this help message and exit
  -r, --rules    Display the rules for the game.
  -n, --newGame  Start a new game.
```


## Modules Used
**argparse** - Used for passing arguments on the command line.<br>
**random** - Used for generating a random number for the random letter generator.<br>
**string** - Used to create a list of ascii letters to use with random to generate a random selection.<br>
**PyDictionary** - Using the PyDictionary to check if a word given is a real english word.<br>
**colorama** - Used to create coloured output in the command line.<br>
