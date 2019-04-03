import json
import os
import argparse
import random
import string
from colorama import init, Fore, Back, Style

# Player class
from player import Player


def display_highscores():
    """
    Prints the highscores.txt file to the terminal.
    :return: Nothing.
    """
    if os.path.isfile("highscores.txt"):
        with open("highscores.txt") as f:
            scores = f.read()
            print(Fore.BLUE + scores)
            print(Style.RESET_ALL)
    else:
        print(Fore.RED + "There are no highscores set in this directory...")


def display_rules():
    """
    Prints the rules for the game.
    :return: Nothing.
    """
    with open("word-craft-rules.txt") as f:
        rules = f.read()
        print(Fore.GREEN + rules)


def build_highscore_file():
    """
    Checks if there is already a highscore file in directory.
    If not, builds one.
    :return: Nothing
    """
    if not os.path.isfile("highscores.txt"):
        f = open("highscores.txt", "w")
        f.write("=== Word Craft ==\n"
                "== HIGH SCORES ==\n"
                "=================\n")
        f.close()


def save_player_score(player_name, score):
    """
    Saves the player's score to a text file score board.
    :return: Nothing.
    """
    # TODO: create a dict of high scores and store in a json file.
    #  Then refer to dict to get top 5 high scores and store them in text file from highest to lowest.
    print(Fore.GREEN + "Saving score...")
    print(Style.RESET_ALL)

    with open("highscores.txt", "a+") as f:
        f.write("Player: %s \n"
                "Score: %s\n"
                "=================\n" % (player_name, score))

    display_highscores()

    print("Thanks for playing! Quitting game...")
    exit()


def end_of_game(scenario, score, player):
    """
    Plays the end of game scenario based on whether the player quit or lost.
    :return:
    """
    if scenario == 'quit':
        print(Fore.RED + "Quitting game. Your final score was %s. " % str(score))
        print(Style.RESET_ALL)
        print("Would you like to save your score? y/n")
        while True:
            save_score = input()
            if save_score == 'y':
                save_player_score(player, score)
                exit()
            elif save_score == 'n':
                print("Thanks for playing! Quitting game...")
                exit()
    elif scenario == 'loss':
        print(Fore.RED + "You have gained 3 strikes. GAME OVER.")
        print(Style.RESET_ALL)
        print("Would you like to save your score? y/n")
        while True:
            save_score = input()
            if save_score == 'y':
                save_player_score(player, score)
                exit()
            elif save_score == 'n':
                print("Thanks for playing! Quitting game...")
                exit()
            else:
                print(Fore.RED + "Please enter either 'y' or 'n'...")


def check_new_word(word, gen_letter, player_obj):
    """
     Checks the word entered in the following order:
        1. Does the word start with the gen_letter?
        2. Is it a real word?
        3. Has it already been added to the player's list?
        If the word passes all these checks, add it to the player's word_list.
     :param word: Word that needs checking.
     :param gen_letter: The generated letter for the game.
     :param player_obj: The list of words that have already been checked and added.
     :return: Nothing
    """
    if word[0] == gen_letter:
        print("%s starts with %s" % (word, gen_letter))
        if word in dictionary:
            print('%s is a word' % word)
            if word not in player_obj.word_list:
                print("%s is not already in your list of words." % word)
                print(Fore.GREEN + "WORD IS VALID!!")
                player_obj.add_word(word)
            else:
                print(Fore.RED + "%s is already in your list. Adding strike" % word)
                print(Style.RESET_ALL)
                striker = player_obj.add_strike()
                # If player has reached 3 strikes.
                if striker is True:
                    end_of_game('loss', player_obj.score, player_obj.player_name)
        else:
            print(Fore.RED + "%s is not a word. Adding strike" % word)
            print(Style.RESET_ALL)
            striker = player_obj.add_strike()
            # If player has reached 3 strikes.
            if striker is True:
                end_of_game('loss', player_obj.score, player_obj.player_name)
    else:
        print(Fore.RED + "%s does not start with %s. Adding strike" % (word, gen_letter))
        print(Style.RESET_ALL)
        striker = player_obj.add_strike()
        # If player has reached 3 strikes.
        if striker is True:
            end_of_game('loss', player_obj.score, player_obj.player_name)


def new_game():
    ####################
    # Welcome to game ##
    ####################

    # Check if there is a highscore file already built.
    build_highscore_file()

    # Read in logo and print.
    with open("word-craft-logo.txt") as f:
        logo = f.read()
        print(logo)

    # Intro.
    print("Please enter a player name: ")
    print(Fore.RED + "Type 'quit' to quit the game.")
    print(Style.RESET_ALL)
    name = input()

    if name == 'quit':
        print(Fore.RED + "Quitting game...")
        print(Style.RESET_ALL)
        exit()

    player_obj = Player(name)

    # Generate a random letter.
    letters = string.ascii_letters.lower()
    gen_letter = random.choice(letters)

    print("Your letter is " + Fore.GREEN + "%s" % gen_letter.upper())
    print(Style.RESET_ALL)

    # Enter word-giving loop.
    while True:
        print(Fore.RED + "------Type 'q' to quit the game.------")
        print(Style.RESET_ALL)
        print("Enter a word beginning with %s: " % gen_letter)
        print(Fore.BLUE + "Score: %s" % str(player_obj.score))
        print(Style.RESET_ALL)
        given_word = input()
        given_word = given_word.lower()

        if given_word == 'q'.lower():
            end_of_game('quit', player_obj.score, player_obj.player_name)
            exit()
        else:
            check_new_word(given_word, gen_letter, player_obj)


if __name__ == '__main__':

    init()  # initializing colorama module.

    ####################
    # Dictionary      ##
    ####################
    dictionary = json.load(open("collection.json"))

    ####################
    # Argparse        ##
    ####################
    parser = argparse.ArgumentParser()
    # Group will make sure that only one of the arguments in the mutually exclusive group is present on CL.
    group = parser.add_mutually_exclusive_group()

    # Adding optional arguments.
    # 'store-true' - Action used for storing True. Makes checking the arguments parsed work for optional args.
    group.add_argument("-r", "--rules", help="Display the rules for the game.", action="store_true")
    group.add_argument("-n", "--newGame", help="Start a new game.", action="store_true")
    group.add_argument("-s", "--highscores", help="See the set highscores.", action="store_true")

    # Parsing arguments.
    args = parser.parse_args()

    # Checking arguments:
    if args.rules:
        display_rules()
    elif args.newGame:
        new_game()
    elif args.highscores:
        display_highscores()


