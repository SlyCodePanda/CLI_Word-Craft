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