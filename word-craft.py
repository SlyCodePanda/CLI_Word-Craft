import os
import argparse
import random
import string
from colorama import init, Fore, Back, Style

# Player class
from player import Player


def display_rules():
    """
    Prints the rules for the game.
    :return: Nothing.
    """
    with open("word-craft-rules.txt") as f:
        rules = f.read()
        print(Fore.GREEN + rules)


def save_player_score(player_name, score):
    """
    Saves the player's score to a text file score board.
    :return: Nothing.
    """
    print(Fore.GREEN + "Saving score...")
    print(Style.RESET_ALL)
    # TODO: Save player name and score to a text file.
    return


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
                return
            elif save_score == 'n':
                print("Thanks for playing! Quitting game...")
                return

    # TODO: Add loss scenario.


def new_game():
    ####################
    # Welcome to game ##
    ####################

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
    letters = string.ascii_letters.upper()
    gen_letter = random.choice(letters)

    print("Your letter is %s." % gen_letter)

    # Enter word-giving loop.
    while True:
        print(Fore.RED + "------Type 'q' to quit the game.------")
        print(Style.RESET_ALL)
        print("Enter a word beginning with %s: " % gen_letter)
        print(Fore.BLUE + "Score: %s" % str(player_obj.score))
        print(Style.RESET_ALL)
        given_word = input()

        if given_word == 'q'.lower():
            end_of_game('quit', player_obj.score, player_obj.player_name)
            exit()


if __name__ == '__main__':

    init()  # initializing colorama module.

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

    # Parsing arguments.
    args = parser.parse_args()

    # Checking arguments:
    if args.rules:
        display_rules()
    elif args.newGame:
        new_game()


